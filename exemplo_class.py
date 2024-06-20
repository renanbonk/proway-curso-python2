class Categoria:
    # Construtor é uma função que é executada quando Categoria() é chamado
    # Tem dois parâmetros id e nome
    def __init__(self, id: int, nome: str):
        # Declarando e atribuindo valor para os atributos (codigo, nome)
        # da classe Categoria
        self.codigo = id
        self.nome = nome

# Instanciando um objeto da classe Categoria
categoria_hatch = Categoria(nome="Hatch", id=20)
categoria_sedan = Categoria(21, "Sedan")
print(categoria_hatch.codigo)
print(categoria_hatch.nome)
print(categoria_sedan.codigo)
print(categoria_sedan.nome)


class Cliente:
    def __init__(self, id: int, nome: str, cpf: str):
        self.id = id
        self.nome = nome
        self.cpf = cpf


renan = Cliente(1, "Renan", "932.482.120-21")
gabriel = Cliente(id=2, nome="Gabriel", cpf="234.123.192-20")
gustavo = Cliente(3, cpf="299.302.201-20", nome="Gustavo")
print(renan.id, renan.nome, renan.cpf)
print(gabriel.id, gabriel.nome, gabriel.cpf)

class Contato:    
    def __init__(self, cliente: Cliente, tipo: str, valor: str):
        self.cliente = cliente
        self.tipo= tipo
        self.valor = valor

# contato_email_renan é um objeto da classe Contato
# instanciando um objeto da classe Contato
contato_email_renan = Contato(renan, "E-mail", "renanzinho@gmail.com")
print(contato_email_renan.cliente.nome, contato_email_renan.tipo, contato_email_renan.valor) 