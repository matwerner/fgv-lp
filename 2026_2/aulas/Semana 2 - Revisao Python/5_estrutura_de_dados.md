# Aula 4: Estruturas de Dados em Python

## 1. Objetos e Métodos

Até agora, utilizamos diferentes tipos de dados em Python:

```python
idade = 20
nome = "Maria"
notas = [7.5, 8.0, 6.5]
```

Podemos descobrir o tipo de cada valor utilizando `type()`:

```python
print(type(idade))
print(type(nome))
print(type(notas))
```

Em Python, valores como números, strings, listas e até mesmo funções são **objetos**.

Cada objeto possui um **tipo**, que determina:
* quais valores ele pode representar;
* quais operações podem ser realizadas sobre ele;
* quais métodos estão disponíveis.

Por exemplo:
```python
nome = "maria"

print(nome.upper())
```

ou:

```python
notas = [7.5, 8.0, 6.5]

notas.append(9.0)
```

Nesse caso:

```python
nome.upper()
notas.append(9.0)
```

utilizam **métodos** associados aos objetos.

Podemos pensar na notação:

```python
objeto.metodo(...)
```

como uma operação associada àquele objeto.

### 1.1 Classes

Todo objeto em Python pertence a uma **classe**.

Uma classe define quais dados e comportamentos objetos daquele tipo podem possuir.

Por exemplo:

```python
lista1 = [1, 2, 3]
lista2 = ["a", "b", "c"]
```

`lista1` e `lista2` são objetos diferentes, mas ambos pertencem à classe:

```python
list
```

Por isso, os dois possuem métodos como:

```python
lista1.append(4)
lista2.append("d")
```

Da mesma forma:

```python
texto1 = "Python"
texto2 = "Programação"
```

são objetos da classe:

```python
str
```

e possuem métodos como:

```python
texto1.upper()
texto2.lower()
```

Nesta aula, **não vamos aprender a criar nossas próprias classes**.

Por enquanto, o importante é entender que os tipos que utilizamos em Python definem objetos que possuem diferentes operações e métodos.

### 1.2 Comparação com C

Em C, podemos utilizar uma `struct` para agrupar informações relacionadas:

```c
struct Pessoa {
    char nome[50];
    int idade;
};
```

Uma `struct` permite representar conjuntamente diferentes dados relacionados.

Classes em Python também podem agrupar dados, mas podem adicionalmente definir operações associadas aos objetos.

De maneira simplificada:

* uma `struct` em C agrupa dados relacionados;
* uma classe em Python pode agrupar **dados e comportamentos**.

Exploraremos a criação de classes em mais detalhes posteriormente.


## 2. Estruturas de Dados Básicas

Python oferece diferentes estruturas para armazenar e organizar conjuntos de valores.

As principais estruturas que veremos são:

| Estrutura      | Sintaxe           | Ordenada | Mutável | Permite repetição | Acesso principal |
| -------------- | ----------------- | -------: | ------: | ----------------: | ---------------- |
| **Lista**      | `[1, 2, 3]`       |      Sim |     Sim |               Sim | Índice           |
| **Tupla**      | `(1, 2, 3)`       |      Sim |     Não |               Sim | Índice           |
| **Conjunto**   | `{1, 2, 3}`       |      Não |     Sim |               Não | Pertencimento    |
| **Dicionário** | `{"nome": "Ana"}` |     Sim* |     Sim |        Chaves não | Chave            |
| **String**     | `"Python"`        |      Sim |     Não |               Sim | Índice           |

> * Dicionários preservam a ordem de inserção dos elementos. Entretanto, normalmente utilizamos suas **chaves**, e não suas posições, para acessar os valores.

De maneira geral:

* **Lista** → quando queremos uma sequência de valores que pode ser modificada;
* **Tupla** → quando queremos uma sequência de valores que não deve ser modificada;
* **Conjunto** → quando nos interessa principalmente saber quais elementos existem, sem repetições;
* **Dicionário** → quando queremos associar uma chave a um valor;
* **String** → quando queremos representar e manipular uma sequência de caracteres.

Ao longo da aula veremos as principais operações disponíveis em cada uma dessas estruturas.


## 3. Listas

Uma **lista** é uma coleção ordenada e modificável de elementos.

