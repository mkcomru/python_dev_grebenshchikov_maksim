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

        blogs = [
            Blog(owner_id=1, name='First Blog', description='Blog for user1'),
            Blog(owner_id=2, name='Second Blog', description='Blog for user2')
        ]
        db_authors.add_all(blogs)
        db_authors.commit()

        posts = [
            Post(header='Hello World', text='First post content', author_id=1, blog_id=1),
            Post(header='Second Post', text='Another post', author_id=2, blog_id=2)
        ]
        db_authors.add_all(posts)
        db_authors.commit()

        print("Данные добавлены в authors_db!")

    except Exception as e:
        print(f"Ошибка при добавлении данных в authors_db: {e}")
        db_authors.rollback()
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
            Log(datetime=datetime.now(), user_id=1, space_type_id=post_space.id, event_type_id=comment_event.id),
            Log(datetime=datetime.now(), user_id=2, space_type_id=post_space.id, event_type_id=comment_event.id),
            Log(datetime=datetime.now(), user_id=1, space_type_id=global_space.id, event_type_id=login_event.id)
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