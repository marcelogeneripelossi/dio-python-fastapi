from datetime import datetime, timezone
from fastapi import FastAPI

app = FastAPI()


@app.get("/post/{framework}")
def read_posts(framework: str):
    return {"posts":[{"titulo":f"Criando uma aplicação com {framework}", "data":datetime.now(timezone.utc)},
                     {"titulo":f"Usando uma aplicação com {framework}", "data":datetime.now(timezone.utc)}]}

