from fastapi import APIRouter #biblioteca APIRouter
from sqlalchemy.orm import sessionmaker # type: ignore #biblioteca sessionmaker
from models import Usuario, db #importa a classe Usuario do arquivo models.py
auth_router = APIRouter(prefix="/auth", tags=["Authentication"]) #definindo a variavel auth_router como APIRouter

#sempre que vc quiser fazer uma nova sessão orders vc vai fazer uma noma função
@auth_router.post("/") #define a rota de login
async def autenticação():
    """
    Essa é a rota de autenticação do nosso sistema
    """
    return {"message": "Voce está na rota de autenticação", "autenticado": False}

@auth_router.post("/login") #define a rota de login
async def entrada(email: str, senha: str): #mostra que str é string mais de uma forma simplificada
    Session = sessionmaker(bind=engine) #cria uma sessão de banco de dados
    session = Session() #cria uma sessão de banco de dados
    usuario = session.query(Usuario).filter(Usuario.email == email, Usuario.senha == senha).first() #faz uma consulta no banco de dados para verificar se o usuário existe e filtra pelo email e senha
    if usuario:
        return {"message": "Login realizado com sucesso", "autenticado": True}
    else:
        novo_usuario = Usuario(email=email, senha=senha) #cria um novo usuário
        session.add(novo_usuario)
        session.commit()
        return {"message": "Usuário criado com sucesso", "autenticado": False}