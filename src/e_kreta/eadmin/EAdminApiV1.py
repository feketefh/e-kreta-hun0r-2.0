from .Dtos import AccessControlSystemItem, Addressee, AddresseeType, Administrator, Applicants, ApplicationDocumentType, ApplicationMandatoryDocument, Attachment, Case, Child, CurrentInstitutionDetails, Decision, EmployeeDetails, FiledApplication, FiledDecision, File, Judgement, MailboxItem, Message, MessageLimitations, OtherThingsToDoAttachments, PostState, ReadMessageRequest, RectificationPost, SendMessageToBinRequest, Signer, State, Status, TemporaryFile, TmgiCasePost, ToDoItem, ToDoMandatoryDocumentsList, Type
from e_kreta.idp.client import Client, AsyncClient, SyncClient, JsonSerializeable
from typing import Awaitable, Any, overload


@overload
def createRectification(session: AsyncClient[JsonSerializeable], caseId: str, body: RectificationPost) -> Awaitable[ResponseBody]: ...
@overload
def createRectification(session: SyncClient[JsonSerializeable], caseId: str, body: RectificationPost) -> ResponseBody: ...
def createRectification(session: Client, caseId: str, body: RectificationPost):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "POST",
        BASE_URL + f"ugy/kerelmek/{caseId}",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        json=body.model_dump(mode="json")
    )

@overload
def createTmgiCase(session: AsyncClient[JsonSerializeable], body: TmgiCasePost) -> Awaitable[ResponseBody]: ...
@overload
def createTmgiCase(session: SyncClient[JsonSerializeable], body: TmgiCasePost) -> ResponseBody: ...
def createTmgiCase(session: Client, body: TmgiCasePost):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "POST",
        BASE_URL + "ugy/kerelmek",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        json=body.model_dump(mode="json")
    )

@overload
def deleteMessagePermanently(session: AsyncClient[JsonSerializeable], isDeleted: boolean) -> Awaitable[ResponseBody]: ...
@overload
def deleteMessagePermanently(session: SyncClient[JsonSerializeable], isDeleted: boolean) -> ResponseBody: ...
def deleteMessagePermanently(session: Client, isDeleted: boolean):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "DELETE",
        BASE_URL + "kommunikacio/postaladaelemek/torles",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        query = {
            "isKuka": isDeleted
        },
        
    )

@overload
def getAccessControlSystemEvents(session: AsyncClient[JsonSerializeable]) -> Awaitable[list[AccessControlSystemItem]]: ...
@overload
def getAccessControlSystemEvents(session: SyncClient[JsonSerializeable]) -> list[AccessControlSystemItem]: ...
def getAccessControlSystemEvents(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "belepteto/kartyaesemenyek/sajat",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        
    )

@overload
def getAddressableClasses(session: AsyncClient[JsonSerializeable], addressedCode: str) -> Awaitable[list[KretaClass]]: ...
@overload
def getAddressableClasses(session: SyncClient[JsonSerializeable], addressedCode: str) -> list[KretaClass]: ...
def getAddressableClasses(session: Client, addressedCode: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "kommunikacio/osztalyok/cimezheto",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        query = {
            "cimzettKod": addressedCode
        },
        
    )

@overload
def getAddressableGuardiansForClass(session: AsyncClient[JsonSerializeable], classId: long) -> Awaitable[list[GuardianEAdmin]]: ...
@overload
def getAddressableGuardiansForClass(session: SyncClient[JsonSerializeable], classId: long) -> list[GuardianEAdmin]: ...
def getAddressableGuardiansForClass(session: Client, classId: long):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + f"kreta/gondviselok/osztaly/{classId}",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        
    )

@overload
def getAddressableSzmkRepesentative(session: AsyncClient[JsonSerializeable]) -> Awaitable[list[GuardianEAdmin]]: ...
@overload
def getAddressableSzmkRepesentative(session: SyncClient[JsonSerializeable]) -> list[GuardianEAdmin]: ...
def getAddressableSzmkRepesentative(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "kommunikacio/szmkkepviselok/cimezheto",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        
    )

