# Funções como objetos

A ideia da aula de hoje é demonstrar a flexibilidade que Python (e outras linguagens modernas) dão às funções, mostrando como elas podem ser manipuladas como objetos, passadas como argumentos, retornadas por outras funções e ainda capturar estado com closures.

## 1. Relembrando ...

Até agora, vimos que funções são blocos de código reutilizaveis que:
* Recebem entradas (parâmetros)
* Fazem um processamento
* Retornam um ou mais valores de saída

```python
def function_name(     # Assinatura
    arg1: int,         # Entrada
    arg2: int          # Entrada
) -> int:
    res = arg1 + arg2  # Processamento
    return res         # Saída

x = 1
y = 2
print(function_name(x, y))
```

## 2. Funções como objetos

No entanto, em Python, tudo é objeto de primeira ordem!
Inclusive funções!

Isso significa que qualquer função pode:
1. Ser criada em tempo de execução;
2. Ser atribuída a uma variável ou elemento de uma estrutura de dados;
3. Ser passada como argumento para outra função;
4. Ser retornada como resultado de uma função.

> **Nota**: Qualquer objeto que **não** atenda essas propriedades não é um objeto de primeira classe.
> Exemplo: Vetores em C.

### 2.1 Exemplo

Para ilustrar, pense em um inteiro:
```python
def dobrar(n):
    res = n * 2
    return res    # 4. retorno

x = 1             # 1. criação em tempo de execução
y = x             # 2. atribuição a outra variável
print(dobrar(y))  # 3. uso como argumento
```

Aqui o número `1` é um objeto, e fizemos com ele todas as operações acima.

### 2.2 O caso das funções

Se funções são objetos, podemos fazer as mesmas manipulações a cima com elas:

#### Criação e atribuição

```python
def soma(a, b):
    return a + b

op = soma
print(op(1, 2))
```

#### Passagem por parâmetro

```python
def divisao(a, b):
    if b == 0:
        print("Divisão por zero")
        exit()
    return a / b

def executar(op, a, b):
    return op(a, b)

print(executar(soma, 2, 3))
print(executar(divisao, 2, 3))
```

#### Retorno da função

```python
def fabrica():  
    def saudacao():
        return "Olá, mundo!"
    return saudacao

func = fabrica()  
print(func())  # "Olá, mundo!"
```

### 2.3 Funções de alta ordem

Uma função de alta ordem é aquela que recebe outras funções como argumento ou retorna uma função como resultado.

> **Nota**: o que vimos acima (passar funções para executar ou retornar funções de fabrica) já é função de alta ordem. Aqui apenas damos o nome e foco formal ao conceito.


### 2.4 Motivação

Por que manipular funções como objetos é útil?

* **Reutilização de código**:\
    Podemos passar diferentes funções para um mesmo “processador”, evitando repetir código.
* **Criação dinâmica de funções**:\
    Podemos gerar funções sob medida em tempo de execução, sem precisar definir todas antecipadamente.
* **Abstrações poderosas**:\
    Habilita construções como `decoradores`, `map`, `filter`, `reduce` ou pipelines de processamento de dados.

### 2.5 Exemplos

#### Função customizada

```python
def saudacao_factory(prefixo):
    def saudacao(nome):
        return f"{prefixo}, {nome}!"
    return saudacao

ola = saudacao_factory("Olá")
bom_dia = saudacao_factory("Bom dia")

print(ola("Maria"))     # "Olá, Maria!"
print(bom_dia("João"))  # "Bom dia, João!"
```


#### Processamento genérico de listas

```python
def dobro(x):
    return x * 2

def soma_10(x):
    return x + 10

def aplicar_operacao(lista, func):
    resultado = []
    for x in lista:
        y = func(x)
        resultado.append(y)
    return resultado

numeros = [1, 2, 3, 4, 5]
print(aplicar_operacao(numeros, dobro))    # [2, 4, 6, 8, 10]
print(aplicar_operacao(numeros, soma_10))  # [11, 12, 13, 14, 15]
```

