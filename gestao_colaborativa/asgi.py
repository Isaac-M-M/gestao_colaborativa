"""
ASGI config for gestao_colaborativa project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""
# O comentário acima é o cabeçalho padrão gerado pelo Django.
# Ele explica que este arquivo configura a aplicação ASGI,
# a interface moderna usada para comunicação assíncrona (WebSockets, HTTP2, etc).

import os
# O módulo os permite acessar variáveis de ambiente do sistema operacional.

from django.core.asgi import get_asgi_application
# get_asgi_application é uma função que prepara a aplicação Django
# para rodar sob servidores ASGI (como Uvicorn, Daphne, Hypercorn).


# Define a variável de ambiente com o caminho do arquivo de configurações
# do projeto Django. Sem isso, o Django não sabe qual settings usar.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestao_colaborativa.settings')

# Cria a instância ASGI da aplicação Django.
# Essa variável "application" é o ponto de entrada que os servidores ASGI usam.
application = get_asgi_application()