@overload
def getAddressableType(session: AsyncClient[JsonSerializeable]) -> Awaitable[list[AddresseeType]]: ...
@overload
def getAddressableType(session: SyncClient[JsonSerializeable]) -> list[AddresseeType]: ...
def getAddressableType(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "kommunikacio/cimezhetotipusok",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        
    )

@overload
def getAddresseeType(session: AsyncClient[JsonSerializeable]) -> Awaitable[list[AddresseeType]]: ...
@overload
def getAddresseeType(session: SyncClient[JsonSerializeable]) -> list[AddresseeType]: ...
def getAddresseeType(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "adatszotarak/cimzetttipusok",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        
    )

@overload
def getAdministrators(session: AsyncClient[JsonSerializeable]) -> Awaitable[list[EmployeeDetails]]: ...
@overload
def getAdministrators(session: SyncClient[JsonSerializeable]) -> list[EmployeeDetails]: ...
def getAdministrators(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "kreta/alkalmazottak/adminisztrator",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        
    )

@overload
def getCase(session: AsyncClient[JsonSerializeable], caseId: str) -> Awaitable[Case]: ...
@overload
def getCase(session: SyncClient[JsonSerializeable], caseId: str) -> Case: ...
def getCase(session: Client, caseId: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + f"ugy/kerelmek/{caseId}",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        
    )

@overload
def getCaseTypes(session: AsyncClient[JsonSerializeable]) -> Awaitable[list[Type]]: ...
@overload
def getCaseTypes(session: SyncClient[JsonSerializeable]) -> list[Type]: ...
def getCaseTypes(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "adatszotarak/kerelemtipusok",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        
    )

@overload
def getCases(session: AsyncClient[JsonSerializeable], avoidFilterClosedCases: boolean) -> Awaitable[list[Case]]: ...
@overload
def getCases(session: SyncClient[JsonSerializeable], avoidFilterClosedCases: boolean) -> list[Case]: ...
def getCases(session: Client, avoidFilterClosedCases: boolean):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "ugy/kerelmek",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        query = {
            "isLezartakIs": avoidFilterClosedCases
        },
        
    )

@overload
def getChildData(session: AsyncClient[JsonSerializeable]) -> Awaitable[Child]: ...
@overload
def getChildData(session: SyncClient[JsonSerializeable]) -> Child: ...
def getChildData(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "kreta/gyerekemadatok",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        
    )

@overload
def getClassMasters(session: AsyncClient[JsonSerializeable]) -> Awaitable[list[EmployeeDetails]]: ...
@overload
def getClassMasters(session: SyncClient[JsonSerializeable]) -> list[EmployeeDetails]: ...
def getClassMasters(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "kreta/alkalmazottak/oszalyfonok",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        
    )

@overload
def getCurrentInstitutionDetails(session: AsyncClient[JsonSerializeable]) -> Awaitable[CurrentInstitutionDetails]: ...
@overload
def getCurrentInstitutionDetails(session: SyncClient[JsonSerializeable]) -> CurrentInstitutionDetails: ...
def getCurrentInstitutionDetails(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "ugy/aktualisIntezmenyAdatok",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        
    )

@overload
def getCurrentInstitutionModules(session: AsyncClient[JsonSerializeable]) -> Awaitable[list[String]]: ...
@overload
def getCurrentInstitutionModules(session: SyncClient[JsonSerializeable]) -> list[String]: ...
def getCurrentInstitutionModules(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "intezmenyek/sajat/modulok",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        
    )

@overload
def getDirectors(session: AsyncClient[JsonSerializeable]) -> Awaitable[list[EmployeeDetails]]: ...
@overload
def getDirectors(session: SyncClient[JsonSerializeable]) -> list[EmployeeDetails]: ...
def getDirectors(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "kreta/alkalmazottak/igazgatosag",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        
    )

@overload
def getMessage(session: AsyncClient[JsonSerializeable], mailboxItemId: long) -> Awaitable[MailboxItem]: ...
@overload
def getMessage(session: SyncClient[JsonSerializeable], mailboxItemId: long) -> MailboxItem: ...
def getMessage(session: Client, mailboxItemId: long):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + f"kommunikacio/postaladaelemek/{mailboxItemId}",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        
    )

