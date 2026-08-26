# Aula 11: Erros e Exceções

## 1. Erros em Programas

Por mais cuidado que tenhamos ao desenvolver um programa, erros fazem parte do processo de programação.

Alguns erros impedem que o programa seja executado. Outros permitem que o programa seja executado, mas produzem um resultado incorreto. Há ainda situações em que o programa começa normalmente, mas encontra um problema durante sua execução.

Podemos dividir esses problemas em três categorias principais:

1. erros de sintaxe;
2. erros lógicos;
3. erros em tempo de execução.

### 1.1. Erros de Sintaxe

Erros de sintaxe ocorrem quando o código viola as regras da linguagem Python.

Por exemplo:

```python
arr = [1, 2, 3, 4]

for v in arr
    print(v)
```

Ao tentar executar esse programa, Python informa que encontrou um problema:

```text
  File "exemplo.py", line 3
    for v in arr
                ^
SyntaxError: expected ':'
```

A mensagem indica:

* o arquivo no qual o erro foi encontrado;
* a linha em que Python identificou o problema;
* aproximadamente onde o problema foi encontrado;
* o tipo do erro;
* uma descrição do problema.

Nesse caso, faltou `:` ao final do `for`.

Erros de sintaxe costumam ser relativamente fáceis de identificar, pois impedem que o código seja interpretado corretamente e são acompanhados de uma mensagem de erro.

### 1.2. Erros Lógicos

Erros lógicos ocorrem quando o programa executa normalmente, mas não implementa corretamente o comportamento desejado.

Considere uma função para encontrar o menor elemento de uma lista:

```python
def find_min_value(arr):
    min_value = 0

    for v in arr:
        if v < min_value:
            min_value = v

    return min_value
```

Ao executar:

```python
arr = [1, 2, 3, 4]

print(find_min_value(arr))
```

o resultado será:

```text
0
```

Entretanto, esperamos que o menor valor seja `1`.

O problema ocorre porque `min_value` foi inicialmente definido como `0`. Como nenhum valor da lista é menor que `0`, esse valor nunca é atualizado.

Observe que Python não identifica nenhum problema nesse programa.

O código é sintaticamente válido e todas as operações realizadas também são válidas. O erro está na lógica utilizada para resolver o problema.

> Um erro lógico não necessariamente produz uma mensagem de erro ou uma exceção.

### 1.3. Erros Lógicos Podem Ser Difíceis de Identificar

Alguns erros lógicos aparecem imediatamente. Outros aparecem apenas para determinadas entradas.

Um exemplo que já encontramos ocorreu na implementação do Wordle / Termo.

Uma primeira solução para identificar letras poderia ser:

```python
def avaliar_palpite(palavra, palpite):
    resultado = ""

    for i in range(len(palpite)):
        if palpite[i] == palavra[i]:
            resultado += "🟩"
        elif palpite[i] in palavra:
            resultado += "🟨"
        else:
            resultado += "⬛"

    return resultado
```

Para diversas palavras, essa implementação parece funcionar corretamente.

O problema aparece quando existem letras repetidas.

Uma ocorrência de uma letra na palavra secreta não pode ser utilizada para justificar múltiplas letras do palpite.

Assim, podemos ter uma implementação que:

* não possui erros de sintaxe;
* não produz nenhuma exceção;
* funciona para diversos exemplos;
* mas ainda produz resultados incorretos para determinados casos.

Esse é um erro lógico.

Outro exemplo aparece ao combinar duas listas previamente ordenadas:

```python
def merge(a, b):
    i = 0
    j = 0
    result = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    return result
```

Ao executar:

```python
print(merge([1, 3], [2, 4]))
```

obtemos:

```text
[1, 2, 3]
```

O valor `4` desapareceu.

Quando uma das listas termina, a condição:

```python
i < len(a) and j < len(b)
```

deixa de ser verdadeira e os elementos restantes da outra lista nunca são adicionados ao resultado.

Mais uma vez, nenhuma exceção foi lançada.

O programa terminou normalmente, mas produziu um resultado incorreto.

Além disso, determinados testes podem não revelar o problema:

```python
merge([], [])
```

retorna corretamente:

```text
[]
```

Portanto, executar corretamente para alguns exemplos não significa necessariamente que uma implementação esteja correta.

Mais adiante veremos como escolher diferentes casos de teste e como automatizar sua execução.

### 1.4. Erros em Tempo de Execução

Considere novamente a função que encontra o menor elemento de uma lista.

