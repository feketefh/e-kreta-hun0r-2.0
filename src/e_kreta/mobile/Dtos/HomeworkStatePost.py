from typing import Optional
from pydantic import BaseModel, Field


class HomeworkStatePost(BaseModel):
    isDone: Optional[bool] = Field(alias="IsMegoldva", default=None, frozen=True)
    teacherHomeworkUid: Optional[str] = Field(alias="TanarHaziFeladatUid", default=None, frozen=True)
