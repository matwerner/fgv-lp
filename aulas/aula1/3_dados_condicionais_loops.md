# Aula Introdutória de Python

Nesta aula, vamos relembrar os tipos básicos de dados do Python, assim como as instruções de controle de fluxo, 
condicionais e laços de repetição.

## Funções (Caso do Print)

Funções em Python são blocos de código reutilizáveis que realizam tarefas específicas.
Um exemplo comum é a função print(), que exibe texto na tela.

Exemplo:

python
```python
print("Olá, mundo!")
```

Existem diversas outras funções built-in no python, como 
```input```,
```type```,
```int```,
```float```,
```str```.

### Tipos de dados básico

### Constantes Numéricas e Textuais

Em Python, você pode trabalhar com constantes:
1. Numéricas (como inteiros e floats);
2. Textuais (strings). 

Elas são valores fixos que não podem ser alterados durante a execução do programa.

Exemplos:

```python
numero = 10
texto = "Python é incrível!"
```

### Nomes de Variáveis

As variáveis em Python devem seguir algumas regras:

    Podem começar com letra ou underscore (_)
    Podem conter letras, números e underscores
    São sensíveis a maiúsculas e minúsculas

Algumas dicas:
1. Seja Descritivo;
2. Seja Conciso;
3. Mantenha a Consistência.

#### Exemplos de convenções de nomenclatura: camelCase e snake_case.

**camelCase**: Capitalize cada palavra, exceto a primeira, sem espaços entre elas.
```python
nomeDoUsuario = "abcde"
contagemDeItens = 10
```

**snake_case**: Use minúsculas e underscores (_) para separar palavras.
```python
nome_do_usuario = "abcde"
contagem_de_itens = 10
```

### Operadores

Python suporta vários tipos de operadores, como divisão, subtração, adição, etc.

| Operador | Descrição       | Exemplo     |
|----------|-----------------|-------------|
| +        | Adição          | `5 + 3`     |
| -        | Subtração       | `5 - 3`     |
| *        | Multiplicação   | `5 * 3`     |
| /        | Divisão         | `5 / 3`     |
| %        | Módulo          | `5 % 3`     |
| **       | Exponenciação   | `5 ** 3`    |
| //       | Divisão Inteira | `5 // 3`    |

### Como Linhas de Código São Processadas

As linhas de código em Python são processadas em uma ordem específica, levando em consideração variáveis, constantes, operadores e funções. Por exemplo, na declaração:

```python
x = 3.9 * x * (1 + x)
```

### Ordem de Avaliação

A ordem de avaliação das expressões em Python segue a regra PEMDAS:
1. Parenteses;
2. Exponenciação;
3. Multiplicação/Divisão;
4. Adição/Subtração.

Em casos ambiguos, a expressão é processada da esquerda para direita.

```python
x = 2 ** 10 * 2 + 3 / 4
```

### Tipos de Variáveis e Operações

Python possui vários tipos de variáveis, como:
* inteiros,
* floats,
* strings,
* boleanos,
* etc.

Cada tipo de variável suporta diferentes operações.

### Conversão de Variáveis

#### Implicita

Às vezes, Python converte automaticamente um tipo de variável em outro, por exemplo, ao realizar operações entre diferentes tipos.

```python
a = True
b = 2
c = 3.9

print(a + b)
print(a + c)
print(b + c)
```

#### Explícita

Você também pode converter explicitamente tipos de variáveis usando funções como int(), float(), str(), etc.

```python
a = True
a = int(a)
print(a)
```

#### Conversão de Valores Passados pelo Usuário

Ao receber entrada do usuário, é importante converter os valores para o tipo correto, caso necessário.

```python
x = input("Insira um número")
x = int(x)
print(x)
```

## Condicionais

As condicionais são operações que nos permitem controlar o fluxo de execução do código com base em condições específicas.
Dependendo das condições definidas, diferentes trechos de códigos serão executados.

### Sintaxe e estrutura

Os condicionais são definidos pelas palavras-chave 
```if```, 
```elif``` (abreviação de "else if") e ```else```.
A estrutura básica dos condicionais é a seguinte:

```python
if condição:
    # bloco de código se a condição for verdadeira
elif outra_condição:
    # bloco de código se a outra condição for verdadeira
else:
    # bloco de código se nenhuma das condições anteriores for verdadeira
```

### Exemplo
Exemplo de avaliação de condições:

```python
x = 10
if x > 5 and x < 15:
    print("x está entre 5 e 15")
elif x <= 5 or x >= 15:
    print("x está fora do intervalo de 5 a 15")
```

### Operações de Comparação

Python suporta as seguintes operações de comparação:

