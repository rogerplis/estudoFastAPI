from fastapi import APIRouter, HTTPException, Depends

from fastapi import APIRouter, HTTPException, Depends

from app.tasks.schemas.schema import User, UserInDB, UserUpdate
from app.tasks.security.security import get_current_user
from app.tasks.services.user_services import select_all, select_one, criar_user, delete_user, update_user

router = APIRouter(prefix='/api/v1', dependencies=[Depends(get_current_user)])


# Rotas Usuario
@router.get('/users')
def listar_users():
    return select_all()


@router.get('/user/{user_id}')
def listar_user(user_id: int):
    return select_one(user_id)


@router.post('/users')
def criar_users(user: User):
    return criar_user(**user.dict())


@router.put("/user/{user_id}", response_model=UserInDB)
def update_users(user_id: int, status: UserUpdate):
    updated_user = update_user(user_id, status)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User nao encontrada")
    return updated_user


@router.delete('/user/{user_id}')
def deletar_user(user_id: int):
    delete_user(user_id)
    return {'message': "Usuario excluido com sucesso"}
