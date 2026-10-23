# Aula 25: Decoradores, `@property` e `@dataclass`

## 1. Motivação: código verboso × código pythonic

### 1.1 O problema: código verboso

Na aula anterior, protegemos a vida do Pokémon com um getter e um setter:

```python
class Pokemon:

    def __init__(self, nome, vida):
        self.nome = nome
        self.set_vida(vida)

    def get_vida(self):
        return self._vida

    def set_vida(self, valor):
        if valor < 0:
            raise ValueError("vida não pode ser negativa")
        self._vida = valor
```

Funciona, mas o uso é pesado:

```python
pikachu.set_vida(pikachu.get_vida() - 20)
```

Para reduzir a vida do Pokémon em 20, precisamos chamar dois métodos. Compare com o que escreveríamos se o atributo fosse público:

```python
pikachu.vida -= 20
```

Esse é um problema comum: para obter um comportamento simples (validar um valor), o código fica mais longo e mais difícil de ler.



### 1.2 O que o Python prioriza

Python dá muito valor a formas **simples** de obter o mesmo resultado. Dizemos que um código é **pythonic** quando ele segue esse espírito: é claro, direto e fácil de ler.

Isso está resumido no "Zen of Python" (que pode ser exibido com `import this`):

```text
Beautiful is better than ugly.        (Bonito é melhor que feio.)

Simple is better than complex.        (Simples é melhor que complexo.)

Readability counts.                   (Legibilidade importa.)
```

Alguns exemplos que já conhecemos:

```python
# Menos pythonic
for i in range(len(nomes)):
    print(nomes[i])

# Mais pythonic
for nome in nomes:
    print(nome)
```

Nos dois casos, o resultado é o mesmo, mas a segunda versão é mais curta e mais próxima da ideia que queremos expressar.

Então, será que existe uma forma pythonic de escrever o nosso Pokémon? Queremos escrever `pikachu.vida -= 20` e, ainda assim, manter a validação por trás.

Existe, e ela usa:

```python
@property
@vida.setter
```

Essas construções são **decoradores**.



### 1.3 Por onde começar

Para entender o que são decoradores (em vez de apenas copiar o `@property` sem saber o que ele faz), precisamos primeiro voltar a falar de **funções como objetos** e de **closures**.



## 2. Revisando: funções como objetos e closures

### 2.1 Funções são objetos

Em Python, uma função é um objeto como qualquer outro. Podemos guardá-la em uma variável, colocá-la em uma lista, passá-la como argumento e devolvê-la como resultado.

Vamos usar como exemplo a **validação de senhas**. Cada regra é uma função:

```python
def tem_tamanho_minimo(senha):
    return len(senha) >= 8

def tem_digito(senha):
    return any(c.isdigit() for c in senha)

def tem_maiuscula(senha):
    return any(c.isupper() for c in senha)
```

E podemos criar uma função que **recebe as regras como argumento**:

```python
def verificar_senha(senha, regras):
    falhas = []
    for regra in regras:
        if not regra(senha):
            falhas.append(regra.__name__)
    return falhas
```

Usando:

```python
regras = [tem_tamanho_minimo, tem_digito, tem_maiuscula]

print(verificar_senha("abc", regras))
print(verificar_senha("abcdefgh", regras))
print(verificar_senha("Abcdefg1", regras))
```

Saída:

```text
['tem_tamanho_minimo', 'tem_digito', 'tem_maiuscula']
['tem_digito', 'tem_maiuscula']
[]
```

Observe dois pontos:

- as funções aparecem na lista **sem parênteses**: estamos passando o próprio objeto função, e não o resultado de chamá-la;
- podemos mudar as regras de validação sem modificar `verificar_senha`. Basta passar outra lista.

Esse padrão (funções que recebem funções) é a base dos decoradores.



### 2.2 Closures

Uma função também pode ser **criada dentro de outra**. A função interna **enxerga** as variáveis da função externa (isso tem a ver com o conceito de **escopo**):

