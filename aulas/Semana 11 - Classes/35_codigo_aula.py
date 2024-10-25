from abc import ABC, abstractmethod

class ClasseBase(ABC):

    @abstractmethod
    def ataque(self):
        pass

class ClasseFilha1(ClasseBase):

    def __init__(self) -> None:
        super().__init__()

# Se descomentar a linha de baixo, ocorrera uma exceção
# f = ClasseFilha1()

from typing import Protocol, runtime_checkable

@runtime_checkable
class Agressivo(Protocol):
    pontos_de_ataque: int
    pontos_de_defesa: int

    def ataque(self) -> None:
        ...

class Personagem:

    def __init__(self) -> None:
        self.pontos_de_ataque: int = 10
        self.pontos_de_defesa: int = 10

    def ataque(self) -> None:
        print("Personagem atacou")

class Funcionario:

    def ataque(self) -> None:
        print("Funcionario atacou")

class Bola:

    def __init__(self) -> None:
        pass

def atacar_forma(forma: Agressivo):
    if not isinstance(forma, Agressivo):
        raise Exception("Opa....")
    forma.ataque()

personagem = Personagem()
func = Funcionario()
ball = Bola()
atacar_forma(personagem)
# atacar_forma(func)
# atacar_forma(ball)

from typing import List

class Personagem:

    def __init__(self, pontos_de_vida: int):
        self.pontos_de_vida: int = pontos_de_vida
        # Agregação
        self.pocoes: List[Pocao] = []
    
    def receber(self, pocao):
        self.pocoes.append(pocao)

    def auto_cura(self):
        if len(self.pocoes) < 1:
            return
        p = self.pocoes[0]
        self.pontos_de_vida += p.pontos_de_cura
        self.pocoes.pop()

class Pocao:

    def __init__(self, pontos_de_cura: int):
        self.pontos_de_cura: int = pontos_de_cura
    
    # # Associacao
    # # Caso nõs não tivessemos implementado a agragacao + auto_cura acima
    # def cura(self, p: Personagem):
    #     p.pontos_de_vida += self.pontos_de_cura

class Jogo:

    def __init__(self) -> None:
        # Composicao
        self.personagem: Personagem = Personagem(100)
        self.pocao: Pocao = Pocao(50)
    
    def executar(self):
        pass

j = Jogo()
j.executar()
del j
