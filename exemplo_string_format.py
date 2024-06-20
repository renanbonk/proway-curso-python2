import os


def formatar_com_porcentual(nome_usuario: str, idade_usuario: int, saldo_usuario: float):
    # %s é ultilizado para string
    # %d é ultilizado para int
    # %f é ultilizado para float

    texto = "Bem vindo %s! Sua idade é %d vc tem o saldo de %f" % (nome_usuario, idade_usuario, saldo_usuario)
    print(texto)


def formatar_com_format_por_posicao(nome_usuario: str, idade_usuario: int, saldo_usuario: float):
    texto = "Bem vindo {nome}! Sua idade é {idade} vc tem o saldo de {}".format(nome_usuario, idade_usuario, saldo_usuario)
    print(texto)


def formatar_com_format_nomeado(nome_usuario: str, idade_usuario: int, saldo_usuario: float):
    texto = "Bem vindo {nome}! Sua idade é {idade} vc tem o saldo de {saldo}".format(
        nome=nome_usuario, idade=idade_usuario, saldo= saldo_usuario,
        )
    print(texto)


def formatar_com_format_top(nome_usuario: str, idade_usuario: int, saldo_usuario: float):
    texto = f"Bem vindo {nome_usuario}! Sua idade é {idade_usuario} vc tem o saldo de {saldo_usuario}"

    
