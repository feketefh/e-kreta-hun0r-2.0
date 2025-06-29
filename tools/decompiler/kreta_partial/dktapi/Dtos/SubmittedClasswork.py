from typing import Optional
from pydantic import BaseModel, Field


class SubmittedClasswork(BaseModel):
    comment: Optional[str] = Field(alias="megjegyzes", default=None, frozen=True)
    evaluatedByAccepting: Optional[bool] = Field(alias="elfogadottNemElfogadott", default=None, frozen=True)
    evaluatedByMark: Optional[bool] = Field(alias="osztalyzattalErtekelt", default=None, frozen=True)
    evaluatedByPercent: Optional[bool] = Field(alias="szazalekkalErtekelt", default=None, frozen=True)
    evaluatedByScore: Optional[bool] = Field(alias="pontszammalErtekelt", default=None, frozen=True)
    evaluatedByText: Optional[bool] = Field(alias="szoveggelErtekelt", default=None, frozen=True)
    evaluationMark: Optional[str] = Field(alias="ertekelesOsztalyzatNev", default=None, frozen=True)
    evaluationPercent: Optional[str] = Field(alias="ertekelesSzazalek", default=None, frozen=True)
    evaluationScore: Optional[float] = Field(alias="pontszam", default=None, frozen=True)
    evaluationText: Optional[str] = Field(alias="ertekelesSzoveg", default=None, frozen=True)
    id: Optional[int] = Field(alias="id", default=None, frozen=True)
    isEvaluatedOrAccepted: Optional[bool] = Field(alias="ertekelveVagyElfogadva", default=None, frozen=True)
    solutionText: Optional[str] = Field(alias="szoveg", default=None, frozen=True)
    statusId: Optional[int] = Field(alias="statuszId", default=None, frozen=True)
    uniqueId: Optional[str] = Field(alias="egyediId", default=None, frozen=True)
