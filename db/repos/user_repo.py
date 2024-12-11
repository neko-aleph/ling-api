from sqlalchemy import select, update
from sqlalchemy.exc import NoResultFound

from db.db import session_maker
from db.models import UserWord, User
from db.repos.sqlalchemy_repo import SqlAlchemyRepository


class UserRepository(SqlAlchemyRepository):
    def __init__(self):
        super().__init__(User)

    async def create(self):
        user = User()
        await self.add(user)
        return user.id