```python
notas = [7.5, 8.0, 6.5]
```

Uma lista pode inclusive armazenar valores de diferentes tipos:

```python
dados = ["Maria", 20, 8.5, True]
```

### 3.1 Acessando Elementos

Os elementos são acessados utilizando índices:

```python
nomes = ["Ana", "Bruno", "Carlos"]

print(nomes[0])   # Primeiro elemento
print(nomes[1])   # Segundo elemento
print(nomes[-1])  # Último elemento
```

Assim como em C, o primeiro elemento possui índice `0`.

### 3.2 Modificando Elementos

Listas são **mutáveis**, ou seja, podem ser modificadas depois de criadas.

```python
notas = [7.5, 8.0, 6.5]

notas[0] = 9.0

print(notas)
```

### 3.3 Métodos Comuns

```python
nomes = ["Ana", "Bruno", "Carlos"]

nomes.append("Daniel")              # Adiciona um elemento ao final da lista
nomes.extend(["Eduardo", "Maria"])  # Adiciona vários elementos ao final
nomes.insert(1, "Pedro")            # Insere um elemento em uma posição específica

nomes.remove("Bruno")               # Remove a primeira ocorrência do valor
ultimo = nomes.pop()                # Remove e retorna o último elemento
primeiro = nomes.pop(0)             # Remove e retorna o elemento da posição 0

nomes.clear()                       # Remove todos os elementos da lista
```

### 3.4 Operações Comuns

Podemos verificar se um valor pertence à lista:

```python
nomes = ["Ana", "Bruno", "Carlos"]

print("Bruno" in nomes)
```

Podemos utilizar algumas funções já fornecidas pelo Python:

```python
notas = [7.5, 5.0, 9.5, 8.0]

print(len(notas))      # Retorna a quantidade de elementos
print(sum(notas))      # Retorna a soma dos elementos
print(min(notas))      # Retorna o menor elemento
print(max(notas))      # Retorna o maior elemento
print(sorted(notas))   # Retorna uma nova lista ordenada
```

Também podemos concatenar listas:

```python
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

print(lista1 + lista2)
```

E repetir seus elementos:

```python
print([0] * 5)
```

Resultado:

```text
[0, 0, 0, 0, 0]
```

### 3.5 Fatiamento

Python permite obter partes de uma sequência utilizando **slicing**:

```python
numeros = [10, 20, 30, 40, 50]

print(numeros[1:4])
```

Resultado:

```text
[20, 30, 40]
```

A sintaxe geral é:

```python
lista[inicio:fim:passo]
```

Por exemplo:

```python
print(numeros[:3])    # Do início até a posição 3
print(numeros[2:])    # Da posição 2 até o final
print(numeros[::2])   # Elementos de 2 em 2
print(numeros[::-1])  # Lista na ordem inversa
```

> **Pergunta:** o índice `fim` está incluído no resultado?

### 3.6 Exercício

Considere uma lista representando uma fila de atendimento:

```python
fila = ["Ana", "Bruno", "Carlos", "Daniel"]
```

Faça as seguintes operações:

1. Adicione `"Eduardo"` ao final da fila;
2. Remova a primeira pessoa da fila;
3. Mostre quantas pessoas ainda estão esperando;
4. Verifique se `"Carlos"` ainda está na fila;
5. Exiba a fila em ordem alfabética.


## 4. Tuplas

Uma **tupla** é uma coleção ordenada e imutável de elementos.

```python
coordenada = (40.7128, -74.0060)
```

Assim como listas, seus elementos podem ser acessados utilizando índices:

```python
print(coordenada[0])  # Primeiro elemento
print(coordenada[1])  # Segundo elemento
```

A principal diferença é que uma tupla é **imutável**.

Por exemplo:

```python
coordenada[0] = 10
```

produz um erro.

### 4.1 Quando Utilizar?

Tuplas são úteis para representar valores relacionados que, conceitualmente, não pretendemos modificar.

Por exemplo:

```python
coordenada = (-22.9068, -43.1729)
```

Também já encontramos tuplas quando estudamos funções:

```python
def dividir(dividendo, divisor):
    return dividendo // divisor, dividendo % divisor
```

O retorno:

```python
resultado = dividir(10, 3)

print(resultado)
```

