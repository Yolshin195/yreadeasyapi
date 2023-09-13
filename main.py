from fastapi import FastAPI, Depends

from router import language_reference_router
from router import part_of_speech_reference_router
from router import word_router

app = FastAPI()

app.include_router(word_router)
app.include_router(language_reference_router)
app.include_router(part_of_speech_reference_router)