```python
def externa():
    mensagem = "oi"

    def interna():
        print(mensagem)

    interna()

externa()
```

Saída:

```text
oi
```

A função `interna` não possui nenhuma variável `mensagem`, mas consegue usar a da função que a envolve.

Agora vem a parte interessante. Uma função pode **devolver** a função interna, e ela continua lembrando das variáveis do lugar onde foi criada, mesmo depois que a função externa terminou. Isso é uma **closure**.

Exemplo: uma regra de tamanho de senha configurável.

```python
def criar_regra_tamanho(minimo):

    def tem_tamanho(senha):
        return len(senha) >= minimo

    return tem_tamanho
```

Usando:

```python
regra_8 = criar_regra_tamanho(8)
regra_12 = criar_regra_tamanho(12)

print(regra_8("abc12345"))
print(regra_12("abc12345"))
```

Saída:

```text
True
False
```

Quando `criar_regra_tamanho(8)` terminou, a variável `minimo` deveria ter desaparecido. Mas a função devolvida **lembra** do valor `8`, e a outra lembra do `12`.

```text
criar_regra_tamanho(minimo)
│
├── define tem_tamanho(senha)    ← usa minimo, que está "fora" dela
│
└── devolve tem_tamanho          ← devolve uma função
```

Uma função que **recebe** ou **devolve** outras funções é chamada de **função de ordem superior**. Os decoradores usam exatamente essa estrutura.



## 3. `*args` e `**kwargs`

Algumas funções precisam aceitar **qualquer quantidade** de argumentos:

```python
def mostrar(*args, **kwargs):
    print(args)
    print(kwargs)


mostrar(1, 2, nome="Ana", idade=20)
```

Saída:

```text
(1, 2)
{'nome': 'Ana', 'idade': 20}
```

Então:

```text
*args      →  tupla com os argumentos posicionais

**kwargs   →  dicionário com os argumentos nomeados
```

O mesmo símbolo funciona no sentido contrário, na **chamada** de uma função:

```python
def somar(a, b):
    return a + b


print(somar(*(2, 3)))
print(somar(**{"a": 2, "b": 3}))
```

Saída:

```text
5
5
```

```text
somar(*(2, 3))                  →  somar(2, 3)

somar(**{"a": 2, "b": 3})       →  somar(a=2, b=3)
```

**Por que isso importa para decoradores?**

Um decorador precisa "embrulhar" funções **sem saber** quais argumentos elas recebem. Com `*args` e `**kwargs`, o embrulho captura tudo o que receber e repassa para a função original:

```python
def embrulho(*args, **kwargs):
    return funcao_original(*args, **kwargs)
```



## 4. Decoradores

### 4.1 O que é um decorador?

> Um **decorador** é um mecanismo para **adicionar uma nova funcionalidade em cima de outra função** (ou classe), **sem modificar o código original**.

Podemos pensar em um embrulho: a função original continua existindo, mas passa a ser "vestida" com um comportamento extra.

```text
          ┌──────────────────────────┐
          │   comportamento extra    │   ← o decorador
          │  ┌────────────────────┐  │
 chamada →│  │  função original   │  │→ resultado
          │  └────────────────────┘  │
          └──────────────────────────┘
```

Tecnicamente, um decorador é uma **função que recebe uma função e devolve outra função**.



### 4.2 Um decorador feito à mão: o logger

Imagine que queremos registrar toda vez que uma função for chamada. Em vez de alterar cada função, criamos um decorador:

```python
def logar(func):

    def wrapper(*args, **kwargs):
        print(f"chamando {func.__name__}")
        return func(*args, **kwargs)

    return wrapper
```

Observe os ingredientes que acabamos de revisar:

```text
logar(func)
│
├── recebe uma função                     (funções são objetos)
├── define wrapper, que usa func          (closure)
├── wrapper aceita *args e **kwargs       (repassa tudo)
└── devolve wrapper
```

Usando:

```python
def somar(a, b):
    return a + b


somar_com_log = logar(somar)

print(somar_com_log(2, 3))
```

