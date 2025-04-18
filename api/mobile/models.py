from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from ..models import UidStructure, UidNameStructure, ValueDescriptor, SubjectDescriptor

class IDK:
    """no data"""

class AnnouncedTest(BaseModel):
    subjectName: str = Field(alias="TantargyNeve", frozen=True)
    announcedAt: datetime = Field(alias="BejelentesDatuma", frozen=True)
    classScheduleNumber: int = Field(alias="OrarendiOraOraszama", frozen=True)
    date: datetime = Field(alias="Datum", frozen=True)
    group: UidStructure = Field(alias="OsztalyCsoport", frozen=True)
    mode: ValueDescriptor = Field(alias="Modja", frozen=True)
    subject: SubjectDescriptor = Field(alias="Tantargy", frozen=True)
    teacher: str = Field(alias="RogzitoTanarNeve", frozen=True)
    theme: str = Field(alias="Temaja", frozen=True)
    uid: str = Field(alias="Uid", frozen=True)

class ClassAverage(BaseModel):
    average: float = Field(alias="TanuloAtlag", frozen=True)
    classAverageNumber: float = Field(alias="OsztalyCsoportAtlag", frozen=True)
    differenceFromClassAverage: float = Field(alias="OsztalyCsoportAtlagtolValoElteres", frozen=True)
    subject: SubjectDescriptor = Field(alias="Tantargy", frozen=True)
    uid: str = Field(alias="Uid", frozen=True)

class ClassMaster(BaseModel):
    listOfClass: list[SchoolClass] = Field(alias="Osztalyai", frozen=True)
    teacher: Teacher = Field(alias="Tanar", frozen=True)
    uid: str = Field(alias="Uid", frozen=True)

class Email(BaseModel):
    email: str = Field(alias="Email", frozen=True)
    uid: str = Field(alias="Uid", frozen=True)

class Employee(BaseModel):
    email: list[Email] = Field(alias="Emailek", frozen=True)
    name: str = Field(alias="Nev", frozen=True)
    phoneList: list[Phone] = Field(alias="Telefonok", frozen=True)
    uid: str = Field(alias="Uid", frozen=True)

class Phone(BaseModel):
    phone: str = Field(alias="Telefonszam", frozen=True)
    uid: str = Field(alias="Uid", frozen=True)

class Teacher(BaseModel):
    employee: Employee = Field(alias="Alkalmazott", frozen=True)
    uid: str = Field(alias="Uid", frozen=True)

class ConsultingHour(BaseModel):
    classroomDescriptor: UidNameStructure = Field(alias="Terem", frozen=True)
    consultingHourTimeSlots: list[ConsultingHourTimeSlot] = Field(alias="Idopontok", frozen=True)
    deadline: datetime = Field(alias="JelentkezesHatarido", frozen=True)
    endTime: datetime = Field(alias="VegIdopont", frozen=True)
    isReservationEnabled: bool = Field(alias="IsJelentkezesFeatureEnabled", frozen=True)
    startTime: datetime = Field(alias="KezdoIdopont", frozen=True)
    uid: str = Field(alias="Uid", frozen=True)

class Evaluation(BaseModel):
    creatingTime: datetime = Field(alias="KeszitesDatuma", frozen=True)
    form: str = Field(alias="Jelleg", frozen=True)
    formType: ValueDescriptor = Field(alias="ErtekFajta", frozen=True)
    group: UidStructure = Field(alias="OsztalyCsoport", frozen=True)
    mode: ValueDescriptor = Field(alias="Mod", frozen=True)
    numberValue: int = Field(alias="SzamErtek", frozen=True)
    recordDate: datetime = Field(alias="RogzitesDatuma", frozen=True)
    seenByTutelary: datetime = Field(alias="LattamozasDatuma", frozen=True)
    shortValue: str = Field(alias="SzovegesErtekelesRovidNev", frozen=True)
    sortIndex: int = Field(alias="SortIndex", frozen=True)
    subject: SubjectDescriptor = Field(alias="Tantargy", frozen=True)
    teacher: str = Field(alias="ErtekeloTanarNeve", frozen=True)
    theme: str = Field(alias="Tema", frozen=True)
    type: ValueDescriptor = Field(alias="Tipus", frozen=True)
    uid: str = Field(alias="Uid", frozen=True)
    value: str = Field(alias="SzovegesErtek", frozen=True)
    weight: str = Field(alias="SulySzazalekErteke", frozen=True)

