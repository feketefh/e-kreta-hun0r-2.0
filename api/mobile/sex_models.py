from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from ..models import SubjectDescriptor, UidNameStructure, UidStructure, ValueDescriptor


class AnnouncedTest(BaseModel):
    subjectName: str = Field(alias="TantargyNeve", frozen=True, default=None)
    announcedAt: datetime = Field(alias="BejelentesDatuma", frozen=True, default=None)
    classScheduleNumber: int = Field(
        alias="OrarendiOraOraszama", frozen=True, default=None
    )
    date: datetime = Field(alias="Datum", frozen=True, default=None)
    group: UidStructure = Field(alias="OsztalyCsoport", frozen=True, default=None)
    mode: ValueDescriptor = Field(alias="Modja", frozen=True, default=None)
    subject: SubjectDescriptor = Field(alias="Tantargy", frozen=True, default=None)
    teacher: str = Field(alias="RogzitoTanarNeve", frozen=True, default=None)
    theme: str = Field(alias="Temaja", frozen=True, default=None)
    uid: str = Field(alias="Uid", frozen=True, default=None)


class ClassAverage(BaseModel):
    average: float = Field(alias="TanuloAtlag", frozen=True, default=None)
    classAverageNumber: float = Field(
        alias="OsztalyCsoportAtlag", frozen=True, default=None
    )
    differenceFromClassAverage: float = Field(
        alias="OsztalyCsoportAtlagtolValoElteres", frozen=True, default=None
    )
    subject: SubjectDescriptor = Field(alias="Tantargy", frozen=True, default=None)
    uid: str = Field(alias="Uid", frozen=True, default=None)


class ClassMaster(BaseModel):
    listOfClass: list[SchoolClass] = Field(alias="Osztalyai", frozen=True, default=None)
    teacher: Teacher = Field(alias="Tanar", frozen=True, default=None)
    uid: str = Field(alias="Uid", frozen=True, default=None)


class Email(BaseModel):
    email: str = Field(alias="Email", frozen=True, default=None)
    uid: str = Field(alias="Uid", frozen=True, default=None)


class Employee(BaseModel):
    email: list[Email] = Field(alias="Emailek", frozen=True, default=None)
    name: str = Field(alias="Nev", frozen=True, default=None)
    phoneList: list[Phone] = Field(alias="Telefonok", frozen=True, default=None)
    uid: str = Field(alias="Uid", frozen=True, default=None)


class Phone(BaseModel):
    phone: str = Field(alias="Telefonszam", frozen=True, default=None)
    uid: str = Field(alias="Uid", frozen=True, default=None)


class Teacher(BaseModel):
    employee: Employee = Field(alias="Alkalmazott", frozen=True, default=None)
    uid: str = Field(alias="Uid", frozen=True, default=None)


class ConsultingHour(BaseModel):
    classroomDescriptor: UidNameStructure = Field(
        alias="Terem", frozen=True, default=None
    )
    consultingHourTimeSlots: list[ConsultingHourTimeSlot] = Field(
        alias="Idopontok", frozen=True, default=None
    )
    deadline: datetime = Field(alias="JelentkezesHatarido", frozen=True, default=None)
    endTime: datetime = Field(alias="VegIdopont", frozen=True, default=None)
    isReservationEnabled: bool = Field(
        alias="IsJelentkezesFeatureEnabled", frozen=True, default=None
    )
    startTime: datetime = Field(alias="KezdoIdopont", frozen=True, default=None)
    uid: str = Field(alias="Uid", frozen=True, default=None)


class Evaluation(BaseModel):
    creatingTime: datetime = Field(alias="KeszitesDatuma", frozen=True, default=None)
    form: str = Field(alias="Jelleg", frozen=True, default=None)
    formType: ValueDescriptor = Field(alias="ErtekFajta", frozen=True, default=None)
    group: UidStructure = Field(alias="OsztalyCsoport", frozen=True, default=None)
    mode: ValueDescriptor = Field(alias="Mod", frozen=True, default=None)
    numberValue: int = Field(alias="SzamErtek", frozen=True, default=None)
    recordDate: datetime = Field(alias="RogzitesDatuma", frozen=True, default=None)
    seenByTutelary: datetime = Field(
        alias="LattamozasDatuma", frozen=True, default=None
    )
    shortValue: str = Field(
        alias="SzovegesErtekelesRovidNev", frozen=True, default=None
    )
    sortIndex: int = Field(alias="SortIndex", frozen=True, default=None)
    subject: SubjectDescriptor = Field(alias="Tantargy", frozen=True, default=None)
    teacher: str = Field(alias="ErtekeloTanarNeve", frozen=True, default=None)
    theme: str = Field(alias="Tema", frozen=True, default=None)
    type: ValueDescriptor = Field(alias="Tipus", frozen=True, default=None)
    uid: str = Field(alias="Uid", frozen=True, default=None)
    value: str = Field(alias="SzovegesErtek", frozen=True, default=None)
    weight: str = Field(alias="SulySzazalekErteke", frozen=True, default=None)


