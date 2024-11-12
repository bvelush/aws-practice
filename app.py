# https://medium.com/@vanyamyshkin/deploy-python-fastapi-for-free-on-aws-ec2-050b46744366


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from random import randint
from math import log10

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the API!"}


@app.get("/api/test")
async def test():
    return "=== HI ==="


@app.get("/api/load")
async def load():
    i = 0
    arr = []
    while i < 1000000:
        i += 1
        arr.append(log10(randint(2, i+3)))
    return f"=== {i} ===, {arr}"