Saída:

```text
chamando somar
5
```

A função original `somar` não foi modificada. Criamos uma **versão decorada** dela.



### 4.3 A sintaxe `@`

Python oferece um atalho para esse padrão:

```python
@logar
def saudar(nome, formal=False):
    if formal:
        return f"Prezado {nome}"
    return f"Oi, {nome}"
```

Isso é exatamente equivalente a:

```python
def saudar(nome, formal=False):
    ...


saudar = logar(saudar)
```

Ou seja:

```text
@decorador
def f(): ...

        ≡

f = decorador(f)
```

Agora, ao chamar `saudar`, estamos chamando o `wrapper`:

```python
print(saudar("Ana", formal=True))
```

Saída:

```text
chamando saudar
Prezado Ana
```

O argumento nomeado `formal=True` passou normalmente pelo `wrapper`: é o `**kwargs` trabalhando.

Um decorador, portanto, **não é mágica**: é apenas uma função aplicada a outra função, com uma sintaxe mais curta.

**Um detalhe:** a função decorada "perde" o nome original (`saudar.__name__` passa a ser `"wrapper"`). Para evitar isso, a biblioteca padrão oferece o decorador `functools.wraps`, usado dentro do nosso decorador:

```python
import functools


def logar(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"chamando {func.__name__}")
        return func(*args, **kwargs)

    return wrapper
```

Por enquanto, basta saber que ele existe e que é boa prática usá-lo.



### 4.4 Outro exemplo: o timer

Outro decorador muito comum mede quanto tempo uma função demora:

```python
import time


def medir_tempo(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()
        print(f"{func.__name__} demorou {fim - inicio:.4f} s")
        return resultado

    return wrapper
```

Usando:

```python
@medir_tempo
def somar_ate(n):
    return sum(range(n))


print(somar_ate(1_000_000))
```

Saída (o tempo varia a cada execução):

```text
somar_ate demorou 0.0127 s
499999500000
```

Observe que o `wrapper` **devolve o resultado** da função original. Se esquecêssemos o `return`, a função decorada passaria a devolver `None`.

A função `somar_ate` não sabe nada sobre medição de tempo. Todo o comportamento foi adicionado "por cima".



### 4.5 Outros decoradores

Existem muitos outros decoradores desse tipo. Todos seguem a mesma estrutura: executam algo **antes e/ou depois** da função original. Alguns exemplos comuns:

```text
contador de chamadas   →  quantas vezes a função foi chamada?

retry                  →  se a função falhar, tentar de novo

cache                  →  guardar resultados já calculados

controle de acesso     →  só executa se o usuário tem permissão
```

Há também decoradores que recebem **configurações**, como `@tentar_novamente(tentativas=5)`. Eles exigem um nível a mais de função, e não vamos desenvolvê-los agora. Apenas saiba que existem.

Na biblioteca padrão e em classes, você também vai encontrar decoradores como `@staticmethod` e `@classmethod`. Não precisamos deles agora.



## 5. `@property`

### 5.1 Lendo um valor como se fosse um atributo

O decorador `@property` transforma um **método** em algo que se **acessa como atributo**:

```python
class Pokemon:

    def __init__(self, nome, vida):
        self.nome = nome
        self._vida = vida

    @property
    def vida(self):
        return self._vida
```

Usando:

```python
pikachu = Pokemon("Pikachu", 100)

print(pikachu.vida)
```

Saída:

```text
100
```

Observe que escrevemos `pikachu.vida`, **sem parênteses**. Quem usa a classe não precisa saber que existe um método por trás.

Sem um setter, a propriedade é **somente leitura**:

```python
pikachu.vida = 50
```

produz:

```text
AttributeError: property 'vida' of 'Pokemon' object has no setter
```



### 5.2 Escrevendo com validação: o setter

Para permitir a escrita com validação, usamos `@vida.setter`:

```python
class Pokemon:

    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        if valor < 0:
            raise ValueError("vida não pode ser negativa")
        self._vida = valor
```

