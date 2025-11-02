from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from src.services.gemini_service import GeminiService
from src.settings import get_settings, Settings
from src.models.enums import AppLang

router = APIRouter(prefix='/topics', tags=['Topics'])

class TopicRequest(BaseModel):
    interes: str = Field(..., min_length=1, description="Područje interesa korisnika / User's area of interest")
    lang: AppLang = Field(default=AppLang.EN, description="Jezik korisnika / User's language")
    
    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "interes": "glazba",
                    "lang": "hr"
                },
                {
                    "interes": "music",
                    "lang": "en"
                }
            ]
        }

class TopicResponse(BaseModel):
    tema: str
    lang: AppLang

def get_gemini_service(settings: Settings = Depends(get_settings)) -> GeminiService:
    """Dependency injection za GeminiService."""
    return GeminiService(settings)

@router.post('/generate', response_model=TopicResponse, status_code=status.HTTP_200_OK)
async def generate_topic(
    request: TopicRequest,
    gemini_service: GeminiService = Depends(get_gemini_service)
):
    """
    Generira temu govora na temelju interesa korisnika.
    Generates a speech topic based on user's interest.
    
    - **interes**: Područje interesa / Area of interest (e.g., "technology", "sport", "music")
    - **lang**: Jezik / Language (en or hr)
    """
    try:
        tema = await gemini_service.generate_topic(request.interes, request.lang)
        return TopicResponse(tema=tema, lang=request.lang)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error generating topic: {str(e)}"
        )