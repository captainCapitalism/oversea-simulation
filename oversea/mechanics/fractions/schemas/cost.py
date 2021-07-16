from pydantic import BaseModel


class Cost(BaseModel):
    cash: int
    geist: int
