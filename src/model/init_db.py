from .database import engine_authors, engine_tech_info, Base
from .models import User, Blog, Post, Log, SpaceType, EventType

def init_databases():
    # Создаем таблицы в первой БД (authors)
    Base.metadata.create_all(bind=engine_authors)
    
    # Создаем таблицы во второй БД (tech_info)
    Base.metadata.create_all(bind=engine_tech_info)

if __name__ == "__main__":
    init_databases()
    print("Базы данных успешно инициализированы!")