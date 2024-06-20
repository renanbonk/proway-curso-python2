import os
from random import choices
from typing import Any, Dict, List, Optional
import questionary

from database_operacoes import alterar_registro_tabela_categorias, alterar_registro_tabela_contatos, alterar_registro_tabela_marcas, alterar_registro_tabela_produtos, apagar_registro_tabela_categorias, apagar_registro_tabela_contatos, apagar_registro_tabela_marcas, apagar_registro_tabela_produtos, conectar, consultar_registros_tabela_categorias, consultar_registros_tabela_clientes, consultar_registros_tabela_contatos, consultar_registros_tabela_marcas, consultar_registros_tabela_produtos, definir_banco_dados, inserir_registro_tabela_categorias, inserir_registro_tabela_clientes, inserir_registro_tabela_contatos, inserir_registro_tabela_marcas, inserir_registro_tabela_produtos, setup
from rich.table import Table
from rich.console import Console


os.system("cls")


def cadastrar():
    nome = questionary.text("Digite o nome da categoria: ").ask().strip()
    # nome deve conter no mínimo 3 caracteres e no máximo 100
    while len(nome) < 3 or len(nome) > 100:
        print("Nome deve conter no mínimo 3 caracteres e no máximo 100")
        nome = questionary.text("Digite o nome da categoria: ").ask().strip()

    inserir_registro_tabela_categorias(nome)

def editar():
    # Consultar as categorias do banco de dados
    categorias = consultar_registros_tabela_categorias()
    # Verificando se não existe categorias cadastradas
    if len(categorias) == 0:
        print("Nenhuma categoria cadastrada, não sendo possível editar neste momento.")
        # Encerra a execução da função editar, ou seja, não irá apresentar a opção para escolher
        return
    # Criar uma lista de Choice para o usuário poder escolher utilizando o questionary
    categorias_choices = []
    for categoria in categorias:
        categorias_choices.append(questionary.Choice(categoria.get("nome"), categoria))
    # Perguntar para o usuário qual a categoria que ele deseja editar
    categoria_escolhida = questionary.select("Escolha a categoria para editar:", categorias_choices).ask()
    categoria_escolhida["nome"] = questionary.text(
        "Digite o nome da categoria: ", 
        categoria_escolhida.get("nome"),
    ).ask().strip()
    # Chamar a função que executará o update na tabela de categoiras, 
    # para efetivar a atualização na base de dados
    alterar_registro_tabela_categorias(categoria_escolhida.get("id"), categoria_escolhida.get("nome"))

def apagar():
    # Consultar as categorias do banco de dados
    categorias = consultar_registros_tabela_categorias()
    # Verificando se não existe categorias cadastradas
    if len(categorias) == 0:
        print("Nenhuma categoria cadastrada, não sendo possível apagar neste momento.")
        # Encerra a execução da função apagar, ou seja, não irá apresentar a opção para escolher
        return
    # Criar uma lista de Choice para o usuário poder escolher utilizando o questionary
    categorias_choices = []
    for categoria in categorias:
        categorias_choices.append(questionary.Choice(categoria.get("nome"), categoria.get("id")))
    # Perguntar para o usuário qual a categoria que ele deseja apagar
    id_escolhido = questionary.select("Escolha a categoria para apagar:", categorias_choices).ask()
    # Executar o delete na tabela de categorias com o id da categoria escolhida
    apagar_registro_tabela_categorias(id_escolhido)
    print("Registro apagado com sucesso")


def listar_todos():
    categorias = consultar_registros_tabela_categorias()
    # Veriifcar se a lista de categorias é vazia
    if len(categorias) == 0:
        # Apresentar mensagem de que não existe categoria cadastrada
        print("Nenhuma categoria cadastrada")
        # return encerrar a execução da função listar_todos, ou seja, não apresentará a tabela
        return
    tabela = Table()
    tabela.add_column("Código")
    tabela.add_column("Nome")
    
    for categoria in categorias:
        tabela.add_row(str(categoria.get("id")), categoria.get("nome"))
    
    console = Console()
    console.print(tabela)



def listar_todas_marcas():
    marcas = consultar_registros_tabela_marcas()
    # Veriifcar se a lista de marcas é vazia
    if len(marcas) == 0:
        # Apresentar mensagem de que não existe marca cadastrada
        print("Nenhuma marca cadastrada")
        # return encerrar a execução da função listar_todos, ou seja, não apresentará a tabela
        return
    tabela = Table()
    tabela.add_column("Código")
    tabela.add_column("Nome")
    tabela.add_column("Endereço")
    
    for marca in marcas:
        tabela.add_row(str(marca.get("id")), marca.get("nome"), marca.get("endereco"))
    
    console = Console()
    console.print(tabela)


