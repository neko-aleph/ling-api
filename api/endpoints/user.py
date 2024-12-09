from gettext import translation

from fastapi import APIRouter
from fastapi.params import Depends

from db.models import UserWord as UW
from db.models import UserWordList
from dependencies.userword_service import userword_service
from dependencies.userwordlist_service import userwordlist_service
from dependencies.word_service import word_service
from dependencies.wordlist_service import wordlist_service
from schemas.results import Results
from schemas.user_word import UserWord
from schemas.word import Word
from schemas.word_list import WordList
from services.userword_service import UserWordService
from services.userwordlist_service import UserWordListService
from services.word_service import WordService
from services.wordlist_service import WordListService

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/{user_id}/wordlists")
async def get_user_lists(user_id: int, service: WordListService = Depends(wordlist_service), uwl_service: UserWordListService = Depends(userwordlist_service)) -> list[WordList]:
    data = await uwl_service.get_by_user_id(user_id)
    ids = [item.wordlist_id for item in data]
    result = []
    for id in ids:
        wordlist = await service.get_by_id(id)
        result.append(wordlist)
    return result

@router.get("/{user_id}/wordlists/{wordlist_id}")
async def get_list(user_id: int, wordlist_id: int, service: WordService = Depends(word_service), uw_service: UserWordService = Depends(userword_service)) -> list[UserWord]:
    words = []
    result = await service.get_by_wordlist_id(wordlist_id)
    for word in result:
        res = await uw_service.get_by_user_id(user_id, word.id)
        userword = UserWord(id=word.id, original=word.original, translation=word.translation, learned=res.learned)
        words.append(userword)
    return words

@router.get("/{user_id}/words/add/{wordlist_id}")
async def add_list(user_id: int, wordlist_id: int, uwl_service: UserWordListService = Depends(userwordlist_service), uw_service: UserWordService = Depends(userword_service), w_service: WordService = Depends(word_service)) -> bool:
    uwl = UserWordList(id=user_id+wordlist_id, user_id=user_id, wordlist_id=wordlist_id)
    await uwl_service.add(uwl)
    word_ids = [w.id for w in await w_service.get_by_wordlist_id(wordlist_id)]
    for word_id in word_ids:
        uw = UW(id=word_id+user_id, user_id=user_id, word_id=word_id, learned=0)
        await uw_service.add(uw)
    return True

@router.get("/{user_id}/words/remove/{wordlist_id}")
async def remove_list(user_id: int, wordlist_id: int, uwl_service: UserWordListService = Depends(userwordlist_service), uw_service: UserWordService = Depends(userword_service), w_service: WordService = Depends(word_service)) -> bool:
    await uwl_service.remove(user_id+wordlist_id)
    word_ids = [w.id for w in await w_service.get_by_wordlist_id(wordlist_id)]
    for word_id in word_ids:
        await uw_service.remove(word_id+user_id)
    return True

@router.get("/{user_id}/learn")
async def get_learn_list(user_id: int, uw_service: UserWordService = Depends(userword_service), w_service: WordService = Depends(word_service)) -> list[Word]:
    ids = [w.word_id for w in await uw_service.get_unlearned(user_id)]
    words = [await w_service.get_by_id(id) for id in ids]
    return words

@router.post("/{user_id}/upload_results")
async def upload_results(user_id: int, results: Results, uw_service: UserWordService = Depends(userword_service)) -> bool:
    for result in results.data:
        if result.correct:
            await uw_service.increment_word_learnedness(user_id, result.id)
    return True