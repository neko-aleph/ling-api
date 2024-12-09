from db.models import UserWordList
from db.repos.sqlalchemy_repo import SqlAlchemyRepository


class UserWordListRepository(SqlAlchemyRepository):
    def __init__(self):
        super().__init__(UserWordList)

    async def get_by_user_id(self, user_id: int):
        return await self.get_all(filters={"user_id": user_id})