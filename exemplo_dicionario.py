from typing import Any, Dict, List
import questionary


def exemplo_basico():
    # Dicionário: um lugar onde é possível armazenar utilizando chave valor
    # Criar dicinário
    notas_pamela  = {
        "nome": "Pamela",
        "nota": 10
    }

    # Chave => valor
    notas_renan = {
        "nome": "Renan",
        "nota": 6.5,
        "status": "Aprovado"
    }

    # Atualizar a nota da Pamela
    notas_pamela["nota"] = 9.8

    # Obter dado do dicionário
    print("Aluna:")
    print("Nome: ", notas_pamela.get("nome"))
    print("Nota: ", notas_pamela.get("nota"))
    print("Status: ", notas_pamela.get("status", "Não definido"))

    print("Aluno:")
    print("Nome: ", notas_renan.get("nome"))
    print("Nota: ", notas_renan.get("nota"))
    print("Status: ", notas_renan.get("status", "Não definido"))


def exemplo_solicitando_para_usuario():
    dados = {}
    dados["nome"] = questionary.text("Digite o seu nome").ask()
    dados["idade"] = int(questionary.text("Digite a idade").ask())
    dados["chave_errada"] = 20
    
    # Remover um elemento do dicionário
    del dados["chave_errada"]
    
    print("Nome: ", dados.get("nome"))
    print("Idade: ", dados.get("idade"))
    
def exemplo_dicionario_complexo():
    alunos = [
        {
            "nome": "Pamela",
            "idade": 23,
            "notas": [10, 9.6, 3]
        },
        {
            "nome": "Julio",
            "idade": 30,
            "nota": 6.8,
        },
        {
            "nome": "KarolComQ",
            "idade": 72,
            "notas": [
                {
                    "nota": 9,
                    "peso": 2 # 4.5
                },
                {
                    "nota": 10,
                    "peso": 5 # 2
                },
                {
                    "nota": 7,
                    "peso": 3 # 2,33
                }
            ]
        }
    ]
    # Obter a nota 10 da Pamela
    notas = alunos[0].get("notas")
    # Obter a nota 6.8 do Julio
    nota = alunos[1].get("nota")
    # Calcular a nota 1 da KarolComQ
    notas_karol_com_q = alunos[2].get("notas")
    resultado1 = notas_karol_com_q[0].get("nota") * notas_karol_com_q[0].get("peso")
    resultado2 = notas_karol_com_q[1].get("nota") * notas_karol_com_q[1].get("peso")
    resultado3 = notas_karol_com_q[2].get("nota") * notas_karol_com_q[2].get("peso")
    soma = (resultado1 + resultado2 + resultado3) / 10
    print(soma)
        

def exemplo_percorrer_dicionario():
    dados = {
        "nome": "Gol",
        "preco": 20000,
        "cor": "Azul",
        "idade": 20
    }

    print("CHAVES: ")
    for chave in dados.keys():
        print(chave)
        
    print("\nVALORES: ")
    for valor in dados.values():
        print(valor)

    print("\nCHAVES COM VALORES: ")
    for chave, valor in dados.items():
        print(chave, valor)


def exemplo_de_lista_com_dicionario():
    alunos: List[Dict[str, Any]] = []
    for i in range(3):
        nome = questionary.text("Digite o nome: ").ask()
        idade = int(questionary.text("Digite a idade: ").ask())
        nota = float(questionary.text("Digite a nota: ").ask())
        # Criando um dicionário com duas chaves idade e nota
        aluno = {
            "idade": idade,
            "nota": nota
        }
        # Criando uma chave chamada nome no dicionário aluno
        aluno["nome"] = nome
        # Adicionando o dicionário no vetor (lista) de alunos
        alunos.append(aluno)

    # for i in range(len(alunos)):
    #     aluno = alunos[i]
    for aluno in alunos: # foreach
        print("Nome: ", aluno.get("nome"))

    
exemplo_de_lista_com_dicionario()

# vetor => [10, 8, 9]
# dicionário => { "nota1": 10, "nota2": 8, "nota3": 9}

# [id, nome, endereco]
# marca = [1, "Fiat", 10000, "SC - Blumenau - Rua São Paulo - 1740"]
# marca[2]

# marca = {
#   "id": 1,
#   "nome": "Fiat",
#   "endereco": "SC - Blumenau - Rua São Paulo - 1740",
#   "faturamento": 10000
# }
# marca.get("endereco")
