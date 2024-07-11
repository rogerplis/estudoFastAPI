from typing import List

from fastapi import APIRouter, Depends

from app.tasks.schemas.schema import UserPwd, PessoaSchema, Pessoa
from app.tasks.security.security import get_current_user
from app.tasks.services.pessoa_service import criar_pessoas, select_one_person, select_all_person, select_person_email, \
    select_person_id
from app.tasks.services.user_services import criar_user

router = APIRouter(prefix='/api/v1')  #


# Rota Pessoa


@router.post('/pessoas')
async def criar_pessoa(pessoas: List[Pessoa]):
    userpwd = '1234'
    verifypwd = '1234'
    for pessoa in pessoas:
        new_person = criar_pessoas(**pessoa.dict())
        criar_user('liberado', pessoa.email, userpwd, verifypwd)

    return {"Pessoas cadastradas com sucesso!"}


@router.get('/pessoa/{cpf}', dependencies=[Depends(get_current_user)])
def listar_pessoa(cpf: str):
    return select_one_person(cpf)


@router.get('/pessoaemail/{email}', dependencies=[Depends(get_current_user)])
def listar_pessoa_email(email: str):
    return select_person_email(email)


@router.get('/pessoaid/{id}', response_model=PessoaSchema, dependencies=[Depends(get_current_user)])
def listar_pessoa_id(id: int):
    return select_person_id(id)


@router.get('/pessoas', response_model=list[PessoaSchema], dependencies=[Depends(get_current_user)])
def listar_pessoa():
    pessoa = select_all_person()
    return pessoa
