import os

from database_operacoes import consultar_registros_tabela_categorias, consultar_registros_tabela_clientes, consultar_registros_tabela_marcas, criar_banco_dados, criar_tabela_categorias, criar_tabela_clientes, criar_tabela_marcas, inserir_registro_tabela_categorias, inserir_registro_tabela_clientes, inserir_registro_tabela_marcas


os.system("cls")
criar_banco_dados()

criar_tabela_marcas()
inserir_registro_tabela_marcas("Fiat", "SC - Blumenau - Rua São Paulo - 1740")
consultar_registros_tabela_marcas()

criar_tabela_categorias()
inserir_registro_tabela_categorias("Hatch")
inserir_registro_tabela_categorias("SUV")
inserir_registro_tabela_categorias("SEDAN")
consultar_registros_tabela_categorias()

criar_tabela_clientes()
inserir_registro_tabela_clientes("John Doe", "920.192.381-20")
consultar_registros_tabela_clientes()

