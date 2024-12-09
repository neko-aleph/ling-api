from fastapi import FastAPI
from api.endpoints.wordlists import router as wordlists_router
from api.endpoints.user import router as user_router

app = FastAPI()
app.include_router(wordlists_router)
app.include_router(user_router)
