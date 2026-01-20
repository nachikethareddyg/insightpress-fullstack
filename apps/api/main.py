from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="InsightPress API")

class Post(BaseModel):
    id: int
    title: str
    content: str
    status: str = "draft"

# in-memory demo data (good enough for proof)
POSTS: List[Post] = [
    Post(id=1, title="Welcome to InsightPress", content="First post!", status="published")
]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/posts")
def list_posts():
    return POSTS

@app.post("/posts")
def create_post(post: Post):
    POSTS.append(post)
    return post