class Group(BaseModel):
    category: ValueDescriptor = Field(
        alias="OktatasNevelesiKategoria", frozen=True, default=None
    )
    classMaster: UidStructure = Field(alias="OsztalyFonok", frozen=True, default=None)
    classMasterAssistant: UidStructure = Field(
        alias="OsztalyFonokHelyettes", frozen=True, default=None
    )
    educationType: ValueDescriptor = Field(
        alias="OktatasNevelesiFeladat", frozen=True, default=None
    )
    isActive: bool = Field(alias="IsAktiv", frozen=True, default=None)
    name: str = Field(alias="Nev", frozen=True, default=None)
    sortIndex: int = Field(
        alias="OktatasNevelesiFeladatSortIndex", frozen=True, default=None
    )
    type: str = Field(alias="Tipus", frozen=True, default=None)
    uid: str = Field(alias="Uid", frozen=True, default=None)


class Guardian4T(BaseModel):
    dateOfBirth: datetime = Field(alias="SzuletesiDatum", frozen=True, default=None)
    firstname: str = Field(alias="Utonev", frozen=True, default=None)
    firstnameOfBirth: str = Field(alias="SzuletesiUtonev", frozen=True, default=None)
    mothersFirstname: str = Field(alias="AnyjaUtonev", frozen=True, default=None)
    mothersSurname: str = Field(alias="AnyjaVezeteknev", frozen=True, default=None)
    namePrefix: str = Field(alias="Elotag", frozen=True, default=None)
    placeOfBirth: str = Field(alias="SzuletesiHely", frozen=True, default=None)
    surname: str = Field(alias="Vezeteknev", frozen=True, default=None)
    surnameOfBirth: str = Field(alias="SzuletesiVezeteknev", frozen=True, default=None)


class Homework(BaseModel):
    subjectName: str = Field(alias="TantargyNeve", frozen=True, default=None)
    attachmentList: list[Attachment] = Field(
        alias="Csatolmanyok", frozen=True, default=None
    )
    createDate: datetime = Field(alias="RogzitesIdopontja", frozen=True, default=None)
    deadlineDate: datetime = Field(alias="HataridoDatuma", frozen=True, default=None)
    group: UidStructure = Field(alias="OsztalyCsoport", frozen=True, default=None)
    isAllowToAttachFile: bool = Field(
        alias="IsCsatolasEngedelyezes", frozen=True, default=None
    )
    isDone: bool = Field(alias="IsMegoldva", frozen=True, default=None)
    isStudentHomeworkEnabled: bool = Field(
        alias="IsTanuloHaziFeladatEnabled", frozen=True, default=None
    )
    isTeacherRecorded: bool = Field(
        alias="IsTanarRogzitette", frozen=True, default=None
    )
    recordDate: datetime = Field(alias="FeladasDatuma", frozen=True, default=None)
    recorderTeacherName: str = Field(
        alias="RogzitoTanarNeve", frozen=True, default=None
    )
    subject: SubjectDescriptor = Field(alias="Tantargy", frozen=True, default=None)
    submitable: bool = Field(alias="IsBeadhato", frozen=True, default=None)
    text: str = Field(alias="Szoveg", frozen=True, default=None)
    uid: str = Field(alias="Uid", frozen=True, default=None)


class Attachment(BaseModel):
    name: str = Field(alias="Nev", frozen=True, default=None)
    type: str = Field(alias="Tipus", frozen=True, default=None)
    uid: str = Field(alias="Uid", frozen=True, default=None)


class LepEvent(BaseModel):
    address: str = Field(alias="Helyszin", frozen=True, default=None)
    creationDate: datetime = Field(alias="Datum", frozen=True, default=None)
    eventEndTime: datetime = Field(alias="EloadasVege", frozen=True, default=None)
    eventStartTime: datetime = Field(alias="EloadasKezdete", frozen=True, default=None)
    eventTitle: str = Field(alias="EloadasNev", frozen=True, default=None)
    hasGuardianPermission: bool = Field(
        alias="GondviseloElfogadas", frozen=True, default=None
    )
    hasStudentAppeared: bool = Field(alias="Megjelent", frozen=True, default=None)
    organizationName: str = Field(alias="SzervezetNev", frozen=True, default=None)
    uid: str = Field(alias="Uid", frozen=True, default=None)


