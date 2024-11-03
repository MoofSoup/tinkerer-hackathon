from dotenv import load_dotenv
from openai import OpenAI
import weave

def hello_world(str) -> str:
    return "hello world!"

def prompt_openai(prompt:str) -> str:
    load_dotenv('.env')
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "say meow after every reply"},
            {"role": "user", "content": prompt}
        ],
    )
    return completion.choices[0].message.content

async def prompt_gemini():
    return True

if __name__ == '__main__':
    val = hello_openai("the game is about chickens, what should I do?")
    print(val)

