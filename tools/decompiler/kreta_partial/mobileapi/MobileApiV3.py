from .Dtos import (
    AnnouncedTest,
    BankAccountNumberPost,
    ClassAverage,
    ClassMaster,
    ConsultingHour,
    ConsultingHourList,
    Contact,
    Evaluation,
    Group,
    Guardian4T,
    Guardian4TPost,
    Homework,
    LepEvent,
    LepEventGuardianPermissionPost,
    Lesson,
    NepEvent,
    NepEventGuardianPermissionPost,
    Note,
    NoticeBoardItem,
    Omission,
    SchoolYearCalendarEntry,
    Student,
    SubjectAverage,
    TeszekRegistration,
    TimeTableWeek,
)
from e_kreta.idp.client import Client, AsyncClient, SyncClient, JsonSerializeable
from typing import Awaitable, overload

BASE_URL = "https://mobile.kreta.hu/api/v3/"


@overload
def deleteBankAccountNumber(
    session: AsyncClient[JsonSerializeable],
) -> Awaitable[None]: ...
@overload
def deleteBankAccountNumber(session: SyncClient[JsonSerializeable]) -> None: ...
def deleteBankAccountNumber(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "DELETE",
        BASE_URL + "sajat/Bankszamla",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
    )


@overload
def deleteReservation(
    session: AsyncClient[JsonSerializeable], timeSlotUid: str
) -> Awaitable[None]: ...
@overload
def deleteReservation(
    session: SyncClient[JsonSerializeable], timeSlotUid: str
) -> None: ...
def deleteReservation(session: Client, timeSlotUid: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "DELETE",
        BASE_URL + f"sajat/Fogadoorak/Idopontok/Jelentkezesek/{timeSlotUid}",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
    )


@overload
def downloadAttachment(
    session: AsyncClient[JsonSerializeable], uid: str
) -> Awaitable[bytes]: ...
@overload
def downloadAttachment(session: SyncClient[JsonSerializeable], uid: str) -> bytes: ...
def downloadAttachment(session: Client, uid: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + f"sajat/Csatolmany/{uid}",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
    )


@overload
def getAnnouncedTest(
    session: AsyncClient[JsonSerializeable], uid: str
) -> Awaitable[list[AnnouncedTest]]: ...
@overload
def getAnnouncedTest(
    session: SyncClient[JsonSerializeable], uid: str
) -> list[AnnouncedTest]: ...
def getAnnouncedTest(session: Client, uid: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "sajat/BejelentettSzamonkeresek",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
        query={"Uids": uid},
    )


@overload
def getAnnouncedTests(
    session: AsyncClient[JsonSerializeable], fromDate: str, toDate: str
) -> Awaitable[list[AnnouncedTest]]: ...
@overload
def getAnnouncedTests(
    session: SyncClient[JsonSerializeable], fromDate: str, toDate: str
) -> list[AnnouncedTest]: ...
def getAnnouncedTests(session: Client, fromDate: str, toDate: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "sajat/BejelentettSzamonkeresek",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
        query={"datumTol": fromDate, "datumIg": toDate},
    )


@overload
def getClassAverage(
    session: AsyncClient[JsonSerializeable], educationTypeUid: str, subjectUid: str
) -> Awaitable[list[ClassAverage]]: ...
@overload
def getClassAverage(
    session: SyncClient[JsonSerializeable], educationTypeUid: str, subjectUid: str
) -> list[ClassAverage]: ...
def getClassAverage(session: Client, educationTypeUid: str, subjectUid: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "sajat/Ertekelesek/Atlagok/OsztalyAtlagok",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
        query={
            "oktatasiNevelesiFeladatUid": educationTypeUid,
            "tantargyUid": subjectUid,
        },
    )


@overload
def getClassMaster(
    session: AsyncClient[JsonSerializeable], uids: str
) -> Awaitable[list[ClassMaster]]: ...
@overload
def getClassMaster(
    session: SyncClient[JsonSerializeable], uids: str
) -> list[ClassMaster]: ...
def getClassMaster(session: Client, uids: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "felhasznalok/Alkalmazottak/Tanarok/Osztalyfonokok",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
        query={"Uids": uids},
    )


