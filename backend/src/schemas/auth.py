from typing import TypedDict

class SessionPayload(TypedDict):
    sub: str  # SuperTokens user_id
    session_handle: str
