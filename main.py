from fastapi import FastAPI  # para definir a biblioteca FastAPI

app = FastAPI()  #definindo a variavel app como FastAPI

from auth_routes import auth_router  #importando a rota de autenticação
from order_routes import order_router #importando a rota de pedidos

app.include_router (auth_router)
app.include_router (order_router)  #definindo a rota de pedidos 

#uvicorn main:app --reload para iniciar nosso codigo execular no terminal

#get: serve para fazer a leitura ou pegar algo 
#post: envinar algo para o servidor ou criar algo
#put: atualizar algo no servidor
#delete: remover algo do servidor

