import boto3
import io
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
from langchain.document_loaders import Blob
#from langchain_community.document_loaders.parsers.pdf import PDFPlumberParser


import pdfplumber
from botocore.client import Config
import os
import json
import re
import fitz
import pandas as pd
from dotenv import load_dotenv
load_dotenv()


from botocore.config import Config

config = Config(
    retries = {
        'max_attempts': 10,
        'mode': 'adaptive'
    }
)

print('Loading function')

key_id=os.environ.get("aws_access_key_id")
aws_access_key=os.environ.get("aws_access_key")
session_token= os.environ.get("session_token")

def retrieve_tables(path, s3_client):
    textract = boto3.client(
            'textract',
            region_name="us-west-2",
            aws_access_key_id=key_id,
            aws_secret_access_key=aws_access_key,
            aws_session_token=session_token
        )

    # Download the PDF file from S3
    response = s3_client.get_object(Bucket='kbrapports', Key=path)
    file_content = response['Body'].read()
    pdf_stream = io.BytesIO(file_content)
    print("Loaded the file content into a BytesIO object")

    # Open the PDF with PyMuPDF
    pdf_document = fitz.open(stream=pdf_stream, filetype='pdf')

    results = []

    # Iterate over each page in the PDF
    for page_number in range(1,len(pdf_document)):
        print(f"Processing page {page_number + 1}")
        page = pdf_document[page_number]

        # Create a pixmap (image) of the page
        pix = page.get_pixmap()
        # Get the image bytes in PNG format
        image_bytes = pix.tobytes("png")

        # Create a BytesIO object from the image bytes
        image_stream = io.BytesIO(image_bytes)

        # Check the size of the image (Textract 'Bytes' limit is 5 MB)
        if len(image_bytes) > 5 * 1024 * 1024:
            print(f"Page {page_number + 1} exceeds the maximum size limit of 5 MB.")
            continue  # Skip this page
        response = textract.analyze_document(
            Document={'Bytes': image_bytes},
            FeatureTypes=["FORMS", "TABLES"]
        )
        tab=extract_tables_from_response(response)
        nombre_de_tables = len(tab)

        if nombre_de_tables > 0:
            results.append(tab)
    print("Tables extracted successfully")        
    return results
    


def extract_tables_from_response(response):
    blocks = response['Blocks']

    # Dictionnaires pour stocker les blocs
    blocks_map = {}
    table_blocks = []
    cell_blocks = {}
    word_blocks = {}

    # Parcourir tous les blocs pour les organiser
    for block in blocks:
        blocks_map[block['Id']] = block
        if block['BlockType'] == 'TABLE':
            table_blocks.append(block)
        elif block['BlockType'] == 'CELL':
            cell_blocks[block['Id']] = block
        elif block['BlockType'] == 'WORD':
            word_blocks[block['Id']] = block

    tables = []

    # Parcourir chaque table détectée
    for table in table_blocks:
        table_id = table['Id']

        # Obtenir les cellules de la table
        cell_ids = [rel['Ids'] for rel in table.get('Relationships', []) if rel['Type'] == 'CHILD']
        cell_ids = [cell_id for sublist in cell_ids for cell_id in sublist]

        # Organiser les cellules en fonction des lignes et des colonnes
        table_data = {}
        max_row = 0
        max_col = 0

        for cell_id in cell_ids:
            cell = cell_blocks[cell_id]
            row_index = cell['RowIndex']
            col_index = cell['ColumnIndex']
            max_row = max(max_row, row_index)
            max_col = max(max_col, col_index)

            # Obtenir le texte de la cellule
            text = ''
            if 'Relationships' in cell:
                for rel in cell['Relationships']:
                    if rel['Type'] == 'CHILD':
                        for child_id in rel['Ids']:
                            word = word_blocks.get(child_id)
                            if word:
                                text += word['Text'] + ' '
            text = text.strip()

            # Stocker le texte dans la structure de la table
            if row_index not in table_data:
                table_data[row_index] = {}
            table_data[row_index][col_index] = text

        # Convertir la table en DataFrame pandas
        table_rows = []
        for row_index in range(1, max_row + 1):
            row = []
            for col_index in range(1, max_col + 1):
                cell_text = table_data.get(row_index, {}).get(col_index, '')
                row.append(cell_text)
            table_rows.append(row)
        df = pd.DataFrame(table_rows)
        tables.append(df)
    return tables



def transform_table_to_dict(tables):
    l=  []
    for table in tables:
        for df in table:
            l.append(df)
   
    return l

def structure_df(dff):
    dff.replace('', pd.NA, inplace=True)

    # Obtenir la liste des colonnes des années (toutes les colonnes à partir de la deuxième)
    year_columns = dff.columns[1:]

    

    # Maintenant, vous pouvez convertir le DataFrame en JSON
    # Mettre 'Income Statement' comme index
    dff.set_index(dff.columns[0], inplace=True)

    # Convertir en JSON avec l'orientation 'index'
    json_result = dff.to_json(orient='index')
    return json_result 







def retrieve_financial_info(results):
    client = boto3.client("bedrock-runtime", region_name="us-west-2", aws_access_key_id=key_id,
                          aws_secret_access_key=aws_access_key, aws_session_token=session_token, config=config)
    model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
    print(results)
    prompt =  f'''
    T'as cette liste de KPIs financiers:
    - Chiffre d'affaires
    - marge brute
    - dette nette
    - bénéfices avant interet
    - Dépréciation et amortissement
    - Capitaux propre
    - Trésorerie
    T'as comme entrée, une liste de listes  {results}. Chaque liste de listes est considérée comme un table qui contient des informations.
    Ton objectif est de selectionner une seule liste de listes qui contient le maximum de KPIs cités en haut à partir de ce document: {results}. 
    Les informations sur les années se trouvent dans le premier dictionnaire de chauque liste.
    La sortie doit etre sous forme de JSON:
    {{Catégorie : {{annee1 : valeur1, annee2 : valeur2}}}}
    Exemple:
    voici mon input:
    [[{{0: 'Income Statement', 1: '2021', 2: '2020'}}, 
        {{0: 'Revenue', 1: '1,103,732', 2: '1,149,990'}},
        {{0: 'Cost of Goods Sold (COGS)', 1: '404533', 2: '432921'}}  
        
    ]]
    voici son output:
    {{
    'Chiffre d Affaire': {{'2021': 1103732, '2020': 1149990}},
    'Cost of Goods Sold (COGS)': {{'2021': 404533, '2020': 432921}}
    }}

    '''

    native_request = {
        "anthropic_version": "bedrock-2023-05-31",
        "temperature": 0,
        "max_tokens": 5000,
        "messages": [
            {
                "role": "user",
                "content": [{"type": "text", "text": prompt}],
            }
        ],
    }

    request = json.dumps(native_request)

    streaming_response = client.invoke_model_with_response_stream(
        modelId=model_id, body=request
    )
    output = ""
    for event in streaming_response["body"]:
        chunk = json.loads(event["chunk"]["bytes"])
        if chunk["type"] == "content_block_delta":
            text = chunk["delta"].get("text", "")
            output += text
   


