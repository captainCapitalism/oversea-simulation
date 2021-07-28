from pydantic import BaseModel


class BaseResources(BaseModel):
    cash: int = 0
    geist: int = 0
    intrigue_cards: int = 0
    magic_cards: int = 0
    goal_cards: int = 0
