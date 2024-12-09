from fastapi import APIRouter
from fastapi.params import Depends

from dependencies.word_service import word_service
from dependencies.wordlist_service import wordlist_service
from schemas.word import Word
from schemas.word_list import WordList
from services.word_service import WordService
from services.wordlist_service import WordListService

router = APIRouter(prefix="/wordlists", tags=["wordlists"])

@router.get("/")
async def get_lists(service: WordListService = Depends(wordlist_service)) -> list[WordList]:
    result = await service.get_all()
    return result

@router.get("/{wordlist_id}")
async def get_list(wordlist_id: int, service: WordService = Depends(word_service)) -> list[Word]:
    result = await service.get_by_wordlist_id(wordlist_id)
    return result

