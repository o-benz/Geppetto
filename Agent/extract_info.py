import boto3
import io
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
from langchain.document_loaders import Blob
from langchain_community.document_loaders.parsers.pdf import PDFPlumberParser


def import_pdf(path, s3_client):
    print("We are looking at the file located at the key : ", path)
    # My Bucket
    bucket_name='datalakefinancier'

    try:
        response= s3_client.get_object(Bucket= bucket_name, Key=path)
        file_content= response['Body'].read() 
        pdf_stream = io.BytesIO(file_content)
        print("Loaded the file content into a BytesIO object")
        pdf_content=pdf_stream.read()
        blob = Blob(data=pdf_content)
        print("Parsed into blob")
        parser = PDFPlumberParser()
        document = parser.parse(blob)
        print("We are returning the document")
        return document
       
    except ClientError as e:
        if e.response['Error']['Code']=='403':
            print("Access forbidden")
        else:
            print('Error',e)





    