class Group(BaseModel):
    category: ValueDescriptor = Field(alias="OktatasNevelesiKategoria", frozen=True)
    classMaster: UidStructure = Field(alias="OsztalyFonok", frozen=True)
    classMasterAssistant: UidStructure = Field(alias="OsztalyFonokHelyettes", frozen=True)
    educationType: ValueDescriptor = Field(alias="OktatasNevelesiFeladat", frozen=True)
    isActive: bool = Field(alias="IsAktiv", frozen=True)
    name: str = Field(alias="Nev", frozen=True)
    sortIndex: int = Field(alias="OktatasNevelesiFeladatSortIndex", frozen=True)
    type: str = Field(alias="Tipus", frozen=True)
    uid: str = Field(alias="Uid", frozen=True)

class Guardian4T(BaseModel):
    dateOfBirth: datetime = Field(alias="SzuletesiDatum", frozen=True)
    firstname: str = Field(alias="Utonev", frozen=True)
    firstnameOfBirth: str = Field(alias="SzuletesiUtonev", frozen=True)
    mothersFirstname: str = Field(alias="AnyjaUtonev", frozen=True)
    mothersSurname: str = Field(alias="AnyjaVezeteknev", frozen=True)
    namePrefix: str = Field(alias="Elotag", frozen=True)
    placeOfBirth: str = Field(alias="SzuletesiHely", frozen=True)
    surname: str = Field(alias="Vezeteknev", frozen=True)
    surnameOfBirth: str = Field(alias="SzuletesiVezeteknev", frozen=True)

class Homework(BaseModel):
    subjectName: str = Field(alias="TantargyNeve", frozen=True)
    attachmentList: list[Attachment] = Field(alias="Csatolmanyok", frozen=True)
    createDate: datetime = Field(alias="RogzitesIdopontja", frozen=True)
    deadlineDate: datetime = Field(alias="HataridoDatuma", frozen=True)
    group: UidStructure = Field(alias="OsztalyCsoport", frozen=True)
    isAllowToAttachFile: bool = Field(alias="IsCsatolasEngedelyezes", frozen=True)
    isDone: bool = Field(alias="IsMegoldva", frozen=True)
    isStudentHomeworkEnabled: bool = Field(alias="IsTanuloHaziFeladatEnabled", frozen=True)
    isTeacherRecorded: bool = Field(alias="IsTanarRogzitette", frozen=True)
    recordDate: datetime = Field(alias="FeladasDatuma", frozen=True)
    recorderTeacherName: str = Field(alias="RogzitoTanarNeve", frozen=True)
    subject: SubjectDescriptor = Field(alias="Tantargy", frozen=True)
    submitable: bool = Field(alias="IsBeadhato", frozen=True)
    text: str = Field(alias="Szoveg", frozen=True)
    uid: str = Field(alias="Uid", frozen=True)

class Attachment(BaseModel):
    name: str = Field(alias="Nev", frozen=True)
    type: str = Field(alias="Tipus", frozen=True, default=None)
    uid: str = Field(alias="Uid", frozen=True)

class LepEvent(BaseModel):
    address: str = Field(alias="Helyszin", frozen=True)
    creationDate: datetime = Field(alias="Datum", frozen=True)
    eventEndTime: datetime = Field(alias="EloadasVege", frozen=True)
    eventStartTime: datetime = Field(alias="EloadasKezdete", frozen=True)
    eventTitle: str = Field(alias="EloadasNev", frozen=True)
    hasGuardianPermission: bool = Field(alias="GondviseloElfogadas", frozen=True)
    hasStudentAppeared: bool = Field(alias="Megjelent", frozen=True)
    organizationName: str = Field(alias="SzervezetNev", frozen=True)
    uid: str = Field(alias="Uid", frozen=True)

