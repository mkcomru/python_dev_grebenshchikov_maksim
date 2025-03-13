from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from src.model.database import SessionLocal_authors, SessionLocal_tech_info
from src.model.models import User, Post, Blog, Log, SpaceType, EventType


app = FastAPI()

def get_db1():
    db = SessionLocal_authors()
    try:
        yield db
    finally:
        db.close()

def get_db2():
    db = SessionLocal_tech_info()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/comments")
def get_comments(login: str, db1: Session = Depends(get_db1), db2: Session = Depends(get_db2)):
    user = db1.query(User).filter(User.login == login).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    comments = db2.query(Log).filter(Log.user_id == user.id, Log.event_type_id == db2.query(EventType).filter(EventType.name == 'comment').first().id).all()
    result = []
    for comment in comments:
        post = db1.query(Post).filter(Post.id == comment.space_type_id).first()
        result.append({
            "login": user.login,
            "header": post.header,
            "author_login": post.author.login,
            "comment_count": len(comments)
        })
    return result