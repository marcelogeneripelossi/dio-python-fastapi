from datetime import datetime, timezone
from typing import Annotated
from pydantic import BaseModel
from fastapi import Cookie, FastAPI, status, Response, Header

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


class Post(BaseModel):
    titulo: str
    data: datetime = datetime.now(timezone.utc)
    publicado: bool = False


@app.post("/posts/", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    fake_db.append(post.model_dump())
    return post


@app.get("/posts/")
def read_posts(
    response: Response,
    limit: int,
    skip: int = 0,
    publicado: bool = True,
    ads_id: Annotated[str | None, Cookie()] = None,
    user_agent: Annotated[str | None, Header()] = None,
):
    response.set_cookie(key="usuario", value="marcelo")
    print(f"Cookie: {ads_id}")
    print(f"User Agent: {user_agent}")
    return [
        post for post in fake_db[skip : skip + limit] if post["publicado"] is publicado
    ]


@app.get("/posts/{framework}")
def read_framework_posts(framework: str):
    return {
        "posts": [
            {
                "titulo": f"Criando uma aplicação com {framework}",
                "data": datetime.now(timezone.utc),
            },
            {
                "titulo": f"Usando uma aplicação com {framework}",
                "data": datetime.now(timezone.utc),
            },
        ]
    }
