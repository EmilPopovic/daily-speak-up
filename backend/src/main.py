import logging
from fastapi import FastAPI, status, Request
from fastapi.responses import JSONResponse

from .api.v1 import (
    health_router,
    user_router,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(health_router, prefix='/api/v1')
app.include_router(user_router, prefix='/api/v1')

@app.get('/', tags=['Root'])
async def root():
    """Root endpoint with API information."""
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'message': 'DailySpeakAPI',
            'version': '1.0.0',
            'docs': '/docs',
            'base': '/api/v1',
            'health': '/api/v1/health'
        }
    )

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f'Global exception handler caught in {request.url.path}: {exc}')
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            'detail': 'Internal server error'
        }
    )

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8123)
