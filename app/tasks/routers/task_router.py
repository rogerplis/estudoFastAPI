from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends

from app.tasks.models.user_models import User
from app.tasks.schemas.schema import SubTask, SubtaskUpdate, SubtaskInDB
from app.tasks.security.security import get_current_user
from app.tasks.services.sub_task_services import criar_sub_task, update_subtask, select_one_subtask, delete_subtask
from app.tasks.services.task_services import select_all_tasks, select_one_task, delete_task

router = APIRouter(prefix='/api/v1',dependencies=[Depends(get_current_user)])

CurrentUser = Annotated[User, Depends(get_current_user)]


# rotas de Task
@router.get('/task')
def listar_tasks(user: CurrentUser):
    if user:
        return select_all_tasks()


@router.get('/task/{task_id}')
def listar_tsak(task_id: int):
    return select_one_task(task_id)


@router.delete('/task/{task_id}')
def deletar_task(task_id: int):
    return delete_task(task_id)


@router.post('/subtask')
def criar_subtask(subtask: SubTask):
    task = select_one_task(subtask.task_id)
    name = subtask.name
    description = subtask.description
    prevision = subtask.prevision
    task_id = subtask.task_id
    criar_sub_task(name, description, task_id, prevision)
    return {'message': f" Sub Task criado para a Task:  {task.name} com sucesso"}


@router.put("/subtask/{subtask_id}", response_model=SubtaskInDB)
def update_subtasks(subtask_id: int, subtask: SubtaskUpdate):
    updated_subtask = update_subtask(subtask_id, subtask)
    if updated_subtask is None:
        raise HTTPException(status_code=404, detail="sub task nao encontrada")
    return updated_subtask


@router.get('/subtask/{subtask_id}')
def listar_subtask(subtask_id: int):
    return select_one_subtask(subtask_id)


# Rota para deletar um item de uma Tarefa, Caso o item tem sido iniciado nao pdera ser deletado.
@router.delete('/subtask/{subtask_id}')
def deletar_subtask(subtask_id: int):
    return delete_subtask(subtask_id)
