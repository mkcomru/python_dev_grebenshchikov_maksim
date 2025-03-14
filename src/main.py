from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from src.model.database import SessionLocal_authors, SessionLocal_tech_info
from src.model.models import User, Post, Blog, Log, SpaceType, EventType
from typing import List, Dict, Any
from datetime import datetime

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

@app.get("/api/comments", response_model=List[Dict[str, Any]])
def get_comments(login: str, db1: Session = Depends(get_db1), db2: Session = Depends(get_db2)):
    try:
        user = db1.query(User).filter(User.login == login).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        comment_event = db2.query(EventType).filter(EventType.name == 'comment').first()
        post_space = db2.query(SpaceType).filter(SpaceType.name == 'post').first()
        
        if not comment_event or not post_space:
            raise HTTPException(status_code=404, detail="Required event or space types not found")

        comments = db2.query(Log).filter(
            Log.user_id == user.id,
            Log.event_type_id == comment_event.id,
            Log.space_type_id == post_space.id
        ).all()

        post_comments = {}
        for comment in comments:
            if comment.space_type_id not in post_comments:
                post_comments[comment.space_type_id] = 0
            post_comments[comment.space_type_id] += 1

        result = []
        for post_id, comment_count in post_comments.items():
            post = db1.query(Post).filter(Post.id == post_id).first()
            if post and post.author:
                result.append({
                    "login": user.login,
                    "header": post.header,
                    "author_login": post.author.login,
                    "comment_count": comment_count
                })

        if not result:
            return [{
                "login": user.login,
                "header": None,
                "author_login": None,
                "comment_count": 0
            }]

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/general", response_model=Dict[str, Any])
def get_general(login: str, db1: Session = Depends(get_db1), db2: Session = Depends(get_db2)):
    try:
        user = db1.query(User).filter(User.login == login).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        logs = db2.query(Log).filter(Log.user_id == user.id).all()

        login_event = db2.query(EventType).filter(EventType.name == 'login').first()
        logout_event = db2.query(EventType).filter(EventType.name == 'logout').first()
        blog_space = db2.query(SpaceType).filter(SpaceType.name == 'blog').first()

        if not logs:
            return {
                "date": datetime.now().date(),
                "login_count": 0,
                "logout_count": 0,
                "blog_actions_count": 0
            }

        return {
            "date": logs[0].datetime.date(),
            "login_count": sum(1 for log in logs if log.event_type_id == login_event.id),
            "logout_count": sum(1 for log in logs if log.event_type_id == logout_event.id),
            "blog_actions_count": sum(1 for log in logs if log.space_type_id == blog_space.id)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))