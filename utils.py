# utils.py
import os
from dotenv import load_dotenv

load_dotenv()  # Charge .env si présent

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def get_openai_api_key():
    return OPENAI_API_KEY   # or return "sk-..."