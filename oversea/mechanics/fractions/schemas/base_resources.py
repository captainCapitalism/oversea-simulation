from pydantic import BaseModel, Field


class BaseResources(BaseModel):
    cash: int
    geist: int
    intrigue_cards: int
    magic_cards: int = Field(0)
    goal_cards: int = Field(0)