def cadastrar_marca():
    nome = questionary.text("Digite o nome da marca: ").ask().strip()
    # nome deve conter no mínimo 2 caracteres e no máximo 50
    while len(nome) < 2 or len(nome) > 50:
        print("Nome deve conter no mínimo 2 caracteres e no máximo 50")
        nome = questionary.text("Digite o nome da marca: ").ask().strip()
    
    endereco = questionary.text("Digite o endereço da marca: ").ask().strip()
    # endereço deve conter no mínimo 2 caracteres e no máximo 150
    while len(endereco) < 2 or len(endereco) > 150:
        print("Endereço deve conter no mínimo 2 caracteres e no máximo 150")
        endereco = questionary.text("Digite o endereço da marca: ").ask().strip()

    inserir_registro_tabela_marcas(nome, endereco)


def editar_marca():
    # Consultar as marcas do banco de dados
    marcas = consultar_registros_tabela_marcas()
    # Verificando se não existe marcas cadastradas
    if len(marcas) == 0:
        print("Nenhuma marca cadastrada, não sendo possível editar neste momento.")
        # Encerra a execução da função editar, ou seja, não irá apresentar a opção para escolher
        return
    # Criar uma lista de Choice para o usuário poder escolher utilizando o questionary
    marcas_choices = []
    for marca in marcas:
        marcas_choices.append(questionary.Choice(marca.get("nome"), marca))
    # Perguntar para o usuário qual a marca que ele deseja editar
    marca_escolhida = questionary.select("Escolha a marca para editar:", marcas_choices).ask()
    marca_escolhida["nome"] = questionary.text(
        "Digite o nome da marca: ", marca_escolhida.get("nome"),
    ).ask().strip()

    # nome deve conter no mínimo 2 caracteres e no máximo 50
    while len(marca_escolhida["nome"]) < 2 or len(marca_escolhida["nome"]) > 50:
        print("Nome deve conter no mínimo 2 caracteres e no máximo 50")
        marca_escolhida["nome"] = questionary.text("Digite o nome da marca: ").ask().strip()

    marca_escolhida["endereco"] = questionary.text(
        "Digite o endereço da marca: ",  marca_escolhida.get("endereco"),
    ).ask().strip()
    # endereço deve conter no mínimo 2 caracteres e no máximo 150
    while len(marca_escolhida["endereco"]) < 2 or len(marca_escolhida["endereco"]) > 150:
        print("Endereço deve conter no mínimo 2 caracteres e no máximo 150")
        marca_escolhida["endereco"] = questionary.text("Digite o endereço da marca: ").ask().strip()
        
    # Chamar a função que executará o update na tabela de categoiras, 
    # para efetivar a atualização na base de dados
    alterar_registro_tabela_marcas(
        marca_escolhida.get("id"), 
        marca_escolhida.get("endereco"),
        marca_escolhida.get("nome"),
    )


def apagar_marca():
    # Consultar as marcas do banco de dados
    marcas = consultar_registros_tabela_marcas()
    # Verificando se não existe marcas cadastradas
    if len(marcas) == 0:
        print("Nenhuma marca cadastrada, não sendo possível apagar neste momento.")
        # Encerra a execução da função apagar, ou seja, não irá apresentar a opção para escolher
        return 
    # Criar uma lista de Choice para o usuário poder escolher utilizando o questionary
    marcas_choices = []
    for marca in marcas:
        marcas_choices.append(questionary.Choice(marca.get("nome"), marca))
    # Perguntar para o usuário qual a marca que ele deseja apagar
    marca_escolhida = questionary.select("Escolha a marca para apagar:", marcas_choices).ask()
    # Executar o delete na tabela de marcas com o id da marca escolhida
    texto = f"Deseja realmente apagar o registro {marca_escolhida.get('nome')}"
    confirmacao = questionary.confirm(texto, default=False).ask()
    if confirmacao == False:
        return

    apagar_registro_tabela_marcas(marca_escolhida.get("id"))
    print("Registro apagado com sucesso")


def listar_todos_clientes():
    clientes = consultar_registros_tabela_clientes()
    # Veriifcar se a lista de clientes é vazia
    if len(clientes) == 0:
        # Apresentar mensagem de que não existe cliente cadastrada
        print("Nenhuma cliente cadastrada")
        # return encerrar a execução da função listar_todos, ou seja, não apresentará a tabela
        return
    tabela = Table()
    tabela.add_column("Código")
    tabela.add_column("Nome")
    tabela.add_column("Endereço")
    
    for cliente in clientes:
        tabela.add_row(str(cliente.get("id")), cliente.get("nome"), cliente.get("cpf"))
    
    console = Console()
    console.print(tabela)


