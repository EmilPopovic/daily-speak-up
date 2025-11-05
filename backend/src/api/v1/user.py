import logging
from fastapi import APIRouter, Security, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from ..deps import get_auth_service
from ...db import get_db
from ...schemas import JWTPayload, UserResponse, UserCreate
from ...models import User

logger = logging.getLogger(__name__)
router = APIRouter(tags=['user'], prefix='/user')

@router.put('/register', response_class=JSONResponse)
def register(
    user_data: UserCreate,
    db: Session = Depends(get_db),
    _: JWTPayload = Security(get_auth_service().verify)
):
    existing_user: User | None = db.query(User).filter(
        User.auth0_user_id == user_data.auth0_id
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='User already exists'
        )

    user = User(
        auth0_user_id=user_data.auth0_id,
        email=user_data.email,
        handle=user_data.auth0_id,
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'message': 'ok'
        }
    )

@router.get('/me', response_model=UserResponse, status_code=status.HTTP_200_OK)
def me(
    db: Session = Depends(get_db),
    auth_result: JWTPayload = Security(get_auth_service().verify),
):
    auth0_user_id = auth_result['sub']

    user: User | None = db.query(User).filter(
        User.auth0_user_id == auth0_user_id
    ).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found'
        )

    return UserResponse(
        role=user.role,
        email=user.email,
        handle=user.handle,
        profile_picture_url=user.profile_picture_url,
        onboarding_status=user.onboarding_status,
        preferred_lang=user.preferred_lang,
        preferred_theme=user.preferred_theme,
        preferred_tz_offset=user.preferred_tz_offset,
        email_notifications_enabled=user.email_notifications_enabled,
        push_notifications_enabled=user.push_notifications_enabled,
        streak_reminders_enabled=user.streak_reminders_enabled,
    )
