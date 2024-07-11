import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.tasks.routers import user_router, pessoa_router, auth_router, task_router

app = FastAPI()

origins = ["http://127.0.0.1:3000", "http://192.168.0.244:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get('/')
def hello_World():
    return 'Bem vindo a aplicação de gerenciamento de tarefas. Faça o login para que possa acessar o conteudo completo'


app.include_router(user_router.router)
app.include_router(pessoa_router.router)
app.include_router(task_router.router)
app.include_router(auth_router.router)

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