## 3. Lambdas: Funções anônimas

Além da forma de criar funções vistas até agora, Python também permite a criação de funções anônimas, chamadas `lambda`:

* São úteis apenas em casos muito simples, quando queremos passar uma função rapidamente;
* Não podem ser reutilizadas, porque não têm nome (a não ser que você atribua a uma variável, mas aí geralmente é melhor criar uma função normal);
* Em geral, prefira funções normais; use lambda só para casos triviais, como passar uma função para outra função de forma rápida.

### 3.1 Sintaxe

```python
# Sintaxe básica
# lambda argumentos: expressão

# Exemplo tradicional equivalente
def quadrado(x):
    return x ** 2

print(quadrado(4))           # 16
print((lambda x: x ** 2)(4)) # 16
```

> A diferença é que o lambda não tem nome, então você não pode chamá-lo de novo em outro lugar facilmente.

### 3.2 Exemplos

#### Processamento genérico de listas:

```python
def aplicar_funcao(lista, func):
    """Aplica a função passada em cada elemento da lista"""
    res = []
    for x in lista:
        y = func(x)
        resultado.append(y)
    return res

numeros = [1, 2, 3, 4, 5]

# Passando um lambda diretamente
resultado = aplicar_funcao(numeros, lambda x: x + 10)
print(resultado)  # [11, 12, 13, 14, 15]
```

> Aqui usamos lambda porque a operação é simples.
> Se fosse mais complexa, o ideal era criar uma função normal.

#### Ordenação

```python
pessoas = [
    ("Maria", 25),
    ("João", 30),
    ("Ana", 20)
]

# Ordena pela idade usando lambda
pessoas.sort(key=lambda x: x[1])
print(pessoas)  # [('Ana', 20), ('Maria', 25), ('João', 30)]
```

> É comum usar lambda com sort, max, min e funções como map ou filter, quando a função é muito simples e local.

### 3.3 Dicas

1. Lambda não deve substituir funções normais para operações complexas
2. Use lambda apenas quando:
    * a função é muito curta,
    * não será reutilizada em outro lugar
3. Para operações mais longas ou reutilizáveis, crie uma função normal

## 4. Exercícios

### 4.1 Ordenando alunos
Dada a lista de alunos com nome e nota:

```python
alunos = [
    { "nome": "Ana",    "nota": 8.5 },
    { "nome": "Bruno",  "nota": 7,2 },
    { "nome": "carla",  "nota": 9,1 },
    { "nome": "Daniel", "nota": 6.8 }
]
```

1. Ordene os alunos **pela nota** usando uma função normal (`def`) como chave no `sorted`.  
2. Repita a ordenação, mas agora usando uma `lambda`.  
3. Qual forma você considera mais clara?  

### 4.2 Formatação de moedas
Implemente uma função `formatar_moeda(valor, formatador)` que recebe um valor numérico e uma função de formatação.  

1. Crie funções normais que formatem em **real** (R$) e em **dólar** (US$), assumindo uma taxa de câmbio fixa (por exemplo, 1 dólar = 5 reais).  
2. Use também `lambda` para criar rapidamente uma função que formate em **euro** (€) multiplicando pelo câmbio.  
3. Teste passando diferentes funções para `formatar_moeda`.  

### 4.3 Pipeline de validação de senha
Crie um programa que verifique se uma senha é válida, aplicando várias funções de validação:  

1. Escreva três funções que verifiquem:  
   - Se a senha tem pelo menos 8 caracteres  
   - Se contém pelo menos um número  
   - Se contém pelo menos uma letra maiúscula  

2. Guarde essas funções em uma lista chamada `validacoes`.  
3. Escreva uma função `validar_senha(senha, validadores)` que percorra a lista e aplique todas as funções de validação.  
4. Teste com diferentes senhas.  
5. Extra: experimente substituir alguma dessas funções por uma `lambda` simples. 

