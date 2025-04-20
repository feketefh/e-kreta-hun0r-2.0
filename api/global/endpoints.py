from typing import Literal, TypeVar, Type, get_origin, get_args, TYPE_CHECKING
from datetime import datetime, timedelta
from .models import *
from ..idp.auth_session import Auth_Session
from requests import Response
from pydantic import BaseModel

T = TypeVar("T")


def global_request(
    session: Auth_Session,
    method: Literal["GET", "DELETE", "POST", "PUT"],
    url: str,
    *args,
    model: Type[T] = Response,
    **kwargs,
) -> T:
    url = "" + url

    r = session.request(method, url, *args, **kwargs)

    if model is Response:
        return r

    data = r.json()

    origin = get_origin(model)
    if origin is list:
        inner_model: BaseModel = get_args(model)[0]
        return [inner_model.model_validate(item) for item in data]

    return model(data)