é:

```text
(3, 1)
```

Podemos desempacotar essa tupla:

```python
quociente, resto = dividir(10, 3)
```

### 4.2 Métodos e Operações Comuns

Tuplas possuem poucos métodos justamente por serem imutáveis.

```python
valores = (10, 20, 10, 30)

print(valores.count(10))  # Conta quantas vezes o valor aparece
print(valores.index(20))  # Retorna o índice da primeira ocorrência
```

Também podemos utilizar:

```python
print(len(valores))   # Retorna a quantidade de elementos
print(20 in valores)  # Verifica se o elemento pertence à tupla
```

E realizar slicing:

```python
print(valores[1:3])   # Retorna os elementos das posições 1 até 2
print(valores[::-1])  # Retorna a tupla na ordem inversa
```

### 4.3 Exercício

Considere:

```python
ponto = (10, 20)
```

1. Armazene os valores da tupla em duas variáveis `x` e `y`;
2. Imprima `x` e `y`;
3. Tente modificar o primeiro elemento da tupla;
4. O que acontece? Por quê?


## 5. Conjuntos

Um **conjunto** (`set`) é uma coleção que não possui elementos duplicados.

```python
numeros = {1, 2, 3, 4, 5}
```

Considere:

```python
numeros = {1, 2, 2, 3, 3, 3}

print(numeros)
```

O que você espera que seja exibido?

Conjuntos são particularmente úteis quando:

* queremos eliminar elementos repetidos;
* queremos verificar pertencimento;
* queremos realizar operações entre grupos de elementos.

Diferentemente de listas e tuplas, não acessamos os elementos de um conjunto utilizando índices.

```python
numeros[0]
```

não é uma operação válida.

### 5.1 Métodos Comuns

```python
cores = {"azul", "verde"}

cores.add("vermelho")      # Adiciona um elemento ao conjunto
cores.remove("azul")       # Remove um elemento; gera erro se ele não existir
cores.discard("amarelo")   # Remove um elemento; não gera erro se ele não existir
cores.clear()              # Remove todos os elementos do conjunto
```

> **Pergunta:** qual é a diferença entre `remove()` e `discard()` quando o elemento não existe?

### 5.2 Pertencimento

Um uso bastante comum de conjuntos é verificar se determinado elemento pertence a um grupo:

```python
palavra = "pix"

palavras_spam = {
    "dinheiro",
    "urgente",
    "pix",
    "ganhador"
}

if palavra in palavras_spam:
    print("Possível spam")
```

### 5.3 Operações entre Conjuntos

Considere:

```python
alunos_python = {"Ana", "Bruno", "Carlos"}
alunos_java = {"Carlos", "Daniel", "Ana"}
```

Podemos calcular a união:

```python
print(alunos_python.union(alunos_java))  # Elementos presentes em pelo menos um conjunto
print(alunos_python | alunos_java)       # Outra forma de calcular a união
```

A interseção:

```python
print(alunos_python.intersection(alunos_java))  # Elementos presentes nos dois conjuntos
print(alunos_python & alunos_java)               # Outra forma de calcular a interseção
```

E a diferença:

```python
print(alunos_python.difference(alunos_java))  # Elementos do primeiro que não aparecem no segundo
print(alunos_python - alunos_java)             # Outra forma de calcular a diferença
```

### 5.4 Exercício

Uma turma possui os seguintes alunos matriculados:

```python
programacao = {"Ana", "Bruno", "Carlos", "Daniel"}
banco_dados = {"Ana", "Carlos", "Eduardo"}
```

Descubra:

1. quais alunos estão em pelo menos uma das disciplinas;
2. quais alunos estão nas duas disciplinas;
3. quais alunos estão apenas em Programação;
4. quantos alunos diferentes existem no total.


## 6. Dicionários

Um **dicionário** (`dict`) armazena associações entre **chaves** e **valores**.

Por exemplo:

```python
produto = {
    "nome": "Camiseta",
    "preco": 29.99,
    "estoque": 100
}
```

Em vez de acessar informações pela posição:

```python
produto[0]
```

utilizamos uma chave:

```python
print(produto["nome"])
print(produto["preco"])
```

Podemos pensar em um dicionário como uma coleção de associações:

