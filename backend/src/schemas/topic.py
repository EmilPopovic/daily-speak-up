from pydantic import BaseModel, Field
from ..models.enums import AppLang


class TopicRequest(BaseModel):
    """Request model for topic generation."""
    
    interes: str = Field(
        ..., 
        min_length=1, 
        description="Područje interesa korisnika / User's area of interest"
    )
    lang: AppLang = Field(
        default=AppLang.EN, 
        description="Jezik korisnika / User's language"
    )
    
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
    """Response model for topic generation."""
    
    tema: str
    lang: AppLang