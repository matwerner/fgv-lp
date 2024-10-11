# PROGRAMACAO PROCEDURAL

p1 = {
    "nome": "Iphone 15X",
    "preco": 10000
}

p2 = {
    "nome": "Samsung Galaxy S24",
    "preco": 4000
}

carrinho = {
    "usuario": "Matheus",
    "produtos": [p1, p2]
}

def total_carrinho(carrinho: dict) -> float:
    total = 0
    for p in carrinho["produtos"]:
        total += p["preco"]
    return total

print(total_carrinho(carrinho))

# ORIENTACAO A OBJETOS

class Produto:

    def __init__(self, nome: str, preco: float=-1):
        self.nome = nome
        self.preco = preco
    
    def copy(self):
        return Produto(self.nome, self.preco)

p1 = Produto("Iphone", 10000)
p2 = Produto("Galaxy", 4000)

from typing import List
class Carrinho:

    def __init__(self, produtos: List[Produto]):
        self.produtos = produtos
        self.nome_usuario = "Matheus"

    def calcular_total(self) -> float:
        total = 0
        for p in self.produtos:
            total += p.preco
        return total

carrinho = Carrinho([p1, p2])
print(carrinho.calcular_total())

conta = {
    "saldo": 1000
}

conta["saldo"] = -10000000

def exibir_saldo(conta):
    print(conta["saldo"])

class Conta:

    def __init__(self, saldo) -> None:
        self.__saldo = saldo          # Publico
        self.__usuario = "Matheus"    # Protegido
        self.__cpf = "111.111.111-00" # Privado
    
    def get_usuario(self):
        return self.__usuario
    
    def set_usuario(self, novo_usuario):
        self.__usuario = novo_usuario
    
    def get_cpf(self):
        return self.__cpf[:3] + ".XXX.XXX-XX"
    
    def set_saldo(self, novo_saldo):
        print("Saldo foi modificado no dia XXXX para valor tal")
        self.__saldo = novo_saldo

    def __str__(self):
        return f"Nome: {self.__usuario}\nCPF: {self.__cpf}"

conta = Conta(1000)
print()
print(conta)