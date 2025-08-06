# Introdução à Programação Funcional em Python

## 1. O que é Programação Funcional?

A Programação Funcional é um dos paradigmas de programação mais antigos e, ao mesmo tempo, um dos mais poderosos.
Ela se concentra no uso de funções matemáticas para processar dados, tratando a computação como a avaliação dessas funções.
O foco principal desse paradigma é descrever o que precisa ser feito, em vez de como fazer isso, como ocorre na Programação Imperativa.

Ao contrário de linguagens orientadas a objetos ou imperativas, onde o fluxo do programa é frequentemente controlado por estados e sequências de operações, na Programação Funcional, a ênfase está na imutabilidade e em funções puras, ou seja, funções que sempre retornam o mesmo resultado para os mesmos argumentos e não produzem efeitos colaterais.

### Comparando Paradigmas

Para entender melhor como a Programação Funcional se distingue de outros paradigmas, vamos comparar uma tarefa simples: exibir os elementos de uma lista que são maiores que 2.
Abaixo estão as abordagens de diferentes paradigmas para essa tarefa.

#### Programação Imperativa
Na Programação Imperativa, definimos como realizar a tarefa, especificando uma série de passos que o programa deve seguir.
Abaixo está um exemplo clássico usando loops:

```python
l = [1, 2, 3, 4]
f = []
for i in l:
    if i > 2:
        f.append(i)
print(f)
```

Aqui, o código é focado no como: percorremos a lista, verificamos a condição e manipulamos diretamente a variável `f` para adicionar os valores maiores que 2.
Essa abordagem envolve a modificação de variáveis conforme o programa avança.

#### Programação Funcional
Na Programação Funcional, nos concentramos mais no o que queremos obter, utilizando funções que trabalham de forma declarativa.
Veja como podemos fazer a mesma tarefa com uma função funcional:

```python
l = (1, 2, 3, 4)
print(filter(lambda i: i > 2, l))
```

Aqui, utilizamos a função `filter` para filtrar os elementos da lista que atendem a uma condição.
Em vez de manipular diretamente uma lista ou variável, simplesmente aplicamos uma função anônima (lambda) que define a regra que queremos aplicar aos elementos.
Não há modificação do estado, e o foco está mais no resultado final.

### Características da Programação Funcional

A Programação Funcional é caracterizada por alguns conceitos centrais que tornam o código mais previsível e fácil de entender:

* **Funções puras**:
Uma função pura é aquela que, dada a mesma entrada, sempre retorna a mesma saída e não altera o estado do programa (como variáveis globais, arquivos, etc.).

* **Funções de alta ordem**:
Funções podem ser passadas como argumentos ou retornadas por outras funções.
Isso permite uma grande flexibilidade e reutilização de código.

* **Imutabilidade**:
Na programação funcional, não alteramos variáveis existentes.
Em vez disso, criamos novos valores.
Isso evita efeitos colaterais e torna o código mais fácil de depurar e testar.

### Vantagens

Embora Python não seja uma linguagem puramente funcional (é orientada a objetos), ela oferece suporte suficiente para simular muitos dos comportamentos essenciais da Programação Funcional.
As principais vantagens desse paradigma são:

* **Clareza e simplicidade**:
O código funcional tende a ser mais conciso e direto, já que ele se concentra em "o que fazer", sem detalhes excessivos de como as operações são realizadas.

* **Facilidade de teste**:
Funções puras são mais fáceis de testar, já que elas sempre retornam os mesmos resultados para as mesmas entradas, sem depender de estados externos.

* **Paralelização**:
Como as funções puras não dependem de variáveis compartilhadas, elas podem ser executadas em paralelo com facilidade, o que pode melhorar o desempenho em operações que manipulam grandes volumes de dados.

## 2. Função pura

Uma das fundações da Programação Funcional é o conceito de funções puras. Em termos simples, uma função pura é aquela que:

1. Sempre retorna o mesmo valor para os mesmos parâmetros de entrada.
2. Não causa efeitos colaterais, ou seja, não altera nada fora de sua própria execução.

Vamos ver um exemplo simples de uma função pura que soma dois números:

```python
def soma(a: int, b: int) -> int:
    return a + b
```