Agora:

```python
pikachu = Pokemon("Pikachu", 100)

pikachu.vida -= 20

print(pikachu.vida)
```

Saída:

```text
80
```

E os valores inválidos são rejeitados:

```python
pikachu.vida = -5
```

produz:

```text
ValueError: vida não pode ser negativa
```

Resolvemos o problema do início da aula: a sintaxe é a de um atributo comum (`pikachu.vida -= 20`), mas todo acesso passa pelo código de validação.

Observe que, no `__init__`, escrevemos `self.vida = vida` (e não `self._vida = vida`). Assim, a validação também é aplicada na criação do objeto:

```python
Pokemon("Pikachu", -10)
```

produz:

```text
ValueError: vida não pode ser negativa
```

Os dados continuam guardados em `_vida`. A propriedade `vida` é apenas uma **porta de entrada** para ele:

```text
pikachu.vida          →  método com @property    →  devolve _vida

pikachu.vida = 80     →  método com @vida.setter →  valida e guarda em _vida
```



### 5.3 Valores calculados

Uma propriedade também pode **calcular** um valor sob demanda, sem guardá-lo. Lembre-se do `Carrinho`:

```python
class Carrinho:

    def __init__(self):
        self.produtos = []

    def adicionar(self, produto):
        self.produtos.append(produto)

    @property
    def total(self):
        return sum(produto.preco for produto in self.produtos)
```

Usando:

```python
print(carrinho.total)
```

Como o total é calculado a cada acesso, ele nunca fica **desatualizado**: se o preço de um produto mudar, `carrinho.total` já reflete a mudança.



### 5.4 Quando usar `@property`

Como `pikachu.vida` pode ser um atributo simples **ou** uma propriedade, e quem usa a classe escreve a mesma coisa nos dois casos, podemos:

```text
1. Começar com um atributo público simples:

       self.vida = vida

2. Mais tarde, se surgir uma regra de validação,
   transformar em @property

   O código que usava pikachu.vida continua funcionando.
```

Por isso, em Python, **não escrevemos getters e setters "por precaução"**. Só criamos propriedades quando existe um motivo: uma validação, ou um valor calculado a partir de outros dados. Isso é, de novo, o espírito pythonic: simples até que a complexidade seja necessária.



## 6. `@dataclass`

### 6.1 Classes que só guardam dados

Observe uma classe simples, que representa apenas um conjunto de dados:

```python
class Golpe:

    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano

    def __repr__(self):
        return f"Golpe(nome={self.nome!r}, dano={self.dano!r})"

    def __eq__(self, outro):
        return self.nome == outro.nome and self.dano == outro.dano
```

Quase todo esse código é **repetitivo**:

```text
__init__   →  repete cada atributo três vezes

__repr__   →  texto que mostra o objeto com todos os seus campos

__eq__     →  compara todos os campos
```

Testando:

```python
g1 = Golpe("Choque do Trovão", 20)
g2 = Golpe("Choque do Trovão", 20)

print(g1)
print(g1 == g2)
print(g1 is g2)
```

Saída:

```text
Golpe(nome='Choque do Trovão', dano=20)
True
False
```

Este é um caso clássico para um decorador, mas desta vez **de classe**: ele recebe uma classe e devolve a classe com métodos adicionados automaticamente.



### 6.2 O que o `@dataclass` gera

```python
from dataclasses import dataclass


@dataclass
class Golpe:
    nome: str
    dano: int
```

Aqui aparece uma sintaxe nova: `nome: str`. Isso é uma **anotação de tipo**. Ela indica **qual tipo de valor esperamos** naquele campo (`nome` deveria ser um texto, `dano` um inteiro).

Dois pontos importantes sobre as anotações:

- o Python **não verifica** o tipo em tempo de execução: elas servem como documentação (e para ferramentas e editores de código que avisam sobre inconsistências);
- o `@dataclass` as usa para **descobrir quais são os campos** da classe, e em que ordem.

