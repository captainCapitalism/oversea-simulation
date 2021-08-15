from typing import Annotated

from pydantic import BaseModel, Field


class BaseResources(BaseModel):
    cash: Annotated[int, Field(ge=0)] = 0
    geist: Annotated[int, Field(ge=0)] = 0
    intrigue_cards: Annotated[int, Field(ge=0)] = 0
    magic_cards: Annotated[int, Field(ge=0)] = 0
    goal_cards: Annotated[int, Field(ge=0)] = 0

    class Config:
        frozen = True
