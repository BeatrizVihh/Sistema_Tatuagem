from fastapi import APIRouter      # organiza rotas em grupos
from pydantic import BaseModel     # valida os dados que chegam na API
from typing import Optional        # permite campos opcionais
from database import conectar      # nossa função de conexão

router = APIRouter()               # cria o grupo de rotas
# GET /clientes — lista todos os clientes
@router.get("/clientes")
def listar_clientes():
    conn = conectar()                        # abre conexão
    cursor = conn.cursor(dictionary=True)    # retorna dicionários em vez de tuplas
    cursor.execute("SELECT * FROM cliente")  # executa o SELECT
    clientes = cursor.fetchall()             # pega todos os resultados
    conn.close()                             # fecha a conexão
    return clientes                          # retorna a lista em JSON