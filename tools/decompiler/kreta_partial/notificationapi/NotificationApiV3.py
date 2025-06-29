from .Dtos import PushNotificationRegistration
from e_kreta.idp.client import Client, AsyncClient, SyncClient, JsonSerializeable
from typing import Awaitable, Any, overload


@overload
def addPushNotificationRegistration(session: AsyncClient[JsonSerializeable], firebaseToken: str, role: int, notificationEnvironment: NotificationEnvironment, platform: str, notificationType: int, notificationSource: str) -> Awaitable[PushNotificationRegistration]: ...
@overload
def addPushNotificationRegistration(session: SyncClient[JsonSerializeable], firebaseToken: str, role: int, notificationEnvironment: NotificationEnvironment, platform: str, notificationType: int, notificationSource: str) -> PushNotificationRegistration: ...
def addPushNotificationRegistration(session: Client, firebaseToken: str, role: int, notificationEnvironment: NotificationEnvironment, platform: str, notificationType: int, notificationSource: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "POST",
        BASE_URL + "Registration",
        
        
        query = {
            "Handle": firebaseToken,
        "NotificationRole": role,
        "NotificationEnvironment": notificationEnvironment,
        "Platform": platform,
        "NotificationType": notificationType,
        "NotificationSource": notificationSource
        },
        
    )

@overload
def deletePushNotificationRegistration(session: AsyncClient[JsonSerializeable], registrationId: str, role: int, notificationEnvironment: NotificationEnvironment, notificationType: int, notificationSource: str) -> Awaitable[ResponseBody]: ...
@overload
def deletePushNotificationRegistration(session: SyncClient[JsonSerializeable], registrationId: str, role: int, notificationEnvironment: NotificationEnvironment, notificationType: int, notificationSource: str) -> ResponseBody: ...
def deletePushNotificationRegistration(session: Client, registrationId: str, role: int, notificationEnvironment: NotificationEnvironment, notificationType: int, notificationSource: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")

    return session.request(
        "DELETE",
        BASE_URL + "Registration",
        
        headers = {
            "apiKey": "7856d350-1fda-45f5-822d-e1a2f3f1acf0"
        },
        
        query = {
            "RegistrationId": registrationId,
        "NotificationRole": role,
        "NotificationEnvironment": notificationEnvironment,
        "NotificationType": notificationType,
        "NotificationSource": notificationSource
        },
        
    )

@overload
def updatePushNotificationRegistration(session: AsyncClient[JsonSerializeable], registrationId: str, firebaseToken: str, role: int, notificationEnvironment: NotificationEnvironment, notificationType: int, notificationSource: str) -> Awaitable[ResponseBody]: ...
@overload
def updatePushNotificationRegistration(session: SyncClient[JsonSerializeable], registrationId: str, firebaseToken: str, role: int, notificationEnvironment: NotificationEnvironment, notificationType: int, notificationSource: str) -> ResponseBody: ...
def updatePushNotificationRegistration(session: Client, registrationId: str, firebaseToken: str, role: int, notificationEnvironment: NotificationEnvironment, notificationType: int, notificationSource: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")

    return session.request(
        "PUT",
        BASE_URL + "Registration",
        
        headers = {
            "apiKey": "7856d350-1fda-45f5-822d-e1a2f3f1acf0"
        },
        
        query = {
            "RegistrationId": registrationId,
        "Handle": firebaseToken,
        "NotificationRole": role,
        "NotificationEnvironment": notificationEnvironment,
        "NotificationType": notificationType,
        "NotificationSource": notificationSource
        },
        
    )
