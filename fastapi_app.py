from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel
from typing import Optional, List
from enum import Enum
import requests

app = FastAPI()


class Projeto(BaseModel):
    titulo: str
    descricao: str
    data_inicio: str
    orcamento: float
    categoria_id: int

class ProjetoSimples(BaseModel):
    titulo: str
    orcamento: float


class StatusProjeto(str, Enum):
    em_andamento = "em_andamento"
    finalizado = "finalizado"
    cancelado = "cancelado"



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


@app.get("/projetos/{projeto_id}")
def obter_projeto_por_id(projeto_id: int = Path(..., gt=0, description="ID do projeto (maior que zero)")):
    return {"mensagem": f"Buscando projeto com ID {projeto_id}"}


@app.get("/projetos/status/{status}")
def listar_por_status(status: StatusProjeto):
    return {"mensagem": f"Projetos com status: {status}"}


@app.get("/projetos/opcional/{projeto_id}")
def buscar_opcional(projeto_id: Optional[int] = None):
    if projeto_id:
        return {"mensagem": f"Projeto específico: {projeto_id}"}
    return {"mensagem": "Listando todos os projetos"}


@app.get("/projetos/filtro")
def buscar_projetos_categoria(
    categoria: Optional[str] = Query(None, min_length=3),
    ativo: Optional[bool] = Query(True)
):
    return {"mensagem": f"Categoria: {categoria}, Ativo: {ativo}"}

@app.get("/projetos/consulta")
def consulta_multipla(
    orcamento_min: Optional[float] = Query(0),
    orcamento_max: Optional[float] = Query(999999)
):
    return {"mensagem": f"Orçamento entre {orcamento_min} e {orcamento_max}"}


@app.post("/projetos/simples")
def novo_projeto_simples(proj: ProjetoSimples):
    return {"mensagem": f"Projeto '{proj.titulo}' com orçamento R$ {proj.orcamento}"}

@app.post("/projetos/validar")
def validar_projeto_completo(proj: Projeto):
    if proj.orcamento < 1000:
        raise HTTPException(status_code=400, detail="Orçamento muito baixo!")
    return {"mensagem": f"Projeto '{proj.titulo}' validado com sucesso"}
