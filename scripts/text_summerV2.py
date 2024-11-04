import boto3
import pprint
from botocore.client import Config
import json
import botocore

#session 
#######################################

session = boto3.Session(
    #aws_access_key_id=AWS_ACCESS_KEY_ID,
    #aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    #aws_session_token=AWS_SESSION_TOKEN
    profile_name="my_profile"

)
region = "us-west-2"
bedrock_config = Config(connect_timeout=120, read_timeout=120, retries={'max_attempts': 0})
bedrock_client = session.client('bedrock-runtime', region_name = region)
bedrock_agent_client = session.client("bedrock-agent-runtime",
                              config=bedrock_config, region_name = region)
print(bedrock_client)
boto3_bedrock = bedrock_client

client = bedrock_client  # Replace with your AWS region




#read file
#############################





def summarize_text(text):


    prompt = f"""
    Human: You are a financial advisor AI system, and provides answers to questions by using fact based and statistical information when possible. 
    Use the following pieces of information to provide a concise answer to the question enclosed in <question> tags. 
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    <context>
    {text}
    </context>

    <question>
    Summarize the following text in a few concise sentences:\n\n'This report covers the quarterly earnings for ABC Corporation, detailing revenue, expenses, and net profit changes over the last quarter. Key highlights include an increase in digital sales, significant reduction in overhead costs, and new market expansion. Challenges faced include supply chain disruptions and increasing material costs. Overall, the company projects a steady growth trajectory despite these challenges.
    </question>

    The response should be specific and use statistics or numbers when possible.

    Assistant:"""

    inference_config = {
            "temperature": 0,
            "maxTokens": 4096,
            "topP": 0.95,
    }


    messages = [
            {
                "role": "user",
                "content": [{"text": prompt}]
            }
        ]


    # modelId = 'amazon.titan-text-premier-v1:0' # Make sure Titan text premier is available in the account you are doing this workhsop in before uncommenting!
    modelId = "anthropic.claude-3-sonnet-20240229-v1:0"



    try:
        response = boto3_bedrock.converse(
                modelId=modelId,
                messages=messages,
                inferenceConfig=inference_config,
        )
        response_body = response['output']['message']
    
        print(response_body.get('content')[0].get('text'))

    except botocore.exceptions.ClientError as error:
        
        if error.response['Error']['Code'] == 'AccessDeniedException':
            print(f"\x1b[41m{error.response['Error']['Message']}\
                    \nTo troubeshoot this issue please refer to the following resources.\
                    \nhttps://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_access-denied.html\
                    \nhttps://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html\x1b[0m\n")
            
        else:
            raise error
    # response_body = json.loads(response['body'])
    return response_body

# Step 4: Combine everything to summarize PDF content
def summarize_pdf(pdf_path):
   with open(pdf_path, "r") as file:
    text = file.read()
    
    # If the PDF is long, split into chunks (adjust chunk size as needed for Bedrock model limits)
    chunk_size = 200000# Character limit for each chunk
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    
    # Summarize each chunk and combine results
    summary =  []
    for chunk in chunks:
        chunk_summary = summarize_text(chunk)
       
       
        summary.append(chunk_summary) ###+= chunk_summary + "\n"
       
    return summary

# Example usage
pdf_path = r"D:\Hacathon\test.txt"  # Path to your PDF file
summary = summarize_pdf(pdf_path)
print("Summary of PDF:", summary)