@overload
def getConsultingHour(
    session: AsyncClient[JsonSerializeable], uid: str
) -> Awaitable[ConsultingHour]: ...
@overload
def getConsultingHour(
    session: SyncClient[JsonSerializeable], uid: str
) -> ConsultingHour: ...
def getConsultingHour(session: Client, uid: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + f"sajat/Fogadoorak/{uid}",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
    )


@overload
def getConsultingHours(
    session: AsyncClient[JsonSerializeable], fromDate: str, toDate: str
) -> Awaitable[list[ConsultingHourList]]: ...
@overload
def getConsultingHours(
    session: SyncClient[JsonSerializeable], fromDate: str, toDate: str
) -> list[ConsultingHourList]: ...
def getConsultingHours(session: Client, fromDate: str, toDate: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "sajat/Fogadoorak",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
        query={"datumTol": fromDate, "datumIg": toDate},
    )


@overload
def getContact(session: AsyncClient[JsonSerializeable]) -> Awaitable[Contact]: ...
@overload
def getContact(session: SyncClient[JsonSerializeable]) -> Contact: ...
def getContact(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "sajat/Elerhetoseg",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
    )


@overload
def getEvaluations(
    session: AsyncClient[JsonSerializeable], fromDate: str, toDate: str
) -> Awaitable[list[Evaluation]]: ...
@overload
def getEvaluations(
    session: SyncClient[JsonSerializeable], fromDate: str, toDate: str
) -> list[Evaluation]: ...
def getEvaluations(session: Client, fromDate: str, toDate: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "sajat/Ertekelesek",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
        query={"datumTol": fromDate, "datumIg": toDate},
    )


@overload
def getGroups(session: AsyncClient[JsonSerializeable]) -> Awaitable[list[Group]]: ...
@overload
def getGroups(session: SyncClient[JsonSerializeable]) -> list[Group]: ...
def getGroups(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "sajat/OsztalyCsoportok",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
    )


@overload
def getGuardian4T(session: AsyncClient[JsonSerializeable]) -> Awaitable[Guardian4T]: ...
@overload
def getGuardian4T(session: SyncClient[JsonSerializeable]) -> Guardian4T: ...
def getGuardian4T(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "sajat/GondviseloAdatlap",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
    )


@overload
def getHomework(
    session: AsyncClient[JsonSerializeable], id: str
) -> Awaitable[Homework]: ...
@overload
def getHomework(session: SyncClient[JsonSerializeable], id: str) -> Homework: ...
def getHomework(session: Client, id: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + f"sajat/HaziFeladatok/{id}",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
    )


@overload
def getHomeworks(
    session: AsyncClient[JsonSerializeable], fromDate: str, toDate: str
) -> Awaitable[list[Homework]]: ...
@overload
def getHomeworks(
    session: SyncClient[JsonSerializeable], fromDate: str, toDate: str
) -> list[Homework]: ...
def getHomeworks(session: Client, fromDate: str, toDate: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "sajat/HaziFeladatok",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
        query={"datumTol": fromDate, "datumIg": toDate},
    )


@overload
def getLEPEvents(
    session: AsyncClient[JsonSerializeable],
) -> Awaitable[list[LepEvent]]: ...
@overload
def getLEPEvents(session: SyncClient[JsonSerializeable]) -> list[LepEvent]: ...
def getLEPEvents(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "Lep/Eloadasok",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
    )


@overload
def getLesson(
    session: AsyncClient[JsonSerializeable], uid: str
) -> Awaitable[Lesson]: ...
@overload
def getLesson(session: SyncClient[JsonSerializeable], uid: str) -> Lesson: ...
def getLesson(session: Client, uid: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "sajat/OrarendElem",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
        query={"orarendElemUid": uid},
    )


@overload
def getLessons(
    session: AsyncClient[JsonSerializeable], fromDate: str, toDate: str
) -> Awaitable[list[Lesson]]: ...
@overload
def getLessons(
    session: SyncClient[JsonSerializeable], fromDate: str, toDate: str
) -> list[Lesson]: ...
def getLessons(session: Client, fromDate: str, toDate: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "sajat/OrarendElemek",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
        query={"datumTol": fromDate, "datumIg": toDate},
    )


