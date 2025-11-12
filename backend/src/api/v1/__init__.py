from .health import router as health_router
from .user import router as user_router
from .topic import router as topic_router
from .userdata import router as userdata_router

__all__ = [
    'health_router',
    'user_router',
    'topic_router',
    'userdata_router',
]
