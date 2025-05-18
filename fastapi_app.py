from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class Projeto(BaseModel):
    titulo: str
    descricao: str
    data_inicio: str
    orcamento: float
    categoria_id: int

@app.get("/projetos/")
def listar_projetos():
    response = requests.get("http://127.0.0.1:8000/api/projetos/")
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Erro ao buscar projetos")
    return response.json()

@app.post("/projetos/")
def criar_projeto(projeto: Projeto):
    response = requests.post("http://127.0.0.1:8000/api/projetos/", json=projeto.dict())
    if response.status_code != 201:
        raise HTTPException(status_code=400, detail="Erro ao criar projeto")
    return response.json()

@app.put("/projetos/{projeto_id}/")
def atualizar_projeto(projeto_id: int, projeto: Projeto):
    response = requests.put(f"http://127.0.0.1:8000/api/projetos/{projeto_id}/", json=projeto.dict())
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Erro ao atualizar projeto")
    return response.json()

@app.delete("/projetos/{projeto_id}/")
def deletar_projeto(projeto_id: int):
    response = requests.delete(f"http://127.0.0.1:8000/api/projetos/{projeto_id}/")
    if response.status_code != 204:
        raise HTTPException(status_code=400, detail="Erro ao deletar projeto")
    return {"mensagem": "Projeto deletado com sucesso"}
