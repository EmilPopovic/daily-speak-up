import logging
from datetime import datetime, timezone
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

logger = logging.getLogger(__name__)
router = APIRouter(tags=['health'])

@router.get('/health')
async def health():
    """Basic health check (returns 200 OK)"""
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'status': 'ok',
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'service': 'DailySpeakUp API'
        }
    )
