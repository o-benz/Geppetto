import boto3
import pprint
from botocore.client import Config
import json
import sys

if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent=2)
    session = boto3.Session(
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
    COmp = sys.argv[1] 
    retriver_query = "give me all relative sentimental information about this document: " + COmp
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
    #pp.pprint(contexts)

    #####################################
    prompt = f"""
    Human: You are an AI sentiment analysis assistant. Your role is to analyze and summarize the sentiment in the provided text by identifying emotions, tone, and key indicators. 
    Use the following information, enclosed within <context> tags, to determine the sentiment. 

    Respond with a concise summary, including a sentiment rating (e.g., Positive, Neutral, Negative) and examples if applicable.
    If the sentiment is ambiguous or mixed, state that.

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
  
    generator_query = "donne moi les 4 grande emotions qui resortent du rapport : AltaGas_Q4 2023 Press Release and MD&A_0.pdf"
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
    # docs = retriever.get_relevant_documents(
    #         query=generator_query
    #     )
    #pp.pprint(docs)

    ######################################
    from langchain.prompts import PromptTemplate
   
    PROMPT_ETMPLATE = """
    Human: You are an AI sentiment analysis assistant. Your role is to analyze and summarize the sentiment in the provided text by identifying emotions, tone, and key indicators. 
    Use the following information, enclosed within <context> tags, to determine the sentiment. 

    Respond with a concise summary, including a sentiment rating (e.g., Positive, Neutral, Negative) and examples if applicable.
    If the sentiment is ambiguous or mixed, state that.

    <context>
    {context}
    </context>

    <task>
    Analyze the sentiment based on the context, noting specific emotions, tone, and any relevant words or phrases. Include any clear indicators for your judgment.
    </task>

    The response should provide a clear sentiment summary with examples where possible.

    Assistant:"""
    claude_prompt = PromptTemplate(template=PROMPT_ETMPLATE, 
                                input_variables=["context","task"])


    from langchain.chains import RetrievalQA

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": claude_prompt}
    )
    print("test:\n")
    answer = qa.invoke(generator_query)
    answer=answer['result']
    print(answer)
   # pp.pprint(answer)


