"""Module docstring"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    """function docstring"""
    return {"message": "Hell on World"}


@app.get("/data/{name}")
async def read_data(name: str):
    """function docstring"""
    return {"message": f"Hell on World {name}"}
