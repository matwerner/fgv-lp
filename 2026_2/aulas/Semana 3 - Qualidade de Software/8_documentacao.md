# Aula 7: Documentação

À medida que uma aplicação cresce, entender o código apenas lendo sua implementação pode se tornar cada vez mais difícil.

Isso acontece principalmente quando:

* o código foi escrito há muito tempo;
* outras pessoas precisam utilizá-lo ou modificá-lo;
* existem regras de negócio que não são óbvias;
* precisamos entender como usar uma função sem conhecer sua implementação.

Nesta aula, veremos diferentes formas de documentar código em Python e quando cada uma delas deve ser utilizada.

## 1. Motivação

Considere a seguinte função:

```python
def processar(v, n, a, x):
    r = 0

    for i in range(len(v)):
        if v[i] > 1000:
            r += 2
        elif v[i] > 500:
            r += 1

        if i > 0 and v[i] > 3 * v[i - 1]:
            r += 2

    if n > 5:
        r += 2

    if a < 30:
        r += 1

    if x:
        r += 3

    if r >= 7:
        return 2
    elif r >= 4:
        return 1

    return 0
```

É possível acompanhar as operações realizadas pela função. No entanto, algumas perguntas permanecem:

* O que representam `v`, `n`, `a` e `x`?
* O que representa `r`?
* O que significam os valores `500` e `1000`?
* Por que é importante verificar se um valor triplicou?
* O que representam os retornos `0`, `1` e `2`?
* Quais valores podem ser passados para a função?

A função poderia, por exemplo, implementar uma classificação simplificada de risco de uma operação financeira:

* `v`: valores das últimas transações;
* `n`: número de tentativas recentes;
* `a`: idade da conta em dias;
* `x`: indica se houve acesso a partir de uma localização incomum;
* `r`: pontuação de risco;
* `0`: risco baixo;
* `1`: risco médio;
* `2`: risco alto.

O código mostra **como** o computador realiza o cálculo, mas não necessariamente deixa claro **o que aquele cálculo representa**.

É nesse ponto que a documentação se torna importante.

## 2. Níveis de Documentação

Podemos pensar na documentação do código em diferentes níveis:

1. **Bloco de código:** comentários utilizados para explicar decisões ou trechos específicos da implementação.
2. **Função:** docstrings que explicam o propósito da função, seus parâmetros, retorno e comportamento.
3. **Módulo / Pacote:** documentação que descreve a responsabilidade geral de uma parte maior do programa.

Cada nível responde a perguntas diferentes.

## 3. Comentários

Comentários são trechos de texto presentes no código-fonte que não são executados pelo interpretador.

Em Python, comentários são iniciados utilizando `#`:

```python
# Isto é um comentário
```

### 3.1 Quando utilizar comentários

Comentários são especialmente úteis quando precisamos explicar:

* uma regra de negócio;
* uma decisão de implementação;
* um comportamento não óbvio;
* por que determinada abordagem foi utilizada.

Em geral, o código já deve deixar claro **o que** está sendo feito.

O comentário deve ser utilizado principalmente quando precisamos explicar **por que** aquilo está sendo feito.

### 3.2 Comentários redundantes

Considere:

```python
contador = 0

# Percorre todos os elementos da lista
for elemento in elementos:
    # Incrementa contador
    contador += 1
```

Os comentários não fornecem nenhuma informação adicional.

O próprio código já deixa claro que existe uma repetição e que o contador está sendo incrementado.

Comentários como esses aumentam o tamanho do código sem facilitar sua compreensão.

### 3.3 Comentários úteis

Vamos voltar ao Wordle / Termo.

Ao lidar com letras repetidas, apenas verificar se uma letra do palpite existe na palavra secreta não é suficiente.

Considere, por exemplo, uma palavra secreta que possua apenas uma ocorrência de determinada letra, enquanto o palpite possui essa mesma letra duas vezes. Apenas uma dessas ocorrências pode ser marcada como presente.

Além disso, uma letra que esteja na **posição correta** deve ter prioridade sobre outra ocorrência da mesma letra que esteja em uma posição diferente.

Por isso, uma possível implementação primeiro identifica as letras que estão nas posições corretas e somente depois procura correspondências para as demais letras:

```python
# Cada letra da palavra secreta só pode ser associada a uma letra do palpite.
# Quando há letras repetidas no palpite, damos prioridade às ocorrências
# que estão na posição correta, o que não necessariamente corresponde
# à primeira ocorrência daquela letra.
for i in range(len(palpite)):
    if palpite[i] == palavra_secreta[i]:
        ...
```

Nesse caso, o comentário é útil porque ele não apenas descreve que as posições corretas são verificadas primeiro. Ele explica **por que essa ordem é necessária para preservar a regra do jogo**.

