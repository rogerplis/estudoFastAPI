from datetime import date, timedelta

from sqlalchemy import delete

from app.conn import session
from app.tasks.models.user_models import Sub_task
from app.tasks.schemas.schema import SubtaskUpdate


def criar_sub_task(name, description, task__id, prevision):
    init_at = date.today() + timedelta(prevision)
    end_at = date.today() + timedelta(prevision)
    subtask = Sub_task(description=description,
                       task_id=task__id,
                       name=name,
                       init_at=init_at,
                       end_at=end_at,
                       prevision=prevision)
    session.add(subtask)
    session.commit()


def update_subtask(subtask_id: int, subtask_update: SubtaskUpdate):
    db_subtask = select_one_subtask(subtask_id)
    if db_subtask is None:
        return None

    substak_data = subtask_update.dict(exclude_unset=True)
    for key, value in substak_data.items():
        setattr(db_subtask, key, value)

    session.commit()
    session.refresh(db_subtask)
    return db_subtask


def select_one_subtask(subtask_id: int):
    result = session.query(Sub_task).filter(
        Sub_task.id == subtask_id).first()  # execute(select(Sub_task).where(Sub_task.id == subtask_id))
    if result is None:
        return {'Message':  'Not found'}
    return result


def delete_subtask(subtask_id: int):
    subtask_db = select_one_subtask(subtask_id)
    if subtask_db['Message']:
        return {'Message':  'Not found'}
    else:
        status = subtask_db.status

    if status.__eq__('started'):
        return {'message': 'the task already gone started, use update then signalize with suspended.'}
    else:
        session.execute(delete(Sub_task).where(Sub_task.id == subtask_id))
        session.commit()
        return {'message': 'the task gone excluded with success.'}




