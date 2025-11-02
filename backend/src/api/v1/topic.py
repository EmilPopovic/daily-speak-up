from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from src.services.gemini_service import GeminiService
from src.settings import get_settings, Settings

router = APIRouter(prefix='/topics', tags=['Topics'])

class TopicRequest(BaseModel):
    interes: str = Field(..., min_length=1, description="Područje interesa korisnika")
    
    class Config:
        json_schema_extra = {
            "example": {
                "interes": "umjetna inteligencija"
            }
        }

class TopicResponse(BaseModel):
    tema: str

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
    
    - **interes**: Područje interesa (npr. "tehnologija", "sport", "glazba")
    """
    try:
        tema = await gemini_service.generate_topic(request.interes)
        return TopicResponse(tema=tema)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Greška pri generiranju teme: {str(e)}"
        )