class Lesson(BaseModel):
    announcedTestUid: str = Field(alias="BejelentettSzamonkeresUid", frozen=True)
    attachments: list[Attachment] = Field(alias="Csatolmanyok", frozen=True)
    classGroup: UidNameStructure = Field(alias="OsztalyCsoport", frozen=True)
    classScheduleNumber: int = Field(alias="Oraszam", frozen=True)
    classroom: str = Field(alias="TeremNeve", frozen=True)
    classworkGroupId: str = Field(alias="FeladatGroupUid", frozen=True)
    digitalInstrumentType: str = Field(alias="DigitalisEszkozTipus", frozen=True)
    digitalPlatformType: str = Field(alias="DigitalisPlatformTipus", frozen=True)
    endTime: datetime = Field(alias="VegIdopont", frozen=True)
    homeWorkUid: str = Field(alias="HaziFeladatUid", frozen=True)
    homeworkEditedByStudentEnabled: bool = Field(alias="IsTanuloHaziFeladatEnabled", frozen=True)
    isDigitalLesson: bool = Field(alias="IsDigitalisOra", frozen=True)
    languageTaskGroupId: str = Field(alias="NyelviFeladatGroupUid", frozen=True)
    lessonNumber: int = Field(alias="OraEvesSorszama", frozen=True)
    name: str = Field(alias="Nev", frozen=True)
    presence: ValueDescriptor = Field(alias="TanuloJelenlet", frozen=True)
    startTime: datetime = Field(alias="KezdetIdopont", frozen=True)
    state: ValueDescriptor = Field(alias="Allapot", frozen=True)
    subject: SubjectDescriptor = Field(alias="Tantargy", frozen=True)
    supplyTeacher: str = Field(alias="HelyettesTanarNeve", frozen=True)
    supportedDigitalInstrumentTypes: list[str] = Field(alias="DigitalisTamogatoEszkozTipusList", frozen=True)
    teacher: str = Field(alias="TanarNeve", frozen=True)
    topic: str = Field(alias="Tema", frozen=True)
    type: ValueDescriptor = Field(alias="Tipus", frozen=True)
    uid: str = Field(alias="Uid", frozen=True)

class Note(BaseModel):
    content: str = Field(alias="Tartalom", frozen=True)
    creatingTime: datetime = Field(alias="KeszitesDatuma", frozen=True)
    date: datetime = Field(alias="Datum", frozen=True)
    group: UidStructure = Field(alias="OsztalyCsoport", frozen=True)
    seenByTutelary: datetime = Field(alias="LattamozasDatuma", frozen=True)
    teacher: str = Field(alias="KeszitoTanarNeve", frozen=True)
    title: str = Field(alias="Cim", frozen=True)
    type: ValueDescriptor = Field(alias="Tipus", frozen=True)
    uid: str = Field(alias="Uid", frozen=True)

class NoticeBoardItem(BaseModel):
    content: str = Field(alias="Tartalom", frozen=True)
    expireEndTime: datetime = Field(alias="ErvenyessegVege", frozen=True)
    expireStartTime: datetime = Field(alias="ErvenyessegKezdete", frozen=True)
    madeBy: str = Field(alias="RogzitoNeve", frozen=True)
    title: str = Field(alias="Cim", frozen=True)
    uid: str = Field(alias="Uid", frozen=True)

