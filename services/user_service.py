from db.models import UserWord, User
from db.repos.user_repo import UserRepository
from db.repos.userword_repo import UserWordRepository
from services.service import Service


class UserService(Service):
    def __init__(self, repo: UserRepository):
        super().__init__(repo)

    async def create_user(self):
        return await self.repo.create()