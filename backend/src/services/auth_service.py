from fastapi.security import (
    SecurityScopes,
    HTTPAuthorizationCredentials,
    HTTPBearer,
)
from fastapi import Depends, HTTPException, status
from typing import Any, Dict, Optional
from jose import jwt, JWTError
from ..api.config import get_settings
from ..schemas import JWTPayload

class UnauthenticatedException(HTTPException):
    def __init__(self, detail: str) -> None:
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=detail)

class AuthService:
    
    def __init__(self) -> None:
        self.config = get_settings()
        self.jwks: Optional[Dict[str, Any]] = None

    async def _get_jwks(self) -> Dict[str, Any]:
        """Get the JWKS from Auth0."""
        if self.jwks is None:
            import httpx
            async with httpx.AsyncClient() as client:
                jwks_url = f'https://{self.config.auth0_domain}/.well-known/jwks.json'
                response = await client.get(jwks_url)
                self.jwks = response.json()
        assert self.jwks is not None
        return self.jwks

    async def verify(
            self,
            security_scopes: SecurityScopes,
            token: Optional[HTTPAuthorizationCredentials] = Depends(HTTPBearer())
    ) -> JWTPayload:
        if token is None:
            raise UnauthenticatedException('No token')

        try:
            jwks = await self._get_jwks()
            payload = jwt.decode(
                token.credentials,
                jwks,
                algorithms=self.config.auth0_algorithms,
                audience=self.config.auth0_api_audience,
                issuer=self.config.auth0_issuer,
            )
        except JWTError as error:
            raise UnauthenticatedException(str(error))

        if len(security_scopes.scopes) > 0:
            self._check_claims(payload, 'scope', security_scopes.scopes)

        return JWTPayload(**payload)
        
    def _check_claims(self, payload, claim_name, expected_value):
        if claim_name not in payload:
            raise UnauthenticatedException(detail=f'No claim "{claim_name}" found in token')

        payload_claim = payload[claim_name]

        if claim_name == 'scope':
            payload_claim = payload[claim_name].split(' ')

        for value in expected_value:
            if value not in payload_claim:
                raise UnauthenticatedException(detail=f'Missing "{claim_name}" scope')