Aqui, a função `soma` é pura, pois seu resultado depende exclusivamente dos argumentos `a` e `b`.
Sempre que fornecemos os mesmos valores, ela retornará o mesmo resultado. Além disso, a função não altera variáveis externas ou o estado do programa.

### Efeitos Colaterais

Uma função impura, por outro lado, pode alterar o estado externo, como modificar variáveis globais, imprimir na tela ou manipular arquivos.
Essas mudanças externas são chamadas de efeitos colaterais.
Um exemplo clássico é a função `print`, que altera o estado do terminal, ou a função `append`, que altera uma lista existente.

### Comparando Funções Puras e Impuras

Vejamos um exemplo de função impura que depende do horário atual para determinar uma saudação:

```python
from datetime import datetime
def greeting_impure(name: str) -> None:
    now = datetime.now()
    if now.hour < 12:
        greeting_type = "Good morning"
    elif now.hour < 18:
        greeting_type = "Good afternoon"
    else:
        greeting_type = "Good evening"
    print(f"{greeting_type}, {name}")
greeting_impure("John")
```

Neste caso, a função `greeting_impure` não é pura, pois ela depende do horário atual (`datetime.now()`) e tem um efeito colateral ao imprimir uma saudação no terminal.
O resultado da função pode variar dependendo de quando ela for executada, e ela altera o estado do terminal.

Agora, vejamos uma versão pura da mesma função:

```python
from datetime import datetime
def greeting_pure(name: str, hour: int) -> str:
    if hour < 12:
        greeting_type = "Good morning"
    elif hour < 18:
        greeting_type = "Good afternoon"
    else:
        greeting_type = "Good evening"
    return f"{greeting_type}, {name}"

hour = datetime.now().hour
print(greeting_pure("John", hour))
```

Aqui, a função `greeting_pure` depende apenas dos parâmetros `name` e `hour`, e não realiza nenhuma ação externa.
O comportamento dela é previsível, tornando-a fácil de testar e reutilizar.

## 3. Imutabilidade

Um dos conceitos mais fundamentais na Programação Funcional é a imutabilidade.
Isso significa que, em vez de alterar o valor de variáveis ou modificar estruturas de dados existentes, sempre trabalhamos criando novos valores.
Ao garantir que os dados não são modificados diretamente, evitamos efeitos colaterais indesejados e tornamos o código mais previsível e fácil de depurar.

### Estruturas de Dados Imutáveis

No Python, um exemplo clássico de estrutura de dados imutável é a tupla.
Uma vez criada, seus elementos não podem ser alterados.
Se quisermos "modificar" uma tupla, na verdade, criamos uma nova com os valores desejados.

```python
a = (1, 2, 3)  # A tupla é imutável
a = a + (4,)   # Não alteramos a tupla original, criamos uma nova
print(a)  # Output: (1, 2, 3, 4)
```

Além da tupla, outras estruturas de dados imutáveis incluem
`collections.namedtuple`, que fornece uma versão imutável de dicionários,
e `frozenset`, uma versão imutável de conjuntos (set).

```python
from collections import namedtuple

Pessoa = namedtuple('Pessoa', 'nome idade')
p = Pessoa('João', 30)
print(p.nome)  # Output: João

# Frozenset
s = frozenset([1, 2, 3])
# s.add(4) -> Isso resultaria em um erro, pois o frozenset é imutável
```

Trabalhar com imutabilidade ajuda a evitar problemas de concorrência em programas paralelos, além de facilitar a compreensão do fluxo de dados.

## 4. Funções Lambda

As funções lambda são funções anônimas em Python, ou seja, elas não são associadas a um nome específico.
São muito úteis quando precisamos de funções simples que serão utilizadas em apenas uma linha de código, especialmente ao passá-las como argumento para outras funções.

Exemplo de função lambda:
```python
f = lambda x: x ** 2
print(f(5))  # Output: 25
```
Aqui, `lambda x: x ** 2` define uma função que recebe um argumento `x` e retorna o quadrado desse valor.
As funções lambda são ideais para situações onde uma função simples é necessária de forma temporária, evitando a necessidade de definir uma função completa com `def`.

### Quando Usar Lambdas?

Funções lambda são ideais quando:
* Você precisa de uma função simples e curta.
* Ela será usada apenas uma vez ou passada como argumento para uma função de alta ordem.
* Não há necessidade de uma função complexa com várias instruções.

## 5. Funções de Alta Ordem