```text
"nome"    → "Camiseta"
"preco"   → 29.99
"estoque" → 100
```

### 6.1 Adicionando e Modificando Valores

Podemos modificar um valor existente:

```python
produto["estoque"] = 90
```

Ou adicionar uma nova chave:

```python
produto["categoria"] = "Vestuário"
```

Também podemos atualizar utilizando o valor anterior:

```python
produto["estoque"] -= 1
```

### 6.2 Métodos Comuns

```python
produto = {
    "nome": "Camiseta",
    "preco": 29.99,
    "estoque": 100
}

produto.get("nome")                  # Retorna o valor associado à chave
produto.get("categoria", "Outros")  # Retorna um valor padrão caso a chave não exista

produto.update({"estoque": 50})     # Atualiza valores existentes ou adiciona novas chaves

produto.keys()                       # Retorna as chaves do dicionário
produto.values()                     # Retorna os valores do dicionário
produto.items()                      # Retorna os pares chave-valor

produto.pop("preco")                 # Remove a chave e retorna seu valor
produto.clear()                      # Remove todos os elementos do dicionário
```

Uma diferença interessante:

```python
print(produto["categoria"])
```

gera um erro caso `"categoria"` não exista.

Já:

```python
print(produto.get("categoria"))
```

retorna:

```text
None
```

### 6.3 Percorrendo um Dicionário

Podemos percorrer apenas as chaves:

```python
for chave in produto:
    print(chave)
```

Ou as chaves e seus valores:

```python
for chave, valor in produto.items():
    print(chave, valor)
```

Observe novamente o desempacotamento:

```python
chave, valor
```

Assim como fizemos anteriormente com tuplas.

### 6.4 Exercício

Considere o estoque:

```python
estoque = {
    "arroz": 10,
    "feijao": 5,
    "macarrao": 8
}
```

Faça um programa que:

1. pergunte qual produto foi vendido;
2. verifique se o produto existe;
3. diminua seu estoque em uma unidade;
4. exiba o estoque atualizado.


## 7. Strings

Uma **string** é uma sequência imutável de caracteres.

```python
texto = "Python"
```

Assim como listas e tuplas, podemos acessar posições:

```python
print(texto[0])   # Primeiro caractere
print(texto[-1])  # Último caractere
```

E utilizar slicing:

```python
print(texto[1:4])   # Retorna os caracteres das posições 1 até 3
print(texto[::-1])  # Retorna a string na ordem inversa
```

Strings são **imutáveis**.

Por isso:

```python
texto[0] = "J"
```

não é permitido.

### 7.1 Métodos Comuns

Considere:

```python
texto = "  Programação em Python  "
```

Alguns métodos bastante utilizados são:

```python
texto.upper()                   # Retorna a string em letras maiúsculas
texto.lower()                   # Retorna a string em letras minúsculas
texto.strip()                   # Remove espaços no início e no final

texto.find("Python")            # Retorna a posição da primeira ocorrência
texto.count("a")                # Conta quantas vezes determinado trecho aparece

texto.replace("Python", "Java") # Substitui ocorrências de um trecho por outro
texto.split()                   # Divide a string e retorna uma lista de partes
```

Observe que strings são imutáveis.

Portanto:

```python
texto.upper()
```

não altera `texto`.

Se quisermos guardar o resultado:

```python
texto = texto.upper()
```

### 7.2 `split()` e `join()`

Podemos transformar uma string em uma lista:

```python
texto = "Programação em Python"

palavras = texto.split()  # Separa a string utilizando espaços

print(palavras)
```

Resultado:

```text
["Programação", "em", "Python"]
```

Também podemos fazer a operação contrária:

```python
palavras = ["Programação", "em", "Python"]

texto = " ".join(palavras)  # Junta os elementos utilizando espaço como separador

print(texto)
```

Resultado:

```text
Programação em Python
```

Observe a sintaxe:

```python
" ".join(palavras)
```

O método `join()` pertence à string que será utilizada como **separador**.

Por exemplo:

```python
"-".join(["10", "08", "2026"])  # Junta os elementos utilizando "-" como separador
```

produz:

```text
10-08-2026
```

### 7.3 Formatação

Podemos construir strings utilizando **f-strings**:

