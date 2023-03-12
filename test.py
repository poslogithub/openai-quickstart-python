# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "あなたは琴葉茜です。"},              # 最初の質問
        {"role": "user", "content": "妹は元気？"},              # 最初の質問
    ],
    stream=True
)
for obj in response:
    print(obj.get('choices')[0].get('delta').get('content'))
print(response)
#print(response.get('choices')[0].get('message').get('content'))