Podemos corrigir o problema anterior inicializando `min_value` com o primeiro elemento:

```python
def find_min_value(arr):
    min_value = arr[0]

    for v in arr:
        if v < min_value:
            min_value = v

    return min_value
```

Para uma lista não vazia:

```python
find_min_value([1, 2, 3, 4])
```

a função retorna corretamente:

```text
1
```

Entretanto:

```python
find_min_value([])
```

resulta em:

```text
IndexError: list index out of range
```

Diferentemente do erro lógico anterior, Python identificou que uma operação não pôde ser realizada.

O programa tentou acessar:

```python
arr[0]
```

mas a lista não possui nenhum elemento.

Em Python, muitas situações encontradas durante a execução são representadas por **exceções**.



## 2. Exceções

Uma exceção representa uma situação encontrada durante a execução do programa que impede que determinada operação seja concluída normalmente.

Considere:

```python
lista = [10, 20, 30]

print(lista[5])
```

Python produz uma mensagem semelhante a:

```text
Traceback (most recent call last):
  File "exemplo.py", line 3, in <module>
    print(lista[5])
          ~~~~~^^^
IndexError: list index out of range
```

A última linha apresenta duas informações importantes:

```text
IndexError: list index out of range
```

`IndexError` identifica o **tipo da exceção**.

`list index out of range` apresenta uma mensagem descrevendo o problema.

### 2.1. Exceções e C

Em C, acessar uma posição inválida de um array pode resultar em comportamento indefinido e, em alguns casos, em uma falha de segmentação.

Em Python, acessos inválidos a uma lista são verificados pela própria linguagem:

```python
lista = [1, 2, 3]

print(lista[100])
```

resulta em:

```text
IndexError: list index out of range
```

Python detecta que a operação não pode ser realizada e sinaliza explicitamente o problema por meio de uma exceção.

### 2.2. Exceções Comuns

Diferentes situações são representadas por diferentes tipos de exceção.

Algumas exceções comuns são:

| Exceção             | Situação                                                                 | Exemplo             |
| ------------------- | ------------------------------------------------------------------------ | ------------------- |
| `ValueError`        | O tipo está correto, mas o valor não pode ser utilizado naquela operação | `float("abc")`      |
| `TypeError`         | Uma operação foi utilizada com tipos incompatíveis                       | `"10" + 5`          |
| `IndexError`        | Uma posição inexistente de uma sequência foi acessada                    | `[1, 2][5]`         |
| `KeyError`          | Uma chave inexistente de um dicionário foi acessada                      | `d["idade"]`        |
| `ZeroDivisionError` | Foi realizada uma divisão por zero                                       | `10 / 0`            |
| `FileNotFoundError` | Um arquivo solicitado não foi encontrado                                 | `open("dados.csv")` |

A maioria das exceções que normalmente tratamos em Python deriva de `Exception`.



## 3. Interpretando um Traceback

Quando uma exceção não é tratada, Python apresenta um **traceback**.

O traceback mostra o caminho percorrido pelo programa até chegar ao ponto em que a exceção ocorreu.

Considere:

```python
def get_first_value(values):
    return values[0]


def calculate(values):
    first = get_first_value(values)
    return first * 2


print(calculate([]))
```

A execução gera uma mensagem semelhante a:

```text
Traceback (most recent call last):
  File "programa.py", line 10, in <module>
    print(calculate([]))
  File "programa.py", line 6, in calculate
    first = get_first_value(values)
  File "programa.py", line 2, in get_first_value
    return values[0]
IndexError: list index out of range
```

Podemos acompanhar as chamadas realizadas:

```text
calculate([])
    ↓
get_first_value([])
    ↓
values[0]
    ↓
IndexError
```

A última linha normalmente contém a informação mais importante:

```text
IndexError: list index out of range
```

As linhas anteriores permitem entender como o programa chegou até o ponto em que ocorreu o problema.

Em programas maiores, com diversas funções e módulos, essa informação se torna especialmente importante.



## 4. Exceções em Dados de Entrada

Até agora utilizamos exemplos pequenos para entender o conceito de exceção.

Entretanto, exceções tornam-se especialmente importantes quando nossos programas recebem dados que não controlamos completamente.

No exercício de finanças pessoais, utilizamos um arquivo CSV contendo transações no seguinte formato:

```text
data,descricao,categoria,valor
2026-08-01,Salário,Receita,8000.00
2026-08-02,Aluguel,Moradia,-2800.00
2026-08-03,Restaurante,Alimentação,-85.50
```

