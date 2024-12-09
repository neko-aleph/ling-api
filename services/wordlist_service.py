from db.repos.wordlist_repo import WordListRepository
from services.service import Service


class WordListService(Service):
    def __init__(self, repo: WordListRepository):
        super().__init__(repo)
