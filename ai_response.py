import os
from openai import AzureOpenAI
from dotenv import load_dotenv
def response(prompt):
    load_dotenv()
    client = AzureOpenAI(
    api_key = os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version="2024-02-15-preview",
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    )

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
                {"role": "system", "content": 'you are an expert in software development and analysis'},
                {"role": "user", "content":prompt},
        ]
    )
    return (response.choices[0].message.content)

