from datetime import datetime, timedelta
from ..idp.auth_session import Auth_Session
from .models import *
from typing import Literal, TypeVar, Type, get_origin, get_args
from requests import Response
from pydantic import BaseModel


T = TypeVar("T")    
def mobile_request(
    session: Auth_Session,
    method: Literal["GET", "DELETE", "POST", "PUT"],
    url: str,
    *args,
    model: Type[T] = Response,
    **kwargs,
) -> T:
    url = "https://{institute_code}.e-kreta.hu/ellenorzo/v3/" + url

    r = session.request(method, url, *args, **kwargs)

    if model is Response:
        return r

    data = r.json()

    origin = get_origin(model)
    if origin is list:
        inner_model: BaseModel = get_args(model)[0]
        return [inner_model.model_validate(item) for item in data]

    return model(data)


def delete_bank_account_number(session: Auth_Session) -> None:
    mobile_request(session, "DELETE", "sajat/Bankszamla")


def delete_reservation(session: Auth_Session, uid: str) -> None:
    mobile_request(
        session,
        "DELETE",
        f"sajat/Fogadoorak/Idopontok/Jelentkezesek/{uid}",
    )


def download_attachment(session: Auth_Session, uid: str) -> bytes:
    return mobile_request(
        session,
        "GET",
        f"sajat/Csatolmany/{uid}",
    ).content


def get_announced_tests(
    session: Auth_Session, from_date: datetime = ..., to_date: datetime = ...
) -> list[AnnouncedTest]:
    params: dict[str, str] = {}
    if from_date is not ...:
        params["datumTol"] = from_date.isoformat()
    if to_date is not ...:
        params["datumIg"] = to_date.isoformat()

    return mobile_request(
        session,
        "GET",
        "sajat/BejelentettSzamonkeresek",
        model=list[AnnouncedTest],
        params=params,
    )


def get_class_average(
    session: Auth_Session, educationalTaskUid: str, subjectUid: str = ...
) -> list[ClassAverage]:
    params: dict[str, str] = {"oktatasiNevelesiFeladatUid": educationalTaskUid}
    if subjectUid is not ...:
        params["tantargyUid"] = subjectUid

    return mobile_request(
        session,
        "GET",
        "sajat/Ertekelesek/Atlagok/OsztalyAtlagok",
        model=list[ClassAverage],
        params=params,
    )

def get_class_master(
    session: Auth_Session, Uids: list[str] = ...
) -> list[ClassMaster]:
    if Uids is not ...:
        params: dict[str, str] = {"Uids": " ".join(Uids)}

    return mobile_request(
        session,
        "GET",
        "felhasznalok/Alkalmazottak/Tanarok/Osztalyfonokok",
        model=list[ClassMaster],
        params=params,
    )


def get_consulting_hour(session: Auth_Session, Uid: str) -> ConsultingHour:
    return mobile_request(
        session,
        "GET",
        f"sajat/Fogadoorak/{Uid}",
        model=ConsultingHour
    )


def get_consulting_hours(
    session: Auth_Session, from_date: datetime = ..., to_date: datetime = ...
) -> list[ConsultingHour]:
    params: dict[str, str] = {}
    if from_date is not ...:
        params["datumTol"] = from_date.isoformat()
    if to_date is not ...:
        params["datumIg"] = to_date.isoformat()

    return mobile_request(
        session,
        "GET",
        "sajat/Fogadoorak",
        model=ConsultingHour,
        params=params,
    )

def get_device_state(session: Auth_Session) -> bool:
    return mobile_request(
        session,
        "GET",
        "TargyiEszkoz/IsEszkozKiosztva"
    ).json()


def get_evaluations(
    session: Auth_Session, from_date: datetime = ..., to_date: datetime = ...
) -> list[Evaluation]:
    params: dict[str, str] = {}
    if from_date is not ...:
        params["datumTol"] = from_date
    if to_date is not ...:
        params["datumIg"] = to_date

    return mobile_request(
        session,
        "GET",
        "sajat/Ertekelesek",
        model=list[Evaluation],
        params=params
    )

def get_groups(session: Auth_Session) -> list[Group]:
    return mobile_request(session, "GET", "sajat/OsztalyCsoportok", model=list[Group]).json()

