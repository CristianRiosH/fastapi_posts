from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Text, List
from datetime import datetime
from uuid import uuid4




app = FastAPI()

posts = []

# post Model
class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False



@app.get("/")
def read_root():
    return {"welcome":"Welcome to my API"}

@app.get("/posts")
def get_posts():
    return posts

@app.post("/posts")
def save_post(post: Post):
    post.id = uuid4().hex
    posts.append(post.dict())
    return posts[-1]


@app.get("/posts/{post_id}")
def get_post(post_id: str):
    for post in posts:
        if post['id'] == post_id:
            return post
    return HTTPException(status_code=404, detail="Post not found")


@app.delete(path="/posts/{post_id}")
def delete_post(post_id: str):
    for index, post in enumerate(posts):
        if post['id'] == post_id:
            posts.pop(index)
            return {"message": "Post deleted"}
    return HTTPException(status_code=404, detail="Post not found")

@app.put(path="/posts/{post_id}")
def update_post(post_id: str, updated_post: Post):
    updated_post = updated_post.dict()
    for index, post in enumerate(posts):
        if post['id'] == post_id:
            posts[index]["title"] = updated_post["title"]
            posts[index]["author"] = updated_post["author"]
            posts[index]["content"] = updated_post["content"]
            return {"message": "Post updated"}
    return HTTPException(status_code=404, detail="Post not found")