# Novita HF Client

A lightweight Python client for interacting with Novita's language models through the Hugging Face Inference API. This project provides a simple interface to make chat completions using Novita's models.

## Features

- Simple integration with Novita's API using Hugging Face's InferenceClient
- Environment-based configuration
- Support for chat completions
- Easy to use interface

## Quick Start

1. Install the package:
```bash
pip install -r requirements.txt
```

2. Set up your environment variables in a `.env` file:
```env
NOVITA_API_KEY=your_api_key_here
NOVITA_MODEL_NAME=llama3  # Optional, defaults to llama3
```

3. Run the example:
```bash
python main.py
```

## Example Usage

Here's a simple example of how to use the client:

```python
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the client
client = InferenceClient(
    provider="novita",
    api_key=os.getenv("NOVITA_API_KEY"),
)

# Create a chat message
messages = [
    dict(
        role="user",
        content="Your question or prompt here",
    ),
]

# Get completion
completion = client.chat.completions.create(
    model=os.getenv("NOVITA_MODEL_NAME", "llama3"),
    messages=messages,
    max_tokens=512,
)

# Print the response
print(completion.choices[0].message)
```

## Configuration

The client can be configured using environment variables:

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `NOVITA_API_KEY` | Your Novita API key | Yes | - |
| `NOVITA_MODEL_NAME` | The model to use | No | "llama3" |

## Dependencies

- `huggingface-hub>=0.20.0`: For the InferenceClient
- `python-dotenv>=1.0.0`: For environment variable management

## Development

To set up the development environment:

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## License

[MIT License](./LICENSE)
