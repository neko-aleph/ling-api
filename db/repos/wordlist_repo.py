from db.models import WordList
from db.repos.sqlalchemy_repo import SqlAlchemyRepository


class WordListRepository(SqlAlchemyRepository):
    def __init__(self):
        super().__init__(WordList)
