# Aula 16: Funções como Objetos

## 1. Relembrando Funções

Até agora, utilizamos funções principalmente como blocos reutilizáveis de código.

Uma função pode:

1. receber valores de entrada;
2. executar algum processamento;
3. retornar um ou mais valores.

Por exemplo:

```python
def soma(a: int, b: int) -> int:
    resultado = a + b
    return resultado


x = 1
y = 2

print(soma(x, y))
```

Normalmente, utilizamos uma função através de sua chamada:

```python
soma(1, 2)
```

Entretanto, em Python, uma função também pode ser manipulada como um valor.



## 2. Funções Também São Objetos

Já vimos vários exemplos de objetos em Python:

```python
idade = 20
nome = "Ana"
notas = [8.0, 9.0, 7.5]
```

Podemos fazer várias operações com esses valores.

Por exemplo, podemos atribuí-los a outras variáveis:

```python
x = 10
y = x
```

armazená-los em estruturas:

```python
valores = [10, 20, 30]
```

passá-los como argumentos:

```python
print(x)
```

e retorná-los de funções:

```python
def obter_valor():
    return x
```

Em Python, funções também são objetos.

Considere:

```python
def soma(a, b):
    return a + b
```

Podemos verificar:

```python
print(type(soma))
```

obtendo:

```text
<class 'function'>
```

Ao executar uma declaração `def`, Python cria um objeto que representa aquela função e associa esse objeto a um nome.

Podemos pensar conceitualmente em:

```text
soma
  ↓
[objeto função]
```

### 2.1. Referência à Função e Chamada da Função

Existe uma diferença importante entre:

```python
soma
```

e:

```python
soma(2, 3)
```

No primeiro caso, estamos nos referindo ao objeto função.

No segundo, estamos executando a função.

Por exemplo:

```python
def soma(a, b):
    return a + b


operacao = soma
resultado = soma(2, 3)
```

Temos:

```text
operacao
    ↓
objeto função soma


resultado
    ↓
5
```

Podemos então fazer:

```python
print(operacao(10, 20))
```

obtendo:

```text
30
```

Observe:

```python
operacao = soma
```

não executa `soma()`.

Estamos apenas fazendo `operacao` referenciar a mesma função.

### 2.2. Objetos Chamáveis

Em Python, alguns objetos podem ser utilizados com a sintaxe:

```python
objeto(...)
```

Esses objetos são chamados de **chamáveis** (*callable*).

Funções são objetos chamáveis. Podemos verificar isso com:

```python
def soma(a, b):
    return a + b


operacao = soma
resultado = soma(2, 3)

print(callable(soma))       # True
print(callable(operacao))   # True
print(callable(resultado))  # False
```

`callable(objeto)` retorna `True` quando o objeto pode ser chamado utilizando `()`.

### 2.3. Objetos de Primeira Classe

Python trata funções como **objetos de primeira classe** (*first-class objects*).

Isso significa que podemos manipulá-las de forma semelhante a outros valores.

Uma função pode, por exemplo:

1. ser atribuída a uma variável;
2. ser armazenada em uma estrutura de dados;
3. ser passada como argumento para outra função;
4. ser retornada por outra função.

### 2.4. Funções Também Possuem Atributos

Como funções são objetos, elas também possuem informações associadas a elas.

Considere:

```python
def soma(a, b):
    """Retorna a soma de dois valores."""
    return a + b
```

Podemos consultar:

```python
print(soma.__name__)
print(soma.__doc__)
```

obtendo:

```text
soma
Retorna a soma de dois valores.
```

Assim como outros objetos possuem atributos e operações, objetos função também possuem características próprias.

Nesta aula, entretanto, nosso interesse principal está em **como podemos atribuir, armazenar, passar e retornar funções**.



## 3. O que Podemos Fazer com Funções?

### 3.1. Atribuir uma Função a uma Variável

Considere:

```python
def soma(a, b):
    return a + b


operacao = soma

print(operacao(2, 3))
```

A variável `operacao` referencia a função `soma`.

Podemos alterar qual função ela referencia:

```python
def multiplicacao(a, b):
    return a * b


operacao = multiplicacao

print(operacao(2, 3))
```

Agora o resultado é:

```text
6
```

### 3.2. Armazenar Funções em Estruturas de Dados

Funções também podem ser elementos de uma lista:

```python
def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


operacoes = [
    soma,
    subtracao,
    multiplicacao
]
```

Podemos percorrer essa lista:

