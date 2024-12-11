from db.repos.user_repo import UserRepository
from services.user_service import UserService


async def user_service():
	return UserService(UserRepository())