@overload
def getNepEvents(
    session: AsyncClient[JsonSerializeable],
) -> Awaitable[list[NepEvent]]: ...
@overload
def getNepEvents(session: SyncClient[JsonSerializeable]) -> list[NepEvent]: ...
def getNepEvents(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "Nep/Programok",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
    )


@overload
def getNotes(
    session: AsyncClient[JsonSerializeable], fromDate: str, toDate: str
) -> Awaitable[list[Note]]: ...
@overload
def getNotes(
    session: SyncClient[JsonSerializeable], fromDate: str, toDate: str
) -> list[Note]: ...
def getNotes(session: Client, fromDate: str, toDate: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "sajat/Feljegyzesek",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
        query={"datumTol": fromDate, "datumIg": toDate},
    )


@overload
def getNoticeBoardItems(
    session: AsyncClient[JsonSerializeable],
) -> Awaitable[list[NoticeBoardItem]]: ...
@overload
def getNoticeBoardItems(
    session: SyncClient[JsonSerializeable],
) -> list[NoticeBoardItem]: ...
def getNoticeBoardItems(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "sajat/FaliujsagElemek",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
    )


@overload
def getOmissions(
    session: AsyncClient[JsonSerializeable], fromDate: str, toDate: str
) -> Awaitable[list[Omission]]: ...
@overload
def getOmissions(
    session: SyncClient[JsonSerializeable], fromDate: str, toDate: str
) -> list[Omission]: ...
def getOmissions(session: Client, fromDate: str, toDate: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "sajat/Mulasztasok",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
        query={"datumTol": fromDate, "datumIg": toDate},
    )


@overload
def getRegistrationEnabled(
    session: AsyncClient[JsonSerializeable],
) -> Awaitable[bool]: ...
@overload
def getRegistrationEnabled(session: SyncClient[JsonSerializeable]) -> bool: ...
def getRegistrationEnabled(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "TargyiEszkoz/IsRegisztracioEngedelyezett",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
    )


@overload
def getSchoolYearCalendar(
    session: AsyncClient[JsonSerializeable],
) -> Awaitable[list[SchoolYearCalendarEntry]]: ...
@overload
def getSchoolYearCalendar(
    session: SyncClient[JsonSerializeable],
) -> list[SchoolYearCalendarEntry]: ...
def getSchoolYearCalendar(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "sajat/Intezmenyek/TanevRendjeElemek",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
    )


@overload
def getStudent(session: AsyncClient[JsonSerializeable]) -> Awaitable[Student]: ...
@overload
def getStudent(session: SyncClient[JsonSerializeable]) -> Student: ...
def getStudent(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "sajat/TanuloAdatlap",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
    )


@overload
def getSubjectAverage(
    session: AsyncClient[JsonSerializeable], educationTypeUid: str
) -> Awaitable[list[SubjectAverage]]: ...
@overload
def getSubjectAverage(
    session: SyncClient[JsonSerializeable], educationTypeUid: str
) -> list[SubjectAverage]: ...
def getSubjectAverage(session: Client, educationTypeUid: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "sajat/Ertekelesek/Atlagok/TantargyiAtlagok",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
        query={"oktatasiNevelesiFeladatUid": educationTypeUid},
    )


@overload
def getTeszekRegistration(
    session: AsyncClient[JsonSerializeable],
) -> Awaitable[TeszekRegistration]: ...
@overload
def getTeszekRegistration(
    session: SyncClient[JsonSerializeable],
) -> TeszekRegistration: ...
def getTeszekRegistration(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "TargyiEszkoz/Regisztracio",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
    )


@overload
def getTimeTableWeeks(
    session: AsyncClient[JsonSerializeable], toDate: str, fromDate: str
) -> Awaitable[list[TimeTableWeek]]: ...
@overload
def getTimeTableWeeks(
    session: SyncClient[JsonSerializeable], toDate: str, fromDate: str
) -> list[TimeTableWeek]: ...
def getTimeTableWeeks(session: Client, toDate: str, fromDate: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "GET",
        BASE_URL + "sajat/Intezmenyek/Hetirendek/Orarendi",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
        query={
            "orarendElemKezdoNapDatuma": toDate,
            "orarendElemVegNapDatuma": fromDate,
        },
    )