class Omission(BaseModel):
    creatingTime: datetime = Field(alias="KeszitesDatuma", frozen=True)
    date: datetime = Field(alias="Datum", frozen=True)
    delayTimeMinutes: int = Field(alias="KesesPercben", frozen=True)
    group: UidStructure = Field(alias="OsztalyCsoport", frozen=True)
    justificationState: str = Field(alias="IgazolasAllapota", frozen=True)
    justificationType: ValueDescriptor = Field(alias="IgazolasTipusa", frozen=True)
    lesson: Lesson = Field(alias="Ora", frozen=True)
    mode: ValueDescriptor = Field(alias="Mod", frozen=True)
    subject: SubjectDescriptor = Field(alias="Tantargy", frozen=True)
    teacher: str = Field(alias="RogzitoTanarNeve", frozen=True)
    type: ValueDescriptor = Field(alias="Tipus", frozen=True)
    uid: str = Field(alias="Uid", frozen=True)

class SchoolYearCalendarEntry(BaseModel):
    date: datetime = Field(alias="Datum", frozen=True)
    dayType: ValueDescriptor = Field(alias="Naptipus", frozen=True)
    group: UidStructure = Field(alias="OsztalyCsoport", frozen=True)
    irregularDay: ValueDescriptor = Field(alias="ElteroOrarendSzerintiTanitasiNap", frozen=True)
    uid: str = Field(alias="Uid", frozen=True)
    weekTypeSchedule: ValueDescriptor = Field(alias="OrarendiNapHetirendje", frozen=True)

class Student(BaseModel):
    addressDataList: list[str] = Field(alias="Cimek", frozen=True)
    bankAccount: BankAccount = Field(alias="Bankszamla", frozen=True)
    dayOfBirth: int = Field(alias="SzuletesiNap", frozen=True)
    emailAddress: str = Field(alias="EmailCim", frozen=True)
    guardianList: list[Guardian] = Field(alias="Gondviselok", frozen=True)
    instituteCode: str = Field(alias="IntezmenyAzonosito", frozen=True)
    instituteName: str = Field(alias="IntezmenyNev", frozen=True)
    institution: Institution = Field(alias="Intezmeny", frozen=True)
    monthOfBirth: int = Field(alias="SzuletesiHonap", frozen=True)
    mothersName: str = Field(alias="AnyjaNeve", frozen=True)
    name: str = Field(alias="Nev", frozen=True)
    nameOfBirth: str = Field(alias="SzuletesiNev", frozen=True)
    phoneNumber: str = Field(alias="Telefonszam", frozen=True)
    placeOfBirth: str = Field(alias="SzuletesiHely", frozen=True)
    schoolYearUID: float = Field(alias="TanevUid", frozen=True)
    uid: str = Field(alias="Uid", frozen=True)
    yearOfBirth: int = Field(alias="SzuletesiEv", frozen=True)

class BankAccount(BaseModel):
    accountNumber: str = Field(alias="BankszamlaSzam", frozen=True)
    isReadOnly: str = Field(alias="IsReadOnly", frozen=True)
    ownerName: str = Field(alias="BankszamlaTulajdonosNeve", frozen=True)
    ownerType: str = Field(alias="BankszamlaTulajdonosTipusId", frozen=True)

class SubjectAverage(BaseModel):
    averageNumber: float = Field(alias="Atlag", frozen=True)
    averagesInTime: list[AverageWithTime] = Field(alias="AtlagAlakulasaIdoFuggvenyeben", frozen=True)
    sortIndex: int = Field(alias="SortIndex", frozen=True)
    subject: SubjectDescriptor = Field(alias="Tantargy", frozen=True)
    sumOfWeightedEvaluations: float = Field(alias="SulyozottOsztalyzatOsszege", frozen=True)
    sumOfWeights: float = Field(alias="SulyozottOsztalyzatSzama", frozen=True)
    uid: str = Field(alias="Uid", frozen=True)

class AverageWithTime(BaseModel):
    average: float = Field(alias="Atlag", frozen=True)
    date: datetime = Field(alias="Datum", frozen=True)

