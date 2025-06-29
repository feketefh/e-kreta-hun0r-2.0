from e_kreta.idp.client import Client, AsyncClient, SyncClient, JsonSerializeable
from typing import Awaitable, Any, overload


@overload
def getIerEnabled(session: AsyncClient[JsonSerializeable]) -> Awaitable[bool]: ...
@overload
def getIerEnabled(session: SyncClient[JsonSerializeable]) -> bool: ...
def getIerEnabled(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "FelhasznaloStatusz/IsEnabledInKretaSzuloiMobilApp",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        
    )