### 3.4 Boas práticas

Ao escrever comentários:

* seja claro e conciso;
* explique informações que não estejam evidentes no código;
* priorize o motivo de uma decisão;
* evite repetir literalmente o código;
* mantenha os comentários atualizados quando o código mudar.

Um comentário incorreto ou desatualizado pode ser pior do que a ausência de comentário.

## 4. Docstrings

Comentários normalmente ajudam quem está tentando entender a **implementação** de um trecho de código.

Mas imagine que queremos apenas utilizar uma função.

Considere a função do Wordle:

```python
def avaliar_palpite(palpite, palavra_secreta):
    ...
```

Para utilizar essa função corretamente, seria interessante saber:

* o que exatamente ela faz;
* o que deve ser passado em `palpite`;
* o que deve ser passado em `palavra_secreta`;
* o que ela retorna;
* como o resultado deve ser interpretado.

Não deveríamos precisar analisar toda a implementação para descobrir essas informações.

Para isso, podemos utilizar **docstrings**.

### 4.1 O que são docstrings

Docstrings (*documentation strings*) são strings utilizadas para documentar funções, módulos, classes e outros elementos de Python.

Uma docstring é normalmente escrita utilizando três aspas duplas:

```python
def minha_funcao():
    """
    Descrição da função.
    """
```

Diferentemente de um comentário comum, uma docstring fica associada ao objeto documentado.

### 4.2 Consultando uma docstring

Considere:

```python
def saudacao(nome):
    """
    Retorna uma mensagem de saudação para uma pessoa.
    """
    return f"Olá, {nome}!"
```

Podemos acessar a documentação utilizando:

```python
print(saudacao.__doc__)
```

ou:

```python
help(saudacao)
```

Isso permite consultar informações sobre a função sem analisar sua implementação.

### 4.3 O que documentar em uma função

Uma docstring pode conter:

* **descrição:** o que a função faz;
* **parâmetros:** o significado dos valores recebidos;
* **retorno:** o significado do valor retornado;
* **exceções:** situações de erro relevantes;
* **exemplos:** quando ajudarem a explicar a utilização.

Nem toda função precisa de uma documentação extensa.

A quantidade de informação deve ser proporcional à complexidade da função.

### 4.4 Exemplo com Wordle

Considere:

```python
def avaliar_palpite(palpite, palavra_secreta):
    """
    Avalia um palpite em relação à palavra secreta.

    Args:
        palpite (str): Palavra informada pelo jogador.
        palavra_secreta (str): Palavra que deve ser descoberta.

    Returns:
        str: Resultado de cada letra do palpite, indicando se ela
        está correta (🟩), presente em outra posição (🟨) ou ausente (⬛).
    
    Examples:
    >>> avaliar_palpite("PORTA", "PAUSE")
    '🟩🟨⬛⬛⬛'
    >>> avaliar_palpite("PARTE", "PAUSE")
    '🟩🟩⬛⬛🟩'
    """
    ...
```

Agora conseguimos entender como utilizar a função sem precisar conhecer sua implementação.

Essa ideia é especialmente importante quando uma função será utilizada por outras partes do programa.

### 4.5 Documentação como contrato

Podemos pensar na documentação de uma função como uma espécie de **contrato**.

Ela informa:

* o que a função espera receber;
* o que a função faz;
* o que ela devolve.

Por exemplo:

```python
def carregar_palavras(caminho):
    """
    Carrega as palavras disponíveis para o jogo.

    Args:
        caminho (str): Caminho para o arquivo contendo as palavras.

    Returns:
        list[str]: Lista das palavras encontradas no arquivo.
    """
```

Quem utiliza `carregar_palavras()` não precisa saber:

* como o arquivo é aberto;
* se foi utilizado `read()` ou `readlines()`;
* como as quebras de linha foram removidas.

Esses são detalhes da implementação.

O usuário da função precisa conhecer apenas seu contrato.

## 5. Convenções para Docstrings

O Python possui convenções para a escrita de docstrings descritas no PEP 257.

Uma recomendação importante é que a primeira linha apresente uma descrição curta e objetiva do elemento documentado.

Por exemplo:

```python
def escolher_palavra(palavras):
    """
    Escolhe aleatoriamente uma palavra da lista fornecida.
    """
```

Quando for necessário fornecer mais informações, podemos adicionar outras seções.

### 5.1 Estilos de Documentação

Existem diferentes convenções para organizar o conteúdo de uma docstring. Entre as mais utilizadas estão o **Google Style** e o **NumPy Style**.

Ambas permitem documentar as mesmas informações, como parâmetros, retornos e exemplos. A principal diferença está na forma como essas informações são organizadas.

#### Google Style

