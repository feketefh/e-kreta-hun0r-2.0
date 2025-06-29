from .Dtos import Institute
from e_kreta.idp.client import Client, AsyncClient, SyncClient, JsonSerializeable
from typing import Awaitable, Any, overload


@overload
def getInstitutes(session: AsyncClient[JsonSerializeable]) -> Awaitable[list[Institute]]: ...
@overload
def getInstitutes(session: SyncClient[JsonSerializeable]) -> list[Institute]: ...
def getInstitutes(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")

    return session.request(
        "GET",
        BASE_URL + "intezmenyek/kreta/publikus",
        
        headers = {
            "api-version": "v1"
        },
        
        
    )
