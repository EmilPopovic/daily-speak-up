from typing import TypedDict, List, Union, Required

class JWTPayload(TypedDict, total=False):
    iss: Required[str]
    sub: Required[str]
    aud: Required[Union[str, List[str]]]
    iat: Required[int]
    exp: Required[int]
    gty: Required[str]
    azp: Required[str]
    scope: str
    email: Required[str]