class Lesson(BaseModel):
    announcedTestUid: str = Field(
        alias="BejelentettSzamonkeresUid", frozen=True, default=None
    )
    attachments: list[Attachment] = Field(
        alias="Csatolmanyok", frozen=True, default=None
    )
    classGroup: UidNameStructure = Field(
        alias="OsztalyCsoport", frozen=True, default=None
    )
    classScheduleNumber: int = Field(alias="Oraszam", frozen=True, default=None)
    classroom: str = Field(alias="TeremNeve", frozen=True, default=None)
    classworkGroupId: str = Field(alias="FeladatGroupUid", frozen=True, default=None)
    digitalInstrumentType: str = Field(
        alias="DigitalisEszkozTipus", frozen=True, default=None
    )
    digitalPlatformType: str = Field(
        alias="DigitalisPlatformTipus", frozen=True, default=None
    )
    endTime: datetime = Field(alias="VegIdopont", frozen=True, default=None)
    homeWorkUid: str = Field(alias="HaziFeladatUid", frozen=True, default=None)
    homeworkEditedByStudentEnabled: bool = Field(
        alias="IsTanuloHaziFeladatEnabled", frozen=True, default=None
    )
    isDigitalLesson: bool = Field(alias="IsDigitalisOra", frozen=True, default=None)
    languageTaskGroupId: str = Field(
        alias="NyelviFeladatGroupUid", frozen=True, default=None
    )
    lessonNumber: int = Field(alias="OraEvesSorszama", frozen=True, default=None)
    name: str = Field(alias="Nev", frozen=True, default=None)
    presence: ValueDescriptor = Field(alias="TanuloJelenlet", frozen=True, default=None)
    startTime: datetime = Field(alias="KezdetIdopont", frozen=True, default=None)
    state: ValueDescriptor = Field(alias="Allapot", frozen=True, default=None)
    subject: SubjectDescriptor = Field(alias="Tantargy", frozen=True, default=None)
    supplyTeacher: str = Field(alias="HelyettesTanarNeve", frozen=True, default=None)
    supportedDigitalInstrumentTypes: list[str] = Field(
        alias="DigitalisTamogatoEszkozTipusList", frozen=True, default=None
    )
    teacher: str = Field(alias="TanarNeve", frozen=True, default=None)
    topic: str = Field(alias="Tema", frozen=True, default=None)
    type: ValueDescriptor = Field(alias="Tipus", frozen=True, default=None)
    uid: str = Field(alias="Uid", frozen=True, default=None)


class Note(BaseModel):
    content: str = Field(alias="Tartalom", frozen=True, default=None)
    creatingTime: datetime = Field(alias="KeszitesDatuma", frozen=True, default=None)
    date: datetime = Field(alias="Datum", frozen=True, default=None)
    group: UidStructure = Field(alias="OsztalyCsoport", frozen=True, default=None)
    seenByTutelary: datetime = Field(
        alias="LattamozasDatuma", frozen=True, default=None
    )
    teacher: str = Field(alias="KeszitoTanarNeve", frozen=True, default=None)
    title: str = Field(alias="Cim", frozen=True, default=None)
    type: ValueDescriptor = Field(alias="Tipus", frozen=True, default=None)
    uid: str = Field(alias="Uid", frozen=True, default=None)


class NoticeBoardItem(BaseModel):
    content: str = Field(alias="Tartalom", frozen=True, default=None)
    expireEndTime: datetime = Field(alias="ErvenyessegVege", frozen=True, default=None)
    expireStartTime: datetime = Field(
        alias="ErvenyessegKezdete", frozen=True, default=None
    )
    madeBy: str = Field(alias="RogzitoNeve", frozen=True, default=None)
    title: str = Field(alias="Cim", frozen=True, default=None)
    uid: str = Field(alias="Uid", frozen=True, default=None)


