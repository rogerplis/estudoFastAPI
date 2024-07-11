from sqlalchemy import URL


def get_database_connection():
    return URL.create(
        "postgresql+psycopg2",
        host="postgres",
        username="admin",
        password="admin",
        database="task"

    )
