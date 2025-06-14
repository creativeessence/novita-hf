from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()

NOVITA_API_KEY = os.getenv("NOVITA_API_KEY")
NOVITA_MODEL_NAME = os.getenv("NOVITA_MODEL_NAME", "llama3")


client = InferenceClient(
    provider="novita",
    api_key=NOVITA_API_KEY,
)

# an example question
messages = [
    dict(
        role="user",
        content="Sally (a girl) has 3 brothers. Each brother has 2 sisters. How many sisters does Sally have?",
    ),
]
completion = client.chat.completions.create(
    # model="meta-llama/llama-3.3-70b-instruct",
    model=NOVITA_MODEL_NAME,
    messages=messages,
    max_tokens=512,
)

print(completion.choices[0].message)
