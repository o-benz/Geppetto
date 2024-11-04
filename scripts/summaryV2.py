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
    COmp = sys.argv[1] # company name
    retriver_query = "Give me precisely the information financial information about this company: " + COmp
    response = retrieve(retriver_query, "POBGPV1JPA", 10)
    retrievalResults = response['retrievalResults']

    #####################################
    def get_contexts(retrievalResults):
        contexts = []
        for retrievedResult in retrievalResults: 
            contexts.append(retrievedResult['content']['text'])
        return contexts

    contexts = get_contexts(retrievalResults)

    #####################################
    # prompt = f"""
    # Human: You are an AI sentiment analysis assistant. Your role is to analyze and summarize the sentiment in the provided text by identifying emotions, tone, and key indicators. 
    # Use the following information, enclosed within <context> tags, to determine the sentiment. 

    # Respond with a concise summary, including a sentiment rating (e.g., Positive, Neutral, Negative) and examples if applicable.
    # If the sentiment is ambiguous or mixed, state that.

    # <context>
    # {contexts}
    # </context>

    # <question>
    # {retriver_query}
    # </question>

    # The response should be specific and use statistics or numbers when possible.

    # Assistant:"""

    # claude_payload = json.dumps({
    #     "prompt": prompt,
    #     "max_tokens": 512,
    #     "temperature": 0.5,
    #     "top_k": 50,
    #     "top_p": 0.9
    # })

    
    # modelId = 'mistral.mistral-7b-instruct-v0:2'  # Replace this with the actual model ID for Claude 3 Sonnet

    # # Define the content type and accept headers
    # accept = 'application/json'
    # contentType = 'application/json'

    # # Invoke the Claude model
    # response = bedrock_client.invoke_model(body=claude_payload, modelId=modelId, accept=accept, contentType=contentType)

    # # Process the response
    # response_body = json.loads(response.get('body').read())
    # response_text = response_body.get('outputs')[0]['text']


    # #pp.pprint(response_text)
    ########################################
    from langchain_aws import ChatBedrock
    from langchain_community.retrievers import AmazonKnowledgeBasesRetriever  # Updated import

    llm = ChatBedrock(model_id="anthropic.claude-3-haiku-20240307-v1:0",
                client = bedrock_client)
  
    generator_query = " Please provide accurate financial information about this company: " + COmp
    retriever = AmazonKnowledgeBasesRetriever(
        knowledge_base_id="POBGPV1JPA",
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
    Human: You are an AI financial analysis assistant. Your role is to analyze and summarize financial data, providing insights on financial performance, trends, and key indicators. 
    Use the following information, enclosed within <context> tags, to perform a financial analysis. 

    Respond with a concise summary that highlights:
    
    Key financial metrics (e.g., revenue, profit margin, growth rates) where available.
    Important trends or changes in the data.
    Any relevant financial risks, strengths, or areas for improvement.

    Provide examples, statistics, and numerical data to support your analysis when applicable.

    If you dont know the company or if any specific data is unclear or missing, mention that you dont know it and don't invent anything.

    <context>
    {context}
    </context>

    <task>
    Generate a concise summary, data-driven, and structured a financial analyst’s report.
    </task>


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
   
    answer = qa.invoke(generator_query)
    answer=answer['result']
    print(answer)
    #pp.pprint(answer)


