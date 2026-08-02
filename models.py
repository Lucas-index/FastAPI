from sqlalchemy import String, creat_enginer, Column, Strinbg, Integer, Boolean, Float, ForeignKey, create_engine
from sqlalchemy.orm import declarite_base
from sqlalchemy_utils.types import ChoiceType
# cria a conexão para o seu banco de dados
db = create_engine("sqlite:///banco.db")

#cria a base para o seu banco
Base = declarative_base() 

# cria as classes/tabelas do seu banco
# Usuario
class Usuario(Base):
    __tablename__ = "usuarios" #define o nome da tabela

    id = Column("id", Integer, primary_key=True, autoincrement=True) #define o id como chave primaria e autoincrementável
    nome = Column("nome", String, nullable=False) #define o nome como campo q nn pode nn ser preenchido por isso a função nullable=False
    email = Column("email", String, nullable=False)
    senha = Column("senha", String, nullable=False)
    ativo = Column("ativo", Boolean, nullable=False)
    telefone = Column("telefone", String, nullable=False)
    admin = Column("admin", Boolean, default=False) #define o admin como campo q nn pode nn ser preenchido

    def __init__(self, nome, email, senha, telefone, ativo=True, admin=False): # define a obrigação de preencher os campos nome, email, senha e telefone, e define o ativo como ele já está ativo e o admin como nn admin
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.telefone = telefone
        self.admin = admin


# Pedido
class Pedido(Base):
    __tablename__ = "pedidos" #define o nome da tabela

    Status_Pedidos = (
        ("Em andamento", "Em andamento"),
        ("Finalizado", "Finalizado"),
        ("Cancelado", "Cancelado"),
    )

    id = Column("id", Integer, primary_key=True, autoincrement=True) #define o id como chave primaria e autoincrementável
    itens = Column("itens", String, nullable=False)
    quantidade = Column("quantidade", Integer)
    preco = Column("preco", Float, nullable=False)
    frete = Column("frete", Float, nullable=False)
    usuario = Column("usuario", Integer, ForeignKey("usuarios.id"), nullable=False) #define o usuario_id como chave estrangeira da tabela usuarios
    status = Column("status", ChoiceType(Status_Pedidos), nullable=False, default="Em andamento") #define q com a função com a ChoiceType o status só pode ser preenchido com os valores definidos na tupla Status_Pedidos

    def __init__(self, itens, quantidade, usuario, preco=0, frete=0, status="Em andamento"): # define a obrigação de preencher os campos itens, quantidade, preco, frete e usuario
        self.itens = itens
        self.quantidade = quantidade
        self.preco = preco
        self.frete = frete
        self.usuario = usuario
        self.status = status
# ItensPedido
class ItemPedido(Base):
    __tablename__ = "itens_pedido" #define o nome da tabela

    id = Column("id", Integer, primary_key=True, autoincrement=True) #define o id como chave primaria e autoincrementável
    tamanho = Column("tamanho", String, nullable=False)
    sabor= Column("sabor", String, nullable=False)
    quantidade = Column("quantidade", Integer, nullable=False)
    preco_unitario = Column("preco_unitario", Float, nullable=False)
    pedido = Column("pedido", Integer, ForeignKey("pedidos.id"), nullable=False) #define o pedido_id como chave estrangeira da tabela pedidos

    def __init__(self, tamanho, sabor, quantidade, preco_unitario, pedido): # define a obrigação de preencher os campos tamanho, sabor, quantidade, preco_unitario e pedido
        self.tamanho = tamanho
        self.sabor = sabor
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.pedido = pedido

#executar a criação dos metadados do banco de dados 

