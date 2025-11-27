"""
WSGI config for gestao_colaborativa project.

Este arquivo configura o WSGI para o projeto gestao_colaborativa.

WSGI (Web Server Gateway Interface) é o padrão tradicional de comunicação
entre servidores web e aplicações Python, usado por servidores como:
- Gunicorn
- uWSGI
- mod_wsgi (Apache)

Este arquivo expõe o objeto `application`, que o servidor utiliza
como ponto de entrada para rodar o Django.

Documentação:
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
# Módulo 'os' é usado para manipular variáveis de ambiente.

from django.core.wsgi import get_wsgi_application
# Função que cria a aplicação WSGI compatível com servidores web.


# ---------------------------------------------------------------
# DEFINE O ARQUIVO DE CONFIGURAÇÃO DO DJANGO
# ---------------------------------------------------------------
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestao_colaborativa.settings')
# Essa linha define qual arquivo de configurações o Django deve usar.
# É obrigatório para que o Django saiba onde estão suas configurações.


# ---------------------------------------------------------------
# CRIA A APLICAÇÃO WSGI
# ---------------------------------------------------------------
application = get_wsgi_application()
# 'application' é o ponto de entrada para o servidor WSGI.
# Ele é responsável por conectar a aplicação Django ao servidor web.