```python
for operacao in operacoes:
    print(operacao(10, 2))
```

Também podemos armazenar funções em um dicionário:

```python
operacoes = {
    "soma": soma,
    "subtracao": subtracao,
    "multiplicacao": multiplicacao
}
```

Agora podemos escolher uma operação utilizando uma string:

```python
nome = "multiplicacao"

operacao = operacoes[nome]

resultado = operacao(10, 2)

print(resultado)
```

Esse tipo de construção permite escolher dinamicamente qual comportamento será utilizado.

### 3.3. Passar uma Função como Argumento

Também podemos passar uma função para outra função.

Considere:

```python
def executar(operacao, a, b):
    return operacao(a, b)
```

Podemos utilizar:

```python
print(executar(soma, 2, 3))
print(executar(multiplicacao, 2, 3))
```

Observe novamente que passamos:

```python
soma
```

e não:

```python
soma()
```

Estamos fornecendo a própria função para `executar()`.

### 3.4. Retornar uma Função

Uma função também pode retornar outra função.

Considere:

```python
def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    return a / b
```

Podemos criar uma função que escolha uma dessas operações:

```python
def obter_operacao(nome):
    if nome == "soma":
        return soma

    if nome == "subtracao":
        return subtracao

    if nome == "multiplicacao":
        return multiplicacao

    if nome == "divisao":
        return divisao

    raise ValueError("Operação desconhecida.")
```

Agora:

```python
operacao = obter_operacao("multiplicacao")
```

Nesse momento, `operacao` referencia uma função.

Somente depois:

```python
resultado = operacao(3, 4)

print(resultado)
```

executamos a função escolhida.

A chamada:

```python
obter_operacao("multiplicacao")
```

não retorna o resultado da multiplicação.

Ela retorna a própria função:

```python
multiplicacao
```

### 3.5. Funções de Ordem Superior

Podemos agora dar um nome para algumas das construções anteriores.

Uma **função de ordem superior** é uma função que:

1. recebe outra função como argumento; ou
2. retorna uma função.

Por exemplo:

```python
def executar(operacao, a, b):
    return operacao(a, b)
```

é uma função de ordem superior porque recebe `operacao`.

Da mesma forma:

```python
def obter_operacao(nome):
    ...
```

é uma função de ordem superior porque retorna uma função.



## 4. Por que Manipular Funções Dessa Forma?

Até agora vimos que é possível atribuir, armazenar, passar e retornar funções.

Mas por que isso seria útil?

Uma das principais vantagens é permitir separar:

```text
estrutura geral do algoritmo
```

de:

```text
comportamento específico
```

A mesma estrutura pode ser utilizada com diferentes comportamentos.

Isso também pode ajudar na **modularização**.

Em vez de colocar todas as regras dentro de uma grande função, diferentes comportamentos podem ser implementados separadamente e fornecidos quando necessário.

Outra vantagem é facilitar a comparação entre abordagens.

Por exemplo, em vez de escrever:

```python
# distancia = distancia_euclidiana(a, b)

distancia = distancia_manhattan(a, b)
```

e ficar alterando ou comentando partes do código, podemos escolher uma função dinamicamente.

Isso também facilita os testes, pois cada comportamento pode ser implementado e testado separadamente.



### 4.1. Exemplo: Leitura com Diferentes Validações

Considere um programa que precisa ler valores do usuário até receber uma entrada válida.

Poderíamos escrever funções diferentes:

```text
ler_idade()
ler_nota()
ler_percentual()
...
```

Entretanto, boa parte da lógica seria repetida:

```text
ler entrada
    ↓
verificar entrada
    ↓
se inválida, mostrar mensagem
    ↓
tentar novamente
```

Podemos separar a lógica de leitura da lógica de validação:

```python
def ler_informacao(mensagem, validador):
    while True:
        valor = input(mensagem)

        if validador(valor):
            return valor

        print("Valor inválido.")
```

Agora podemos criar diferentes validadores.

Para idade:

```python
def idade_valida(valor):
    if not valor.isdigit():
        return False

    idade = int(valor)

    if idade < 0 or idade > 120:
        return False

    return True
```

Uso:

```python
idade = ler_informacao(
    "Digite sua idade: ",
    idade_valida
)
```

Para nota:

```python
def nota_valida(valor):
    try:
        nota = float(valor)
    except ValueError:
        return False

    if nota < 0 or nota > 10:
        return False

    return True
```

Uso:

```python
nota = ler_informacao(
    "Digite sua nota: ",
    nota_valida
)
```

