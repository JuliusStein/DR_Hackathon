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
    if exclusive == True:
        messages=[
            {"role": "system", "content": "You are a categorical labeler for data science projects"},
            {"role": "user", "content": "Given a list of categories, categorize the following messages. Only assign one category for each message. Only assign messages to categories found in the given list. \nMessage: "+message+"\nList of categories: "+", ".join(categoryList)}
        ]
    else:
        messages=[
            {"role": "system", "content": "You are a categorical labeler for data science projects"},
            {"role": "user", "content": "Given a list of categories, categorize the following messages. Only assign messages to categories found in the given list. \nMessage: "+message+"\nList of categories: "+", ".join(categoryList)}
        ]
    response = client.chat.completions.create(
        model="gpt-4o",
            messages=messages
    )
    return response.choices[0].message.content

def encode_variables(message, variableList):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a machine learning variable encoder"},
            {"role": "user", "content": "Given a list of variables, assign each varaiable a boolean value of either True or False based on whether or not the text is related to that variable. Only assign values to variables found in the given list. \nMessage: "+message+"\nList of variables: "+", ".join(variableList)}
        ]
    )
    return response.choices[0].message.content

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