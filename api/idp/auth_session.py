from .auth_token import Auth_Token
from .errors import raise_error
import requests
from typing import Self, TypeVar, Type


class Auth_Session(requests.Session):
    def __init__(self, token: Auth_Token, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.token = token
        self.headers.update({"Authorization": str(self.token)})

    def __enter__(self) -> Self:
        return super().__enter__()

    def __exit__(self, *args, **kwargs) -> None:
        self.close()
        super().__exit__(*args, **kwargs)

    def close(self) -> None:
        try:
            self.token.revoke()
            self.token = None
            self.headers.pop("Authorization")
        except Exception:
            pass
        super().close()

    @classmethod
    def login(cls, username: str, password: str, institute_code: str) -> Self:
        token = Auth_Token.login(username, password, institute_code)
        return cls(token)

    def request(self, method, url, *args, **kwargs) -> requests.Response:
        if "{institute_code}" in url:
            url = url.format(institute_code=self.token.institute_code)
        if self.token.is_expired():
            self.token.refresh()
            self.headers.update({"Authorization": str(self.token)})
        response = super().request(method, url, *args, **kwargs)
        raise_error(response)

        return response
