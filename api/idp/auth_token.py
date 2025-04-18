from functools import partial
from datetime import datetime, timedelta
from pydantic import BaseModel, Field
import jwt

field = partial(Field, frozen=True)

class Auth_Token:
    def __init__(self, token: str, id_token: str, token_type: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.token_type = token_type
        self.token = token
        self.head = jwt.get_unverified_header(token)
        self.body = jwt.decode(token, verify=False, algorithms=[self.head["alg"]])
        self.id_token = id_token
        self.id_head = jwt.get_unverified_header(id_token)
        self.id_body = jwt.decode(id_token, verify=False, algorithms=[self.id_head["alg"]])

    def __str__(self) -> str:
        """
        Returns a string representation of the access token in the format
        "token_type access_token", for example "Bearer myaccesstoken"
        """        
        return f"{self.token_type} {self.token}"
    
    def __repr__(self) -> str:        
        """
        Returns a string representation of the access token.

        Returns
        -------
        str
            A string representation of the access token in the format
            "token_type access_token", for example "Bearer myaccesstoken"
        """
        return self.__str__()

class Token(BaseModel):
    def __str__(self) -> str:
        """
        Returns a string representation of the access token in the format
        "token_type access_token", for example "Bearer myaccesstoken"
        """        
        return f"{self.token_type} {self.access_token}"
    
    def __repr__(self) -> str:        
        """
        Returns a string representation of the access token.

        Returns
        -------
        str
            A string representation of the access token in the format
            "token_type access_token", for example "Bearer myaccesstoken"
        """
        return self.__str__()
    
    def is_expired(self) -> bool:
        """Whether the access token has expired."""
        return datetime.now() > self.exp
    
    def expires_in(self) -> timedelta:
        """The number of seconds until the access token expires."""
        return self.exp - datetime.now()
    
    iss: str = field(alias="iss")
    """The issuer of the access token."""
    
    nbf: datetime = field(alias="nbf")
    """The time at which the access token becomes valid."""
    
    iat: datetime = field(alias="iat")
    """The time at which the access token was issued."""
    
    exp: datetime = field(alias="exp")
    """The time at which the access token expires."""
    
    aud: list[str] = field(alias="sub")
    """The audience of the access token."""
    
    scope: list[str] = field(alias="scope")
    """The scope of the access token."""
    
    amr: list[str] = field(alias="amr")
    """Authentication Methods."""
    
    client_id: str = field(alias="client_id")
    """The client_id of the access token."""
    
    sub: str = field(alias="sub")
    """The subject of the access token. This is the unique identifier of the user."""
    
    auth_time: datetime = field(alias="auth_time")
    """The time at which the user last authenticated. This is the time when the
    authentication took place, not when the access token was issued."""
    
    idp: str = field(alias="idp")
    """The Identity Provider of the user."""
    
    kreta_institute_user_idp_unique_id: str = field(alias="kreta:institute_user_idp_unique_id")
    """The unique identifier of the user at the Identity Provider of the user."""
    
    kreta_institute_code: str = field(alias="kreta:institute_code")
    """The code of the institution of the user."""
    
    kreta_institute_user_id: str = field(alias="kreta:institute_user_id")
    """The unique identifier of the user in the institution."""
    
    kreta_institute_user_unique_id: str = field(alias="kreta:institute_user_unique_id")
    """The unique identifier of the user in the institution. This is the identifier that
    is unique accross all institutions and identity providers."""
    
    kreta_school_year_id: str = field(alias="kreta:school_year_id")
    """The identifier of the school year in the institution."""
    
    kreta_school_year_unique_id: str = field(alias="kreta:school_year_unique_id")
    """The unique identifier of the school year in the institution. This is the identifier that
    is unique accross all institutions and identity providers."""
    
    kreta_institute_unique_id: str = field(alias="")
    """The unique identifier of the institution. This is the identifier thkreta:institute_unique_idat
    is unique accross all institutions and identity providers."""
    
    name: str = field(alias="name")
    """The full name of the user."""
    
    kreta_user_name: str = field(alias="kreta:user_name")
    """The username of the user in the institution."""
    
    role: str = field(alias="kreta:role")
    """The role of the user in the institution. The possible values are:
    - Tanulo (no more are known)"""
    
    kreta_user_type: str = field(alias="kreta:user_type")
    """The type of the user. The possible values are:
    - Tanulo (no more are known)"""
    
    sid: str = field(alias="sid")
    """The session id of the user. This is the identifier of the user
    in the session. This is unique accross all institutions and identity providers."""
    
    jti: str = field(alias="jti")
    """The JWT Token Identifier. This is the identifier of the JWT token.
    This is unique accross all institutions and identity providers."""
