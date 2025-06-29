from .Dtos import ClassworkAttachment, Classwork, ClassworkSolutionAttachment, ClassworkSolutionAttachmentPost, ClassworkSolutionPut, ClassworkTeachingMaterial, ClassworkTeachingMaterialPost, DriversLicenseRegistrationStatus, HomeworkSolutionAttachment, HomeworkSolutionAttachmentPost, HomeworkSolutionPut, LanguageSubTask, LanguageSubTaskSubmission, LanguageTask, LanguageTaskSubmission, SubmittedClasswork, SubmittedHomework
from e_kreta.idp.client import Client, AsyncClient, SyncClient, JsonSerializeable
from typing import Awaitable, Any, overload


@overload
def deleteHomeworkSolutionAttachment(session: AsyncClient[JsonSerializeable], homeworkSolutionId: str, fileId: str) -> Awaitable[ResponseBody]: ...
@overload
def deleteHomeworkSolutionAttachment(session: SyncClient[JsonSerializeable], homeworkSolutionId: str, fileId: str) -> ResponseBody: ...
def deleteHomeworkSolutionAttachment(session: Client, homeworkSolutionId: str, fileId: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "DELETE",
        BASE_URL + f"mobil/intezmenyek/tanulok/orak/hazifeladatok/beadasok/{homeworkSolutionId}/fajlok/{fileId}",
        
        headers = {
            "apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"
        },
        
        
    )

@overload
def deleteSolutionAttachment(session: AsyncClient[JsonSerializeable], classworkSolutionId: str, fileId: str) -> Awaitable[ResponseBody]: ...
@overload
def deleteSolutionAttachment(session: SyncClient[JsonSerializeable], classworkSolutionId: str, fileId: str) -> ResponseBody: ...
def deleteSolutionAttachment(session: Client, classworkSolutionId: str, fileId: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "DELETE",
        BASE_URL + f"mobil/intezmenyek/tanulok/orak/oraifeladatok/beadasok/{classworkSolutionId}/fajlok/{fileId}",
        
        headers = {
            "apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"
        },
        
        
    )

@overload
def getClasswork(session: AsyncClient[JsonSerializeable], classworkId: str) -> Awaitable[Classwork]: ...
@overload
def getClasswork(session: SyncClient[JsonSerializeable], classworkId: str) -> Classwork: ...
def getClasswork(session: Client, classworkId: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + f"mobil/intezmenyek/tanulok/orak/oraifeladatok/{classworkId}",
        
        headers = {
            "apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"
        },
        
        
    )

@overload
def getClassworkAttachmentUrl(session: AsyncClient[JsonSerializeable], classworkId: str, fileId: str) -> Awaitable[str]: ...
@overload
def getClassworkAttachmentUrl(session: SyncClient[JsonSerializeable], classworkId: str, fileId: str) -> str: ...
def getClassworkAttachmentUrl(session: Client, classworkId: str, fileId: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + f"mobil/intezmenyek/tanulok/orak/oraifeladatok/{classworkId}/fajlok/{fileId}/url",
        
        headers = {
            "apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"
        },
        
        
    )

@overload
def getClassworkAttachments(session: AsyncClient[JsonSerializeable], classworkId: str) -> Awaitable[list[ClassworkAttachment]]: ...
@overload
def getClassworkAttachments(session: SyncClient[JsonSerializeable], classworkId: str) -> list[ClassworkAttachment]: ...
def getClassworkAttachments(session: Client, classworkId: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + f"mobil/intezmenyek/tanulok/orak/oraifeladatok/{classworkId}/fajlok",
        
        headers = {
            "apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"
        },
        
        
    )

