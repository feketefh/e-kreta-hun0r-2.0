from __future__ import annotations
from typing import Self, TYPE_CHECKING, TypeVar, Type, get_origin, get_args, Any, Optional
from urllib.parse import urlparse, parse_qs
from aiohttp import ClientSession, ClientResponse
from bs4 import BeautifulSoup as bs
from models import AuthToken
from bs4.element import Tag
from warnings import warn

if TYPE_CHECKING:
    from pydantic import BaseModel

Primitive = str | int | float | bool | None
Model = TypeVar("Model", BaseModel, list[BaseModel], ClientResponse)

def raise_exception(message: str) -> None:
    raise Exception(message)

class AsyncClient:
    """ASynchronous client Protocol."""

    token: Optional[AuthToken]
    """Bearer token for authentication."""
    session: Optional[ClientSession]
    """network handler of choice"""

    def __init__(
        self, token: AuthToken, *args: Any, session: Optional[ClientSession] = None, **kwargs: Any
    ) -> None:
        self.token = token
        if session is None:
            session = ClientSession(*args, **kwargs)
        elif args or kwargs:
            raise ValueError(
                "Already instanced session cannot have additional arguments"
            )
        self.session = session

    @classmethod
    async def login(
        cls, user_name: str, password: str, institute_code: str, *args: Any, **kwargs: Any
    ) -> Self:
        """
        Classmethod constructor for login.

        Args:
            user_name (str): The education id of the user.
            password (str): The default is the user's birthdate in the format YYYY-MM-DD.
            institute_code (str): The first of the 2 on [the site](https://intezmenykereso.e-kreta.hu/). Usually starts with klik.
        """

        async with ClientSession("https://idp.e-kreta.hu", *args, **kwargs) as session:
            async with session.request(
                "GET",
                "/Account/Login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fprompt%3Dlogin%26nonce%3DwylCrqT4oN6PPgQn2yQB0euKei9nJeZ6_ffJ-VpSKZU%26response_type%3Dcode%26code_challenge_method%3DS256%26scope%3Dopenid%2520email%2520offline_access%2520kreta-ellenorzo-webapi.public%2520kreta-eugyintezes-webapi.public%2520kreta-fileservice-webapi.public%2520kreta-mobile-global-webapi.public%2520kreta-dkt-webapi.public%2520kreta-ier-webapi.public%26code_challenge%3DHByZRRnPGb-Ko_wTI7ibIba1HQ6lor0ws4bcgReuYSQ%26redirect_uri%3Dhttps%253A%252F%252Fmobil.e-kreta.hu%252Fellenorzo-student%252Fprod%252Foauthredirect%26client_id%3Dkreta-ellenorzo-student-mobile-ios%26state%3Dkreten_student_mobile%26suppressed_prompt%3Dlogin",
            ) as response:
                html = await response.text()

            soup = bs(html, "html.parser")

            _rvt = soup.find("input", {"name": "__RequestVerificationToken"})
            _return_url = soup.find("input", {"name": "ReturnUrl"})
            _is_temporary_login = soup.find("input", {"name": "IsTemporaryLogin"})
            _login_type = soup.find("input", {"name": "loginType"})
            if not (isinstance(_rvt, Tag) and isinstance(_return_url, Tag) and isinstance(_is_temporary_login, Tag) and isinstance(_login_type, Tag)):
                raise Exception("Could not find all inputs")
            rvt = _rvt["value"]
            return_url = _return_url["value"]
            is_temporary_login = _is_temporary_login["value"]
            login_type = _login_type["value"]
            if not (isinstance(rvt, str) and isinstance(return_url, str) and isinstance(is_temporary_login, str) and isinstance(login_type, str)):
                raise Exception("Could not find all inputs")

            login_form_data = {
                "ReturnUrl": return_url,
                "IsTemporaryLogin": is_temporary_login,
                "UserName": user_name,
                "Password": password,
                "InstituteCode": institute_code,
                "loginType": login_type,
                "__RequestVerificationToken": rvt,
            }

            # TODO: check if headers are required
            # get cookies NOT useless
            async with session.request(
                "POST",
                "/account/login",
                data=login_form_data,
                allow_redirects=False,
            ) as response:
                pass

            async with session.request(
                "GET",
                return_url,
                allow_redirects=False,
            ) as response:
                headers = response.headers
                url = urlparse(headers["Location"])
                code = parse_qs(url.query)["code"][0]

            token_form = {
                "code": code,
                "code_verifier": "DSpuqj_HhDX4wzQIbtn8lr8NLE5wEi1iVLMtMK0jY6c",
                "redirect_uri": "https://mobil.e-kreta.hu/ellenorzo-student/prod/oauthredirect",
                "client_id": "kreta-ellenorzo-student-mobile-ios",
                "grant_type": "authorization_code",
            }

            async with session.request(
                "POST",
                "/connect/token",
                data=token_form,
            ) as response:
                token_data = await response.json()

        token = AuthToken(**token_data)

        return cls(token, *args, **kwargs)

    async def revokeToken(self) -> None:
        """
        Revokes the refresh token and closes the session.
        (access token may still be valid for a maximum of 1h)
        """
        if not self.token:
            warn("Token already revoked!")
            return
        if not self.session or self.session.closed:
            raise Exception("Can't revoke token without active session!")
        data = {
            "token": self.token.refresh_token,
            "client_id": self.token.body.client_id,
        }
        async with self.session.request(
            "POST",
            "https://idp.e-kreta.hu/connect/revocation",
            data=data,
        ) as response:  # noqa: F841
            pass
        self.token = None
        await self.session.close()
        self.session = None

    async def extendToken(self) -> None:
        """
        Extends the refresh and access tokens.
        Mostly only a helper method because the request function is supposed to make this call when needed.
        """
        if not self.token:
            raise Exception("Can't extend token without active token!")
        data = await self._refresh2access(
            self.token.body.kreta_institute_code,
            self.token.refresh_token,
            self.token.body.client_id,
        )
        id_token=data["id_token"]
        access_token=data["access_token"]
        expires_in=data["expires_in"]
        token_type=data["token_type"]
        refresh_token=data["refresh_token"]
        scope=data["scope"]
        if not (isinstance(id_token))
        self.token.__init__(
            
            
            
            
            
            
        )
        self.session.headers.update({"Authorization": str(self.token)})

    async def dump(self) -> dict[str, str]:
        """
        Dumps the client to a json serializable object.

        Returns:
            dict[str, str]: Map of the data required for token refresh.
        """
        return {
            "institute_code": self.token.body.kreta_institute_code,
            "refresh_token": self.token.refresh_token,
            "client_id": self.token.body.client_id,
        }

    @classmethod
    async def load(cls, data: dict[str, str], *args, **kwargs) -> Self:
        """
        Loads the client from a json serializable object.

        Args:
            data (dict[str, str]): Map of the data required for token refresh. (same key-value pairs as that returned by `.dump`)
        """
        token_data = await cls._refresh2access(**data)
        token = AuthToken(**token_data)
        return cls(token, *args, **kwargs)

    async def request(
        self, *args, model: Type[Model] = ClientSession, **kwargs
    ) -> Model:
        """
        Wrapper of the session's request method.
        It should auto fill `{institute_code}` fields with the user's institute code.
        It should also check if the token is valid and refresh it if needed.

        Args:
            *args: args for the request as defined in `aiohttp.ClientSession.request`
            model (Model, optional): If specified the response will be validated for this pydantic model.
                Can be `Type[list[BaseModel]]` if the response is a list
                If not specified the return of the underlying network handler should be returned.
            **kwargs: kwargs for the request as defined in `aiohttp.ClientSession.request`

        Returns:
            Model: The model specified or the underlying network handler's return.
        """
        if self.token.is_expired():
            await self.extendToken()

        if len(args) < 2:
            raise ValueError("At least 2 arguments are required: method and url")

        if "{institute_code}" in args[1]:
            args = list(args)
            args[1] = args[1].format(
                institute_code=self.token.body.kreta_institute_code
            )

        async with self.session.request(*args, **kwargs) as response:
            await response.raise_for_status()
            data = await response.json()

        if get_origin(model) is list:
            model = get_args(model)[0]
            return [model.model_validate(item) for item in data]

        elif issubclass(model, BaseModel):
            return model.model_validate(**response.json())

        return response

    @staticmethod
    async def _refresh2access(
        institute_code: str, refresh_token: str, client_id: str
    ) -> dict[str, str|int]:
        """
        Static method for the request of refreshing tokens.

        Args:
            institute_code (str): The education id of the user.
            refresh_token (str): refresh token base64 encoded string
            client_id (str): client id

        Returns:
            dict: default login response
        """
        data = {
            "institute_code": institute_code,
            "refresh_token": refresh_token,
            "grant_type": "refresh_token",
            "client_id": client_id,
        }
        async with ClientSession() as session:
            async with session.request(
                "POST", "https://idp.e-kreta.hu/connect/token", data=data
            ) as r:
                response = await r.json()
        return response