A primeira linha identifica as colunas do arquivo.

Uma implementação simplificada poderia ser:

```python
def ler_transacoes(nome_arquivo):
    transacoes = []

    with open(nome_arquivo, encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    for linha in linhas[1:]:
        data, descricao, categoria, valor = linha.strip().split(",")

        transacoes.append({
            "data": data,
            "descricao": descricao,
            "categoria": categoria,
            "valor": float(valor)
        })

    return transacoes
```

Para um arquivo corretamente formatado, essa função pode funcionar.

Mas o arquivo é uma entrada externa ao nosso programa.

O que acontece se seu conteúdo não estiver exatamente no formato esperado?

### 4.1. Arquivo Inexistente

Considere:

```python
ler_transacoes("arquivo_inexistente.csv")
```

Se o arquivo não existir, a chamada:

```python
open(nome_arquivo)
```

levanta:

```text
FileNotFoundError
```

### 4.2. Quantidade Incorreta de Colunas

Considere agora uma linha com apenas três campos:

```text
2026-08-02,Aluguel,-2800.00
```

O programa executará:

```python
data, descricao, categoria, valor = linha.strip().split(",")
```

Entretanto:

```python
linha.strip().split(",")
```

produzirá apenas três valores.

Python não consegue armazenar três valores em quatro variáveis e levanta uma `ValueError`:

```text
ValueError: not enough values to unpack
```

O problema também ocorre se existirem colunas demais:

```text
2026-08-02,Aluguel,Moradia,-2800.00,XYZ
```

Nesse caso:

```text
ValueError: too many values to unpack
```

### 4.3. Valor Inválido

Considere:

```text
2026-08-03,Restaurante,Alimentação,oitenta
```

A divisão das colunas funciona normalmente:

```python
data, descricao, categoria, valor = linha.strip().split(",")
```

Entretanto, ao executar:

```python
valor = float(valor)
```

Python tenta calcular:

```python
float("oitenta")
```

e levanta:

```text
ValueError
```

Portanto, mesmo uma única linha do arquivo pode apresentar diferentes tipos de problema.



## 5. Tratando Exceções

Uma exceção não precisa necessariamente encerrar o programa.

Python permite interceptar determinadas exceções e definir como o programa deve reagir utilizando os blocos `try` e `except`.

### 5.1. `try` e `except`

Considere:

```python
numero = int(input("Digite um número: "))

print(10 / numero)
```

O usuário pode escrever:

```text
abc
```

causando:

```text
ValueError
```

ou:

```text
0
```

causando:

```text
ZeroDivisionError
```

Podemos tratar essas situações:

```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero

except ValueError:
    print("Você precisa digitar um número inteiro.")

except ZeroDivisionError:
    print("Não é possível dividir por zero.")
```

O código dentro do bloco `try` começa a ser executado normalmente.

Se nenhuma exceção ocorrer, os blocos `except` são ignorados.

Se uma exceção ocorrer, Python interrompe a execução do restante do bloco `try` e procura um `except` compatível.

### 5.2. Fluxo de Execução

Considere:

```python
try:
    print("A")

    numero = int(input("Digite um número: "))

    print("B")

    resultado = 10 / numero

    print("C")

except ValueError:
    print("D")

except ZeroDivisionError:
    print("E")

print("F")
```

Se o usuário digitar `2`:

```text
A
B
C
F
```

Se digitar `abc`:

```text
A
D
F
```

Quando `int()` levanta `ValueError`, o restante do bloco `try` não é executado.

Se o usuário digitar `0`:

```text
A
B
E
F
```

Nesse caso, a conversão funciona normalmente. A exceção ocorre posteriormente na divisão.



## 6. Tratando Problemas no Arquivo de Transações

Podemos agora aplicar `try` e `except` ao programa de finanças pessoais.

### 6.1. Arquivo Inexistente

Uma primeira possibilidade é tratar a abertura do arquivo:

```python
try:
    with open("transacoes.csv", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

except FileNotFoundError:
    print("O arquivo de transações não foi encontrado.")
```

Agora, a ausência do arquivo não resulta necessariamente no encerramento abrupto do programa.

O programa pode informar o problema e decidir como continuar.

### 6.2. Valor Inválido em uma Transação

Considere:

```python
data, descricao, categoria, valor = linha.strip().split(",")
```

seguido de:

```python
valor = float(valor)
```

Podemos tratar uma conversão inválida:

```python
try:
    valor = float(valor)

except ValueError:
    print(f"Valor inválido: {valor}")
```

