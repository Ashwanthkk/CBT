from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.create_account_api import router as create_api
from api.otp_authenticate_api import router as otp_api


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(create_api)
app.include_router(otp_api)