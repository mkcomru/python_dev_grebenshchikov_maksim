from src.model.database import SessionLocal_tech_info
from src.model.models import SpaceType, EventType

def init_types():
    db = SessionLocal_tech_info()
    try:
        space_types = [
            SpaceType(name="global"),
            SpaceType(name="blog"),
            SpaceType(name="post")
        ]
        
        event_types = [
            EventType(name="login"),
            EventType(name="comment"),
            EventType(name="create_post"),
            EventType(name="delete_post"),
            EventType(name="logout")
        ]
        
        db.add_all(space_types)
        db.add_all(event_types)
        db.commit()
        print("Начальные данные добавлены")
    except Exception as e:
        print(f"Ошибка при добавлении данных: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_types() 