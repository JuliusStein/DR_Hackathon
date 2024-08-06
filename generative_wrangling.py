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
            {"role": "system", "content": "You are an assistant specializing in rephrasing."},
            {"role": "user", "content": "Rephrase the following message using a " + tone + " tone: " + message}
        ],
        max_tokens=length,
        temperature=0.85
    )
    return response.choices[0].message.content

def summarize_message(message, length):
    response = client.chat.completions.create(
        model="gpt-4o", # model = "deployment_name".
        messages=[
            {"role": "system", "content": "You are an assistant specializing in summarizing."},
            {"role": "user", "content": "Summarize the following message into a more concise format: " + message}
        ],
        max_tokens=length,
        temperature=0.7
    )
    return response.choices[0].message.content

def label_categories(message, categoryList, exclusive):
    pass

def encode_variables(message, variableList):
    pass

def translate_message(message, outputLang):
    response = client.chat.completions.create(
        model="gpt-4o", # model = "deployment_name".
        messages=[
            {"role": "system", "content": "You are a translator."},
            {"role": "user", "content": "Translate the following message into English: " + message}
        ],
        max_tokens=50,
        temperature=0.6
    )
    return response.choices[0].message.content

def analyze_sentiment(message, emotionList):
    response = client.chat.completions.create(
        model="gpt-4o", # model = "deployment_name".
        messages=[
            {"role": "system", "content": "You are a sentiment analyzer."},
            {"role": "user", "content": "Score the following message according to these emotions: " + str(emotionList) + ". Message: " + message}
        ],
        max_tokens=100
    )