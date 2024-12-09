from db.repos.wordlist_repo import WordListRepository
from services.wordlist_service import WordListService


async def wordlist_service():
	return WordListService(WordListRepository())