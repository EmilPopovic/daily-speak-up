from fastapi import APIRouter, Depends, HTTPException, status

from ...schemas import TopicRequest, TopicResponse
from ...services.gemini_service import GeminiService
from ..deps import get_gemini_service


router = APIRouter(prefix='/topics', tags=['Topics'])


@router.post(
    '/generate', 
    response_model=TopicResponse, 
    status_code=status.HTTP_200_OK
)
async def generate_topic(
    request: TopicRequest,
    gemini_service: GeminiService = Depends(get_gemini_service)
):
    try:
        tema = await gemini_service.generate_topic(request.interes, request.lang)
        return TopicResponse(tema=tema, lang=request.lang)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error generating topic: {str(e)}"
        )