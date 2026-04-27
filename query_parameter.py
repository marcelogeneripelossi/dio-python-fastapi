from datetime import datetime, timezone
from fastapi import FastAPI

app = FastAPI()

fake_db = [
    {
        "titulo": "Criando uma aplicação com FastAPI",
        "data": datetime.now(timezone.utc),
        "publicado": True,
    },
    {
        "titulo": "Criando uma aplicação com Python",
        "data": datetime.now(timezone.utc),
        "publicado": True,
    },
    {
        "titulo": "Criando uma aplicação com Flask",
        "data": datetime.now(timezone.utc),
        "publicado": False,
    },
    {
        "titulo": "Criando uma aplicação com Starlett",
        "data": datetime.now(timezone.utc),
        "publicado": True,
    },
]


@app.get("/posts/")
def read_posts(skip: int = 0, limit: int = len(fake_db), publicado: bool = True):
    return [
        post for post in fake_db[skip : skip + limit] if post["publicado"] is publicado
    ]
