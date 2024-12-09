from pydantic import BaseModel


class Word(BaseModel):
    id: int
    original: str
    translation: str
    