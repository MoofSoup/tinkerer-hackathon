from dotenv import load_dotenv
from openai import OpenAI
import weave
import openai

load_dotenv('.env')
weave.init("tinkerer-project")

from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)