from sqlalchemy import select, update, delete
from sqlalchemy.exc import NoResultFound

from db.db import session_maker
from db.models import Base
from db.repos.repo import Repository


class SqlAlchemyRepository(Repository):
    def __init__(self, model: Base):
        self.model = model

    async def get(self, id: int):
        async with session_maker() as session:
            try:
                result = await session.execute(select(self.model).where(self.model.id == id))
                return result.scalar_one()
            except NoResultFound:
                return None

    async def get_all(self, filters: dict = None):
        async with session_maker() as session:
            query = select(self.model)
            if filters:
                for field, value in filters.items():
                    query = query.where(getattr(self.model, field) == value)

            try:
                result = await session.execute(query)
                return result.scalars().all()
            except NoResultFound:
                return None

    async def add(self, instance):
        async with session_maker() as session:
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return instance

    async def update(self, id: int, data: dict):
        async with session_maker() as session:
            query = (
                update(self.model)
                .where(self.model.id == id)
                .values(**data)
            )
            await session.execute(query)
            await session.commit()

    async def delete(self, id: int):
        async with session_maker() as session:
            query = delete(self.model).where(self.model.id == id)
            await session.execute(query)
            await session.commit()