def get_guardian4t(session: Auth_Session) -> Guardian4T:
    return mobile_request(
        session,
        "GET",
        "sajat/GondviseloAdatlap",
        model=Guardian4T
    )

def get_homework(session: Auth_Session, id: str) -> Homework:
    return mobile_request(
        session,
        "GET",
        f"sajat/HaziFeladatok/{id}",
        model=Homework
    )

def get_homeworks(
    session: Auth_Session, from_date: datetime = ..., to_date: datetime = ...
) -> list[Homework]:
    params: dict[str, str] = {"datumTol": from_date.isoformat()}
    if to_date is not ...:
        params["datumIg"] = to_date.isoformat()

    return mobile_request(
        session,
        "GET",
        "sajat/HaziFeladatok",
        model=list[Homework],
        params=params,
    )


def get_lep_events(session: Auth_Session) -> list[LepEvent]:
    return mobile_request(
        session, "GET", "Lep/Eloadasok",
        model=LepEvent
    )


def get_lesson(session: Auth_Session, LessonUid: str) -> Lesson:
    params: dict[str, str] = {"ororendElemUid": LessonUid}

    return mobile_request(
        session,
        "GET",
        "OrarendElem",
        model=Lesson,
        params=params,
    )


def get_lessons(
    session: Auth_Session, from_date: datetime = ..., to_date: datetime = ...
) -> list[Lesson]:
    params: dict[str, str] = {}
    if from_date is not ...:
        params["datumTol"] = from_date.isoformat()
    if to_date is not ...:
        params["datumIg"] = to_date.isoformat()

    return mobile_request(
        session,
        "GET",
        "OrarendElem",
        model=list[Lesson],
        params=params,
    )


def get_notes(
    session: Auth_Session, from_date: datetime = ..., to_date: datetime = ...
) -> list[Note]:
    params: dict[str, str] = {}
    if from_date is not ...:
        params["datumTol"] = from_date.isoformat()
    if to_date is not ...:
        params["datumIg"] = to_date.isoformat()

    return mobile_request(
        session,
        "GET",
        "Feljegyzesek",
        model=list[Note],
        params=params,
    )


def get_noticeboard_items(session: Auth_Session) -> list[NoticeBoardItem]:
    return mobile_request(session, "GET", "FaliujsagElemek", model=list[NoticeBoardItem])


def get_ommissions(
    session: Auth_Session, from_date: datetime = ..., to_date: datetime = ...
) -> list[Omission]:
    params: dict[str, str] = {}
    if from_date is not ...:
        params["datumTol"] = from_date.isoformat()
    if to_date is not ...:
        params["datumIg"] = to_date.isoformat()

    return mobile_request(
        session,
        "GET",
        "Mulasztasok",
        model=list[Omission],
        params=params,
    )


def get_registration_state(session: Auth_Session) -> dict | str | int | list:
    return mobile_request(
        session,
        "GET",
        "https://{institute_code}.e-kreta.hu/ellenorzo/v3/TargyiEszkoz/IsRegisztralt",
    ).json()


def get_schoolyear_calendar(
    session: Auth_Session,
) -> list[SchoolYearCalendarEntry]:
    return mobile_request(
        session,
        "GET",
        "Intezmenyek/TanevRendjeElemek",
        model=list[SchoolYearCalendarEntry]
    )

def get_student(session: Auth_Session) -> Student:
    return mobile_request(session, "GET", "TanuloAdatlap", model=Student)


def get_subject_average(
    session: Auth_Session, educationalTaskUid: str
) -> list[SubjectAverage]:
    params: dict[str, str] = {"oktatasiNevelesiFeladatUid": educationalTaskUid}

    return mobile_request(
        session,
        "GET",
        "Ertekelesek/Atlagok/OsztalyAtlagok",
        model=list[SubjectAverage],
        params=params,
    )