Por exemplo, para:

```text
2026-08-03,Restaurante,Alimentação,oitenta
```

podemos produzir:

```text
Valor inválido: oitenta
```

### 6.3. Validando o Número de Colunas

Uma linha também pode possuir um número incorreto de colunas:

```text
2026-08-02,Aluguel,-2800.00
```

Uma possibilidade seria simplesmente tentar realizar o desempacotamento:

```python
try:
    data, descricao, categoria, valor = linha.strip().split(",")

except ValueError:
    print("Linha inválida.")
```

Entretanto, nesse caso existe uma condição simples que podemos verificar diretamente:

```python
campos = linha.strip().split(",")

if len(campos) != 4:
    print("A linha deve possuir exatamente 4 colunas.")
```

Depois da validação:

```python
data, descricao, categoria, valor = campos
```

Isso levanta uma questão importante:

> Quando devemos verificar uma condição com `if` e quando devemos utilizar `try` e `except`?

Não existe uma única regra para todas as situações.

Nesse exemplo, verificar o número de campos é simples e deixa explícita a regra esperada:

```python
if len(campos) != 4:
```

Já verificar manualmente se uma string pode ser convertida para `float` seria mais complicado.

Nesse caso, podemos simplesmente tentar realizar a operação:

```python
try:
    valor = float(valor)
except ValueError:
    ...
```



## 7. Tratando Cada Linha Separadamente

Suponha que nosso arquivo contenha:

```text
data,descricao,categoria,valor
2026-08-01,Salário,Receita,8000.00
2026-08-02,Aluguel,Moradia,-2800.00
2026-08-03,Restaurante,Alimentação,oitenta
2026-08-04,Internet,Contas,-120.00
```

Se uma única linha estiver incorreta, precisamos decidir o que fazer.

Algumas possibilidades são:

1. encerrar todo o processamento;
2. ignorar a linha inválida;
3. informar o erro e continuar processando as demais linhas.

Essas alternativas representam diferentes decisões de projeto.

Suponha que desejemos informar o problema e continuar.

Podemos utilizar:

```python
for numero_linha, linha in enumerate(linhas[1:], start=2):
    campos = linha.strip().split(",")

    if len(campos) != 4:
        print(
            f"Linha {numero_linha}: "
            "esperadas exatamente 4 colunas."
        )
        continue

    data, descricao, categoria, valor = campos

    try:
        valor = float(valor)
    except ValueError:
        print(
            f"Linha {numero_linha}: "
            f"'{valor}' não é um valor válido."
        )
        continue

    transacoes.append({
        "data": data,
        "descricao": descricao,
        "categoria": categoria,
        "valor": valor
    })
```

Agora um problema em uma transação não impede necessariamente que as demais sejam processadas.

Observe também que a mensagem informa **onde** o problema ocorreu.



## 8. Tratando Diferentes Exceções

### 8.1. Um `except` para Cada Situação

Quando diferentes problemas exigem comportamentos diferentes, podemos utilizar diferentes blocos `except`:

```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero

except ValueError:
    print("Entrada inválida.")

except ZeroDivisionError:
    print("O número não pode ser zero.")
```

### 8.2. Tratando Vários Tipos da Mesma Forma

Quando diferentes exceções devem resultar na mesma ação, podemos agrupá-las:

```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero

except (ValueError, ZeroDivisionError):
    print("Não foi possível realizar a operação.")
```

### 8.3. Acessando a Exceção

Podemos também acessar o objeto que representa a exceção:

```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero

except (ValueError, ZeroDivisionError) as e:
    print(f"Não foi possível realizar a operação: {e}")
```

Por exemplo:

```text
Digite um número: 0
```

pode resultar em:

```text
Não foi possível realizar a operação: division by zero
```

A variável `e` referencia a exceção que foi levantada.



## 9. Boas Práticas

### 9.1. Trate Exceções Específicas

Considere:

```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero

except:
    print("Algo deu errado.")
```

Esse código captura praticamente qualquer problema ocorrido.

Isso pode esconder erros inesperados e dificultar a depuração.

Em geral, prefira:

```python
except ValueError:
    ...
```

ou:

```python
except ZeroDivisionError:
    ...
```

quando esses forem os problemas que sabemos como tratar.

### 9.2. Não Ignore Exceções Sem Motivo

Evite:

```python
try:
    numero = int(input("Digite um número: "))

except ValueError:
    pass
```

O programa encontrou um problema, mas nenhuma ação foi tomada e nenhuma informação foi fornecida.

