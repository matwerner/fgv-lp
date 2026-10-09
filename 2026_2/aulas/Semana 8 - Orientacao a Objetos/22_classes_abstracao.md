# Aula 23: Abstração

## 1. De onde estamos partindo?

Na aula anterior, apresentamos quatro ideias associadas à Orientação a Objetos:

```text
Abstração

Encapsulamento

Herança

Polimorfismo
```

Vimos que cada uma delas está relacionada a uma pergunta diferente.

No caso da **abstração**, a pergunta era:

> Quais informações e operações realmente importam para o problema que queremos resolver?

Considere novamente nossa classe `Mensagem`.

Ao representá-la, escolhemos atributos como `nome`, `texto`, `data_envio`, `lida` e `favorita`.

Uma mensagem poderia possuir muitas outras informações, como o dispositivo utilizado, a localização ou o idioma.

Mas essas informações não eram necessárias para o problema que queríamos resolver. Essa escolha é uma forma de **abstração**.

Nesta aula, vamos olhar para essa ideia com mais cuidado.



## 2. O que é abstração?

Quando desenvolvemos um programa, normalmente estamos interessados apenas em alguns aspectos do problema.

Não precisamos representar todos os detalhes da realidade.

Podemos pensar no processo da seguinte maneira:

```text
Problema real
     ↓
escolhemos o que é relevante
     ↓
Abstração
     ↓
representação no programa
```

Uma abstração busca representar os aspectos importantes para um determinado problema e ignorar detalhes que não são necessários naquele contexto.



### 2.1 A abstração depende do problema

Imagine que queremos representar um livro.

Quais informações um livro deve possuir?

Poderíamos pensar em título, autor, ISBN, número de páginas, editora, preço, peso, estoque, posição de leitura, número de exemplares...

Mas antes de escolher os atributos, precisamos responder:

> Qual problema estamos tentando resolver?

Em uma **biblioteca**, talvez sejam importantes:

```text
Livro (biblioteca)

atributos:   titulo, autor, isbn, exemplares
operações:   emprestar(), devolver()
```

Em uma **loja virtual**:

```text
Livro (loja)

atributos:   titulo, autor, preco, estoque
operações:   aplicar_desconto(), verificar_estoque()
```

Em um **aplicativo de leitura**:

```text
Livro (aplicativo de leitura)

atributos:   titulo, autor, arquivo, posicao_atual
operações:   avancar_pagina(), adicionar_marcador()
```

O conceito continua sendo um livro.

Mas a forma como o representamos depende do problema. Além disso, cada contexto também decide o que **ignorar**: a biblioteca não precisa do preço, a loja não precisa saber quantos exemplares estão emprestados, e o aplicativo não precisa do peso.

Isso acontece porque:

> Uma abstração não representa tudo o que existe sobre alguma coisa.

Ela representa aquilo que é relevante **para o problema atual**.

Podemos resumir:

```text
Mesmo conceito
      +
problemas diferentes
      ↓
abstrações diferentes
```



### 2.2 Abstrair envolve decisões

Na prática, nem sempre é óbvio quais conceitos devemos representar ou quais informações e comportamentos pertencem a cada um deles.

Voltemos ao livro da biblioteca. O atributo `exemplares` já esconde uma decisão importante.

Ao desenvolver esse sistema, podemos perguntar:

```text
Livro deve representar uma obra ou um exemplar físico?

Empréstimo deve ser uma classe?

Quem deve realizar um empréstimo:
Usuario, Exemplar ou Biblioteca?
```

Diferentes soluções podem ser adequadas para o mesmo problema.

Ao construir uma abstração, precisamos tomar decisões como:

```text
Quais conceitos precisamos representar?

Quais atributos pertencem a cada conceito?

Quais comportamentos pertencem a cada conceito?

Quais detalhes podemos ignorar?
```

Não existe necessariamente uma única abstração correta.

Uma abstração deve ser avaliada considerando os requisitos do sistema e o quanto ela ajuda a tornar o programa compreensível e fácil de modificar.

Além disso, conforme entendemos melhor o problema ou novos requisitos aparecem, nossas abstrações podem precisar mudar.



### 2.3 Um aviso sobre a palavra "abstração"

Em Orientação a Objetos, a palavra "abstração" também aparece em outro sentido: esconder detalhes de funcionamento atrás de uma interface simples, como acontece com as chamadas **classes abstratas**.

Nesta aula, usamos a palavra no sentido de **escolher o que representar**.

O outro sentido aparecerá mais adiante, quando estudarmos herança e polimorfismo.



## 3. Exemplo: uma batalha Pokémon

### 3.1 Definindo o problema

Vamos agora construir uma abstração juntos.

