import os
from openai import AzureOpenAI

client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version="2024-02-01"
)

def rephrase_message(message, tone, length):
    response = client.chat.completions.create(
        model="gpt-4o", # model = "deployment_name".
        messages=[
            {"role": "system", "content": "Rephrase the following message using a " + tone + " tone."},
            {"role": "user", "content": message}
        ],
        max_tokens=length
    )
    return response.choices[0].message.content

def summarize_message(message, length):
    response = client.chat.completions.create(
        model="gpt-4o", # model = "deployment_name".
        messages=[
            {"role": "system", "content": "Summarize the following message."},
            {"role": "user", "content": message}
        ],
        max_tokens=length
    )
    return response.choices[0].message.content

def label_categories(message, categoryList, exclusive):
    pass

def encode_variables(message, variableList):
    pass

def translate_message(message, inputLang, outputLang):
    pass

def analyze_sentiment(message, emotionList):
    pass