@overload
def postBankAccountNumber(
    session: AsyncClient[JsonSerializeable], set: BankAccountNumberPost
) -> Awaitable[None]: ...
@overload
def postBankAccountNumber(
    session: SyncClient[JsonSerializeable], set: BankAccountNumberPost
) -> None: ...
def postBankAccountNumber(session: Client, set: BankAccountNumberPost):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "POST",
        BASE_URL + "sajat/Bankszamla",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
        json=set.model_dump(mode="json"),
    )


@overload
def postContact(
    session: AsyncClient[JsonSerializeable], emailAddress: str, phoneNumber: str
) -> Awaitable[None]: ...
@overload
def postContact(
    session: SyncClient[JsonSerializeable], emailAddress: str, phoneNumber: str
) -> None: ...
def postContact(session: Client, emailAddress: str, phoneNumber: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "POST",
        BASE_URL + "sajat/Elerhetoseg",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
    )


@overload
def postCovidForm(session: AsyncClient[JsonSerializeable]) -> Awaitable[None]: ...
@overload
def postCovidForm(session: SyncClient[JsonSerializeable]) -> None: ...
def postCovidForm(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "POST",
        BASE_URL + "Bejelentes/Covid",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
    )


@overload
def postEmailVerification(
    session: AsyncClient[JsonSerializeable],
) -> Awaitable[None]: ...
@overload
def postEmailVerification(session: SyncClient[JsonSerializeable]) -> None: ...
def postEmailVerification(session: Client):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "POST",
        BASE_URL + "sajat/Email/Megerosites",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
    )


@overload
def postReservation(
    session: AsyncClient[JsonSerializeable], timeSlotUid: str
) -> Awaitable[None]: ...
@overload
def postReservation(
    session: SyncClient[JsonSerializeable], timeSlotUid: str
) -> None: ...
def postReservation(session: Client, timeSlotUid: str):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "POST",
        BASE_URL + f"sajat/Fogadoorak/Idopontok/Jelentkezesek/{timeSlotUid}",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
    )


@overload
def postTeszekRegistration(
    session: AsyncClient[JsonSerializeable], body: Guardian4TPost
) -> Awaitable[None]: ...
@overload
def postTeszekRegistration(
    session: SyncClient[JsonSerializeable], body: Guardian4TPost
) -> None: ...
def postTeszekRegistration(session: Client, body: Guardian4TPost):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "POST",
        BASE_URL + "TargyiEszkoz/Regisztracio",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
        json=body.model_dump(mode="json"),
    )


@overload
def updateGuardian4T(
    session: AsyncClient[JsonSerializeable], body: Guardian4TPost
) -> Awaitable[None]: ...
@overload
def updateGuardian4T(
    session: SyncClient[JsonSerializeable], body: Guardian4TPost
) -> None: ...
def updateGuardian4T(session: Client, body: Guardian4TPost):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "PUT",
        BASE_URL + "sajat/GondviseloAdatlap",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
        json=body.model_dump(mode="json"),
    )


@overload
def updateLepEventPermission(
    session: AsyncClient[JsonSerializeable], body: LepEventGuardianPermissionPost
) -> Awaitable[None]: ...
@overload
def updateLepEventPermission(
    session: SyncClient[JsonSerializeable], body: LepEventGuardianPermissionPost
) -> None: ...
def updateLepEventPermission(session: Client, body: LepEventGuardianPermissionPost):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "POST",
        BASE_URL + "Lep/Eloadasok/GondviseloEngedelyezes",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
        json=body.model_dump(mode="json"),
    )


@overload
def updateNepEventPermission(
    session: AsyncClient[JsonSerializeable], body: NepEventGuardianPermissionPost
) -> Awaitable[None]: ...
@overload
def updateNepEventPermission(
    session: SyncClient[JsonSerializeable], body: NepEventGuardianPermissionPost
) -> None: ...
def updateNepEventPermission(session: Client, body: NepEventGuardianPermissionPost):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")
    return session.request(
        "POST",
        BASE_URL + "Nep/Programok/GondviseloEngedelyezes",
        headers={"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463"},
        json=body.model_dump(mode="json"),
    )
