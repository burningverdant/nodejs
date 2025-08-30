# vexyapi.py
from ollama import Client

MODEL_NAME = "llama3.2:1b"  # Change model here

class VexyAPI:
    def __init__(self):
        self.client = Client()

    def generate_response(self, messages):
        """Query Ollama model with chat messages."""
        response = self.client.chat(model=MODEL_NAME, messages=messages)
        return response["message"]["content"]
