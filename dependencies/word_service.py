from db.repos.word_repo import WordRepository
from services.word_service import WordService


async def word_service():
	return WordService(WordRepository())