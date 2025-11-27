from django.test import TestCase
# Importa a classe base TestCase, usada para criar testes automatizados no Django.
# Ela fornece um ambiente de teste com banco de dados isolado e várias ferramentas
# para verificar o comportamento do código.


# Create your tests here.
# Este comentário é gerado automaticamente quando o app é criado.
# É aqui que você deve definir as classes e métodos de teste.
#
# Exemplo de estrutura básica de um teste:
#
# from .models import Projeto
#
# class ProjetoModelTest(TestCase):
#     def test_criacao_projeto(self):
#         # Cria um projeto de exemplo
#         projeto = Projeto.objects.create(
#             titulo="Projeto Teste",
#             descricao="Descrição teste",
#             categoria=alguma_categoria,
#             data_inicio=date(2025, 1, 1),
#             data_fim=date(2025, 1, 10),
#             orcamento=1000.00
#         )
#
#         # Verifica se o título foi salvo corretamente
#         self.assertEqual(projeto.titulo, "Projeto Teste")
#
#         # Verifica se a duração está sendo calculada corretamente
#         self.assertEqual(projeto.duracao, 9)
#
# Você pode rodar os testes com:
# python manage.py test