Imagine que queremos desenvolver um pequeno simulador de batalhas Pokémon.

Um Pokémon real, dentro dos jogos, possui muitas características:

```text
nome
nível
tipo
HP
ataque
defesa
ataque especial
defesa especial
velocidade
experiência
nature
habilidade
IV
EV
status
golpes
PP
...
```

Precisamos representar tudo isso?

Antes de responder, precisamos definir nosso problema.

Queremos construir inicialmente uma batalha bastante simplificada:

```text
- existem dois Pokémon;

- cada Pokémon possui pontos de vida;

- cada Pokémon possui alguns golpes;

- cada golpe possui um dano;

- um Pokémon pode atacar outro;

- a batalha termina quando a vida de um Pokémon chega a zero.
```

Agora podemos perguntar novamente:

> Quais informações realmente precisamos representar?

Uma possibilidade seria:

```text
Pokemon
├── nome
├── vida
└── golpes
```

E:

```text
Golpe
├── nome
└── dano
```

Observe tudo o que decidimos **não representar**:

```text
nível
tipo
experiência
nature
IV
EV
velocidade
PP
...
```

Essas características existem nos jogos.

Mas não são necessárias para o problema que estamos resolvendo.

Essa decisão faz parte da nossa abstração.



### 3.2 Comportamentos

Também precisamos decidir quais comportamentos são relevantes.

Um Pokémon pode:

```text
aprender_golpe()
receber_dano()
esta_vivo()
atacar()
```

Um golpe, inicialmente, pode apenas armazenar:

```text
nome
dano
```

Nossa abstração pode então ser representada aproximadamente como:

```text
Pokemon

atributos:
    nome
    vida
    golpes

comportamentos:
    aprender_golpe()
    receber_dano()
    esta_vivo()
    atacar()


Golpe

atributos:
    nome
    dano
```

Agora podemos transformar essa abstração em código.



### 3.3 Representando a abstração em classes

Começamos pelo golpe:

```python
class Golpe:

    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano
```

Depois, representamos um Pokémon:

```python
class Pokemon:

    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def aprender_golpe(self, golpe):
        self.golpes.append(golpe)

    def receber_dano(self, dano):
        self.vida -= dano

    def esta_vivo(self):
        return self.vida > 0
```

Observe a diferença entre dois métodos:

- `receber_dano()` **altera o estado** do objeto e não retorna nada;
- `esta_vivo()` apenas **consulta o estado** e retorna um resultado.

Podemos criar alguns objetos:

```python
choque = Golpe("Choque do Trovão", 20)
brasa = Golpe("Brasa", 15)

pikachu = Pokemon("Pikachu", 100)
charmander = Pokemon("Charmander", 100)

pikachu.aprender_golpe(choque)
charmander.aprender_golpe(brasa)
```

Agora podemos simular um ataque:

```python
charmander.receber_dano(choque.dano)

print(charmander.vida)
```

Saída:

```text
80
```

Ainda não temos uma batalha completa.

Mas já temos uma representação suficiente para começar a resolver nosso problema.



### 3.4 Atacando e batalhando

Falta implementar o comportamento `atacar()`.

Quem ataca é um Pokémon, mas o ataque afeta **outro** Pokémon. Esse padrão é parecido com o método `transferir(destino, valor)` do exercício das contas bancárias: dois objetos da mesma classe participam do mesmo método.

Adicionamos à classe `Pokemon`:

```python
    def atacar(self, alvo, golpe):
        print(f"{self.nome} usou {golpe.nome}!")
        alvo.receber_dano(golpe.dano)
        print(f"{alvo.nome} ficou com {alvo.vida} de vida.")
```

Nesse método, `self` é o Pokémon que ataca e `alvo` é o Pokémon que recebe o dano.

Agora podemos simular uma batalha completa. Vamos criar novos Pokémon, com a vida cheia:

```python
pikachu = Pokemon("Pikachu", 100)
charmander = Pokemon("Charmander", 100)

pikachu.aprender_golpe(choque)
charmander.aprender_golpe(brasa)

while pikachu.esta_vivo() and charmander.esta_vivo():
    pikachu.atacar(charmander, pikachu.golpes[0])

    if charmander.esta_vivo():
        charmander.atacar(pikachu, charmander.golpes[0])

if pikachu.esta_vivo():
    print(f"{pikachu.nome} venceu!")
else:
    print(f"{charmander.nome} venceu!")
```

Saída:

