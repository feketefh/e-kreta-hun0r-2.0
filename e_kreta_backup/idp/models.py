from datetime import datetime, timezone
from typing import Optional

import jwt
from pydantic import BaseModel, Field


class Header(BaseModel):
    alg: str = Field(alias="alg", frozen=True)
    """Signature or encryption algorithm"""
    kid: str = Field(alias="kid", frozen=True)
    """Key ID"""
    x5t: str = Field(alias="x5t", frozen=True)
    """X.509 Fingerprint (SHA-1)"""
    typ: str = Field(alias="typ", frozen=True)
    """Type of token"""


class AccessToken(BaseModel):
    iss: str = Field(alias="iss", frozen=True)
    """Issuer (who created and signed this token)"""
    nbf: datetime = Field(alias="nbf", frozen=True)
    """Not valid before"""
    iat: datetime = Field(alias="iat", frozen=True)
    """Issued at"""
    exp: datetime = Field(alias="exp", frozen=True)
    """Expiration time"""

    def is_expired(self) -> bool:
        return datetime.now(timezone.utc) > self.exp

    aud: list[str] = Field(alias="aud", frozen=True)
    """audience (who or what the token is intended for)"""
    scope: list[str] = Field(alias="scope", frozen=True)
    """Scope of the token"""
    amr: list[str] = Field(alias="amr", frozen=True)
    """Authentication Methods array"""
    client_id: str = Field(alias="client_id", frozen=True)
    """Client ID"""
    sub: str = Field(alias="sub", frozen=True)
    """Subject (whom the token refers to)"""
    auth_time: datetime = Field(alias="auth_time", frozen=True)
    """Time when authentication occurred"""
    idp: str = Field(alias="idp", frozen=True)
    """Identity Provider"""
    kreta_institute_user_idp_unique_id: str = Field(
        alias="kreta:institute_user_idp_unique_id", frozen=True
    )
    """kreta:institute_user_idp_unique_id"""
    kreta_institute_code: str = Field(alias="kreta:institute_code", frozen=True)
    """kreta:institute_code"""
    kreta_institute_user_id: str = Field(alias="kreta:institute_user_id", frozen=True)
    """kreta:institute_user_id"""
    kreta_institute_user_unique_id: str = Field(
        alias="kreta:institute_user_unique_id", frozen=True
    )
    """kreta:institute_user_unique_id"""
    name: str = Field(alias="name", frozen=True)
    """name"""
    kreta_user_name: str = Field(alias="kreta:user_name", frozen=True)
    """kreta:user_name"""
    role: str = Field(alias="role", frozen=True)
    """kreta:role"""
    kreta_user_type: str = Field(alias="kreta:user_type", frozen=True)
    """kreta:user_type"""
    sid: str = Field(alias="sid", frozen=True)
    """Session ID (String identifier for a Session)"""
    jti: str = Field(alias="jti", frozen=True)
    """JWT ID (unique identifier for this token)"""


class IdToken(BaseModel):
    iss: str = Field(alias="iss", frozen=True)
    """Issuer (who created and signed this token)"""
    nbf: datetime = Field(alias="nbf", frozen=True)
    """Not valid before"""
    iat: datetime = Field(alias="iat", frozen=True)
    """Issued at"""
    exp: datetime = Field(alias="exp", frozen=True)
    """Expiration time"""
    aud: str = Field(alias="aud", frozen=True)
    """audience (who or what the token is intended for)"""
    amr: list[str] = Field(alias="amr", frozen=True)
    """Authentication Methods array"""
    nonce: Optional[str] = Field(alias="nonce", frozen=True, default=None)
    """Unique value associating request to token"""
    at_hash: str = Field(alias="at_hash", frozen=True)
    """Access Token hash value"""
    sid: str = Field(alias="sid", frozen=True)
    """Session ID (String identifier for a Session)"""
    sub: str = Field(alias="sub", frozen=True)
    """Subject (whom the token refers to)"""
    auth_time: datetime = Field(alias="auth_time", frozen=True)
    """Time when authentication occurred"""
    idp: str = Field(alias="idp", frozen=True)
    """Identity Provider"""
    email: str = Field(alias="email", frozen=True)
    """Email address of user"""
    email_verified: bool = Field(alias="email_verified", frozen=True)
    """Email address has been verified"""
    kreta_institute_user_idp_unique_id: str = Field(
        alias="kreta:institute_user_idp_unique_id", frozen=True
    )
    """kreta:institute_user_idp_unique_id"""
    kreta_institute_code: str = Field(alias="kreta:institute_code", frozen=True)
    """kreta:institute_code"""
    kreta_institute_user_id: str = Field(alias="kreta:institute_user_id", frozen=True)
    """kreta:institute_user_id"""
    kreta_institute_user_unique_id: str = Field(
        alias="kreta:institute_user_unique_id", frozen=True
    )
    """kreta:institute_user_unique_id"""
    name: str = Field(alias="name", frozen=True)
    """name"""
    kreta_user_name: str = Field(alias="kreta:user_name", frozen=True)
    """kreta:user_name"""
    role: str = Field(alias="role", frozen=True)
    """kreta:role"""
    mfa_enabled: bool = Field(alias="mfa_enabled", frozen=True)
    """Multi Factor Authentication (MFA) enabled"""
    kreta_user_type: str = Field(alias="kreta:user_type", frozen=True)
    """kreta:user_type"""


class AuthToken:
    def __init__(
        self,
        id_token: str,
        access_token: str,
        expires_in: int,
        token_type: str,
        refresh_token: str,
        scope: str,
        *args,
        **kwargs,
    ) -> None:
        self.token_type = token_type
        self.expires_in = expires_in
        """duration of the token not actual seconds until expiration"""
        self.scope = scope.split()

        self.refresh_token = refresh_token

        self.token = access_token
        self.head = Header.model_validate(jwt.get_unverified_header(access_token))
        self.body = AccessToken.model_validate(
            jwt.decode(
                access_token,
                options={"verify_signature": False},
                algorithms=[self.head.alg],
            )
        )

        self.id_token = id_token
        self.id_head = Header.model_validate(jwt.get_unverified_header(id_token))
        self.id_body = IdToken.model_validate(
            jwt.decode(
                id_token,
                options={"verify_signature": False},
                algorithms=[self.id_head.alg],
            )
        )

    def __str__(self) -> str:
        return f"{self.token_type} {self.token}"

    def __repr__(self) -> str:
        return str(self)

    def is_expired(self) -> bool:
        return self.body.is_expired()