```python
nome = "Maria"
idade = 20

mensagem = f"{nome} tem {idade} anos."

print(mensagem)
```

Também podemos incluir expressões:

```python
a = 10
b = 20

print(f"A soma é {a + b}")
```

### 7.4 Exercício

Considere:

```python
nome_completo = "Maria Silva Souza"
```

Faça um programa que:

1. converta todo o nome para letras minúsculas;
2. separe o nome em uma lista de palavras;
3. descubra quantas partes existem no nome;
4. obtenha o primeiro nome;
5. obtenha o último sobrenome;
6. produza um identificador no formato:

```text
maria.souza
```


## 8. Voltando ao Wordle

Na aula anterior, implementamos uma versão simplificada do Wordle.

Nossa função para avaliar um palpite era semelhante a:

```python
def avaliar_palpite(palpite, palavra_secreta):
    resultado = ""

    for i in range(len(palpite)):
        if palpite[i] == palavra_secreta[i]:
            resultado += "🟩"
        elif palpite[i] in palavra_secreta:
            resultado += "🟨"
        else:
            resultado += "⬛"

    return resultado
```

Para muitos casos, essa solução parece funcionar.

Por exemplo:

```python
print(avaliar_palpite("TEMPO", "TERMO"))
```

produz:

```text
🟩🟩🟩⬛🟩
```

Mas existe um problema.

### 8.1 Letras Repetidas

Considere:

```python
palavra_secreta = "SERRA"
palpite = "ARARA"
```

Nossa implementação atual analisa cada posição utilizando:

```python
elif palpite[i] in palavra_secreta:
    resultado += "🟨"
```

Como `"A"` pertence à palavra `"SERRA"`, qualquer `A` que não esteja na posição correta será considerado amarelo.

A implementação anterior produziria:

```text
🟨🟨🟨🟩🟩
```

Mas isso está errado.

Considere as duas palavras:

```text
SERRA
ARARA
```

A palavra secreta possui apenas **um `A`**.

Além disso, esse `A` já foi utilizado na última posição:

```text
S E R R A
        🟩
```

Portanto, os outros `A`s do palpite não podem também receber uma indicação amarela.

O resultado correto é:

```text
⬛🟨⬛🟩🟩
```

Temos então um novo problema:

> Não basta saber se uma letra existe na palavra. Precisamos saber também quantas ocorrências daquela letra ainda estão disponíveis.


### 8.2 Um Conjunto Resolveria?

Acabamos de aprender sobre conjuntos.

Poderíamos pensar em fazer:

```python
letras = set("SERRA")

print(letras)
```

Um possível resultado seria:

```text
{'S', 'E', 'R', 'A'}
```

Mas conjuntos não possuem elementos repetidos.

Perdemos a informação de que:

```text
R aparece 2 vezes
```

Portanto, um conjunto consegue responder:

> A letra `R` existe?

Mas não consegue representar diretamente:

> Quantos `R`s existem?

Para resolver nosso problema, precisamos manter essa informação.


### 8.3 Controlando as Letras Disponíveis

Uma possibilidade é transformar a palavra secreta em uma lista:

```python
palavra_secreta = "SERRA"

letras_disponiveis = list(palavra_secreta)

print(letras_disponiveis)
```

Resultado:

```text
['S', 'E', 'R', 'R', 'A']
```

Agora temos cada ocorrência de cada letra representada individualmente.

Podemos fazer a avaliação em **duas etapas**:

1. encontrar as letras verdes;
2. encontrar as letras amarelas utilizando apenas as letras que ainda estão disponíveis.


### 8.4 Primeira Etapa: Letras Verdes

Primeiro criamos uma lista para armazenar o resultado:

```python
resultado = ["⬛"] * len(palpite)
```

Por exemplo:

```text
['⬛', '⬛', '⬛', '⬛', '⬛']
```

Também criamos uma lista com as letras disponíveis:

```python
letras_disponiveis = list(palavra_secreta)
```

Agora verificamos as posições corretas:

```python
for i in range(len(palpite)):
    if palpite[i] == palavra_secreta[i]:
        resultado[i] = "🟩"
        letras_disponiveis[i] = None
```

Quando encontramos uma letra verde:

```python
resultado[i] = "🟩"
```

marcamos aquela posição como correta.