| Operador | Descrição                  | Exemplo           |
|----------|----------------------------|-------------------|
| ==       | Igual a                    | `a == b`          |
| !=       | Diferente de               | `a != b`          |
| <        | Menor que                  | `a < b`           |
| >        | Maior que                  | `a > b`           |
| <=       | Menor ou igual a           | `a <= b`          |
| >=       | Maior ou igual a           | `a >= b`          |

### Operadores lógicos

Enquanto suporta os seguintes operados lógicos:

| Operador | Descrição                                              | Exemplo                                  |
|----------|--------------------------------------------------------|------------------------------------------|
| and      | Retorna True se ambos os operandos forem True         | `True and True`                          |
| or       | Retorna True se pelo menos um dos operandos for True   | `True or False`                          |
| not      | Retorna True se o operando for False e False se o operando for True | `not False`                     |

onde esse são todos os possiveis resultados de cada operação\
(Lembrar que True = 1 e False = 0)

**AND**

| A     | B     | A and B |
|-------|-------|---------|
| 0     | 0     | 0       |
| 0     | 1     | 0       |
| 1     | 0     | 0       |
| 1     | 1     | 1       |

**OR**

| A     | B     | A or B |
|-------|-------|--------|
| 0     | 0     | 0      |
| 0     | 1     | 1      |
| 1     | 0     | 1      |
| 1     | 1     | 1      |

**NOT**

| A     | not A |
|-------|-------|
| 0     | 1     |
| 1     | 0     |

### Ordem de Avaliação

Dado a condicional abaixo, qual mensagem será exibida na tela?

```python
x = 25
if x > 20 or x > 10 and x < 15:
    print("Opção A")
else:
    print("Opção B")
```

Similar ao que vimos com as operações matemáticas, operadores lógicos tambem
seguem uma ordem de avaliação:
1. Not
2. And
3. Or

## Loops

Loops são estruturas de controle de fluxo em programação que permitem
repetir  a execução de um mesmo bloco de código enquanto 
uma condição específica é verdadeira ou para um número específico de vezes.

### Sintaxe e estrutura

#### While

O loop ```while``` é usado para executar um bloco de código repetidamente enquanto uma condição especificada for verdadeira.

```python
# Sintaxe do loop while
while condição:
    # bloco de código a ser repetido enquanto a condição for verdadeira
```

```python
# Exemplo de loop while para imprimir os números de 1 a 5
i = 1
while i <= 5:
    print(i)
    i += 1
```

Obs: Python não possui um loop ```until``` como vimos em bash.
Contudo, o mesmo efeito pode ser obtido em python simplesmente negando a condição do ```while```.

#### For

Já loop ```for``` é usado para iterar sobre uma sequência de elementos, 
como uma ```lista```, ```tupla```, ```dicionário``` ou ```intervalo numérico```.
Estruturas de dados que veremos detalhadamente mais para frente.

```python
# Sintaxe do loop for
for elemento in sequencia:
    # bloco de código a ser repetido para cada elemento na sequência
```

```python
# Exemplo de loop for para iterar sobre uma lista de cores
cores = ["vermelho", "verde", "azul"]
for cor in cores:
    print(cor)
```

#### Função Range

No caso do ```intervalo numérico```, a função ```range``` é comumente usada.
Ela permite gerar uma sequência de números em um intervalo específico e é utilizada
em loops for para especificar a quantidade de iterações.

```python
# Sintaxe da função range
range(início, fim, passo)
```

```python
# Exemplo de uso da função range em um loop for
for i in range(1, 6):
    print(i)  # Imprime os números de 1 a 5
```

### Interrompendo o fluxo

Dentro de loops, podemos adicionar as declarações ```break``` e ```continue```
para interromper a execução natural de um bloco de código dentro do loop.

#### Break

A declaração break é usada para interromper a execução de um loop antes que ele seja concluído, com base em uma condição específica.
Quando o Python encontra a declaração break, ele sai imediatamente do loop e continua a execução do código após o loop.

```python
for n in range(1, 6):
    if n == 3:
        break
    print(n)
print("Fim!")
```

#### Continue

A declaração continue é usada para pular para a próxima iteração do loop, ignorando o restante do código dentro do bloco do loop.
Quando o Python encontra a declaração continue, ele volta para o início do loop e continua com a próxima iteração.

```python
for n in range(1,6):
    if numero % 2 == 0:
        continue
    print(n)
```

## Exercícios

1. Crie um programa que solicita ao usuário uma nota de 0 a 100 e converte essa nota para uma classificação em letras.
As classificações são:
    A: 80 a 100
    B: 65 a 79
    C: 40 a 64
    D: 30 a 39
    F: 0 a 29

2. Crie um programa que recebe um número inteiro positivo $n$ e imprime todos os números pares de 1 até n.

3. Altere o c;odigo do exercicio acima de forma que o mesmo também conte quantos números pares foram encontrados
e imprima essa contagem no final.
