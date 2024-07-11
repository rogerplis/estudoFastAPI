import datetime

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    status: str
    email: str
    password: str
    verify_pwd: str


class UserPwd(BaseModel):
    password: str
    verifypwd: str


class UserUpdate(BaseModel):
    status: str


class UserInDB(User):
    id: int


class Task(BaseModel):
    name: str
    description: str
    user_id: int


class TaskUpdate(Task):
    pass


class SubTask(BaseModel):
    name: str
    description: str
    prevision: int
    task_id: int


class SubtaskUpdate(BaseModel):
    name: str
    description: str
    init_at: datetime.date
    status: str


class SubtaskInDB(SubTask):
    id: int


class PessoaSchema(BaseModel):
    id: int
    nome: str
    idade: int
    cpf: str
    rg: str
    sexo: str
    email: str
    cep: str
    endereco: str
    numero: int
    bairro: str
    cidade: str
    estado: str
    celular: str
    cor: str


class Pessoa(BaseModel):
    nome: str
    idade: int
    cpf: str
    rg: str
    sexo: str
    email: str
    cep: str
    endereco: str
    numero: int
    bairro: str
    cidade: str
    estado: str
    celular: str
    cor: str


class PessoaUser(BaseModel):
    email: str
    id: int


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class LoginUser(BaseModel):
    email: EmailStr
    password: str
