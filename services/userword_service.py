from db.models import UserWord
from db.repos.userword_repo import UserWordRepository
from services.service import Service


class UserWordService(Service):
    def __init__(self, repo: UserWordRepository):
        super().__init__(repo)

    async def get_by_user_id(self, user_id: int, word_id: int) -> UserWord:
        return await self.repo.get_by_id(user_id, word_id)

    async def get_unlearned(self, user_id: int) -> list[UserWord]:
        return await self.repo.get_unlearned(user_id)

    async def increment_word_learnedness(self, user_id: int, word_id: int):
        return await self.repo.increment_word_learnedness(user_id, word_id)