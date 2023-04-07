import os
from dotenv import load_dotenv
import openai

# Load .env info
load_dotenv(dotenv_path=".env")

#  openai sets
openai.organization = os.getenv("ORGANIZATION_ID")
openai.api_key = os.getenv("API_KEY")
openai.Model.list()

# test functions
# print(os.getenv("ORGANIZATION_ID"))
# print(openai.Model.list)

def loopGPT() -> None:
    print('Running...')
    
    while True:
        message = input("\n[@] You: ")
        
        if message.lower() == "\exit":
            print("\n[@] Exiting...")
            break

        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message}]
        )

        print(f"\n[@] ChatGPT: {completion.choices[0].message.content}")

loopGPT()