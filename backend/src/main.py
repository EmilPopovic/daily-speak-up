import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, status, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# SuperTokens imports
from supertokens_python import get_all_cors_headers
from supertokens_python.framework.fastapi import get_middleware

from .api.v1 import (
    health_router,
    user_router,
    topic_router
)
from .services.supertokens_service import init_supertokens
from .api.config import get_settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get settings
settings = get_settings()

# Initialize SuperTokens BEFORE creating the app
init_supertokens()
logger.info("SuperTokens initialized")

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan events"""
    try:
        logger.info("Running startup tasks...")
        logger.info("Startup tasks completed successfully")
    except Exception as e:
        logger.error(f"Error during startup: {e}")
        raise
    yield
    logger.info("Application shutdown")

app = FastAPI(lifespan=lifespan)

# Add CORS middleware (must be before SuperTokens middleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.website_domain],
    allow_credentials=True,
    allow_methods=["GET", "PUT", "POST", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["Content-Type"] + get_all_cors_headers(),
)

# Add SuperTokens middleware
app.add_middleware(get_middleware())

# Include routers
app.include_router(health_router, prefix='/api/v1')
app.include_router(user_router, prefix='/api/v1')
app.include_router(topic_router, prefix='/api/v1')

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
            'health': '/api/v1/health',
            'topics': '/api/v1/topics'
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
