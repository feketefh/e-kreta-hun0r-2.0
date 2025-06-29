from __future__ import annotations
from typing import Self, TYPE_CHECKING, TypeVar, Any, Protocol, Type, Optional
from models import AuthToken

if TYPE_CHECKING:
    from pydantic import BaseModel

Primitive = str | int | float | bool | None
JsonSerializeable = Primitive | list[JsonSerializeable] | dict[str, JsonSerializeable]
DefaultReturnType = Any
Model = TypeVar("Model", BaseModel, list[BaseModel], DefaultReturnType)
SessionType = Any
DumpObj = TypeVar("DumpObj", bound = JsonSerializeable)

class SyncClient(Protocol[DumpObj]):
    """Synchronous client Protocol."""

    token: Optional[AuthToken]
    """Bearer token for authentication."""
    session: Optional[SessionType]
    """network handler of choice"""
    def __init__(self, token: AuthToken, *args: Any, **kwargs: Any) -> None: ...
    @classmethod
    def login(cls, user_name: str, password: str, institute_code: str, *args: Any, **kwargs: Any) -> Self:
        """
        Classmethod constructor for login.

        Args:
            user_name (str): The education id of the user.
            password (str): The default is the user's birthdate in the format YYYY-MM-DD.
            institute_code (str): The first of the 2 on [the site](https://intezmenykereso.e-kreta.hu/). Usually starts with klik.
        """

    def revokeToken(self) -> None:
        """
        Revokes the refresh token and closes the session.
        (access token may still be valid for a maximum of 1h)
        """

    def extendToken(self) -> None:
        """
        Extends the refresh and access tokens.
        Mostly only a helper method because the request function is supposed to make this call when needed.
        """

    def dump(self) -> DumpObj:
        """
        Dumps the client to a json serializable object.

        Returns:
            DumpObj: The json serializable object. It is supposed to match the argument of the load method.
        """

    @classmethod
    def load(cls, data: DumpObj, *args: Any, **kwargs: Any) -> Self:
        """
        Loads the client from a json serializable object.

        Args:
            data (DumpObj): The json serializable object. It is supposed to match the result of the dump method.
        """

    def request(self, *args: Any, model: Type[Model] = Type[DefaultReturnType], **kwargs: Any) -> Model:
        """
        Wrapper of the session's request method.
        It should auto fill `{institute_code}` fields with the user's institute code.
        It should also check if the token is valid and refresh it if needed.

        Args:
            model (Model, optional): if specified the response will be validated for this pydantic model.
                If not specified the return of the underlying network handler should be returned.

        Returns:
            Model: The model specified or the underlying network handler's return.
        """
    def is_closed(self) -> bool:
        """
        Used to tell if requests can be made with this session.
        Doesn't require the token to be valid.
        """

class AsyncClient(Protocol[DumpObj]):
    """ASynchronous client Protocol."""

    token: Optional[AuthToken]
    """Bearer token for authentication."""
    session: Optional[SessionType]
    """network handler of choice"""
    def __init__(self, token: AuthToken, *args: Any, **kwargs: Any) -> None: ...
    @classmethod
    async def login(cls, user_name: str, password: str, institute_code: str, *args: Any, **kwargs: Any) -> Self:
        """
        Classmethod constructor for login.

        Args:
            user_name (str): The education id of the user.
            password (str): The default is the user's birthdate in the format YYYY-MM-DD.
            institute_code (str): The first of the 2 on [the site](https://intezmenykereso.e-kreta.hu/). Usually starts with klik.
        """

    async def revokeToken(self) -> None:
        """
        Revokes the refresh token and closes the session.
        (access token may still be valid for a maximum of 1h)
        """

    async def extendToken(self) -> None:
        """
        Extends the refresh and access tokens.
        Mostly only a helper method because the request function is supposed to make this call when needed.
        """

    async def dump(self) -> DumpObj:
        """
        Dumps the client to a json serializable object.

        Returns:
            DumpObj: The json serializable object. It is supposed to match the argument of the load method.
        """

    @classmethod
    async def load(cls, data: DumpObj, *args: Any, **kwargs: Any) -> Self:
        """
        Loads the client from a json serializable object.

        Args:
            data (DumpObj): The json serializable object. It is supposed to match the result of the dump method.
        """

    async def request(self, *args: Any, model: Type[Model] = Type[DefaultReturnType], **kwargs: Any) -> Model:
        """
        Wrapper of the session's request method.
        It should auto fill `{institute_code}` fields with the user's institute code.
        It should also check if the token is valid and refresh it if needed.

        Args:
            model (Model, optional): if specified the response will be validated for this pydantic model.
                If not specified the return of the underlying network handler should be returned.

        Returns:
            Model: The model specified or the underlying network handler's return.
        """
    def is_closed(self) -> bool:
        """
        Used to tell if requests can be made with this session.
        Doesn't require the token to be valid.
        """

Client = SyncClient[JsonSerializeable] | AsyncClient[JsonSerializeable]
