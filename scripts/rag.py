import boto3
import pprint
from botocore.client import Config
import json

pp = pprint.PrettyPrinter(indent=2)
session = boto3.Session(
    aws_access_key_id="ASIA5HLSELP4X2P7V2FI",
    aws_secret_access_key="GXR/J91d6mBbtQ3D7Q0N1Wdt10+M7Jfbv5V798Wt",
    aws_session_token="IQoJb3JpZ2luX2VjEFAaCXVzLWVhc3QtMSJHMEUCIAiWCJqnP4s4fPBTkwrah7B1b5+zUmEp0fZXh3brHA9EAiEA+9U4ml/BN+GtwGMfnpCHNBiFIHqqvMldujra8UaBYcoqogIIyP//////////ARABGgw5MDkxNjE4MTUwMzMiDMR2niBPznKakYIzYCr2AckwgjskU4svJVePKrl3Uf1tUi2cUSaUrt1pT7mte3zEtPsGE2V02QDYlP/mbFL2tOmM+k3ulW26caKe8HlqC68DV9xUg5rDL2c8xARHm7RKAVbYTwd9xX5faxQJdEAnsmCBekSa8vdjeFm0J82vwal+74HA5ZQdJWGkqZ5sWJI4EB1nUWhVEDtrrc8+8tOa+RL4n7Ibz8G6RPLco2VCD7hZjZ6abzSY+FWuQ0ot6wCAXhynOoeniEk//Gte5OF6zz2Z03F9wNJXUG+BwYrRMM8NNTe3pq33rJowz8Kw9/t84gBPNoavZisgBeV3Itywg+u/1tLWpDCX4pq5BjqdAccmTlosPZ9xfx3JSiX1d9dARPefGPY0JXtc8qudTav5hdqveGfxzRqPvC794xzLIsNY29JDNgrevh5Pmpm82/5OHAqokKR4Ka25WCBZw4FPY/62LI4Xq1HYRxUsK5YSawJK/1m0iqOS3GBght7F5V5oPpSCRiJhw3UBdv96hGCiu9FJNCVHQVnQ7f5rmgwJ8Tg1kcKwg5jYN+x4zv0=",
    region_name="us-west-2"  # Replace with your region
)
kb_id = "CGZ8KWKHGQ"
region = "us-west-2"
bedrock_config = Config(connect_timeout=120, read_timeout=120, retries={'max_attempts': 0})
bedrock_client = session.client('bedrock-runtime', region_name = region)
bedrock_agent_client = session.client("bedrock-agent-runtime",
                              config=bedrock_config, region_name = region)
print(session)

def retrieve(query, kbId, numberOfResults=5):
    try:
        return bedrock_agent_client.retrieve(
            retrievalQuery={'text': query},
            knowledgeBaseId=kbId,
            retrievalConfiguration={
                'vectorSearchConfiguration': {
                    'numberOfResults': numberOfResults
                }
            }
        )
    except Exception as e:
        print(f"Error during retrieval: {e}")

query = "what is CN revenue in 2023"
response = retrieve(query, "CGZ8KWKHGQ", 5)
retrievalResults = response['retrievalResults']
#pp.pprint(retrievalResults)

#####################################
def get_contexts(retrievalResults):
    contexts = []
    for retrievedResult in retrievalResults: 
        contexts.append(retrievedResult['content']['text'])
    return contexts

contexts = get_contexts(retrievalResults)
#pp.pprint(contexts)

#####################################
prompt = f"""
Human: You are a financial advisor AI system, and provides answers to questions by using fact based and statistical information when possible. 
Use the following pieces of information to provide a concise answer to the question enclosed in <question> tags. 
If you don't know the answer, just say that you don't know, don't try to make up an answer.
<context>
{contexts}
</context>

<question>
{query}
</question>

The response should be specific and use statistics or numbers when possible.

Assistant:"""

claude_payload = json.dumps({
    "prompt": prompt,
    "max_tokens": 512,
    "temperature": 0.5,
    "top_k": 50,
    "top_p": 0.9
})

# Update the model ID for Claude 3 Sonnet
modelId = 'mistral.mistral-7b-instruct-v0:2'  # Replace this with the actual model ID for Claude 3 Sonnet

# Define the content type and accept headers
accept = 'application/json'
contentType = 'application/json'

# Invoke the Claude model
response = bedrock_client.invoke_model(body=claude_payload, modelId=modelId, accept=accept, contentType=contentType)

# Process the response
response_body = json.loads(response.get('body').read())
response_text = response_body.get('outputs')[0]['text']

# Pretty print the output text
#pp.pprint(response_text)
########################################
from langchain_aws import ChatBedrock
from langchain.retrievers.bedrock import AmazonKnowledgeBasesRetriever

llm = ChatBedrock(model_id="anthropic.claude-3-haiku-20240307-v1:0",
              client = bedrock_client)
query = "By what CN did AWS revenue grow year-over-year in 2022?"
retriever = AmazonKnowledgeBasesRetriever(
        knowledge_base_id=kb_id,
        retrieval_config={"vectorSearchConfiguration": 
                          {"numberOfResults": 4,
                           'overrideSearchType': "SEMANTIC", # optional
                           }
                          }
        # endpoint_url=endpoint_url,
        # region_name=region,
        # credentials_profile_name="<profile_name>",
    )
docs = retriever.get_relevant_documents(
        query=query
    )
pp.pprint(docs)
