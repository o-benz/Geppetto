import json
import urllib.parse
import boto3
from extract_info import retrieve_financial_info,retrieve_tables,transform_table_to_dict,structure_df
import os
from dotenv import load_dotenv
load_dotenv()


print('Loading function')

key_id=os.environ.get("aws_access_key_id")
aws_access_key=os.environ.get("aws_access_key")
#session_token= os.environ.get("session_token")


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    pdf_name=os.path.basename(event['path'])
    filename_without_ext = os.path.splitext(pdf_name)[0]
    print('we are processing the file:',filename_without_ext)
    session = boto3.Session(
    aws_access_key_id=key_id,
    aws_secret_access_key=aws_access_key,
    #aws_session_token=session_token,
    region_name="us-west-2" )

    s3 = session.client('s3')
    path=event['path']
    #document=import_pdf(path, s3)
    document=retrieve_tables(path,s3)
    #ress=retrieve_financial_info(document)
    #r=extract_list_from_table(document)
     # Assurez-vous que target_table_index est défini
    result_dict = transform_table_to_dict(document)
    #res=retrieve_financial_info(result_dict)
    #ress=retrieve_financial_info(result_dict)
    dff=result_dict[10]
    dff.columns = dff.iloc[0]
    dff = dff[1:].reset_index(drop=True)
    
    json_content=structure_df(dff)  
    json_string = json.dumps(json_content) 
    bucket_name = 'kbrapports'
    path = 'tablesjson/'+filename_without_ext +'.json'  

    # Enregistrer la chaîne JSON dans S3
    s3.put_object(
        Bucket=bucket_name,
        Key=path,
        Body=json_string,
        ContentType='application/json'
    )
  


event= {
  "path": "Industriel/Ferroviaire/CN/CN_2019.pdf"
}


lambda_handler(event, None)