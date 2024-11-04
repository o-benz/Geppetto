import boto3
import pprint
from botocore.client import Config
import json

AWS_ACCESS_KEY_ID="AKIA5HLSELP4262I5ZN6 "
AWS_SECRET_ACCESS_KEY="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"
AWS_SESSION_TOKEN="IQoJb3JpZ2luX2VjEFEaCXVzLWVhc3QtMSJHMEUCIFszFAsTmpmJSK7ASK/DQFgC9Cw7ggn9lbi4iXmmhyQsAiEAjBphxC79trdGzX7mCyf2k70cugUmudB6GbWvkYC4qW4qogIIyv//////////ARABGgw5MDkxNjE4MTUwMzMiDAGCQnNPga0OnsfqeCr2Af2WAscFOJ+wmhD/5CAEPDElP8tLdhTHrw+KsRh+qKOd3JGTlRmKt7q1H1hLQxRBw5rAwKJRKs9tPMRTdwrWin9NZiGBm4F4940XkBEcw31WDtgVptdXYNWJSwlkmkNdB02JwXoRGf1LZs8vb5d3hz1jGGiQT8QAhdiu6xKh06hjkAVVevU9MrSLZSM48ImmWNk8sF0uGg6IlyC+gjDY1MOOfEi/KuljxfpCETEhoad2J9RortZVcLs6m7yr9KIOFo3C03EV/iMPY0ZtelA5E1N2BUs5ratD8ayJpqqDKvh6jSea0Tt+ZWU6Sgp4IaYm0/8o5S+C/jDQh5u5BjqdAfQy0Ibo5HcG4PugbMjyIBR9XRO0XfonrgkeSVwlBTGZXVpAFZPKOJ7DRdQRNfufdLYSsqukiqPsREDOpYPl8R3f9GD+HusWQO4MsSKG7aNRySFD+ZawYkKyMuEyPbrZEcVOTlvagbAecHD7Z/hyhqSOz7tY9BBYkt0niwUwpp3UtFgw0Y1rlpATUcMaUT2sjON9A7MeQi1ODPEp8YM="
pp = pprint.PrettyPrinter(indent=2)
session = boto3.Session(
    #aws_access_key_id=AWS_ACCESS_KEY_ID,
    #aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    #aws_session_token=AWS_SESSION_TOKEN
    profile_name="my_profile"

)
kb_id = 'CGZ8KWKHGQ'
region = "us-west-2"
bedrock_config = Config(connect_timeout=120, read_timeout=120, retries={'max_attempts': 0})
bedrock_client = session.client('bedrock-runtime', region_name = region)
bedrock_agent_client = session.client("bedrock-agent-runtime",
                              config=bedrock_config, region_name = region)
print(bedrock_client)

def retrieve(query, kbId, numberOfResults=10):
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

retriver_query = "give me all relative statistical information about this document: AltaGas_Q4 2023 Press Release and MD&A_0.pdf"
response = retrieve(retriver_query, "CGZ8KWKHGQ", 10)
retrievalResults = response['retrievalResults']
#pp.pprint(retrievalResults)

#####################################
def get_contexts(retrievalResults):
    contexts = []
    for retrievedResult in retrievalResults: 
        contexts.append(retrievedResult['content']['text'])
    return contexts

contexts = get_contexts(retrievalResults)
pp.pprint(contexts)

#####################################
prompt = f"""
Human: You are a financial advisor AI system, and provides answers to questions by using fact based and statistical information when possible. 
Use the following pieces of information to provide a concise answer to the question enclosed in <question> tags. 
If you don't know the answer, just say that you don't know, don't try to make up an answer.
<context>
{contexts}
</context>

<question>
{retriver_query}
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


# pp.pprint(response_text)
########################################
from langchain_aws import ChatBedrock
from langchain_community.retrievers import AmazonKnowledgeBasesRetriever  # Updated import

llm = ChatBedrock(model_id="anthropic.claude-3-haiku-20240307-v1:0",
              client = bedrock_client)
generator_query = "donne moi le resume du rapport de ce rapport : AltaGas_Q4 2023 Press Release and MD&A_0.pdf"
retriever = AmazonKnowledgeBasesRetriever(
    knowledge_base_id="CGZ8KWKHGQ",
    retrieval_config={
        "vectorSearchConfiguration": {
            "numberOfResults": 4,
            'overrideSearchType': "SEMANTIC",  # optional
     }
    },
    credentials_profile_name="my_profile",
    # Passing the session to the retriever
    session=session,
    region_name="us-west-2",
)
docs = retriever.get_relevant_documents(
        query=generator_query
    )
#pp.pprint(docs)

######################################
# from langchain.prompts import PromptTemplate

# PROMPT_TEMPLATE = """
# Human: You are a financial advisor AI system, and provides answers to questions by using fact based and statistical information when possible. 
# Use the following pieces of information to provide a concise answer to the question enclosed in <question> tags. 
# If you don't know the answer, just say that you don't know, don't try to make up an answer.
# <context>
# {context}
# </context>

# <question>
# {question}
# </question>

# The response should be specific and use statistics or numbers when possible.

# Assistant:"""
# claude_prompt = PromptTemplate(template=PROMPT_TEMPLATE, 
#                                input_variables=["context","question"])


# from langchain.chains import RetrievalQA

# qa = RetrievalQA.from_chain_type(
#     llm=llm,
#     chain_type="stuff",
#     retriever=retriever,
#     return_source_documents=True,
#     chain_type_kwargs={"prompt": claude_prompt}
# )
# print("test:\n")
# answer = qa.invoke(generator_query)
# pp.pprint(answer)

# PROMPT_TEMPLATE = """
# Human: You are a financial advisor AI system, and provides comparison to betwen this summary and the data of other companies in the knowledge base by using fact based and statistical information when possible. 
# Use the following pieces of information to provide a concise answer to the question enclosed in <summary> tags. 
# If you don't know the answer, just say that you don't know, don't try to make up an answer.
# <context>
# {context}
# </context>

# <summary>
# {summary}
# </summary>

# The response should be specific and use statistics or numbers when possible.

# Assistant:"""
# claude_prompt = PromptTemplate(template=PROMPT_TEMPLATE, 
#                                input_variables=["context","summary"])
