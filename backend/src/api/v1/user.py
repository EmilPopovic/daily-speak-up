import logging
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from ..deps import get_session
from ...db import get_db
from ...schemas import UserResponse, UserCreate
from ...models import User
from supertokens_python.recipe.session import SessionContainer

logger = logging.getLogger(__name__)
router = APIRouter(tags=['user'], prefix='/user')

@router.put('/register', response_class=JSONResponse)
async def register(
    user_data: UserCreate,
    db: Session = Depends(get_db),
    session: SessionContainer = Depends(get_session)
):
    # Get user_id from SuperTokens session
    supertokens_user_id = session.get_user_id()
    
    existing_user: User | None = db.query(User).filter(
        User.supertokens_user_id == supertokens_user_id
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='User already exists'
        )

    user = User(
        supertokens_user_id=supertokens_user_id,
        email=user_data.email,
        handle=supertokens_user_id,  # Default handle
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
async def me(
    db: Session = Depends(get_db),
    session: SessionContainer = Depends(get_session)
):
    supertokens_user_id = session.get_user_id()

    user: User | None = db.query(User).filter(
        User.supertokens_user_id == supertokens_user_id
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