A partir dos campos declarados, o decorador **escreve por nós** os métodos especiais `__init__`, `__repr__` e `__eq__`:

```python
g1 = Golpe("Choque do Trovão", 20)
g2 = Golpe("Choque do Trovão", 20)

print(g1)
print(g1 == g2)
print(g1 is g2)
```

Saída:

```text
Golpe(nome='Choque do Trovão', dano=20)
True
False
```

O resultado é exatamente o mesmo da versão escrita à mão, com muito menos código.

Isso responde a duas perguntas que apareceram antes:

```text
Dois golpes com o mesmo nome e dano devem ser iguais?
→ Com @dataclass, sim: __eq__ compara todos os campos.

Como imprimir um objeto de forma legível?
→ O __repr__ gerado mostra todos os campos.
```



### 6.3 Objetos imutáveis com `frozen=True`

Na Aula 23, discutimos a ideia de objetos **imutáveis**. O `@dataclass` oferece uma forma direta de criá-los:

```python
@dataclass(frozen=True)
class Golpe:
    nome: str
    dano: int
```

Agora, tentar modificar um campo gera um erro:

```python
choque = Golpe("Choque", 20)

choque.dano = 50
```

produz:

```text
FrozenInstanceError: cannot assign to field 'dano'
```

Diferentemente da convenção `_atributo`, aqui o Python **impõe** a imutabilidade.

Para "alterar" um objeto imutável, criamos **um novo** com os valores desejados, como fazemos com strings:

```python
choque_forte = Golpe(choque.nome, 50)
```

Um objeto imutável também pode ser usado como **chave de um dicionário**, o que é útil em vários casos.



### 6.4 O que fica para depois

O `@dataclass` tem outras funcionalidades (valores padrão, validação na criação do objeto, comparação com `<` e `>`, entre outras). Não vamos estudá-las agora. O importante é entender o que o decorador **resolve**: ele escreve por nós o código repetitivo de classes que guardam dados.

```text
Use @dataclass quando a classe é, principalmente, um conjunto de dados:

    Golpe, Produto, Mensagem

Prefira uma classe comum quando o comportamento e a validação
são o centro da classe:

    Pokemon com regras de vida
```



## 7. Exercícios

### 7.1 Contando chamadas

Escreva um decorador `contar_chamadas` que guarde, **na própria função decorada**, quantas vezes ela foi chamada.

Exemplo:

```python
@contar_chamadas
def saudar(nome):
    print(f"Olá, {nome}!")


saudar("Ana")
saudar("Bruno")

print(saudar.chamadas)
```

Saída esperada:

```text
Olá, Ana!
Olá, Bruno!
2
```

Dica: funções são objetos, então podem ter atributos.

**Para pensar:**

1. Por que o decorador precisa usar `*args` e `**kwargs`?
2. O que aconteceria se o `wrapper` não devolvesse o resultado da função original?



### 7.2 Produto com propriedade

Reescreva a classe `Produto` usando `@property`:

- `preco` deve rejeitar valores negativos, inclusive na criação do objeto;
- `preco_final` deve ser uma propriedade **somente leitura**, calculada a partir de `preco` e de um atributo `desconto` (em porcentagem).

Teste:

```python
p = Produto("Notebook", 5000, 10)

print(p.preco_final)

p.preco_final = 100
```

**Para pensar:**

1. Qual erro aparece na última linha? Por quê?
2. Se `desconto` mudar depois, o `preco_final` muda? Por quê?



### 7.3 Golpes e produtos como dataclasses

Transforme `Golpe` (nome, dano) e `Produto` (nome, preço) em dataclasses.

Depois:

1. Crie dois golpes iguais e verifique `==` e `is`.
2. Torne `Golpe` imutável e tente modificar o dano.
3. Use um golpe como chave de um dicionário.

**Para pensar:**

1. Por que `Golpe` pode ser imutável, mas `Pokemon` (com a vida que muda a cada ataque) provavelmente não?