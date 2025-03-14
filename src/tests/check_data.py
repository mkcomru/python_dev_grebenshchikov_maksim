from src.model.database import SessionLocal_authors, SessionLocal_tech_info
from src.model.models import User, Blog, Post, Log, SpaceType, EventType

def check_data():
    db_authors = SessionLocal_authors()
    try:
        print("\n=== Authors DB ===")
        users = db_authors.query(User).all()
        print("\nUsers:")
        for user in users:
            print(f"ID: {user.id}, Login: {user.login}, Email: {user.email}")

        posts = db_authors.query(Post).all()
        print("\nPosts:")
        for post in posts:
            print(f"ID: {post.id}, Header: {post.header}, Author ID: {post.author_id}")

    except Exception as e:
        print(f"Ошибка при проверке authors_db: {e}")
    finally:
        db_authors.close()

    db_tech = SessionLocal_tech_info()
    try:
        print("\n=== Tech Info DB ===")
        
        space_types = db_tech.query(SpaceType).all()
        print("\nSpace Types:")
        for st in space_types:
            print(f"ID: {st.id}, Name: {st.name}")

        event_types = db_tech.query(EventType).all()
        print("\nEvent Types:")
        for et in event_types:
            print(f"ID: {et.id}, Name: {et.name}")

        logs = db_tech.query(Log).all()
        print("\nLogs:")
        for log in logs:
            space = db_tech.query(SpaceType).filter(SpaceType.id == log.space_type_id).first()
            event = db_tech.query(EventType).filter(EventType.id == log.event_type_id).first()
            print(f"ID: {log.id}, User ID: {log.user_id}, Space: {space.name if space else 'None'}, Event: {event.name if event else 'None'}")

    except Exception as e:
        print(f"Ошибка при проверке tech_info_db: {e}")
    finally:
        db_tech.close()

if __name__ == "__main__":
    check_data() 