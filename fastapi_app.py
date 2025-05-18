from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

# Modelo Pydantic para entrada de dados
class Projeto(BaseModel):
    titulo: str
    descricao: str
    data_inicio: str  # formato: 'YYYY-MM-DD'
    orcamento: float
    categoria_id: int

# Endpoint para listar os projetos (GET)
@app.get("/projetos/")
def listar_projetos():
    response = requests.get("http://127.0.0.1:8000/api/projetos/")
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Erro ao buscar projetos")
    return response.json()

# Endpoint para criar um novo projeto (POST)
@app.post("/projetos/")
def criar_projeto(projeto: Projeto):
    response = requests.post("http://127.0.0.1:8000/api/projetos/", json=projeto.dict())
    if response.status_code != 201:
        raise HTTPException(status_code=400, detail="Erro ao criar projeto")
    return response.json()

# Endpoint para atualizar um projeto (PUT)
@app.put("/projetos/{projeto_id}/")
def atualizar_projeto(projeto_id: int, projeto: Projeto):
    response = requests.put(f"http://127.0.0.1:8000/api/projetos/{projeto_id}/", json=projeto.dict())
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Erro ao atualizar projeto")
    return response.json()

# Endpoint para deletar um projeto (DELETE)
@app.delete("/projetos/{projeto_id}/")
def deletar_projeto(projeto_id: int):
    response = requests.delete(f"http://127.0.0.1:8000/api/projetos/{projeto_id}/")
    if response.status_code != 204:
        raise HTTPException(status_code=400, detail="Erro ao deletar projeto")
    return {"mensagem": "Projeto deletado com sucesso"}
