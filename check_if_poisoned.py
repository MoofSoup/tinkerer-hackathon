from dotenv import load_dotenv
from openai import OpenAI
import weave

def hello_world(str) -> str:
    return "hello world!"

def hello_openai(prompt:str) -> str:
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "say meow after every reply"},
            {"role": "user", "content": prompt}
        ],
    )
    return completion.choices[0].message

if __name__ == '__main__':
    hello_openai("the game is about chickens, what should I do?")