Isso pode tornar erros mais difíceis de identificar.

### 9.3. Mantenha o `try` Focado

Considere:

```python
try:
    data, descricao, categoria, valor = linha.strip().split(",")
    valor = float(valor)
except ValueError:
    print("Linha inválida.")
```

Esse código funciona, mas existe uma dificuldade.

Tanto:

```python
data, descricao, categoria, valor = ...
```

quanto:

```python
float(valor)
```

podem levantar `ValueError`.

Ao colocar as duas operações dentro do mesmo `try`, perdemos informação sobre qual delas falhou.

Quando possível, mantenha o bloco `try` limitado às operações cujas exceções desejamos tratar.

Por exemplo:

```python
campos = linha.strip().split(",")

if len(campos) != 4:
    print("Quantidade incorreta de colunas.")
    continue

data, descricao, categoria, valor = campos

try:
    valor = float(valor)
except ValueError:
    print("Valor inválido.")
    continue
```

Além de facilitar o tratamento, isso deixa mais claro qual problema cada parte do código está tratando.



## 10. Erros Lógicos e Exceções São Problemas Diferentes

É importante distinguir os problemas apresentados ao longo da aula.

Considere:

| Situação        | Python identifica automaticamente? | Exemplo                                            |
| --------------- | ---------------------------------- | -------------------------------------------------- |
| Erro de sintaxe | Sim                                | `for x in valores` sem `:`                         |
| Exceção         | Sim                                | `float("abc")`                                     |
| Erro lógico     | Geralmente não                     | tratamento incorreto de letras repetidas no Wordle |

O mecanismo de exceções permite lidar com operações que não puderam ser realizadas normalmente.

Ele não permite descobrir automaticamente que o algoritmo implementado está logicamente incorreto.

No Wordle, por exemplo, Python não sabe quais deveriam ser as regras para letras repetidas.

Para identificar esse tipo de problema, precisamos verificar o comportamento do programa para diferentes entradas.

Esse será um dos principais objetivos quando estudarmos **testes automatizados**.



## 11. Exercícios

### 11.1. Fluxo de Execução

Considere:

```python
try:
    print("A")

    x = int(input())

    print("B")

    y = 10 / x

    print("C")

except ValueError:
    print("D")

except ZeroDivisionError:
    print("E")

print("F")
```

Determine a saída produzida para cada entrada:

1. `2`;
2. `0`;
3. `abc`.

Explique em qual momento o fluxo de execução muda em cada caso.

### 11.2. Identificando Exceções

Para cada trecho abaixo:

1. informe se uma exceção será levantada;
2. caso seja, indique qual tipo de exceção.

```python
int("42")
```

```python
int("quarenta")
```

```python
[10, 20, 30][4]
```

```python
{"nome": "Ana"}["idade"]
```

```python
10 / 0
```

```python
"10" + 5
```

### 11.3. Transações Financeiras

Considere um arquivo `transacoes.csv` no formato:

```text
data,descricao,categoria,valor
2026-08-01,Salário,Receita,8000.00
2026-08-02,Aluguel,Moradia,-2800.00
2026-08-03,Restaurante,Alimentação,-85.50
```

Escreva uma função que leia o arquivo e produza uma lista de dicionários representando as transações.

O programa deve considerar as seguintes situações:

* o arquivo não existe;
* uma linha possui uma quantidade diferente de quatro colunas;
* o valor de uma transação não pode ser convertido para `float`.

Quando uma linha possuir um formato inválido, o programa deve informar o número da linha e continuar processando as demais transações.

Por exemplo:

```text
data,descricao,categoria,valor
2026-08-01,Salário,Receita,8000.00
2026-08-02,Aluguel,-2800.00
2026-08-03,Restaurante,Alimentação,oitenta
2026-08-04,Internet,Contas,-120.00
```

poderia produzir:

```text
Erro na linha 3: esperadas exatamente 4 colunas.
Erro na linha 4: 'oitenta' não é um valor válido.
```

As transações válidas devem continuar sendo processadas.

### 11.4. Investigando um Erro Lógico

Considere:

```python
def merge(a, b):
    i = 0
    j = 0
    result = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    return result
```

1. Identifique o problema na implementação.
2. Dê um exemplo de entrada para o qual o erro aparece.
3. Dê um exemplo de entrada para o qual a função retorna o resultado esperado apesar do erro.
4. Corrija a implementação.
5. Proponha pelo menos quatro entradas diferentes que seriam úteis para verificar se a nova implementação está correta.
