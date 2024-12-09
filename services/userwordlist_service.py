from db.models import UserWordList
from db.repos.userwordlist_repo import UserWordListRepository
from services.service import Service


class UserWordListService(Service):
    def __init__(self, repo: UserWordListRepository):
        super().__init__(repo)

    async def get_by_user_id(self, user_id: int) -> list[UserWordList]:
        return await self.repo.get_by_user_id(user_id)