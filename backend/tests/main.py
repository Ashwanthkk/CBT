
from fastapi import FastAPI
from api.create_account_api import router

app = FastAPI()

app.include_router(router)