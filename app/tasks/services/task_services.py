from sqlalchemy import delete
from sqlalchemy.future import select

from app.conn import session
from app.tasks.models.user_models import Task


def criar_task(name, description, user_id):
    task = Task(name=name, description=description, user_id=user_id)
    session.add(task)
    session.commit()


def select_all_tasks():
    result = session.execute(select(Task))
    return result.scalars().all()


def select_one_task(task_id: int):
    result = session.execute(select(Task).where(Task.id == task_id))
    return result.scalars().one()


def delete_task(task_id: int):
    session.execute(delete(Task).where(Task.id == task_id))
    session.commit()