A função:

```python
ler_informacao()
```

controla a estrutura geral:

```text
ler
 ↓
validar
 ↓
repetir se necessário
```

Enquanto:

```text
idade_valida
nota_valida
```

definem diferentes comportamentos de validação.



### 4.2. Exemplo: Sequência de Validadores

Considere agora um sistema que utiliza diferentes regras para validar uma senha.

Podemos definir cada regra separadamente.

```python
def tamanho_valido(senha):
    return len(senha) >= 8
```

```python
def possui_numero(senha):
    for caractere in senha:
        if caractere.isdigit():
            return True

    return False
```

```python
def possui_maiuscula(senha):
    for caractere in senha:
        if caractere.isupper():
            return True

    return False
```

Como funções são objetos, podemos armazená-las em uma lista:

```python
validadores = [
    tamanho_valido,
    possui_numero,
    possui_maiuscula
]
```

E criar:

```python
def validar_senha(senha, validadores):
    for validador in validadores:
        if not validador(senha):
            return False

    return True
```

A função `validar_senha()` não precisa saber quais regras existem.

Ela apenas assume que cada elemento de `validadores` é uma função que:

```text
recebe uma senha
      ↓
retorna True ou False
```

Se quisermos acrescentar outra regra:

```python
def possui_caractere_especial(senha):
    especiais = "!@#$%&*"

    for caractere in senha:
        if caractere in especiais:
            return True

    return False
```

podemos fazer:

```python
validadores.append(possui_caractere_especial)
```

sem alterar a implementação de:

```python
validar_senha()
```

Esse tipo de estrutura pode aparecer, por exemplo, em:

* validação de senhas;
* validação de formulários;
* validação de arquivos;
* regras de negócio;
* filtros.



### 4.3. Exemplo: Escolhendo uma Métrica de Distância

Considere diferentes maneiras de calcular a distância entre dois vetores.

Uma possibilidade é a distância de Manhattan:

```python
def distancia_manhattan(a, b):
    distancia = 0

    for i in range(len(a)):
        distancia += abs(a[i] - b[i])

    return distancia
```

Outra possibilidade é a distância Euclidiana:

```python
def distancia_euclidiana(a, b):
    soma = 0

    for i in range(len(a)):
        diferenca = a[i] - b[i]
        soma += diferenca ** 2

    return soma ** 0.5
```

Também podemos calcular a distância de Hamming:

```python
def distancia_hamming(a, b):
    if len(a) != len(b):
        raise ValueError(
            "Os valores devem possuir o mesmo tamanho."
        )

    distancia = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            distancia += 1

    return distancia
```

Podemos escolher a estratégia através de:

```python
def obter_distancia(nome):
    if nome == "manhattan":
        return distancia_manhattan

    if nome == "euclidiana":
        return distancia_euclidiana

    if nome == "hamming":
        return distancia_hamming

    raise ValueError("Métrica de distância desconhecida.")
```

Uso:

```python
distancia = obter_distancia("manhattan")

resultado = distancia(
    [1, 2, 3],
    [4, 2, 1]
)

print(resultado)
```

Podemos trocar:

```python
"manhattan"
```

por:

```python
"euclidiana"
```

sem alterar o restante do programa.

Essa estrutura permite, por exemplo:

* comparar algoritmos;
* selecionar uma estratégia a partir de uma configuração;
* permitir que o usuário escolha uma abordagem;
* testar diferentes estratégias sem modificar a estrutura principal do programa.



## 5. Funções Lambda

Até agora todas as funções que passamos como argumentos possuíam um nome.

Por exemplo:

```python
def obter_preco(produto):
    return produto["preco"]
```

Em alguns casos, entretanto, precisamos de uma função muito pequena que será utilizada apenas naquele ponto do programa.

Python permite criar **funções anônimas** utilizando `lambda`.

### 5.1. Sintaxe

Considere:

```python
def quadrado(x):
    return x ** 2
```

Uma função equivalente pode ser escrita como:

```python
lambda x: x ** 2
```

A estrutura geral é:

```text
lambda parâmetros: expressão
```

Podemos fazer:

```python
quadrado = lambda x: x ** 2

print(quadrado(4))
```

Entretanto, nesse caso normalmente seria mais claro utilizar uma função definida com `def`.

Lambdas são especialmente úteis quando queremos fornecer uma função simples diretamente para outra função.

### 5.2. Exemplo: `sorted`

Considere:

