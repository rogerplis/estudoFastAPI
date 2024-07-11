import datetime

from sqlalchemy import Column, Integer, String, DATE, ForeignKey
from sqlalchemy.orm import relationship

from app.conn import Base, engine


class User(Base):
    __tablename__ = 'tb_user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    pessoa_id = Column(Integer, ForeignKey('tb_pessoa.id'))
    status = Column(String(10))
    password = Column(String(100))
    email = Column(String(100))
    task = relationship('Task', backref='tb_user', lazy='subquery', cascade="all, delete-orphan")

    def __init__(self, pessoas_id, status, email, password):
        self.pessoa_id = pessoas_id
        self.status = status
        self.email = email
        self.password = password


class Task(Base):
    __tablename__ = 'tb_task'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    description = Column(String(200))
    create_at = Column(DATE, default=datetime.date.today())
    status = Column(String(20), default='created')
    user_id = Column(Integer, ForeignKey('tb_user.id'))
    sub_tasks = relationship('Sub_task', backref='tb_task', lazy='subquery', cascade="all, delete-orphan")

    def __init__(self, name, description, user_id):
        self.description = description
        self.name = name
        self.user_id = user_id


class Sub_task(Base):
    __tablename__ = 'tb_sub_tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    description = Column(String(200))
    create_at = Column(DATE, default=datetime.date.today())
    status = Column(String(20), default='created')
    init_at = Column(DATE, nullable=True)
    end_at = Column(DATE, nullable=True)
    prevision = Column(Integer)
    task_id = Column(Integer, ForeignKey('tb_task.id'))

    def __init__(self, name, description, init_at, end_at, prevision, task_id):
        self.description = description
        self.name = name
        self.init_at = init_at
        self.end_at = end_at
        self.prevision = prevision
        self.task_id = task_id


class Pessoa(Base):
    __tablename__ = 'tb_pessoa'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    idade = Column(Integer, nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    rg = Column(String(20), nullable=False)
    sexo = Column(String(10), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    cep = Column(String(8), nullable=False)
    endereco = Column(String(100), nullable=False)
    numero = Column(Integer, nullable=False)
    bairro = Column(String(100), nullable=False)
    cidade = Column(String(100), nullable=False)
    estado = Column(String(2), nullable=False)
    celular = Column(String(14), nullable=False)
    cor = Column(String(20), nullable=False)
    user = relationship('User', backref='tb_pessoa', lazy='subquery', cascade="all, delete-orphan")

    def __init__(self, nome, idade, cpf, rg, sexo, email, cep, endereco, numero, bairro, cidade, estado, celular, cor):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.rg = rg
        self.sexo = sexo
        self.email = email
        self.cep = cep
        self.endereco = endereco
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.celular = celular
        self.cor = cor


Base.metadata.create_all(engine)