class Omission(BaseModel):
    creatingTime: datetime = Field(alias="KeszitesDatuma", frozen=True, default=None)
    date: datetime = Field(alias="Datum", frozen=True, default=None)
    delayTimeMinutes: int = Field(alias="KesesPercben", frozen=True, default=None)
    group: UidStructure = Field(alias="OsztalyCsoport", frozen=True, default=None)
    justificationState: str = Field(alias="IgazolasAllapota", frozen=True, default=None)
    justificationType: ValueDescriptor = Field(
        alias="IgazolasTipusa", frozen=True, default=None
    )
    lesson: Lesson = Field(alias="Ora", frozen=True, default=None)
    mode: ValueDescriptor = Field(alias="Mod", frozen=True, default=None)
    subject: SubjectDescriptor = Field(alias="Tantargy", frozen=True, default=None)
    teacher: str = Field(alias="RogzitoTanarNeve", frozen=True, default=None)
    type: ValueDescriptor = Field(alias="Tipus", frozen=True, default=None)
    uid: str = Field(alias="Uid", frozen=True, default=None)


class SchoolYearCalendarEntry(BaseModel):
    date: datetime = Field(alias="Datum", frozen=True, default=None)
    dayType: ValueDescriptor = Field(alias="Naptipus", frozen=True, default=None)
    group: UidStructure = Field(alias="OsztalyCsoport", frozen=True, default=None)
    irregularDay: ValueDescriptor = Field(
        alias="ElteroOrarendSzerintiTanitasiNap", frozen=True, default=None
    )
    uid: str = Field(alias="Uid", frozen=True, default=None)
    weekTypeSchedule: ValueDescriptor = Field(
        alias="OrarendiNapHetirendje", frozen=True, default=None
    )


class Student(BaseModel):
    addressDataList: list[str] = Field(alias="Cimek", frozen=True, default=None)
    bankAccount: BankAccount = Field(alias="Bankszamla", frozen=True, default=None)
    dayOfBirth: int = Field(alias="SzuletesiNap", frozen=True, default=None)
    emailAddress: str = Field(alias="EmailCim", frozen=True, default=None)
    guardianList: list[Guardian] = Field(alias="Gondviselok", frozen=True, default=None)
    instituteCode: str = Field(alias="IntezmenyAzonosito", frozen=True, default=None)
    instituteName: str = Field(alias="IntezmenyNev", frozen=True, default=None)
    institution: Institution = Field(alias="Intezmeny", frozen=True, default=None)
    monthOfBirth: int = Field(alias="SzuletesiHonap", frozen=True, default=None)
    mothersName: str = Field(alias="AnyjaNeve", frozen=True, default=None)
    name: str = Field(alias="Nev", frozen=True, default=None)
    nameOfBirth: str = Field(alias="SzuletesiNev", frozen=True, default=None)
    phoneNumber: str = Field(alias="Telefonszam", frozen=True, default=None)
    placeOfBirth: str = Field(alias="SzuletesiHely", frozen=True, default=None)
    schoolYearUID: float = Field(alias="TanevUid", frozen=True, default=None)
    uid: str = Field(alias="Uid", frozen=True, default=None)
    yearOfBirth: int = Field(alias="SzuletesiEv", frozen=True, default=None)


class BankAccount(BaseModel):
    accountNumber: str = Field(alias="BankszamlaSzam", frozen=True, default=None)
    isReadOnly: str = Field(alias="IsReadOnly", frozen=True, default=None)
    ownerName: str = Field(alias="BankszamlaTulajdonosNeve", frozen=True, default=None)
    ownerType: str = Field(
        alias="BankszamlaTulajdonosTipusId", frozen=True, default=None
    )


class SubjectAverage(BaseModel):
    averageNumber: float = Field(alias="Atlag", frozen=True, default=None)
    averagesInTime: list[AverageWithTime] = Field(
        alias="AtlagAlakulasaIdoFuggvenyeben", frozen=True, default=None
    )
    sortIndex: int = Field(alias="SortIndex", frozen=True, default=None)
    subject: SubjectDescriptor = Field(alias="Tantargy", frozen=True, default=None)
    sumOfWeightedEvaluations: float = Field(
        alias="SulyozottOsztalyzatOsszege", frozen=True, default=None
    )
    sumOfWeights: float = Field(
        alias="SulyozottOsztalyzatSzama", frozen=True, default=None
    )
    uid: str = Field(alias="Uid", frozen=True, default=None)


class AverageWithTime(BaseModel):
    average: float = Field(alias="Atlag", frozen=True, default=None)
    date: datetime = Field(alias="Datum", frozen=True, default=None)