```python
produtos = [
    {"nome": "Mouse", "preco": 120, "avaliacao": 4.7},
    {"nome": "Teclado", "preco": 250, "avaliacao": 4.5},
    {"nome": "Monitor", "preco": 900, "avaliacao": 4.9}
]
```

Podemos ordenar por preço criando:

```python
def obter_preco(produto):
    return produto["preco"]
```

e passando a função:

```python
ordenados = sorted(
    produtos,
    key=obter_preco
)
```

O parâmetro `key` recebe uma função.

Essa função é utilizada para obter o valor que deve servir como critério da ordenação.

Como:

```python
def obter_preco(produto):
    return produto["preco"]
```

é uma operação muito simples, podemos escrever:

```python
ordenados = sorted(
    produtos,
    key=lambda produto: produto["preco"]
)
```

Da mesma forma:

```python
ordenados = sorted(
    produtos,
    key=lambda produto: produto["avaliacao"]
)
```

### 5.3. Exemplo: `max`

O mesmo recurso aparece em outras funções.

Considere novamente a lista de produtos.

Para encontrar o produto mais caro:

```python
mais_caro = max(
    produtos,
    key=lambda produto: produto["preco"]
)
```

Para encontrar o produto com maior avaliação:

```python
melhor_avaliado = max(
    produtos,
    key=lambda produto: produto["avaliacao"]
)
```

A função:

```python
max()
```

controla o algoritmo utilizado para encontrar o maior elemento.

A função fornecida através de `key` informa **qual característica deve ser considerada**.

### 5.4. Quando Utilizar Lambda

Lambdas são úteis principalmente quando:

1. a operação é simples;
2. a função será utilizada apenas naquele ponto;
3. criar um nome separado para a função não melhora significativamente a legibilidade.

Por exemplo:

```python
lambda produto: produto["preco"]
```

é simples de entender.

Para comportamentos maiores ou reutilizáveis, normalmente é melhor utilizar:

```python
def ...
```



## 6. Exercícios

### 6.1. Escolhendo um Critério de Ordenação

Considere:

```python
alunos = [
    {"nome": "Ana", "nota": 8.5, "faltas": 3},
    {"nome": "Bruno", "nota": 7.2, "faltas": 1},
    {"nome": "Carla", "nota": 9.1, "faltas": 5},
    {"nome": "Daniel", "nota": 6.8, "faltas": 0}
]
```

Implemente funções que retornem:

1. o nome de um aluno;
2. a nota de um aluno;
3. a quantidade de faltas de um aluno.

Depois implemente:

```python
def obter_criterio(nome):
    ...
```

A função deve:

1. receber `"nome"`, `"nota"` ou `"faltas"`;
2. retornar a função correspondente ao critério;
3. lançar `ValueError` caso o critério seja desconhecido.

O programa principal deve:

1. solicitar ao usuário por qual critério deseja ordenar os alunos;
2. obter a função correspondente utilizando `obter_criterio()`;
3. utilizar essa função como `key` de `sorted()`;
4. apresentar os alunos ordenados.

Por exemplo:

```text
Ordenar por: nota
```

deve produzir a ordenação utilizando as notas dos alunos.

Depois, reescreva pelo menos uma das formas de ordenação utilizando uma `lambda`.



### 6.2. Contagem de Palavras com Pré-processamento

Considere uma função que conta a frequência das palavras de um texto:

```python
def contar_palavras(texto, preprocessar):
    texto = preprocessar(texto)

    palavras = texto.split()

    contagem = {}

    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    return contagem
```

A função responsável pela contagem não deve precisar conhecer antecipadamente como o texto será preparado.

Implemente diferentes estratégias de pré-processamento.

Por exemplo:

```python
def sem_preprocessamento(texto):
    return texto
```

e:

```python
def converter_minusculas(texto):
    return texto.lower()
```

Depois:

1. execute `contar_palavras()` utilizando `sem_preprocessamento`;
2. execute novamente utilizando `converter_minusculas`;
3. compare os resultados para um texto contendo palavras como `"Python"` e `"python"`;
4. crie outra função de pré-processamento;
5. utilize essa nova função sem modificar `contar_palavras()`.

Por exemplo, a nova função pode:

* remover determinados sinais de pontuação;
* remover espaços extras;
* realizar alguma outra transformação simples.

Considere:

```text
Python python PYTHON
```

Como diferentes formas de pré-processamento alteram o resultado da contagem?

Por que `contar_palavras()` não precisa conhecer antecipadamente todas as estratégias de pré-processamento que podem existir?
