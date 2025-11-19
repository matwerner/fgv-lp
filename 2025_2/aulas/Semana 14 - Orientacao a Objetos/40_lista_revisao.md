# Exercícios de Revisão

## Questão 1

A academia FitSquared utiliza um sistema legado para gerenciar planos de assinatura, calcular preços totais com base no plano escolhido, adicionar extras opcionais e processar upgrades solicitados pelos alunos.
Com a expansão da academia e o aumento da variedade de planos e benefícios, o módulo acabou acumulando responsabilidades e regras de negócio que se misturam entre as classes existentes.

Considere o código legado abaixo, utilizado atualmente no sistema:

```python
class Plan:
    def __init__(self, plan_type, base_price, extras=None):
        self.plan_type = plan_type          # "basic" ou "premium"
        self.base_price = base_price
        self.extras = extras or []          # lista de strings

    def get_total_price(self):
        price = self.base_price

        if self.plan_type == "premium":
            price += 100  # personal incluso

        for e in self.extras:
            if e == "nutricao":
                price += 50
            elif e == "massagem":
                price += 80
            elif e == "pilates":
                price += 40
            elif e == "avaliacao":
                price += 60

        return price

class Member:
    def __init__(self, name, email, plan):
        self.name = name
        self.email = email
        self.plan = plan

    def upgrade_plan(self, new_plan):
        # lógica de diferencial de preço indevida
        old_price = self.plan.get_total_price()
        new_price = new_plan.get_total_price()
        diff = new_price - old_price

        print(f"{self.name} está mudando de {self.plan.plan_type} para {new_plan.plan_type}.")
        print(f"Preço antigo: R$ {old_price}, novo preço: R$ {new_price}. Diferença: R$ {diff}.")

        # troca do plano
        self.plan = new_plan

    def describe_features(self):
        features = ["aulas em grupo"]
        if self.plan_type == "premium":
            features.append("personal")
        for e in self.extras:
            features.append(e)
        return features

class SubscriptionService:
    def process_upgrade(self, member, new_plan):
        # lógica de log acoplada ao serviço
        with open("subscriptions.log", "a") as f:
            f.write(
                f"{member.name} -> {new_plan.plan_type} "
                f"(extras: {new_plan.extras}, total: {new_plan.get_total_price()})\n"
            )

        # lógica de cálculo deixada no Member
        member.upgrade_plan(new_plan)

        print("Upgrade concluído!")
```

Tarefas:
- **A.** Identifique e explique problemas de design no código acima, relacionando-os explicitamente aos princípios **SOLI** (exceto o D).
Justifique cada violação indicando onde e por que ocorre.
- **B.** Proponha uma refatoração completa do módulo, reorganizando corretamente as responsabilidades e utilizando polimorfismo quando apropriado.
- **C.** Escreva um pequeno trecho de código demonstrando o uso do design refatorado.

## Questão 2

O hotel Praia Brava utiliza um sistema legado para sugerir quartos, calcular preços dinâmicos, verificar disponibilidade e enviar confirmações ao cliente.
Com o crescimento da empresa, o módulo acabou acumulando responsabilidades e diversas regras de negócio.


```python
import random
from datetime import datetime, timedelta

class RoomDatabase:
    def get_available_rooms(self, start, end):
        print(f"Buscando quartos disponíveis entre {start} e {end}...")
        base = [("standard", 200), ("deluxe", 350), ("suite", 600)]
        # remove aleatoriamente um para simular ocupação
        if random.random() < 0.5:
            base.pop(0)
        return base

    def get_discounts(self):
        print("Buscando descontos aplicáveis...")
        return {"standard": 0.05, "suite": 0.1}

class ReservationSystem:

    def reserve(
        self,
        user,
        start,
        end,
        user_is_vip=False,
        prefer_suite=False,
        include_breakfast=False,
        notify_email=True,
        notify_sms=False
    ):
        db = RoomDatabase()

        # coletar quartos disponíveis
        rooms = db.get_available_rooms(start, end)

        # aplicar discounts
        discounts = db.get_discounts()
        final = []
        for (rtype, base_price) in rooms:
            price = base_price

            if include_breakfast:
                price += 35

            if user_is_vip and rtype in discounts:
                price = price * (1 - discounts[rtype])

            final.append((rtype, price))

        # preferências do usuário
        if prefer_suite:
            final.sort(key=lambda x: 0 if x[0] == "suite" else 1)
        else:
            final.sort(key=lambda x: x[1])

        chosen = final[0]

        # simula persistência
        with open("reservas.log", "a") as f:
            f.write(f"{user}:{chosen}:{start}->{end}\n")

        # enviar notificações
        msg = f"Reserva confirmada para o quarto {chosen[0]} no valor de {chosen[1]:.2f}"
        if notify_email:
            print(f"Enviando email para {user}: {msg}")
        if notify_sms:
            print(f"Enviando SMS para {user}: {msg}")

        return chosen
        

def main():
    user = "carla@cliente.com"
    start = datetime.now()
    end = start + timedelta(days=3) # Operação entre datas

    rs = ReservationSystem()
    reserva = rs.reserve(
        user, start, end,
        user_is_vip=True,                  # agora precisa desse flag
        prefer_suite=True,
        include_breakfast=True
    )
    print(reserva)
```