```python
def avaliar_palpite(palpite, palavra_secreta):
    """
    Avalia um palpite em relação à palavra secreta.

    Args:
        palpite (str): Palavra informada pelo jogador.
        palavra_secreta (str): Palavra que deve ser descoberta.

    Returns:
        list: Situação de cada letra do palpite.
    """
```

O Google Style utiliza seções como `Args` e `Returns`, com uma estrutura relativamente compacta.

#### NumPy Style

```python
def avaliar_palpite(palpite, palavra_secreta):
    """
    Avalia um palpite em relação à palavra secreta.

    Parameters
    ----------
    palpite : str
        Palavra informada pelo jogador.
    palavra_secreta : str
        Palavra que deve ser descoberta.

    Returns
    -------
    list
        Situação de cada letra do palpite.
    """
```

O NumPy Style separa as informações em seções mais explícitas, utilizando cabeçalhos como `Parameters` e `Returns`.

As duas formas documentam essencialmente as mesmas informações:

| Google Style            | NumPy Style                |
| ----------------------- | -------------------------- |
| `Args:`                 | `Parameters`               |
| `Returns:`              | `Returns`                  |
| Mais compacto           | Mais estruturado           |
| Tipo junto ao parâmetro | Tipo separado da descrição |

Não é necessário misturar estilos dentro de um mesmo projeto. O mais importante é escolher uma convenção e utilizá-la de forma consistente.


## 6. Documentação de Módulos e Pacotes

Além de funções individuais, também podemos documentar partes maiores de um programa, como **módulos** e **pacotes**.

De forma geral:

* um **módulo** corresponde a um arquivo Python, como `game.py` ou `words.py`;
* um **pacote** agrupa módulos relacionados dentro de uma mesma estrutura.

Enquanto a documentação de uma função explica como utilizar uma operação específica, a documentação de um módulo ou pacote apresenta sua **responsabilidade geral** e como ele se encaixa na aplicação.

### 6.1 Documentação de um Módulo

A docstring de um módulo deve aparecer no início do arquivo.

Em módulos simples, uma pequena descrição de sua responsabilidade pode ser suficiente.

Por exemplo, considere um módulo `words.py`:

```python
"""
Gerencia as palavras utilizadas pelo jogo Termo.

Este módulo contém funções responsáveis por carregar, validar
e selecionar palavras utilizadas durante o jogo.
"""
```

O objetivo não é necessariamente descrever detalhadamente cada função, mas permitir que alguém entenda rapidamente **para que aquele módulo existe**.

Em módulos maiores, podemos fornecer uma documentação mais detalhada, incluindo suas principais funções e exemplos de utilização.

Por exemplo, considere o módulo `game.py`, responsável pelas regras do jogo:

```python
"""
Implementa as regras do jogo Termo.

Este módulo contém as operações utilizadas para avaliar os palpites
do jogador e determinar se a palavra secreta foi descoberta.

Functions
---------
avaliar_palpite(palpite, palavra_secreta)
    Compara um palpite com a palavra secreta e produz o resultado
    correspondente para cada letra.

venceu(palpite, palavra_secreta)
    Verifica se o jogador descobriu a palavra secreta.

Examples
--------
>>> import game
>>> game.avaliar_palpite("PORTA", "PAUSE")
'🟩🟨⬛⬛⬛'

>>> game.venceu("PAUSE", "PAUSE")
True
"""
```

Nesse caso, a documentação apresenta:

* o propósito geral do módulo;
* suas principais funções;
* um exemplo básico de utilização.

Essas seções não precisam aparecer em todos os módulos. A quantidade de documentação deve acompanhar a complexidade e a forma como o módulo será utilizado.

Também podemos consultar a documentação durante a execução:

```python
import game

print(game.__doc__)
```

ou:

```python
help(game)
```

O `help()` pode apresentar, além da descrição geral do módulo, informações sobre funções e outros elementos definidos nele.

### 6.2 Documentação de um Pacote

À medida que o Wordle cresce, podemos separar diferentes responsabilidades em módulos:

```text
wordle/
├── __init__.py
├── main.py
├── game.py
├── words.py
└── interface.py
```

Nesse exemplo:

* `main.py` coordena o fluxo geral da aplicação e contém a função `jogar()`;
* `game.py` contém as regras do jogo;
* `words.py` gerencia o carregamento, seleção e validação das palavras;
* `interface.py` é responsável pela entrada e saída de informações com o jogador;
* `wordle` agrupa esses módulos em um mesmo pacote.

Uma documentação simples do pacote poderia ser colocada no arquivo `__init__.py`:

```python
"""
Implementação do jogo Termo.

O pacote reúne módulos responsáveis pelo fluxo principal da aplicação,
pelas regras do jogo, pelo gerenciamento das palavras e pela interação
com o jogador.
"""
```

