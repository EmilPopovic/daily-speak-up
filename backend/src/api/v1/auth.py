import logging
from fastapi import APIRouter, Security
from ..deps import get_auth_service

logger = logging.getLogger(__name__)
router = APIRouter(tags=['auth'], prefix='/auth')

@router.get("/private")
def private(auth_result: str = Security(get_auth_service().verify)):
    """A valid access token is required to access this route"""
    return auth_result
