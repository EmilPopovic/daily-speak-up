from fastapi import Request, HTTPException, status
from supertokens_python.recipe.session.framework.fastapi import verify_session
from supertokens_python.recipe.session import SessionContainer
from typing import Optional

class UnauthenticatedException(HTTPException):
    def __init__(self, detail: str) -> None:
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=detail)

class AuthService:
    """
    SuperTokens-based authentication service.
    Uses session-based authentication instead of JWT verification.
    """
    
    def __init__(self) -> None:
        pass
    
    async def verify(self, session: SessionContainer) -> dict:
        """
        Verify the user's session and return user info.
        
        Args:
            session: The SuperTokens session container (injected by verify_session)
        
        Returns:
            dict with 'sub' (user_id) and other session data
        """
        user_id = session.get_user_id()
        
        return {
            'sub': user_id,
            'session_handle': session.get_handle(),
        }

# FastAPI dependency for protected routes
async def get_session(request: Request):
    """
    FastAPI dependency that verifies the session.
    Use with Depends() in route handlers.
    """
    session = await verify_session()(request)
    return session