class TimeTableWeek(BaseModel):
    endDate: datetime = Field(alias="VegNapDatuma", frozen=True, default=None)
    numberOfWeek: int = Field(alias="HetSorszama", frozen=True, default=None)
    startDate: datetime = Field(alias="KezdoNapDatuma", frozen=True, default=None)
    type: ValueDescriptor = Field(alias="Tipus", frozen=True, default=None)
    uid: str = Field(alias="Uid", frozen=True, default=None)


class BankAccountNumberPost(BaseModel):
    bankAccountNumber: str = Field(alias="BankszamlaSzam", frozen=True, default=None)
    bankAccountOwnerName: str = Field(
        alias="BankszamlaTulajdonosNeve", frozen=True, default=None
    )
    bankAccountOwnerType: int = Field(
        alias="BankszamlaTulajdonosTipusId", frozen=True, default=None
    )
    bankName: str = Field(alias="SzamlavezetoBank", frozen=True, default=None)


class Guardian4TPost(BaseModel):
    dateOfBirth: datetime = Field(alias="SzuletesiDatum", frozen=True, default=None)
    firstname: str = Field(alias="Utonev", frozen=True, default=None)
    firstnameOfBirth: str = Field(alias="SzuletesiUtonev", frozen=True, default=None)
    isAszfAccepted: bool = Field(alias="IsElfogadottAszf", frozen=True, default=None)
    mothersFirstname: str = Field(alias="AnyjaUtonev", frozen=True, default=None)
    mothersSurname: str = Field(alias="AnyjaVezeteknev", frozen=True, default=None)
    namePrefix: str = Field(alias="Elotag", frozen=True, default=None)
    placeOfBirth: str = Field(alias="SzuletesiHely", frozen=True, default=None)
    surname: str = Field(alias="Vezeteknev", frozen=True, default=None)
    surnameOfBirth: str = Field(alias="SzuletesiVezeteknev", frozen=True, default=None)


class LepEventGuardianPermissionPost(BaseModel):
    eventId: int = Field(alias="EloadasId", frozen=True, default=None)
    isPermitted: bool = Field(alias="Dontes", frozen=True, default=None)


class SchoolClass(BaseModel):
    category: ValueDescriptor = Field(
        alias="OktatasNevelesiKategoria", frozen=True, default=None
    )
    name: str = Field(alias="Nev", frozen=True, default=None)
    uid: str = Field(alias="Uid", frozen=True, default=None)


class ConsultingHourTimeSlot(BaseModel):
    endTime: datetime = Field(alias="VegIdopont", frozen=True, default=None)
    isReservedByMe: bool = Field(alias="IsJelentkeztem", frozen=True, default=None)
    startTime: datetime = Field(alias="KezdoIdopont", frozen=True, default=None)
    uid: str = Field(alias="Uid", frozen=True, default=None)


class Guardian(BaseModel):
    email: str = Field(alias="EmailCim", frozen=True, default=None)
    isLegalRepresentative: bool = Field(
        alias="IsTorvenyesKepviselo", frozen=True, default=None
    )
    name: str = Field(alias="Nev", frozen=True, default=None)
    phoneNumber: str = Field(alias="Telefonszam", frozen=True, default=None)
    uid: str = Field(alias="Uid", frozen=True, default=None)


class Institution(BaseModel):
    customizationSettings: CustomizationSettings = Field(
        alias="TestreszabasBeallitasok", frozen=True, default=None
    )
    shortName: str = Field(alias="RovidNev", frozen=True, default=None)
    systemModuleList: list[SystemModule] = Field(
        alias="Rendszermodulok", frozen=True, default=None
    )
    uid: str = Field(alias="Uid", frozen=True, default=None)


class CustomizationSettings(BaseModel):
    delayOfNotifications: int = Field(
        alias="ErtekelesekMegjelenitesenekKesleltetesenekMerteke",
        frozen=True,
        default=None,
    )
    isClassAverageVisible: bool = Field(
        alias="IsOsztalyAtlagMegjeleniteseEllenorzoben", frozen=True, default=None
    )
    isLessonsThemeVisible: bool = Field(
        alias="IsTanorakTemajaMegtekinthetoEllenorzoben", frozen=True, default=None
    )
    nextServerDeploy: datetime = Field(
        alias="KovetkezoTelepitesDatuma", frozen=True, default=None
    )


class SystemModule(BaseModel):
    isActive: bool = Field(alias="IsAktiv", frozen=True, default=None)
    type: str = Field(alias="Tipus", frozen=True, default=None)
    url: str = Field(alias="Url", frozen=True, default=None)