@overload
def getClassworkGroups(session: AsyncClient[JsonSerializeable], classworkGroupId: str) -> Awaitable[list[Classwork]]: ...
@overload
def getClassworkGroups(session: SyncClient[JsonSerializeable], classworkGroupId: str) -> list[Classwork]: ...
def getClassworkGroups(session: Client, classworkGroupId: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + f"mobil/intezmenyek/tanulok/orak/oraifeladatok/groupok/{classworkGroupId}",
        
        headers = {
            "apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"
        },
        
        
    )

@overload
def getClassworkSolutionAttachmentUrl(session: AsyncClient[JsonSerializeable], classworkSolutionId: str, fileId: str) -> Awaitable[str]: ...
@overload
def getClassworkSolutionAttachmentUrl(session: SyncClient[JsonSerializeable], classworkSolutionId: str, fileId: str) -> str: ...
def getClassworkSolutionAttachmentUrl(session: Client, classworkSolutionId: str, fileId: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + f"mobil/intezmenyek/tanulok/orak/oraifeladatok/beadasok/{classworkSolutionId}/fajlok/{fileId}/url",
        
        headers = {
            "apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"
        },
        
        
    )

@overload
def getClassworkTeachingMaterial(session: AsyncClient[JsonSerializeable], set: ClassworkTeachingMaterialPost) -> Awaitable[list[ClassworkTeachingMaterial]]: ...
@overload
def getClassworkTeachingMaterial(session: SyncClient[JsonSerializeable], set: ClassworkTeachingMaterialPost) -> list[ClassworkTeachingMaterial]: ...
def getClassworkTeachingMaterial(session: Client, set: ClassworkTeachingMaterialPost):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "POST",
        BASE_URL + "mobil/intezmenyek/tanulok/orak/tananyagok",
        
        headers = {
            "apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"
        },
        
        json=set.model_dump(mode="json")
    )

@overload
def getDriversLicenseRegistrationStatus(session: AsyncClient[JsonSerializeable]) -> Awaitable[DriversLicenseRegistrationStatus]: ...
@overload
def getDriversLicenseRegistrationStatus(session: SyncClient[JsonSerializeable]) -> DriversLicenseRegistrationStatus: ...
def getDriversLicenseRegistrationStatus(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "mobil/intezmenyek/gondviselok/jogositvany/kepzesjelentkezes",
        
        headers = {
            "apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"
        },
        
        
    )

@overload
def getHomeworkSolutionAttachmentUrl(session: AsyncClient[JsonSerializeable], homeworkSolutionId: str, fileId: str) -> Awaitable[str]: ...
@overload
def getHomeworkSolutionAttachmentUrl(session: SyncClient[JsonSerializeable], homeworkSolutionId: str, fileId: str) -> str: ...
def getHomeworkSolutionAttachmentUrl(session: Client, homeworkSolutionId: str, fileId: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + f"mobil/intezmenyek/tanulok/orak/hazifeladatok/beadasok/{homeworkSolutionId}/fajlok/{fileId}/url",
        
        headers = {
            "apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"
        },
        
        
    )

@overload
def getHomeworkSolutionAttachments(session: AsyncClient[JsonSerializeable], submittedHwId: str) -> Awaitable[list[HomeworkSolutionAttachment]]: ...
@overload
def getHomeworkSolutionAttachments(session: SyncClient[JsonSerializeable], submittedHwId: str) -> list[HomeworkSolutionAttachment]: ...
def getHomeworkSolutionAttachments(session: Client, submittedHwId: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + f"mobil/intezmenyek/tanulok/orak/hazifeladatok/beadasok/{submittedHwId}/fajlok",
        
        headers = {
            "apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"
        },
        
        
    )

@overload
def getLanguageTask(session: AsyncClient[JsonSerializeable], groupId: str) -> Awaitable[LanguageTask]: ...
@overload
def getLanguageTask(session: SyncClient[JsonSerializeable], groupId: str) -> LanguageTask: ...
def getLanguageTask(session: Client, groupId: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + f"mobil/intezmenyek/tanulok/orak/nyelvifeladatok/{groupId}",
        
        headers = {
            "apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"
        },
        
        
    )

