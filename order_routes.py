from fastapi import APIRouter

order_router = APIRouter(prefix="/orders", tags=["Orders"]) #define na parte visual a vialização dessa 

#sempre que vc quiser fazer uma nova sessão orders vc vai fazer uma noma função
@order_router.get("/pedidos") #define a rota de lista de pedidos
async def list_orders():
    """
     Essa é a rota de lista de pedidos do nosso sistema
    """
    return {"message": "Voce acessou a lista de pedidos"}