Na Programação Funcional, as funções são tratadas como cidadãos de primeira classe, o que significa que elas podem ser manipuladas como qualquer outra variável.
Elas podem ser passadas como argumentos para outras funções, retornadas de funções ou armazenadas em estruturas de dados.
Isso dá uma grande flexibilidade na forma como podemos compor e reutilizar funções.

As funções de alta ordem são aquelas que recebem outras funções como argumento ou retornam uma função como resultado.
Essas funções permitem a composição de comportamentos, facilitando a criação de código reutilizável e modular.

### Exemplos de Funções de Alta Ordem em Python

Python inclui várias funções de alta ordem na sua biblioteca padrão.
Vamos explorar três das mais comuns: `map`, `filter` e `reduce`.

### Exemplo 1: map

A função `map` aplica uma função a cada elemento de um iterável, retornando um novo iterável com os resultados.

```python
cientistas = [
    {'nome': 'Marie Curie', 'campo': 'Física'},
    {'nome': 'Isaac Newton', 'campo': 'Física'},
    {'nome': 'Charles Darwin', 'campo': 'Biologia'},
    {'nome': 'Albert Einstein', 'campo': 'Física'},
    {'nome': 'Gregor Mendel', 'campo': 'Biologia'},
    {'nome': 'Rosalind Franklin', 'campo': 'Biologia'}
]

nomes_em_maiusculo = list(map(lambda c: {'nome': c['nome'].upper(), 'campo': c['campo']}, cientistas))
print(nomes_em_maiusculo)
# [
#     {'nome': 'MARIE CURIE', 'campo': 'Física'},
#     {'nome': 'ISAAC NEWTON', 'campo': 'Física'},
#     {'nome': 'CHARLES DARWIN', 'campo': 'Biologia'},
#     {'nome': 'ALBERT EINSTEIN', 'campo': 'Física'},
#     {'nome': 'GREGOR MENDEL', 'campo': 'Biologia'},
#     {'nome': 'ROSALIND FRANKLIN', 'campo': 'Biologia'}
# ]
```

### Exemplo 2: filter

A função `filter` cria um novo iterável contendo apenas os elementos que atendem a uma condição especificada por uma função.

```python
biologos = list(filter(lambda c: c['campo'] == 'Biologia', cientistas))
print(biologos)
# [
#     {'nome': 'Charles Darwin', 'campo': 'Biologia'},
#     {'nome': 'Gregor Mendel', 'campo': 'Biologia'},
#     {'nome': 'Rosalind Franklin', 'campo': 'Biologia'}
# ]
```

### Exemplo 3: reduce

A função `reduce`, disponível no módulo `functools`, aplica uma função cumulativa aos elementos de um iterável, reduzindo-o a um único valor.

```python
from functools import reduce

def agrupar_por_campo(grupo, cientista):
    campo = cientista['campo']
    if campo not in grupo:
        grupo[campo] = []
    grupo[campo].append(cientista['nome'])
    return grupo

cientistas_agrupados = reduce(agrupar_por_campo, cientistas, {})
print(cientistas_agrupados)
# {
#     'Física': ['Marie Curie', 'Isaac Newton', 'Albert Einstein'],
#     'Biologia': ['Charles Darwin', 'Gregor Mendel', 'Rosalind Franklin']
# }
```

No exemplo acima, `reduce` usa uma função lambda para somar todos os elementos da lista, acumulando o resultado ao longo da iteração.

### Benefícios da Abordagem Funcional

Embora funções como `map`, `filter` e `reduce` sejam simples quando usadas individualmente, elas se tornam extremamente poderosas e flexíveis quando combinadas.
Em vez de usarmos laços aninhados ou múltiplas instruções imperativas para processar dados, podemos compor essas funções de maneira clara e concisa para obter comportamentos complexos a partir de pequenas operações simples.

#### Exemplo: Combinando map, filter e reduce

Objetivo: Queremos agrupar os cientistas por campo de atuação, mas apenas aqueles cujos nomes têm mais de 12 caracteres, e também queremos que seus nomes sejam transformados para maiúsculas.

