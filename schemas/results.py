from pydantic import BaseModel

from schemas.result import Result


class Results(BaseModel):
    data: list[Result]
