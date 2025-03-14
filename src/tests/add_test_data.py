from src.model.database import SessionLocal_authors, SessionLocal_tech_info
from src.model.models import User, Blog, Post, Log, SpaceType, EventType
from datetime import datetime

def add_test_data():
    db_authors = SessionLocal_authors()
    try:
        users = [
            User(email='user1@example.com', login='user1'),
            User(email='user2@example.com', login='user2'),
            User(email='test@test.com', login='test_user')
        ]
        db_authors.add_all(users)
        db_authors.commit()

        user1 = db_authors.query(User).filter(User.login == 'user1').first()
        user2 = db_authors.query(User).filter(User.login == 'user2').first()

        blogs = [
            Blog(owner_id=user1.id, name='First Blog', description='Blog for user1'),
            Blog(owner_id=user2.id, name='Second Blog', description='Blog for user2')
        ]
        db_authors.add_all(blogs)
        db_authors.commit()

        blog1 = db_authors.query(Blog).filter(Blog.owner_id == user1.id).first()
        blog2 = db_authors.query(Blog).filter(Blog.owner_id == user2.id).first()

        posts = [
            Post(header='Hello World', text='First post content', author_id=user1.id, blog_id=blog1.id),
            Post(header='Second Post', text='Another post', author_id=user2.id, blog_id=blog2.id)
        ]
        db_authors.add_all(posts)
        db_authors.commit()

        print("Данные добавлены в authors_db!")

        post1 = db_authors.query(Post).filter(Post.author_id == user1.id).first()
        post2 = db_authors.query(Post).filter(Post.author_id == user2.id).first()

    except Exception as e:
        print(f"Ошибка при добавлении данных в authors_db: {e}")
        db_authors.rollback()
        return
    finally:
        db_authors.close()

    db_tech = SessionLocal_tech_info()
    try:
        space_types = [
            SpaceType(name='global'),
            SpaceType(name='blog'),
            SpaceType(name='post')
        ]
        db_tech.add_all(space_types)
        db_tech.commit()

        event_types = [
            EventType(name='login'),
            EventType(name='comment'),
            EventType(name='create_post'),
            EventType(name='delete_post'),
            EventType(name='logout')
        ]
        db_tech.add_all(event_types)
        db_tech.commit()

        post_space = db_tech.query(SpaceType).filter(SpaceType.name == 'post').first()
        global_space = db_tech.query(SpaceType).filter(SpaceType.name == 'global').first()
        comment_event = db_tech.query(EventType).filter(EventType.name == 'comment').first()
        login_event = db_tech.query(EventType).filter(EventType.name == 'login').first()

        logs = [
            Log(datetime=datetime.now(), user_id=user1.id, space_type_id=post1.id, event_type_id=comment_event.id),
            Log(datetime=datetime.now(), user_id=user2.id, space_type_id=post2.id, event_type_id=comment_event.id),
            Log(datetime=datetime.now(), user_id=user1.id, space_type_id=global_space.id, event_type_id=login_event.id),
            Log(datetime=datetime.now(), user_id=user2.id, space_type_id=global_space.id, event_type_id=login_event.id)
        ]
        db_tech.add_all(logs)
        db_tech.commit()

        print("Данные добавлены в tech_info_db!")

    except Exception as e:
        print(f"Ошибка при добавлении данных в tech_info_db: {e}")
        db_tech.rollback()
    finally:
        db_tech.close()

if __name__ == "__main__":
    add_test_data() 