from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from ...db import get_db
from ...models import User

router = APIRouter(prefix="/handles", tags=["Handles"])


@router.get("/check")
async def check_handle_availability(
    handle: str,
    db: Session = Depends(get_db)
):
    """Check if a handle is available."""
    existing_user: User | None = db.query(User).filter(
        User.handle == handle
    ).first()
    
    return {
        "available": existing_user is None
    }
