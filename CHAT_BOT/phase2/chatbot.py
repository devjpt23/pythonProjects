import os
from dotenv import load_dotenv
import openai
from promptlayer import PromptLayer

load_dotenv('.env')
promplayer_client = PromptLayer(api_key=os.getenv("PROMPTLAYER_API_KEY"))

OpenAI = promplayer_client.openai.OpenAI
client = OpenAI()

user_input = input("Hello my name is Bob, may I please take your order?")

mychatbot_prompt = promplayer_client.templates.get("MyChatBOT",{
    "provider":"openai",
    "input_variables":{
        "question": user_input
    }
})

response = client.chat.completions.create(
    **mychatbot_prompt['llm_kwargs'],
    pl_tags=["mychatgpt-dev"],
)

print(response.choices[0].message.content)