@overload
def getLanguageTaskSubmission(session: AsyncClient[JsonSerializeable], groupId: str) -> Awaitable[LanguageTaskSubmission]: ...
@overload
def getLanguageTaskSubmission(session: SyncClient[JsonSerializeable], groupId: str) -> LanguageTaskSubmission: ...
def getLanguageTaskSubmission(session: Client, groupId: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + f"mobil/intezmenyek/tanulok/orak/nyelvifeladatok/groupok/{groupId}/beadas",
        
        headers = {
            "apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"
        },
        
        
    )

@overload
def getSolutionAttachments(session: AsyncClient[JsonSerializeable], id: str) -> Awaitable[list[ClassworkSolutionAttachment]]: ...
@overload
def getSolutionAttachments(session: SyncClient[JsonSerializeable], id: str) -> list[ClassworkSolutionAttachment]: ...
def getSolutionAttachments(session: Client, id: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + f"mobil/intezmenyek/tanulok/orak/oraifeladatok/beadasok/{id}/fajlok",
        
        headers = {
            "apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"
        },
        
        
    )

@overload
def getStudentHasAccessToDriversLicenseCourse(session: AsyncClient[JsonSerializeable]) -> Awaitable[bool]: ...
@overload
def getStudentHasAccessToDriversLicenseCourse(session: SyncClient[JsonSerializeable]) -> bool: ...
def getStudentHasAccessToDriversLicenseCourse(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "mobil/intezmenyek/gondviselok/jogositvany/kepzesjelentkezes/elerheto",
        
        headers = {
            "apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"
        },
        
        
    )

@overload
def getSubmittedClasswork(session: AsyncClient[JsonSerializeable], classworkId: str) -> Awaitable[SubmittedClasswork]: ...
@overload
def getSubmittedClasswork(session: SyncClient[JsonSerializeable], classworkId: str) -> SubmittedClasswork: ...
def getSubmittedClasswork(session: Client, classworkId: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + f"mobil/intezmenyek/tanulok/orak/oraifeladatok/{classworkId}/beadas",
        
        headers = {
            "apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"
        },
        
        
    )

@overload
def getSubmittedHomework(session: AsyncClient[JsonSerializeable], homeworkId: str) -> Awaitable[SubmittedHomework]: ...
@overload
def getSubmittedHomework(session: SyncClient[JsonSerializeable], homeworkId: str) -> SubmittedHomework: ...
def getSubmittedHomework(session: Client, homeworkId: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + f"mobil/intezmenyek/tanulok/orak/hazifeladatok/{homeworkId}/beadas",
        
        headers = {
            "apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"
        },
        
        
    )

@overload
def isDriversLicenseActiveForGuardian(session: AsyncClient[JsonSerializeable]) -> Awaitable[bool]: ...
@overload
def isDriversLicenseActiveForGuardian(session: SyncClient[JsonSerializeable]) -> bool: ...
def isDriversLicenseActiveForGuardian(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "mobil/intezmenyek/gondviselok/jogositvany/modul/aktiv",
        
        headers = {
            "apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"
        },
        
        
    )

@overload
def isDriversLicenseActiveForStudent(session: AsyncClient[JsonSerializeable]) -> Awaitable[bool]: ...
@overload
def isDriversLicenseActiveForStudent(session: SyncClient[JsonSerializeable]) -> bool: ...
def isDriversLicenseActiveForStudent(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "mobil/intezmenyek/tanulok/jogositvany/modul/aktiv",
        
        headers = {
            "apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"
        },
        
        
    )

@overload
def postGuardianApproval(session: AsyncClient[JsonSerializeable]) -> Awaitable[None]: ...
@overload
def postGuardianApproval(session: SyncClient[JsonSerializeable]) -> None: ...
def postGuardianApproval(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "POST",
        BASE_URL + "mobil/intezmenyek/gondviselok/jogositvany/kepzesjelentkezes/jovahagy",
        
        headers = {
            "apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"
        },
        
        
    )

