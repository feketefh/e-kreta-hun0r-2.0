from typing import Optional
from pydantic import BaseModel, Field


class LanguageSubTaskSubmission(BaseModel):
    evaluationMarkId: Optional[int] = Field(alias="ertekelesOsztalyzatId", default=None, frozen=True)
    evaluationPercent: Optional[int] = Field(alias="ertekelesSzazalek", default=None, frozen=True)
    evaluationText: Optional[str] = Field(alias="ertekelesSzoveg", default=None, frozen=True)
    id: Optional[int] = Field(alias="id", default=None, frozen=True)
    isAccepted: Optional[bool] = Field(alias="ertekelveVagyElfogadva", default=None, frozen=True)
    isEvaluationByMark: Optional[bool] = Field(alias="osztalyzattalErtekelt", default=None, frozen=True)
    isEvaluationByPercentage: Optional[bool] = Field(alias="szazalekkalErtekelt", default=None, frozen=True)
    isEvaluationByText: Optional[bool] = Field(alias="szoveggelErtekelt", default=None, frozen=True)
    percent: Optional[int] = Field(alias="xeropanSzazalek", default=None, frozen=True)
    state: Optional[State] = Field(alias="statusz", default=None, frozen=True)
    submissionDateAsString: Optional[str] = Field(alias="xeropanMegoldasBekuldesiIdeje", default=None, frozen=True)
    taskId: Optional[int] = Field(alias="feladatId", default=None, frozen=True)
    timeSpent: Optional[int] = Field(alias="xeropanMegoldassalToltottIdoPerc", default=None, frozen=True)

class State(BaseModel):
    stateName: Optional[str] = Field(alias="nev", default=None, frozen=True)
    uid: Optional[int] = Field(alias="id", default=None, frozen=True)
