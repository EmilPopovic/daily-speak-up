import logging
from fastapi import APIRouter, Security, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from ..deps import get_auth_service
from ...db import get_db
from ...schemas import JWTPayload
from ...models import User

logger = logging.getLogger(__name__)
router = APIRouter(tags=['user'], prefix='/user')

@router.put('/register', response_model=JSONResponse)
def register(
    db: Session = Depends(get_db),
    auth_result: JWTPayload = Security(get_auth_service().verify)
):
    auth0_user_id = auth_result['sub']

    existing_user: User | None = db.query(User).filter(
        User.auth0_user_id == auth0_user_id
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='User already exists.'
        )
    
    user = User(
        auth0_user_id=auth0_user_id,
        email=auth_result['email'],
        handle=auth0_user_id,
    )
    db.add(user)
    db.flush()
    db.commit()

    return status.HTTP_200_OK
