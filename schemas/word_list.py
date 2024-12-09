from pydantic import BaseModel

class WordList(BaseModel):
    id: int
    name: str

