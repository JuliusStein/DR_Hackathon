import os
from openai import AzureOpenAI

client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version="2024-02-01"
)

#translation_test_message = "Un entretenimiento fascinante, con pasajes de inusual belleza, servido con mano maestra por James Cameron. Es también un alegato ecologista y pacifista, justo en tiempos de creciente militarismo y abuso de recursos naturales."
sentiment_test_message = "I am very happy with the service I received today. The staff was very friendly and helpful."
emotionList = ['happy', 'sad', 'angry', 'neutral']
response = client.chat.completions.create(
        model="gpt-4o", # model = "deployment_name".
        messages=[
            {"role": "system", "content": "You are a sentiment analyzer."},
            {"role": "user", "content": "Score the following message according to these emotions: " + str(emotionList) + ". Message: " + sentiment_test_message}
        ],
        max_tokens=100
    )

print(response.choices[0].message.content)