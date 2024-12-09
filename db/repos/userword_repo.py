from sqlalchemy import select, update
from sqlalchemy.exc import NoResultFound

from db.db import session_maker
from db.models import UserWord
from db.repos.sqlalchemy_repo import SqlAlchemyRepository


class UserWordRepository(SqlAlchemyRepository):
    def __init__(self):
        super().__init__(UserWord)

    async def get_by_id(self, user_id: int, word_id: int):
        return await self.get(user_id+word_id)

    async def get_unlearned(self, user_id: int):
        async with session_maker() as session:
            query = select(self.model).where(getattr(self.model, "user_id") == user_id).where(getattr(self.model, "learned") < 3).fetch(10)
            try:
                result = await session.execute(query)
                return result.scalars().all()
            except NoResultFound:
                return None

    async def increment_word_learnedness(self, user_id: int, word_id: int):
        learned = (await self.get_by_id(user_id, word_id)).learned
        await self.update(user_id, {"learned": learned+1})
        async with session_maker() as session:
            query = update(self.model).where(UserWord.id == user_id+word_id).values(learned=learned+1)
            await session.execute(query)
            await session.commit()