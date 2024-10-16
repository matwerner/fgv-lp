import random

class Personagem:

    def __init__(self, vida, ataque_min, ataque_max, defesa):
        self.vida = vida
        self.ataque_min = ataque_min
        self.ataque_max = ataque_max
        self.defesa = defesa
    
    def ataque(self, outro):
        ataque = random.randint(self.ataque_min, self.ataque_max)
        delta = ataque - outro.defesa
        outro.vida -= max(0, delta)

class SimuladorBatalha:

    def __init__(self, p1: Personagem, p2: Personagem) -> None:
        self.p1: Personagem = p1
        self.p2: Personagem = p2

    def batalhar(self):
        round = 1
        while self.p1.vida > 0 and self.p2.vida > 0:
            print(f"Round #{round}")
            n = random.randint(0, 100)
            if n > 50:
                print("P1 atacou!")
                self.p1.ataque(self.p2)
            else:
                print("P2 atacou!")
                self.p2.ataque(self.p1)
            print(f"p1: {p1.vida}")
            print(f"p2: {p2.vida}")
            print()
            round += 1
        if self.p1.vida <= 0:
            print("P2 venceu!")
        else:
            print("P1 venceu!")

p1 = Personagem(100, 10, 20, 10)
p2 = Personagem(100, 20, 40, 0)
similador = SimuladorBatalha(p1, p2)
similador.batalhar()