Em um pacote maior, também podemos apresentar sua organização e suas principais funcionalidades:

```python
"""
Implementação do jogo Termo.

O pacote fornece as funcionalidades necessárias para executar uma
partida, carregar e validar palavras, avaliar os palpites e interagir
com o jogador.

Modules
-------
main
    Coordena o fluxo geral de uma partida.

game
    Implementa as regras de avaliação dos palpites.

words
    Carrega, valida e seleciona as palavras utilizadas no jogo.

interface
    Realiza a entrada e saída de informações com o jogador.

Examples
--------
>>> from wordle import game
>>> game.avaliar_palpite("PORTA", "PAUSE")
'🟩🟨⬛⬛⬛'
"""
```

A documentação do pacote fornece uma visão geral da aplicação, enquanto cada módulo apresenta mais detalhes sobre uma responsabilidade específica.

Também podemos consultar a documentação do pacote:

```python
import wordle

help(wordle)
```

### 6.3 Funções, Módulos e Pacotes

Os diferentes níveis de documentação possuem objetivos complementares:

| Nível      | Principal pergunta respondida                                                |
| ---------- | ---------------------------------------------------------------------------- |
| **Função** | Como utilizo esta operação?                                                  |
| **Módulo** | Qual é a responsabilidade deste arquivo e quais funcionalidades ele oferece? |
| **Pacote** | Qual é a finalidade deste conjunto de módulos e como ele está organizado?    |

Por exemplo, ao utilizar o projeto Wordle / Termo, alguém poderia:

1. consultar a documentação do pacote `wordle` para entender sua organização;
2. consultar o módulo `game` para descobrir onde estão as regras do jogo;
3. consultar a função `avaliar_palpite()` para descobrir como utilizá-la e interpretar seu retorno.

Assim, a documentação se torna progressivamente mais específica:

```text
wordle
   ↓
game
   ↓
avaliar_palpite()
```

### 6.4 Docstrings vs Documentação do Projeto

Nem toda documentação precisa ficar dentro do código.

Docstrings são apropriadas principalmente para documentar elementos do próprio programa, como:

* funções;
* módulos;
* pacotes.

Já informações mais gerais sobre o projeto Wordle, como:

* como executar o jogo;
* quais arquivos são necessários;
* como instalar suas dependências;
* quais são as regras gerais do jogo;
* como o projeto está organizado;

podem ser colocadas em um arquivo como `README.md`.

Por exemplo:

```text
wordle/
├── __init__.py
├── main.py
├── game.py
├── words.py
├── interface.py
├── palavras.txt
└── README.md
```

Voltaremos a esse tipo de documentação ao discutir a organização e estruturação de projetos.

## 7. Comentários vs Docstrings

Comentários e docstrings possuem objetivos diferentes.

Considere novamente a avaliação de um palpite:

```python
def avaliar_palpite(palpite, palavra_secreta):
    """
    Avalia um palpite e retorna a situação de cada letra.

    Args:
        palpite (str): Palavra informada pelo jogador.
        palavra_secreta (str): Palavra que deve ser descoberta.

    Returns:
        list: Situação de cada letra do palpite.
    """

    resultado = ["⬛"] * len(palpite)

    # Cada ocorrência de uma letra na palavra secreta só pode ser utilizada uma vez.
    # Quando há letras repetidas no palpite, damos prioridade às ocorrências
    # que estão na posição correta, que não necessariamente são as primeiras.
    ...
```

A docstring explica **como utilizar a função**.

O comentário explica **uma decisão interna da implementação**.

Essa distinção é uma das ideias principais desta aula.

## 8. Aplicando ao Wordle / Termo

Considere as principais funções desenvolvidas para o jogo, por exemplo:

```python
carregar_palavras(...)
escolher_palavra(...)
avaliar_palpite(...)
validar_palpite(...)
jogar(...)
```

Para cada função, podemos perguntar:

1. Qual é a responsabilidade da função?
2. Quais informações ela recebe?
3. O que cada parâmetro representa?
4. O que ela retorna?
5. Existem comportamentos que não são óbvios?
6. É necessário algum comentário dentro da implementação?

A ideia não é adicionar comentários em todas as linhas nem escrever docstrings enormes.

O objetivo é fornecer informação suficiente para que outra pessoa consiga utilizar e modificar o programa com segurança.

### 8.1 Exercício

Escolha funções da implementação do Wordle / Termo e adicione documentação adequada.

Para cada função:

* escreva uma docstring;
* documente seus parâmetros;
* documente o retorno, quando houver;
* identifique trechos em que um comentário realmente agregaria informação;
* remova comentários que apenas repitam o código.

Ao final, tente utilizar uma das funções consultando apenas sua docstring, sem analisar sua implementação.