def cadastrar_cliente():
    nome = questionary.text("Digite o nome do cliente: ").ask().strip()
    # nome deve conter no mínimo 2 caracteres e no máximo 100
    while len(nome) < 2 or len(nome) > 100:
        print("Nome deve conter no mínimo 2 caracteres e no máximo 100")
        nome = questionary.text("Digite o nome do cliente: ").ask().strip()
    
    cpf = questionary.text("Digite o cpf do cliente: ").ask().strip()
    # cpf deve conter no mínimo 14 caracteres e no máximo 14
    while len(cpf) < 14 or len(cpf) > 14:
        print("cpf deve conter no mínimo 14 caracteres e no máximo 14")
        cpf = questionary.text("Digite o cpf do cliente: ").ask().strip()

    inserir_registro_tabela_clientes(nome, cpf)


def editar_cliente():
    pass


def apagar_cliente():
    pass

def menu():
    opcao = 0
    opcoes = [
        questionary.Choice("Categoria", 1),
        questionary.Choice("Cliente", 2),
        questionary.Choice("Marca", 3),
        questionary.Choice("Produtos", 4),
        questionary.Choice("Contatos", 5),
        questionary.Choice("Sair", 1000),
    ]
    while opcao != 1000:
        opcao = int(questionary.select("Escolha o menu:", opcoes).ask())
        if opcao == 1:
            menu_categoria()
        elif opcao == 2:
            menu_cliente()
        elif opcao == 3:
            menu_marca()
        elif opcao == 4:
            menu_produtos()
        elif opcao == 5:
            menu_contato()


def menu_cliente():
    opcao = 0
    opcoes = [    
        questionary.Choice("Listar todos", 1),
        questionary.Choice("Cadastro", 2),
        questionary.Choice("Editar", 3),
        questionary.Choice("Apagar", 4),
        questionary.Choice("Voltar", 1000),
    ]
    while opcao != 1000:
        opcao = int(questionary.select("Escolha o menu de cliente:", opcoes).ask())
        if opcao == 1:
            listar_todos_clientes()
        elif opcao == 2:
            cadastrar_cliente()
        elif opcao == 3:
            editar_cliente()
        elif opcao == 4:
            apagar_cliente()

def menu_categoria():
    opcao = 0
    opcoes = [    
        questionary.Choice("Listar todos", 1),
        questionary.Choice("Cadastro", 2),
        questionary.Choice("Editar", 3),
        questionary.Choice("Apagar", 4),
        questionary.Choice("Voltar", 1000),
    ]
    while opcao != 1000:
        opcao = int(questionary.select("Escolha o menu de categoria:", opcoes).ask())
        if opcao == 1:
            listar_todos()
        elif opcao == 2:
            cadastrar()
        elif opcao == 3:
            editar()
        elif opcao == 4:
            apagar()


def listar_todos_produtos():
    produtos = consultar_registros_tabela_produtos()
    # Veriifcar se a lista de produtos é vazia
    if len(produtos) == 0:
        # Apresentar mensagem de que não existe produto cadastrada
        print("Nenhuma produto cadastrada")
        # return encerrar a execução da função listar_todos, ou seja, não apresentará a tabela
        return
    tabela = Table()
    tabela.add_column("Código")
    tabela.add_column("Categoria")
    tabela.add_column("Nome")

    for produto in produtos:
        tabela.add_row(
            str(produto.get("id")), 
            produto.get("categoria").get("nome"), 
            produto.get("nome"),
        )
    
    console = Console()
    console.print(tabela)


def obter_catergorias_choices() -> List[questionary.Choice]:
        # obter a lista de categorias para permitir o usuário escolher a categoria 
    # que o produto será atrelado
    categorias = consultar_registros_tabela_categorias()
    categorias_choices = []
    for categoria in categorias:
        categorias_choices.append(questionary.Choice(categoria.get("nome"), categoria))
    return categorias_choices


def cadastrar_produto():
    categorias_choices = obter_catergorias_choices()
    nome = questionary.text("Digite o nome do produto: ").ask().strip()
    categoria = questionary.select("Escolha a categoria: ", categorias_choices).ask()

    inserir_registro_tabela_produtos(nome, categoria.get("id"))
    print("Produto cadastrad com sucesso")


def editar_produto():
    produto_escolhido = escolher_produto()
    if produto_escolhido is None:
        return
    
    categorias_choices= obter_catergorias_choices()
    produto_escolhido["nome"] = questionary.text(
        "Digite o nome do produto: ", default=produto_escolhido.get("nome")
    ).ask().strip()
    produto_escolhido["categoria"] = questionary.text(
        "Digite o nome do produto: ", default=produto_escolhido.get("nome"),
    ).ask().strip()
    alterar_registro_tabela_produtos(produto_escolhido)
    print("Produto alterado com sucesso")


