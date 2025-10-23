import sys
import logging
from datetime import datetime, timezone
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from sqlalchemy import select, literal
from ..config import get_settings
from ...db import engine

logger = logging.getLogger(__name__)
router = APIRouter(tags=['health'], prefix='/health')

@router.get('/')
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

@router.get('/detailed')
async def detailed():
    """Detailed health check including database connectivity"""
    health_status = {
        'status': 'ok',
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'service': 'DailySpeakUp API',
        'checks': {}
    }

    try:
        with engine.connect() as conn:
            conn.execute(select(literal(1)))
        health_status['checks']['database'] = {
            'status': 'ok',
            'message': 'connected',
        }
    except Exception as e:
        health_status['checks']['database'] = {
            'status': 'ok',
            'message': f'Connection failed: {str(e)}',
        }
        health_status['status'] = 'degraded'

    health_status['checks']['environment'] = {
        'status': 'ok',
        'python_version': sys.version,
        'environment': get_settings().environment
    }

    return JSONResponse(
        status_code=status.HTTP_200_OK if health_status['status'] == 'ok' else status.HTTP_503_SERVICE_UNAVAILABLE,
        content=health_status
    )
