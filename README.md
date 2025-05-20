# Gestão Colaborativa

Sistema de gerenciamento de projetos, tarefas e comentários, desenvolvido com **Django**, **Django REST Framework** e **FastAPI**.

## 📋 Funcionalidades

- Cadastro e visualização de Projetos
- Atribuição de Tarefas a membros
- Comentários com anexos
- Integração com Django Rest Framework (API)
- Integração com FastAPI para consumo dos dados via HTTP
- Estilização com Tailwind CSS + Bootstrap (versão leve)
- Templates com condicionais, loops, includes e filtros

---

## 🧰 Tecnologias Utilizadas

- Python 3.13
- Django 5.2
- Django REST Framework
- FastAPI
- SQLite (banco de dados)
- Tailwind CSS + Bootstrap
- HTML5, CSS3

---

## 🚀 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/Isaac-M-M/gestao_colaborativa.git
cd gestao_colaborativa
2. Crie e ative o ambiente virtual
bash
Copiar
Editar
python -m venv venv
venv\Scripts\activate  # Windows
3. Instale as dependências
bash
Copiar
Editar
pip install -r requirements.txt
4. Execute as migrações do banco
bash
Copiar
Editar
python manage.py makemigrations
python manage.py migrate
5. Inicie o servidor Django
bash
Copiar
Editar
python manage.py runserver
Acesse: http://127.0.0.1:8000/

🧪 API com FastAPI
Rodar FastAPI (em outro terminal):
bash
Copiar
Editar
uvicorn fastapi_app:app --reload
Endpoints disponíveis:
GET /projetos/ – Lista os projetos

POST /projetos/ – Cria um novo projeto

PUT /projetos/{id}/ – Atualiza projeto

DELETE /projetos/{id}/ – Remove projeto

Documentação interativa:

Swagger: http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc

📁 Estrutura do Projeto
csharp
Copiar
Editar
gestao_colaborativa/
├── core/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── serializers.py
│   ├── templates/
│   │   ├── base.html
│   │   └── core/
│   │       ├── index.html
│   │       ├── projeto_list.html
│   │       ├── projeto_form.html
│   │       ├── projeto_detail.html
│   │       └── projeto_confirm_delete.html
├── gestao_colaborativa/
│   └── settings.py
├── fastapi_app.py
├── manage.py
└── requirements.txt
👨‍💻 Autor
Desenvolvido por Isaac Mesquita Moreira - 38211521
Yuri Henrique de Lara Cardoso Valadares - 35674695
Diego Santana dos Santos - 35989262
Repositório: github.com/Isaac-M-M
