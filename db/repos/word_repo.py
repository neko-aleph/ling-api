from db.models import Word
from db.repos.sqlalchemy_repo import SqlAlchemyRepository


class WordRepository(SqlAlchemyRepository):
    def __init__(self):
        super().__init__(Word)

    async def get_by_wordlist_id(self, wordlist_id: int):
        return await self.get_all(filters={"wordlist_id": wordlist_id})