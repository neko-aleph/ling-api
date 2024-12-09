from db.repos.userword_repo import UserWordRepository
from services.userword_service import UserWordService


async def userword_service():
	return UserWordService(UserWordRepository())