```python
from functools import reduce

cientistas = [
    {'nome': 'Marie Curie', 'campo': 'Física'},
    {'nome': 'Isaac Newton', 'campo': 'Física'},
    {'nome': 'Charles Darwin', 'campo': 'Biologia'},
    {'nome': 'Albert Einstein', 'campo': 'Física'},
    {'nome': 'Gregor Mendel', 'campo': 'Biologia'},
    {'nome': 'Rosalind Franklin', 'campo': 'Biologia'}
]

# Passo 1: Filtrar cientistas cujos nomes têm mais de 12 caracteres
cientistas_com_nomes_grandes = list(filter(lambda c: len(c['nome']) > 12, cientistas))

# Passo 2: Transformar os nomes para maiúsculas
cientistas_maiusculos = list(map(lambda c: {'nome': c['nome'].upper(), 'campo': c['campo']}, cientistas_com_nomes_grandes))

# Passo 3: Agrupar os cientistas por campo de atuação
def agrupar_por_campo(grupo, cientista):
    campo = cientista['campo']
    if campo not in grupo:
        grupo[campo] = []
    grupo[campo].append(cientista['nome'])
    return grupo

cientistas_agrupados = reduce(agrupar_por_campo, cientistas_maiusculos, {})

print(cientistas_agrupados)
# {
#     'Biologia': ['CHARLES DARWIN', 'ROSALIND FRANKLIN'],
#     'Física': ['ALBERT EINSTEIN']
# }
```

Explicação do Exemplo:
1. **Passo 1 - filter**:
Primeiro, usamos filter para selecionar apenas os cientistas cujos nomes têm mais de 12 caracteres. Este passo reduz a lista para aqueles que atendem a esse critério.
2. **Passo 2 - map**:
Em seguida, aplicamos map para transformar os nomes dos cientistas em maiúsculas, preparando-os para o agrupamento.
3. **Passo 3 - reduce**:
Por fim, usamos reduce para agrupar os cientistas por campo de atuação, garantindo que os cientistas com nomes grandes estejam organizados de acordo com suas áreas de estudo.

#### Implementação Imperativa (para referência):

```python
cientistas = [
    {'nome': 'Marie Curie', 'campo': 'Física'},
    {'nome': 'Isaac Newton', 'campo': 'Física'},
    {'nome': 'Charles Darwin', 'campo': 'Biologia'},
    {'nome': 'Albert Einstein', 'campo': 'Física'},
    {'nome': 'Gregor Mendel', 'campo': 'Biologia'},
    {'nome': 'Rosalind Franklin', 'campo': 'Biologia'}
]

# Passo 1: Filtrar cientistas cujos nomes têm mais de 12 caracteres
cientistas_com_nomes_grandes = []
for cientista in cientistas:
    if len(cientista['nome']) > 12:
        cientistas_com_nomes_grandes.append(cientista)

# Passo 2: Transformar os nomes para maiúsculas
cientistas_maiusculos = []
for cientista in cientistas_com_nomes_grandes:
    cientistas_maiusculos.append({'nome': cientista['nome'].upper(), 'campo': cientista['campo']})

# Passo 3: Agrupar os cientistas por campo de atuação
cientistas_agrupados = {}
for cientista in cientistas_maiusculos:
    campo = cientista['campo']
    if campo not in cientistas_agrupados:
        cientistas_agrupados[campo] = []
    cientistas_agrupados[campo].append(cientista['nome'])

# Exibir resultado
print(cientistas_agrupados)
```

## 6. Exercícios

1. Funções puras:
    * Implemente uma função pura que receba uma lista de números e retorne uma nova lista contendo apenas os números pares da lista original.

2. Imutabilidade:
    * Modifique a lista de números [1, 2, 3, 4, 5] para que todos os seus elementos sejam multiplicados por 2, sem alterar a lista original. Use uma abordagem funcional para resolver isso.

3. Funções Lambda:
    * Escreva uma função lambda que eleve ao quadrado todos os números de uma lista [1, 2, 3, 4].

4. Funções de alta ordem:
    * Utilize a função map para transformar uma lista de números [1, 2, 3, 4, 5] em uma lista de seus cubos (ou seja, eleve cada número ao cubo).
    * Utilize a função filter para filtrar os números maiores que 3 de uma lista.
    * Use a função reduce para somar todos os elementos de uma lista de números.

5. Agrupamento usando reduce:
    * Dada uma lista de dicionários representando pessoas e suas idades, agrupe as pessoas em maiores ou menores de idade usando reduce.