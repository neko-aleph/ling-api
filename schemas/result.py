from pydantic import BaseModel


class Result(BaseModel):
    id: int
    correct: bool