```text
Pikachu usou Choque do Trovão!
Charmander ficou com 80 de vida.
Charmander usou Brasa!
Pikachu ficou com 85 de vida.
Pikachu usou Choque do Trovão!
Charmander ficou com 60 de vida.
Charmander usou Brasa!
Pikachu ficou com 70 de vida.
Pikachu usou Choque do Trovão!
Charmander ficou com 40 de vida.
Charmander usou Brasa!
Pikachu ficou com 55 de vida.
Pikachu usou Choque do Trovão!
Charmander ficou com 20 de vida.
Charmander usou Brasa!
Pikachu ficou com 40 de vida.
Pikachu usou Choque do Trovão!
Charmander ficou com 0 de vida.
Pikachu venceu!
```

Observe que o laço `while` usa apenas `esta_vivo()`. Ele não precisa saber como a vida é representada: apenas pergunta ao Pokémon se ele ainda está vivo.

Nossa abstração, ainda que simples, já é suficiente para o problema que definimos.



## 4. A abstração pode mudar

### 4.1 Novos requisitos

Agora imagine que alteramos os requisitos.

Queremos que um golpe possa errar.

Precisamos representar uma nova informação:

```text
acurácia
```

Nossa abstração de `Golpe` muda:

```text
Golpe
├── nome
├── dano
└── acuracia
```

Poderíamos então ter:

```python
class Golpe:

    def __init__(self, nome, dano, acuracia):
        self.nome = nome
        self.dano = dano
        self.acuracia = acuracia
```

Note que essa mudança também afeta os lugares em que criamos golpes, pois agora é preciso informar a acurácia.

Agora imagine que queremos implementar vantagens de tipo:

```text
água > fogo
fogo > planta
planta > água
```

Talvez seja necessário adicionar:

```text
Pokemon
└── tipo

Golpe
└── tipo
```

Nossa abstração mudou novamente.

Isso não significa que a abstração anterior estava errada.

Ela era suficiente para o problema anterior.

Quando os requisitos mudam, a abstração também pode precisar mudar.



### 4.2 O que vem a seguir

Vamos continuar usando os Pokémon nas próximas aulas:

```text
vida       → como impedir que a vida assuma valores inválidos?
             (encapsulamento)

tipos      → como representar Pokémon de tipos diferentes?
             (herança e polimorfismo)
```



## 5. Exercícios

### 5.1 Escolhendo uma abstração

Queremos criar uma classe `Filme`.

Quais atributos e métodos ela deve possuir?

Antes de responder, considere três sistemas diferentes:

1. um serviço de streaming;
2. um sistema de venda de ingressos de cinema;
3. um catálogo pessoal de filmes assistidos.

Para cada caso:

- escolha os atributos relevantes;
- escolha possíveis métodos;
- identifique pelo menos duas informações que poderiam existir sobre um filme, mas que você decidiu não representar.

Compare as três soluções.

**Para pensar:**

1. Por que as classes podem ser diferentes mesmo representando o mesmo conceito?



### 5.2 Modelando uma biblioteca

Queremos desenvolver um sistema para uma biblioteca.

O sistema deve permitir:

- cadastrar livros disponíveis na biblioteca;
- manter mais de um exemplar do mesmo livro;
- cadastrar usuários;
- registrar o empréstimo de um exemplar para um usuário;
- registrar a devolução;
- consultar quais exemplares estão disponíveis.

**Atenção:** neste exercício, não escreva código. Apenas proponha uma possível modelagem. Discutiremos as soluções em uma aula futura, quando estudarmos as relações entre objetos.

Para cada conceito identificado, indique:

- quais seriam as classes;
- quais seriam seus principais atributos;
- quais seriam seus principais métodos.

**Para pensar:**

1. Existe alguma informação mencionada no problema que não precisa ser representada?
2. Alguma responsabilidade poderia ser atribuída a mais de uma classe?
3. Existe apenas uma maneira correta de modelar esse sistema?



### 5.3 Evoluindo a batalha Pokémon

Considere as classes `Golpe` e `Pokemon` desta aula, incluindo o método `atacar(alvo, golpe)`.

**Parte 1: Vida negativa**

Um Pokémon não pode ficar com vida negativa.

Teste o problema criando um golpe com dano `150` e atacando um Pokémon com vida `100`.

O que precisa mudar na nossa implementação?

**Parte 2: Será que resolvemos?**

Depois de corrigir o método `receber_dano()`, considere:

```python
pikachu.vida = -50
```

**Para pensar:**

1. Essa instrução é permitida?
2. O que impede alguém de colocar um Pokémon em um estado inválido fora da classe?
3. Que mudança na classe `Pokemon` seria necessária para impedir isso?

**Desafio extra:** adicione o atributo `acuracia` à classe `Golpe` (um valor entre 0 e 100) e faça com que `atacar()` possa errar. Dica: o módulo `random` possui a função `random.randint(1, 100)`.