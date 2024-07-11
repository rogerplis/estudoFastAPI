from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select

from app.conn import session
from app.tasks.models.user_models import User, Pessoa
from app.tasks.schemas.schema import Token, LoginUser
from app.tasks.security.security import verify_password, create_access_token, get_current_user

router = APIRouter(prefix='/auth', tags=['auth'])

OAuth2Form = Annotated[OAuth2PasswordRequestForm, Depends()]


@router.post('/login')
async def login_for_access_token(payload: LoginUser):
    global pessoa
    user = session.scalar(select(User).where(User.email == payload.email))
    if user:
        pessoa = session.scalar(select(Pessoa).where(Pessoa.id == user.pessoa_id))
    if not user:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Incorrect email or password',

        )
    if not verify_password(payload.password, user.password):
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Incorrect email or password',

        )
    access_token = create_access_token(data={'sub': user.email})

    return {'access_token': access_token, 'token_type': 'bearer', 'user':
        {"id": user.id,
         'email': user.email,
         'nome': pessoa.nome}}


@router.post('/refresh_token', response_model=Token)
def refresh_access_token(
        user: User = Depends(get_current_user), ):
    new_access_token = create_access_token(data={'sub': user.email})

    return {'access_token': new_access_token, 'token_type': 'bearer'}