@overload
def getMessageLimitations(session: AsyncClient[JsonSerializeable]) -> Awaitable[MessageLimitations]: ...
@overload
def getMessageLimitations(session: SyncClient[JsonSerializeable]) -> MessageLimitations: ...
def getMessageLimitations(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "kommunikacio/uzenetek/kuldhetok/korlat",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        
    )

@overload
def getMessages(session: AsyncClient[JsonSerializeable]) -> Awaitable[list[MailboxItem]]: ...
@overload
def getMessages(session: SyncClient[JsonSerializeable]) -> list[MailboxItem]: ...
def getMessages(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "kommunikacio/postaladaelemek/sajat",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        
    )

@overload
def getSigner(session: AsyncClient[JsonSerializeable], typeCode: int, signerId: int) -> Awaitable[Signer]: ...
@overload
def getSigner(session: SyncClient[JsonSerializeable], typeCode: int, signerId: int) -> Signer: ...
def getSigner(session: Client, typeCode: int, signerId: int):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + f"ugy/alkalmazott/{typeCode}/{signerId}",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        
    )

@overload
def getStatus(session: AsyncClient[JsonSerializeable]) -> Awaitable[Status]: ...
@overload
def getStatus(session: SyncClient[JsonSerializeable]) -> Status: ...
def getStatus(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "status",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        
    )

@overload
def getTeachers(session: AsyncClient[JsonSerializeable]) -> Awaitable[list[EmployeeDetails]]: ...
@overload
def getTeachers(session: SyncClient[JsonSerializeable]) -> list[EmployeeDetails]: ...
def getTeachers(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "kreta/alkalmazottak/tanar",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        
    )

@overload
def getTmgiCaseTypes(session: AsyncClient[JsonSerializeable]) -> Awaitable[list[Type]]: ...
@overload
def getTmgiCaseTypes(session: SyncClient[JsonSerializeable]) -> list[Type]: ...
def getTmgiCaseTypes(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "adatszotarak/tmgiigazolastipusok",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        
    )

@overload
def getUnreadMessagesCount(session: AsyncClient[JsonSerializeable]) -> Awaitable[Integer]: ...
@overload
def getUnreadMessagesCount(session: SyncClient[JsonSerializeable]) -> Integer: ...
def getUnreadMessagesCount(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "kommunikacio/postaladaelemek/olvasatlanokszama",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        
    )

@overload
def readMessage(session: AsyncClient[JsonSerializeable], set: ReadMessageRequest) -> Awaitable[ResponseBody]: ...
@overload
def readMessage(session: SyncClient[JsonSerializeable], set: ReadMessageRequest) -> ResponseBody: ...
def readMessage(session: Client, set: ReadMessageRequest):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "POST",
        BASE_URL + "kommunikacio/postaladaelemek/olvasott",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        json=set.model_dump(mode="json")
    )

@overload
def sendMessage(session: AsyncClient[JsonSerializeable], set: Message) -> Awaitable[ResponseBody]: ...
@overload
def sendMessage(session: SyncClient[JsonSerializeable], set: Message) -> ResponseBody: ...
def sendMessage(session: Client, set: Message):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "POST",
        BASE_URL + "kommunikacio/uzenetek",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        json=set.model_dump(mode="json")
    )

@overload
def sendMessageToBin(session: AsyncClient[JsonSerializeable], set: SendMessageToBinRequest) -> Awaitable[ResponseBody]: ...
@overload
def sendMessageToBin(session: SyncClient[JsonSerializeable], set: SendMessageToBinRequest) -> ResponseBody: ...
def sendMessageToBin(session: Client, set: SendMessageToBinRequest):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "POST",
        BASE_URL + "kommunikacio/postaladaelemek/kuka",
        
        headers = {
            "X-Uzenet-Lokalizacio": "hu-HU"
        },
        
        json=set.model_dump(mode="json")
    )
