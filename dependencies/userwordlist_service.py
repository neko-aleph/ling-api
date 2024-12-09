from db.repos.userwordlist_repo import UserWordListRepository
from services.userwordlist_service import UserWordListService


async def userwordlist_service():
	return UserWordListService(UserWordListRepository())