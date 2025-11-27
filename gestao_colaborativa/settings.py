"""
Django settings for gestao_colaborativa project.

Este arquivo contém todas as configurações principais do projeto Django.
Foi gerado automaticamente pelo comando:
    django-admin startproject

Documentação recomendada:
https://docs.djangoproject.com/en/5.2/topics/settings/
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
# Pathlib é usada para trabalhar com caminhos de diretórios de forma moderna.

# ---------------------------------------------------------------
# CAMINHO BASE DO PROJETO
# ---------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR aponta para a pasta raiz do projeto (onde fica manage.py).
# É usada como referência para caminhos de templates, banco de dados, etc.


# ---------------------------------------------------------------
# CHAVE SECRETA DO DJANGO
# ---------------------------------------------------------------
SECRET_KEY = 'django-insecure-21r0p=c)kuh*34)!=ds2xse8e=2%el-+!yifb^4%p@#a)0tcg%'
# Essa chave é usada para criptografia, sessões, CSRF e outros recursos internos.
# Em produção, NUNCA deve ser exposta. Aqui está ok, pois é um projeto acadêmico.


# ---------------------------------------------------------------
# MODO DEBUG
# ---------------------------------------------------------------
DEBUG = True
# Se True → mostra erros detalhados e habilita modo de desenvolvimento.
# Em produção deve ser False.


# ---------------------------------------------------------------
# HOSTS PERMITIDOS
# ---------------------------------------------------------------
ALLOWED_HOSTS = []
# Lista de domínios autorizados a acessar o servidor.
# Em desenvolvimento pode ficar vazia.


# ---------------------------------------------------------------
# APLICAÇÕES INSTALADAS
# ---------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',          # Painel administrativo do Django
    'django.contrib.auth',           # Sistema de autenticação (login/usuários)
    'django.contrib.contenttypes',   # Tipos de conteúdo
    'django.contrib.sessions',       # Gerenciamento de sessões do usuário
    'django.contrib.messages',       # Sistema de mensagens (alerts)
    'django.contrib.staticfiles',    # Gerenciamento de arquivos estáticos (CSS/JS)

    # Apps do projeto
    'core',                          # Seu app principal da aplicação

    # Django Rest Framework – API REST
    'rest_framework',
]


# ---------------------------------------------------------------
# MIDDLEWARES
# ---------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',   # Segurança básica
    'django.contrib.sessions.middleware.SessionMiddleware',  # Controle de sessão
    'django.middleware.common.CommonMiddleware',        # Funções comuns (ex.: URL rewriting)
    'django.middleware.csrf.CsrfViewMiddleware',        # Proteção contra ataques CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Login/logout automáticos
    'django.contrib.messages.middleware.MessageMiddleware',    # Mensagens visuais
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Protege contra clickjacking
]


# ---------------------------------------------------------------
# ARQUIVO PRINCIPAL DE URLs DO PROJETO
# ---------------------------------------------------------------
ROOT_URLCONF = 'gestao_colaborativa.urls'
# Define qual arquivo controla todas as URLs principais.


# ---------------------------------------------------------------
# CONFIGURAÇÃO DE TEMPLATES
# ---------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', 
        # Define o mecanismo de template (HTML)

        'DIRS': [],  
        # Diretórios adicionais de templates (você poderia colocar templates globais aqui)

        'APP_DIRS': True,
        # Quando True → Django busca automaticamente templates na pasta /templates de cada app

        'OPTIONS': {
            'context_processors': [
                # Insere variáveis automáticas em todos os templates
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ---------------------------------------------------------------
# CONFIGURAÇÃO DO WSGI (deploy tradicional)
# ---------------------------------------------------------------
WSGI_APPLICATION = 'gestao_colaborativa.wsgi.application'
# Usado por servidores WSGI (Gunicorn, uWSGI).
# Para ASGI (WebSockets), o arquivo é o asgi.py.


# ---------------------------------------------------------------
# BANCO DE DADOS
# ---------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',    # SQLite (banco padrão do Django)
        'NAME': BASE_DIR / 'db.sqlite3',           # Arquivo físico do banco
    }
}
# Em produção, normalmente se usa PostgreSQL ou MySQL.


# ---------------------------------------------------------------
# VALIDAÇÃO DE SENHAS
# ---------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        # Verifica se a senha é muito parecida com dados do usuário.
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        # Define um tamanho mínimo para a senha.
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        # Evita senhas muito comuns.
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        # Impede senhas compostas apenas por números.
    },
]


# ---------------------------------------------------------------
# CONFIGURAÇÕES DE LINGUAGEM E TIMEZONE
# ---------------------------------------------------------------
LANGUAGE_CODE = 'en-us'   # Idioma padrão
TIME_ZONE = 'UTC'         # Fuso horário padrão

USE_I18N = True           # Ativa internacionalização
USE_TZ = True             # Ativa suporte a timezones


# ---------------------------------------------------------------
# ARQUIVOS ESTÁTICOS (CSS, JS, IMAGENS)
# ---------------------------------------------------------------
STATIC_URL = 'static/'
# Em produção, normalmente há configurações adicionais como STATIC_ROOT.


# ---------------------------------------------------------------
# CAMPO PADRÃO DE CHAVE PRIMÁRIA
# ---------------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Define que IDs automáticos terão 64 bits por padrão.
