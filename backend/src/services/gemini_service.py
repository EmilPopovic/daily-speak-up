from google import genai
from ..models import AppLang


class GeminiService:
    def __init__(self, api_key: str, model_id: str):
        self.client = genai.Client(api_key=api_key)
        self.model_id = model_id
    
    async def generate_topic(self, interes: str, lang: AppLang = AppLang.EN) -> str:
    
        # Prompt prema jeziku
        if lang == AppLang.HR:
            prompt = f"""Na temelju sljedećeg područja interesa: "{interes}"
Generiraj zanimljivu i konkretnu temu za govor.
Tema treba biti jasna, privlačna i relevantna.
Odgovori samo s temom govora, bez dodatnih objašnjenja.
Odgovori na hrvatskom jeziku."""
        else:
            prompt = f"""Based on the following area of interest: "{interes}"
Generate an interesting and specific speech topic.
The topic should be clear, engaging, and relevant.
Respond only with the speech topic, without additional explanations.
Respond in English."""
        
        try:
            response = await self.client.aio.models.generate_content(
                model=self.model_id,
                contents=prompt
            )
            
            if response.text is None:
                raise Exception('No text in response from Gemini API')
            
            return response.text.strip()
        except Exception as e:
            raise Exception(f"Error generating topic: {str(e)}")