def apagar_produto():
    produto_escolhido = escolher_produto()
    if produto_escolhido is None:
        return
    confirmacao = questionary.confirm(f"Deseja realmente apagar '{produto_escolhido.get ('nome')}'").ask()
    if confirmacao == False:
        return
    apagar_registro_tabela_produtos(produto_escolhido.get("id"))
    print("Produto apagado com sucesso")


def escolher_produto() -> Optional[Dict[str,Any]]:
    produtos = consultar_registros_tabela_produtos()
    if len(produtos) == 0:
        print ("Nenhum produto cadastrado")
        return None
    
    choices = [questionary.Choice (produto.get("nome"),produto)
               for produto in produtos]
    produto_escolhido = questionary.select("Escolha o produto", choices).ask()
    return produto_escolhido


def menu_marca():
    opcao = 0
    opcoes = [    
        questionary.Choice("Listar todos", 1),
        questionary.Choice("Cadastro", 2),
        questionary.Choice("Editar", 3),
        questionary.Choice("Apagar", 4),
        questionary.Choice("Voltar", 1000),
    ]
    while opcao != 1000:
        opcao = int(questionary.select("Escolha o menu de marca:", opcoes).ask())
        # match é um comando que valida que o valor no case é igual a variável
        match(opcao):
            case 1: listar_todas_marcas()
            case 2: cadastrar_marca()
            case 3: editar_marca()
            case 4: apagar_marca()


def menu_produtos():
    opcao = 0
    opcoes = [    
        questionary.Choice("Listar todos", 1),
        questionary.Choice("Cadastro", 2),
        questionary.Choice("Editar", 3),
        questionary.Choice("Apagar", 4),
        questionary.Choice("Voltar", 1000),
    ]
    while opcao != 1000:
        opcao = int(questionary.select("Escolha o menu de produtos:", opcoes).ask())
        # match é um comando que valida que o valor no case é igual a variável
        match(opcao):
            case 1: listar_todos_produtos()
            case 2: cadastrar_produto()
            case 3: editar_produto()
            case 4: apagar_produto()


def menu_contato():
    opcao = 0
    opcoes = [
        questionary.Choice("Listar todos", 1),
        questionary.Choice("Cadastro", 2),
        questionary.Choice("Editar",3),
        questionary.Choice("Apagar", 4),
        questionary.Choice("Voltar", 1000),
    ]
    while opcao != 1000:
        opcao = int(questionary.select("Escolha o menu de contatos",opcoes).ask())
        match(opcao):
            case 1: listar_todos_contatos()
            case 2: cadastrar_contato()
            case 3: editar_contato()
            case 4: apagar_contato()
        
    
def listar_todos_contatos():
    contatos = consultar_registros_tabela_contatos()
    if len(contatos) == 0:
        print ("Nenhum contato cadastrado")
        return
    tabela = Table()
    tabela.add_column("Código")
    tabela.add_column("cliente")
    tabela.add_column("tipo")
    tabela.add_column("valor")

    for contato in contatos:
        tabela.add_row(
            str(contato.get("id")),
            contato.get("cliente").get ("nome"),
            contato.get("tipo"),
            contato.get("valor"),
        )
    console = Console()
    console.print(tabela)


def obter_clientes_choices():
    clientes = consultar_registros_tabela_clientes()
    clientes_choices = []
    for cliente in clientes:
        clientes_choices.append(questionary.Choice(cliente.get("nome"), cliente))
    return clientes_choices

def cadastrar_contato():
    clientes_choices = obter_clientes_choices()
    nome = questionary.text ("Digite o nome do contato: ").ask().strip()
    cliente = questionary.select("Escolha o cliente: ", clientes_choices).ask()

    inserir_registro_tabela_contatos(nome, cliente.get("id"))
    print ("Contato cadastrado com sucesso")



def editar_contato():
    contato_escolhido = escolher_contato()
    if contato_escolhido is None:
        return

    contato_escolhido["nome"] = questionary.text(
        "Digite o nome do contato: ", default=contato_escolhido.get
        ("nome")).ask().strip()
    contato_escolhido["cliente"] = questionary.text(
        "Digite o nome do contato: ", default=contato_escolhido.get("nome"),
    ).ask().strip()
    alterar_registro_tabela_contatos(contato_escolhido)



def escolher_contato() -> Optional[dict[str,Any]]:
    contatos = consultar_registros_tabela_contatos()
    if len(contatos) == 0:
        print ("Nenhum contato cadastrado")
        return None

    choices =[questionary.Choice (contato.get("nome").contato)
               for contato in contatos]
    contato_escolhido = questionary.select("Escolha o contato", choices). ask()
    return contato_escolhido


def apagar_contato():
    contato_escolhido = escolher_contato()
    if contato_escolhido is None:
        return
    apagar_registro_tabela_contatos(contato_escolhido.get("id"))
    print("Contato apagado com sucesso")

setup()
menu()  