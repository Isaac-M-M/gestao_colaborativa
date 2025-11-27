from django.apps import AppConfig
# Importa a classe base AppConfig, usada para configurar aplicações Django.


class CoreConfig(AppConfig):
    """
    CoreConfig define as configurações da aplicação 'core'.
    O Django utiliza esta classe para identificar, iniciar e gerenciar
    componentes da aplicação automaticamente.
    """

    # Define o tipo padrão para chaves primárias automáticas.
    # BigAutoField cria IDs inteiros de 64 bits (muito maiores que AutoField).
    default_auto_field = 'django.db.models.BigAutoField'

    # Nome da aplicação dentro do projeto Django.
    # É utilizado para identificar a pasta onde ela está localizada.
    name = 'core'
