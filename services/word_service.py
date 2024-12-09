from db.models import Word
from db.repos.word_repo import WordRepository
from services.service import Service


class WordService(Service):
    def __init__(self, repo: WordRepository):
        super().__init__(repo)

    async def get_by_wordlist_id(self, wordlist_id: int) -> list[Word]:
        return await self.repo.get_by_wordlist_id(wordlist_id)