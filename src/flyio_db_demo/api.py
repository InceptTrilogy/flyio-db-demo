from fastapi import FastAPI
from typing import Literal

app = FastAPI(title="Fly.io DB Demo")

@app.get("/")
def read_root() -> dict[Literal["message"], str]:
    return {"message": "Hello World"}
