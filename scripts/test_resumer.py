

import boto3
import botocore

import boto3
import pprint
from botocore.client import Config
import json



#conexion AWS

####################################
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
region = "us-west-2"
bedrock_config = Config(connect_timeout=120, read_timeout=120, retries={'max_attempts': 0})
bedrock_client = session.client('bedrock-runtime', region_name = region)
bedrock_agent_client = session.client("bedrock-agent-runtime",
                              config=bedrock_config, region_name = region)
print(bedrock_client)
boto3_bedrock = bedrock_client



# prompt et summary
##############################################

prompt = """
Please provide a summary of the following text.
<text>
AWS took all of that feedback from customers, and today we are excited to announce Amazon Bedrock, \
a new service that makes FMs from AI21 Labs, Anthropic, Stability AI, and Amazon accessible via an API. \
Bedrock is the easiest way for customers to build and scale generative AI-based applications using FMs, \
democratizing access for all builders. Bedrock will offer the ability to access a range of powerful FMs \
for text and images—including Amazons Titan FMs, which consist of two new LLMs we’re also announcing \
today—through a scalable, reliable, and secure AWS managed service. With Bedrock’s serverless experience, \
customers can easily find the right model for what they’re trying to get done, get started quickly, privately \
customize FMs with their own data, and easily integrate and deploy them into their applications using the AWS \
tools and capabilities they are familiar with, without having to manage any infrastructure (including integrations \
with Amazon SageMaker ML features like Experiments to test different models and Pipelines to manage their FMs at scale).
</text>

"""

# Base inference parameters.
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

# response = boto3_bedrock.converse(
#             modelId=modelId,
#             messages=messages,
#             inferenceConfig=inference_config,
#     )
# response_body = response['output']['message']['content'][0]['text']


# print(response_body)



    





