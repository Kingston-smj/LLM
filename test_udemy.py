import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
from transformers import pipeline

# Load environment variables
load_dotenv(override=True)
api_key = os.getenv('HF_TOKEN')

if not api_key:
    print("No Hugging Face API key found - please add it to your .env file")
else:
    print("API key found!")

class HuggingFace:
    def __init__(self, model_name="gpt2"):
        # Initialize the text generation pipeline with the specified model
        self.generator = pipeline('text-generation', model=model_name)

    def generate_text(self, prompt, max_length=50, num_return_sequences=1):
        # Generate text based on the prompt
        return self.generator(prompt, max_length=max_length, num_return_sequences=num_return_sequences)

# Create an instance of the HuggingFace class
hugging_face = HuggingFace(model_name="gpt2")  # You can specify any model available on Hugging Face

# Your message
message = "Hello, GPT! This is my first ever message to you! Hi!"

# Generate a response using the HuggingFace instance
response = hugging_face.generate_text(message, max_length=50, num_return_sequences=1)

# Print the generated response
print(response[0]['generated_text'])