Tarefas:
- **A.**  Identifique e explique problemas de design no código acima, relacionando-os explicitamente aos princípios SOLI (exceto o D).
Justifique cada violação mostrando onde e por que ocorre.
- **B.**  Proponha uma refatoração completa da arquitetura de reserva, separando responsabilidades e usando polimorfismo quando apropriado.
- **C.**  Escreva um pequeno trecho de código demonstrando o uso do design refatorado.

## Questão 3

A plataforma **LeagueManager** deseja gerenciar torneios de futebol no formato *todos contra todos* (pontos corridos).
Cada **Time** possui nome e pontuação acumulada.
Uma **Partida** envolve dois times e deve registrar o placar e determinar quem recebe os pontos (3 vitória, 1 empate, 0 derrota).
Um **Torneio** contém a lista de times participantes, gera automaticamente todas as partidas possíveis e permite registrar resultados conforme elas acontecem.

Implemente um modelo orientado a objetos em Python representando esse cenário. Inclua:

1. As classes principais, atributos e métodos relevantes.
2. As relações entre classes (por exemplo: o Torneio compõe Partidas; Partidas se associam a Times).
3. Um pequeno trecho de código simulando a criação do torneio, registro de um resultado e atualização da tabela.

## Questão 4

A plataforma **SkillSwap** permite que usuários troquem aulas e mentorias entre si, sem envolver pagamento.
Cada **Membro** pode ofertar habilidades (como “guitarra”, “python”, “cozinha japonesa”) e solicitar sessões com outros membros.

Uma **Habilidade** possui nome, nível de proficiência (iniciante, intermediário, avançado) e uma breve descrição.
Uma **Sessão** representa um encontro entre dois membros, e deve armazenar:

* mentor,
* aprendiz,
* habilidade ensinada,
* duração prevista,
* status (agendada, realizada, cancelada).

Implemente um modelo orientado a objetos em Python que represente esse cenário. Inclua:

1. Classes principais com seus atributos e métodos;
2. Relações adequadas entre objetos (associação, composição, herança, etc.);
3. Um pequeno exemplo de código criando dois membros e simulando a realização de uma sessão.

## Questão 5

Considere o dataset **Goodreads-Books**, disponível em:
[https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks/data](https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks/data)

Carregue o arquivo correspondente em um `DataFrame` e responda aos itens abaixo utilizando **pandas**:

- **a)** Quantos livros existem no total do dataset? Quantos autores distintos existem? Qual é a **razão média de livros por autor**?

- **b)** Qual autor possui o maior número de livros registrados no dataset?

- **c)** Considerando apenas os livros com **mais de 10.000 avaliações** (`ratings_count > 10000`), qual autor apresenta a **maior média de avaliação** (`average_rating`)?

- **d)** Crie uma nova coluna que marque um livro como **“bem avaliado”** se `average_rating > 4.0` **e** `ratings_count > 5000`.
Quantos livros atendem a esse critério e qual o percentual em relação ao total?

- **e)** Classifique os livros em **faixas de tamanho** (ex.: menos de 200 páginas, entre 200 e 400 páginas, mais de 400 páginas) e, para cada faixa, apresente **quantos livros há** e a **média de `average_rating`**.