Depois fazemos:

```python
letras_disponiveis[i] = None
```

para indicar que aquela ocorrência da letra **já foi utilizada**.

Ela não poderá ser novamente utilizada para gerar uma letra amarela.


### 8.5 Segunda Etapa: Letras Amarelas

Depois de identificar todas as letras verdes, percorremos novamente o palpite:

```python
for i in range(len(palpite)):
    if resultado[i] == "🟩":
        continue

    if palpite[i] in letras_disponiveis:
        resultado[i] = "🟨"
        letras_disponiveis.remove(palpite[i])
```

Se uma posição já está verde:

```python
if resultado[i] == "🟩":
    continue
```

não precisamos analisá-la novamente.

Caso contrário, verificamos:

```python
if palpite[i] in letras_disponiveis:
```

Se a letra ainda estiver disponível, marcamos:

```python
resultado[i] = "🟨"
```

e removemos uma ocorrência:

```python
letras_disponiveis.remove(palpite[i])
```

Assim, aquela mesma ocorrência não poderá ser usada duas vezes.


### 8.6 Atualizando `avaliar_palpite`

Podemos então modificar a função desenvolvida na aula anterior:

```python
def avaliar_palpite(palpite, palavra_secreta):
    resultado = ["⬛"] * len(palpite)
    letras_disponiveis = list(palavra_secreta)

    # Primeiro identificamos as letras na posição correta
    for i in range(len(palpite)):
        if palpite[i] == palavra_secreta[i]:
            resultado[i] = "🟩"
            letras_disponiveis[i] = None

    # Depois identificamos letras existentes em outras posições
    for i in range(len(palpite)):
        if resultado[i] == "🟩":
            continue

        if palpite[i] in letras_disponiveis:
            resultado[i] = "🟨"
            letras_disponiveis.remove(palpite[i])

    return "".join(resultado)
```

Agora:

```python
print(avaliar_palpite("ARARA", "SERRA"))
```

produz corretamente:

```text
⬛🟨⬛🟩🟩
```

Outro exemplo:

```python
print(avaliar_palpite("SERRA", "SORTE"))
```

produz:

```text
🟩🟨🟩⬛⬛
```


### 8.7 O que Utilizamos?

Observe quantos conceitos desta aula aparecem na nova implementação.

Criamos uma lista a partir de uma string:

```python
letras_disponiveis = list(palavra_secreta)
```

Criamos uma lista repetindo um elemento:

```python
resultado = ["⬛"] * len(palpite)
```

Acessamos elementos utilizando índices:

```python
resultado[i]
```

Modificamos elementos de uma lista:

```python
resultado[i] = "🟩"
```

Verificamos pertencimento:

```python
palpite[i] in letras_disponiveis
```

Removemos uma ocorrência:

```python
letras_disponiveis.remove(palpite[i])
```

E transformamos uma lista de strings em uma única string:

```python
"".join(resultado)
```

A nova solução utiliza as estruturas de dados não apenas para **armazenar informações**, mas também para representar o **estado do problema durante sua resolução**.


### 8.8 Exercício

Modifique o Wordle desenvolvido na aula anterior para tratar corretamente palavras que possuem letras repetidas.

Teste sua implementação com pelo menos os seguintes casos:

```python
print(avaliar_palpite("ARARA", "SERRA"))
print(avaliar_palpite("SERRA", "SORTE"))
print(avaliar_palpite("AAAAA", "ARARA"))
print(avaliar_palpite("ARARA", "ARARA"))
```

Os resultados esperados são:

```text
⬛🟨⬛🟩🟩
🟩🟨🟩⬛⬛
🟩⬛🟩⬛🟩
🟩🟩🟩🟩🟩
```

#### Para Pensar

1. Por que a implementação da aula anterior não funciona corretamente com letras repetidas?
2. Por que um conjunto (`set`) não é suficiente para resolver o problema?
3. Por que precisamos identificar primeiro todas as letras verdes?
4. O que aconteceria se não removêssemos uma letra de `letras_disponiveis` depois de marcá-la como amarela?
5. Seria possível resolver o mesmo problema utilizando um dicionário?
6. Como poderíamos utilizar um dicionário para representar quantas vezes cada letra ainda está disponível?
