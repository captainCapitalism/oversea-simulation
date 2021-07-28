from pydantic import BaseModel, Field


class BaseResources(BaseModel):
    cash: int = Field(0)
    geist: int = Field(0)
    intrigue_cards: int = Field(0)
    magic_cards: int = Field(0)
    goal_cards: int = Field(0)
