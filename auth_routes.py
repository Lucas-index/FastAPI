from fastapi import APIRouter #biblioteca APIRouter

auth_router = APIRouter(prefix="/auth", tags=["Authentication"]) #definindo a variavel auth_router como APIRouter

#sempre que vc quiser fazer uma nova sessão orders vc vai fazer uma noma função
@auth_router.post("/") #define a rota de login
async def autenticação():
    """
    Essa é a rota de autenticação do nosso sistema
    """
    return {"message": "Voce está na rota de autenticação"}