from pydantic import BaseModel, Field


class Cost(BaseModel):
    cash: int = Field(0, ge=0)
    geist: int = Field(0, ge=0)
