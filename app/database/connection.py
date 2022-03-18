import sqlalchemy as sa
from app.config.settings import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool

engine = create_engine(
    url=settings.SQLALCHEMY_URL,
    echo=settings.DB_ECHO,
    poolclass=QueuePool,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

metadata = sa.MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)

Base = declarative_base(metadata=metadata)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