@overload
def putSaveSolution(session: AsyncClient[JsonSerializeable], id: str, body: ClassworkSolutionPut) -> Awaitable[str]: ...
@overload
def putSaveSolution(session: SyncClient[JsonSerializeable], id: str, body: ClassworkSolutionPut) -> str: ...
def putSaveSolution(session: Client, id: str, body: ClassworkSolutionPut):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "PUT",
        BASE_URL + f"mobil/intezmenyek/tanulok/orak/oraifeladatok/beadasok/{id}",
        
        headers = {
            "apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"
        },
        
        json=body.model_dump(mode="json")
    )

@overload
def saveHomeworkAttachment(session: AsyncClient[JsonSerializeable], submittedHwId: str, set: HomeworkSolutionAttachmentPost) -> Awaitable[ResponseBody]: ...
@overload
def saveHomeworkAttachment(session: SyncClient[JsonSerializeable], submittedHwId: str, set: HomeworkSolutionAttachmentPost) -> ResponseBody: ...
def saveHomeworkAttachment(session: Client, submittedHwId: str, set: HomeworkSolutionAttachmentPost):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "POST",
        BASE_URL + f"mobil/intezmenyek/tanulok/orak/hazifeladatok/beadasok/{submittedHwId}/fajlok/veglegesites",
        
        headers = {
            "apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"
        },
        
        json=set.model_dump(mode="json")
    )

@overload
def saveHomeworkSolution(session: AsyncClient[JsonSerializeable], homeworkId: str, body: HomeworkSolutionPut) -> Awaitable[str]: ...
@overload
def saveHomeworkSolution(session: SyncClient[JsonSerializeable], homeworkId: str, body: HomeworkSolutionPut) -> str: ...
def saveHomeworkSolution(session: Client, homeworkId: str, body: HomeworkSolutionPut):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "PUT",
        BASE_URL + f"mobil/intezmenyek/tanulok/orak/hazifeladatok/beadasok/{homeworkId}",
        
        headers = {
            "apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"
        },
        
        json=body.model_dump(mode="json")
    )

@overload
def saveSolutionAttachment(session: AsyncClient[JsonSerializeable], classworkSolutionId: str, set: ClassworkSolutionAttachmentPost) -> Awaitable[ResponseBody]: ...
@overload
def saveSolutionAttachment(session: SyncClient[JsonSerializeable], classworkSolutionId: str, set: ClassworkSolutionAttachmentPost) -> ResponseBody: ...
def saveSolutionAttachment(session: Client, classworkSolutionId: str, set: ClassworkSolutionAttachmentPost):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "POST",
        BASE_URL + f"mobil/intezmenyek/tanulok/orak/oraifeladatok/beadasok/{classworkSolutionId}/fajlok/veglegesites",
        
        headers = {
            "apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"
        },
        
        json=set.model_dump(mode="json")
    )

@overload
def submitClassworkSolution(session: AsyncClient[JsonSerializeable], id: str) -> Awaitable[str]: ...
@overload
def submitClassworkSolution(session: SyncClient[JsonSerializeable], id: str) -> str: ...
def submitClassworkSolution(session: Client, id: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + f"mobil/intezmenyek/tanulok/orak/oraifeladatok/beadasok/{id}/beadas",
        
        headers = {
            "apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"
        },
        
        
    )

@overload
def submitHomeworkSolution(session: AsyncClient[JsonSerializeable], id: str) -> Awaitable[str]: ...
@overload
def submitHomeworkSolution(session: SyncClient[JsonSerializeable], id: str) -> str: ...
def submitHomeworkSolution(session: Client, id: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + f"mobil/intezmenyek/tanulok/orak/hazifeladatok/beadasok/{id}/beadas",
        
        headers = {
            "apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"
        },
        
        
    )
