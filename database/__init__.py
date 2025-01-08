from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# подключение к файлу базы данных
SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'


# создание дважка для базы данных
engine = create_engine(SQLALCHEMY_DATABASE_URI)


# создание функции для создания сессий
SessionLocal = sessionmaker(bind=engine)


# создание суперкласса для моделей
Base = declarative_base()


# создание функции-генератора сессий
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()