def get_timetable_weeks(
    session: Auth_Session, start_week: datetime, no_weeks: Literal[1, 2, 3]
) -> list[TimeTableWeek]:
    date = start_week.date()
    monday = date - timedelta(days=date.weekday())
    friday = monday + timedelta(days=6, weeks=no_weeks - 1)

    params: dict[str, str] = {}
    if monday is not ...:
        params["orarendElemKezdoNapDatuma"] = monday.isoformat()
    if friday is not ...:
        params["orarendElemVegNapDatuma"] = friday.isoformat()

    return mobile_request(
        session,
        "GET",
        "Intezmenyek/Hetirendek/Orarendi",
        model=list[TimeTableWeek],
        params=params,
    )

def post_bank_account_number(
    session: Auth_Session,
    bankAccountNumber: str,
    bankAccountOwnerName: str,
    bankAccountOwnerType: int,
    bankName: str,
) -> None:
    json = {
        "BankszamlaSzam": bankAccountNumber,
        "BankszamlaTulajdonosNeve": bankAccountOwnerName,
        "BankszamlaTulajdonosTipusId": bankAccountOwnerType,
        "SzamlavezetoBank": bankName,
    }

    mobile_request(
        session,
        "POST",
        "Bankszamla",
        json=json,
    )
    return None


def post_contact(session: Auth_Session, email: str, phone_number: str) -> None:
    data = {"email": email, "telefonszam": phone_number}

    mobile_request(
        session,
        "POST",
        "Elerhetoseg",
        data=data,
    )
    return None


def post_covid_form(session: Auth_Session) -> None:
    mobile_request(
        session,
        "POST",
        "https://{institute_code}.e-kreta.hu/ellenorzo/v3/Bejelentes/Covid",
    )
    return None


def post_reservation(session: Auth_Session, uid: str) -> None:
    mobile_request(
        session,
        "POST",
        f"Fogadoorak/Idopontok/Jelentkezesek/{uid}",
    )
    return None


def post_teszek_registration(
    session: Auth_Session,
    dateOfBirth: datetime,
    firstname: str,
    firstnameOfBirth: str,
    isAszfAccepted: bool,
    mothersFirstname: str,
    mothersSurname: str,
    namePrefix: str,
    placeOfBirth: str,
    surname: str,
    surnameOfBirth: str,
) -> None:
    data = {
        "SzuletesiDatum": dateOfBirth,
        "Utonev": firstname,
        "SzuletesiUtonev": firstnameOfBirth,
        "IsElfogadottAszf": isAszfAccepted,
        "AnyjaUtonev": mothersFirstname,
        "AnyjaVezeteknev": mothersSurname,
        "Elotag": namePrefix,
        "SzuletesiHely": placeOfBirth,
        "Vezeteknev": surname,
        "SzuletesiVezeteknev": surnameOfBirth,
    }

    mobile_request(
        session,
        "POST",
        "https://{institute_code}.e-kreta.hu/ellenorzo/v3/TargyiEszkoz/Regisztracio",
        data=data,
    )
    return None


def update_guardian4T(
    session: Auth_Session,
    dateOfBirth: datetime,
    firstname: str,
    firstnameOfBirth: str,
    isAszfAccepted: bool,
    mothersFirstname: str,
    mothersSurname: str,
    namePrefix: str,
    placeOfBirth: str,
    surname: str,
    surnameOfBirth: str,
) -> None:
    data = {
        "SzuletesiDatum": dateOfBirth,
        "Utonev": firstname,
        "SzuletesiUtonev": firstnameOfBirth,
        "IsElfogadottAszf": isAszfAccepted,
        "AnyjaUtonev": mothersFirstname,
        "AnyjaVezeteknev": mothersSurname,
        "Elotag": namePrefix,
        "SzuletesiHely": placeOfBirth,
        "Vezeteknev": surname,
        "SzuletesiVezeteknev": surnameOfBirth,
    }

    mobile_request(
        session,
        "PUT",
        "GondviseloAdatlap",
        data=data,
    )
    return None


def update_LEP_event_permission(
    session: Auth_Session, eventId: int, isPermitted: bool
) -> None:
    json = {"EloadasId": eventId, "Dontes": isPermitted}

    mobile_request(
        session,
        "POST",
        "https://{institute_code}.e-kreta.hu/ellenorzo/v3/Lep/Eloadasok/GondviseloEngedelyezes",
        json=json,
    )
    return None
