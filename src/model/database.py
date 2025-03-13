from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.config import settings


engine_authors = create_engine(settings.AUTHORS_DB_URL)
engine_tech_info = create_engine(settings.TECH_INFO_DB_URL)

SessionLocal_authors = sessionmaker(autocommit=False, autoflush=False, bind=engine_authors)
SessionLocal_tech_info = sessionmaker(autocommit=False, autoflush=False, bind=engine_tech_info)

Base = declarative_base()

