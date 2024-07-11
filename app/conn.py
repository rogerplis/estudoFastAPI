import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker

from app.databases.db_connect import get_database_connection

engine = sqlalchemy.create_engine(get_database_connection(), echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()
session = Session()


