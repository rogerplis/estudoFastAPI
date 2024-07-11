from app.conn import session
from app.tasks.models.user_models import User, Pessoa
from sqlalchemy.future import select
from sqlalchemy import delete

from app.tasks.schemas.schema import UserUpdate
from app.tasks.security.security import get_password_hash, verify_password
from app.tasks.services.pessoa_service import select_person_email


def criar_user(status, email, password, verify_pwd):
    pessoa_id = select_person_email(email)
    pwd_encoded = get_password_hash(password)
    pwd_verify = verify_password(verify_pwd, pwd_encoded)
    if pwd_verify:
        user = User(pessoa_id, status, email=email, password=pwd_encoded)
        session.add(user)
        session.commit()
        return {"Message" : f'Usuario {email} criado com sucesso'}
    else:
        return {"Message": "Password diferente ㊇"}


def select_all():
    result = session.execute(select(User).join(Pessoa))
    return result.scalars().all()


def select_one(user_id: int):
    result = session.execute(select(User).where(User.id == user_id))
    return result.scalars().one()


def delete_user(user_id: int):
    session.execute(delete(User).where(User.id == user_id))
    session.commit()


def update_user(user_id: int, user_update: UserUpdate):
    db_user = select_one(user_id)
    user_data = user_update.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(db_user, key, value)

    session.commit()
    session.refresh(db_user)
    return db_user

