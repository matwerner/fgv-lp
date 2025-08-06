class Personagem:

    def __init__(self, vida, ataque, defesa):
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
    
    def atacar(self, outro_personagem):
        print("Personagem deu um soco!")

class Guerreiro(Personagem):

    def __init__(self, vida, ataque, defesa):
        super().__init__(vida, ataque, defesa)
    
    def atacar(self, outro_personagem):
        print("Guerreiro desferiu um golpe de espada!")

class Mago(Personagem):

    def __init__(self, vida, ataque, defesa):
        super().__init__(vida, ataque, defesa)

    def atacar(self, outro_personagem):
        print("Mago utilizou uma bola de fogo!")

from typing import List

def executar_ataque_em_conjunto(personagens: List[Personagem], alvo: Personagem):
    for p in personagens:
        p.atacar(alvo)

class Reptil:

    def __init__(self):
        pass

    def caminhe(self):
        print("Estou caminhando")

class Voador:

    def __init__(self):
        pass

    def voa(self):
        print("Estou voando")

class Dragao(Voador, Reptil):

    def __init__(self):
        self.asa = Dragao.Asa()

    class Asa:

        def __init__(self):
            pass

from abc import ABC, abstractmethod

class Forma(ABC):

    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    # def area(self):
    #     return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

if __name__ == "__main__":
    npc1 = Personagem(20, 20, 20)
    mago1 = Mago(50, 200, 20)
    guerreiro1 = Guerreiro(200, 50, 100)

    grupo = [npc1, mago1]
    executar_ataque_em_conjunto(grupo, guerreiro1)

    d = Dragao()
    d.caminhe()
    d.voa()

    a = Dragao.Asa()

    # Exemplo de uso
    forma = Forma()
    # retangulo = Retangulo(5, 3)
    # print(retangulo.perimetro())