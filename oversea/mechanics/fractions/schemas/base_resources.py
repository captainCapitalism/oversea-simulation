from pydantic import BaseModel, Field


class BaseResources(BaseModel):
    cash: int
    geist: int
    intrigue_cards: int
    magic_cards: int
    goal_cards: int