class TimeTableWeek(BaseModel):
    endDate: datetime = Field(alias="VegNapDatuma", frozen=True)
    numberOfWeek: int = Field(alias="HetSorszama", frozen=True)
    startDate: datetime = Field(alias="KezdoNapDatuma", frozen=True)
    type: ValueDescriptor = Field(alias="Tipus", frozen=True)
    uid: str = Field(alias="Uid", frozen=True)

class BankAccountNumberPost(BaseModel):
    bankAccountNumber: str = Field(alias="BankszamlaSzam", frozen=True)
    bankAccountOwnerName: str = Field(alias="BankszamlaTulajdonosNeve", frozen=True)
    bankAccountOwnerType: int = Field(alias="BankszamlaTulajdonosTipusId", frozen=True)
    bankName: str = Field(alias="SzamlavezetoBank", frozen=True)

class Guardian4TPost(BaseModel):
    dateOfBirth: datetime = Field(alias="SzuletesiDatum", frozen=True)
    firstname: str = Field(alias="Utonev", frozen=True)
    firstnameOfBirth: str = Field(alias="SzuletesiUtonev", frozen=True)
    isAszfAccepted: bool = Field(alias="IsElfogadottAszf", frozen=True)
    mothersFirstname: str = Field(alias="AnyjaUtonev", frozen=True)
    mothersSurname: str = Field(alias="AnyjaVezeteknev", frozen=True)
    namePrefix: str = Field(alias="Elotag", frozen=True)
    placeOfBirth: str = Field(alias="SzuletesiHely", frozen=True)
    surname: str = Field(alias="Vezeteknev", frozen=True)
    surnameOfBirth: str = Field(alias="SzuletesiVezeteknev", frozen=True)

class LepEventGuardianPermissionPost(BaseModel):
    eventId: int = Field(alias="EloadasId", frozen=True)
    isPermitted: bool = Field(alias="Dontes", frozen=True)

class SchoolClass(BaseModel):
    category: ValueDescriptor = Field(alias="OktatasNevelesiKategoria", frozen=True)
    name: str = Field(alias="Nev", frozen=True)
    uid: str = Field(alias="Uid", frozen=True)

class ConsultingHourTimeSlot(BaseModel):
    endTime: datetime = Field(alias="VegIdopont", frozen=True)
    isReservedByMe: bool = Field(alias="IsJelentkeztem", frozen=True)
    startTime: datetime = Field(alias="KezdoIdopont", frozen=True)
    uid: str = Field(alias="Uid", frozen=True)

class Guardian(BaseModel):
    email: str = Field(alias="EmailCim", frozen=True)
    isLegalRepresentative: bool = Field(alias="IsTorvenyesKepviselo", frozen=True)
    name: str = Field(alias="Nev", frozen=True)
    phoneNumber: str = Field(alias="Telefonszam", frozen=True)
    uid: str = Field(alias="Uid", frozen=True)

class Institution(BaseModel):
    customizationSettings: CustomizationSettings = Field(alias="TestreszabasBeallitasok", frozen=True)
    shortName: str = Field(alias="RovidNev", frozen=True)
    systemModuleList: list[SystemModule] = Field(alias="Rendszermodulok", frozen=True)
    uid: str = Field(alias="Uid", frozen=True)

class CustomizationSettings(BaseModel):
    delayOfNotifications: int = Field(alias="ErtekelesekMegjelenitesenekKesleltetesenekMerteke", frozen=True)
    isClassAverageVisible: bool = Field(alias="IsOsztalyAtlagMegjeleniteseEllenorzoben", frozen=True)
    isLessonsThemeVisible: bool = Field(alias="IsTanorakTemajaMegtekinthetoEllenorzoben", frozen=True)
    nextServerDeploy: datetime = Field(alias="KovetkezoTelepitesDatuma", frozen=True)

class SystemModule(BaseModel):
    isActive: bool = Field(alias="IsAktiv", frozen=True)
    type: str = Field(alias="Tipus", frozen=True)
    url: str = Field(alias="Url", frozen=True)
