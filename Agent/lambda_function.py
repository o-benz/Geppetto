import json
import urllib.parse
import boto3
from extract_info import import_pdf
import os


print('Loading function')

key_id=os.environ.get("aws_access_key_id")
aws_access_key=os.environ.get("aws_access_key")
session_token= os.environ.get("session_token")


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    session = boto3.Session(
    aws_access_key_id=key_id,
    aws_secret_access_key=aws_access_key,
    aws_session_token=session_token,
    region_name="us-west-2" )

    s3 = session.client('s3')
    path=event['path']
    read_pdf=import_pdf(path, s3)
    print(read_pdf)
