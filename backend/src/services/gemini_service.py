from google import genai
from google.genai.errors import APIError
import os
from dotenv import load_dotenv

load_dotenv()

class GeminiService:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        genai.configure(api_key = self.api_key)

        self.model = genai.GenerativeModel("gemini-2.5-flash")
        