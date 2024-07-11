from sqlalchemy import delete
from sqlalchemy.future import select

from app.conn import session
from app.tasks.models.user_models import Pessoa
from app.util.cpf_validator import validate

"""
Funçao para criar novas pessoas, com tratamento de exceção para caso ja exista a pessoa.
E validação de CPF
"""


def criar_pessoas(nome, celular, cpf, endereco, rg, cep, email,
                  cor, sexo, idade, bairro, cidade, estado, numero):
    if not validate(cpf):
        return {'Messagem': 'CPF invalido 🎵'}
    pessoa = Pessoa(nome=nome,
                    celular=celular,
                    cpf=cpf,
                    endereco=endereco,
                    rg=rg,
                    cep=cep,
                    email=email,
                    cor=cor,
                    sexo=sexo,
                    idade=idade,
                    bairro=bairro,
                    cidade=cidade,
                    estado=estado,
                    numero=numero
                    )
    print(pessoa.cpf)
    try:
        session.add(pessoa)
        session.commit()
        return {'pessoa': pessoa.nome}
    except:
        print("algum erro aconteceu")


def select_all_person():
    result = session.execute(select(Pessoa))
    return result.scalars().all()


def select_one_person(cpf: str):
    result = session.execute(select(Pessoa).where(Pessoa.cpf.__eq__(cpf)))
    if result is None:
        return {"Messagem": "Pessoa nao encontrada"}
    return result.scalars().first()


def select_person_email(email: str):
    result = session.execute(select(Pessoa.id).where(Pessoa.email.__eq__(email)))
    if result is None:
        return {"Messagem": "Pessoa nao encontrada"}
    return result.scalars().one()


def select_person_id(id: int):
    result = session.execute(select(Pessoa).where(Pessoa.id == id))
    if result is None:
        return {"Messagem": "Pessoa nao encontrada"}
    return result.scalars().one()


def delete_person(pessoa_id: int):
    session.execute(delete(Pessoa).where(Pessoa.id == pessoa_id))
    session.commit()
