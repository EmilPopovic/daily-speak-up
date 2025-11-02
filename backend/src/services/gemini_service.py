from google import genai
from google.genai.errors import APIError
from src.settings import Settings

class GeminiService:
    def __init__(self, settings: Settings):
        genai.configure(api_key=settings.gemini_api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash")
    
    async def generate_topic(self, interes: str) -> str:
        prompt = f"""
        Na temelju sljedećeg područja interesa: "{interes}"
        Generiraj zanimljivu i konkretnu temu za govor.
        Tema treba biti jasna, privlačna i relevantna.
        Odgovori samo s temom govora, bez dodatnih objašnjenja.
        Odgovori na hrvatskom jeziku.
        """
        
        try:
            response = await self.model.generate_content_async(prompt)
            return response.text.strip()
        except APIError as e:
            raise Exception(f"Gemini API greška: {str(e)}")
        except Exception as e:
            raise Exception(f"Greška pri generiranju teme: {str(e)}")
