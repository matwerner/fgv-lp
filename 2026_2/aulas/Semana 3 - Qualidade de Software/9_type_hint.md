# Aula 8: Type Hints

Na aula anterior, vimos como comentários e docstrings podem ajudar a documentar nosso código.

Por exemplo, uma das funções do Wordle / Termo poderia ser documentada da seguinte forma:

```python
def avaliar_palpite(palpite, palavra_secreta):
    """
    Avalia um palpite em relação à palavra secreta.

    Args:
        palpite (str): Palavra informada pelo jogador.
        palavra_secreta (str): Palavra que deve ser descoberta.

    Returns:
        str: Resultado da avaliação das letras.
    """
```

Nesse caso, utilizamos a docstring não apenas para explicar o significado dos parâmetros, mas também para informar seus tipos.

Mas podemos colocar parte dessa informação diretamente na definição da função.

## 1. Type Hints

**Type Hints** são anotações utilizadas para indicar os tipos esperados para variáveis, parâmetros e retornos de funções.

Por exemplo:

```python
def avaliar_palpite(palpite: str, palavra_secreta: str) -> str:
    ...
```

Agora conseguimos observar diretamente na assinatura da função que:

* `palpite` deve ser uma `str`;
* `palavra_secreta` deve ser uma `str`;
* a função retorna uma `str`.

Isso torna o código mais fácil de compreender e também fornece informações para ferramentas de desenvolvimento, como IDEs e verificadores estáticos de tipos.

### 1.1 Type Hints e Docstrings

Type Hints não substituem as docstrings.

Com Type Hints, podemos evitar repetir algumas informações:

```python
def avaliar_palpite(palpite: str, palavra_secreta: str) -> str:
    """
    Avalia um palpite em relação à palavra secreta.

    Args:
        palpite: Palavra informada pelo jogador.
        palavra_secreta: Palavra que deve ser descoberta.

    Returns:
        Resultado da avaliação das letras.
    """
```

Nesse caso:

* o **Type Hint** informa qual é o tipo;
* a **docstring** explica o que aquele valor representa.

Por exemplo, saber que `palpite` é uma `str` não explica que ela representa a palavra informada pelo jogador.

### 1.2 Type Hints não Alteram a Tipagem do Python

Adicionar Type Hints não transforma Python em uma linguagem estaticamente tipada.

Considere:

```python
def soma(a: int, b: int) -> int:
    return a + b
```

Apesar das anotações, Python não impede automaticamente uma chamada como:

```python
soma("Olá", " Mundo")
```

O programa ainda pode ser executado.

Os Type Hints são principalmente utilizados para:

* documentar expectativas sobre os tipos;
* auxiliar IDEs;
* fornecer autocomplete mais preciso;
* permitir análise estática do código;
* identificar possíveis erros antes da execução.

Posteriormente veremos uma ferramenta capaz de utilizar essas anotações para verificar possíveis inconsistências.

## 2. Sintaxe Básica

Para indicar o tipo de um parâmetro, utilizamos `:` após seu nome.

Para indicar o tipo retornado pela função, utilizamos `->`.

```python
def escolher_palavra(palavras: list[str]) -> str:
    ...
```

A função recebe uma lista de strings e retorna uma string.

Podemos aplicar Type Hints às funções que já desenvolvemos para o Wordle:

```python
def avaliar_palpite(palpite: str, palavra_secreta: str) -> str:
    ...
```

```python
def carregar_palavras(caminho: str) -> list[str]:
    ...
```

```python
def escolher_palavra(palavras: list[str]) -> str:
    ...
```

```python
def validar_palpite(palpite: str, palavras: list[str]) -> bool:
    ...
```

```python
def ler_palpite() -> str:
    ...
```

Observe que uma função sem parâmetros também pode indicar seu tipo de retorno.

### 2.1 Funções que não Retornam Valores

Quando uma função não possui um retorno significativo, podemos utilizar `None`:

```python
def exibir_resultado(resultado: str) -> None:
    print(resultado)
```

Outro exemplo:

```python
def jogar() -> None:
    ...
```

Nesse caso, `-> None` deixa explícito que a função é utilizada por seu comportamento e não para produzir um valor a ser utilizado pelo código que a chamou.

### 2.2 Anotações em Variáveis

Também podemos adicionar Type Hints diretamente a variáveis:

```python
palavra_secreta: str = "PAUSE"
numero_tentativas: int = 0
jogo_encerrado: bool = False
```

Normalmente, quando o tipo é evidente pelo valor atribuído, a anotação pode ser desnecessária:

```python
palavra_secreta = "PAUSE"
```

Entretanto, anotações podem ser úteis em situações nas quais queremos deixar explícita a intenção de determinada variável.

## 3. Tipos de Dados

Os tipos que já conhecemos podem ser utilizados diretamente como Type Hints.

### 3.1 Tipos Simples

Alguns exemplos:

* `int`
* `float`
* `str`
* `bool`

```python
def calcular_pontuacao(vitorias: int, derrotas: int) -> float:
    return vitorias / (vitorias + derrotas)
```

No Wordle:

```python
def validar_tamanho(palpite: str, tamanho: int) -> bool:
    return len(palpite) == tamanho
```

### 3.2 Coleções

Também podemos indicar os tipos armazenados dentro das estruturas de dados.

#### Listas

Uma lista de strings:

```python
palavras: list[str]
```

Por exemplo:

```python
def carregar_palavras(caminho: str) -> list[str]:
    ...
```

#### Conjuntos

Um conjunto de letras:

```python
letras_usadas: set[str]
```

Por exemplo:

```python
def obter_letras_usadas(palpites: list[str]) -> set[str]:
    ...
```

#### Dicionários

Também podemos indicar separadamente o tipo das chaves e dos valores:

```python
dict[tipo_chave, tipo_valor]
```

Por exemplo:

```python
def contar_letras(palavra: str) -> dict[str, int]:
    contagem = {}

    for letra in palavra:
        contagem[letra] = contagem.get(letra, 0) + 1

    return contagem
```

Nesse caso:

```python
dict[str, int]
```

indica que:

* as chaves são strings;
* os valores são inteiros.

#### Tuplas

Também podemos indicar o tipo de cada posição de uma tupla:

```python
tuple[str, int]
```

Por exemplo:

```python
def obter_resultado() -> tuple[str, int]:
    return ("Vitória", 4)
```

Nesse caso, a tupla contém uma `str` seguida de um `int`.

### 3.3 Combinando Tipos

Type Hints podem representar estruturas mais complexas.

Por exemplo:

```python
dict[str, list[str]]
```

representa um dicionário:

* com chaves do tipo `str`;
* cujos valores são listas de strings.

Um possível exemplo para diferentes temas do Wordle:

```python
palavras_por_tema: dict[str, list[str]] = {
    "animais": ["TIGRE", "PORCO"],
    "objetos": ["PORTA", "PRATO"]
}
```

## 4. Valores Opcionais e Múltiplos Tipos

Existem situações em que um valor pode possuir mais de um tipo possível.

### 4.1 Um Tipo ou `None`

Considere uma função que procura uma palavra:

```python
def buscar_palavra(palavras: list[str], prefixo: str) -> str | None:
    for palavra in palavras:
        if palavra.startswith(prefixo):
            return palavra

    return None
```

O retorno:

```python
str | None
```

indica que a função pode retornar:

* uma `str`, caso encontre uma palavra;
* `None`, caso nenhuma palavra seja encontrada.

Isso deixa explícito que quem utiliza a função deve considerar as duas possibilidades:

```python
palavra = buscar_palavra(palavras, "PA")

if palavra is None:
    print("Nenhuma palavra encontrada.")
else:
    print(palavra)
```

### 4.2 Múltiplos Tipos

O operador `|` também pode indicar que mais de um tipo é aceito.

Por exemplo:

```python
def exibir_mensagem(mensagem: str | int) -> None:
    print(mensagem)
```

Nesse caso, `mensagem` pode ser uma `str` ou um `int`.

Entretanto, permitir muitos tipos diferentes normalmente torna uma função mais difícil de compreender.

Sempre que possível, é interessante que funções possuam contratos simples e previsíveis.

### 4.3 `Optional` e `Union`

Também é possível encontrar código utilizando o módulo `typing`:

```python
from typing import Optional, Union
```

Por exemplo:

```python
Optional[str]
```

representa uma `str` ou `None`.

E:

```python
Union[str, int]
```

representa uma `str` ou um `int`.

Em versões modernas do Python, podemos escrever essas mesmas ideias de forma mais direta:

```python
str | None
```

e:

```python
str | int
```

Nesta disciplina, utilizaremos preferencialmente essa sintaxe.

## 5. Verificação Estática de Tipos

Como vimos, Python não utiliza Type Hints para impedir automaticamente a execução de código com tipos incompatíveis.

Entretanto, ferramentas podem analisar essas anotações **antes da execução do programa**.

Chamamos esse processo de **verificação estática de tipos**.

Considere:

```python
def escolher_palavra(palavras: list[str]) -> str:
    ...
```

Agora fazemos:

```python
escolher_palavra("palavras.txt")
```

Existe uma inconsistência:

* a função espera `list[str]`;
* foi fornecida uma `str`.

Python pode tentar executar esse código, mas uma ferramenta de análise estática pode identificar o problema antecipadamente.

### 5.1 MyPy

MyPy é uma ferramenta de verificação estática de tipos para Python.

Podemos instalá-la utilizando:

```shell
pip install mypy
```

E verificar um arquivo:

```shell
mypy wordle.py
```

Considere:

```python
def escolher_palavra(palavras: list[str]) -> str:
    return palavras[0]


escolher_palavra("palavras.txt")
```

Ao analisar o código, o MyPy pode indicar que uma `str` foi fornecida onde era esperada uma `list[str]`.

### 5.2 Outro Exemplo

Considere:

```python
def carregar_palavras(caminho: str) -> list[str]:
    ...
```

Agora:

```python
palavras: list[str] = carregar_palavras("palavras.txt")
```

As anotações ajudam a ferramenta a acompanhar os tipos pelo programa.

Se posteriormente fizermos algo incompatível:

```python
numero: int = palavras
```

um verificador estático pode identificar a inconsistência sem precisar executar o programa.

### 5.3 IDEs

IDEs como Visual Studio Code e PyCharm também utilizam Type Hints para:

* autocomplete;
* sugestões de métodos;
* identificação de possíveis erros;
* navegação pelo código;
* apresentação da assinatura das funções.

Por exemplo, sabendo que:

```python
def normalizar_palavra(palavra: str) -> str:
    return palavra.strip().upper()
```

a IDE sabe que `palavra` é uma `str` e pode sugerir operações relacionadas a strings dentro da função.

## 6. PEP 8: Guia de Estilo para Python

Além de documentar e explicitar os tipos utilizados pelo programa, também é importante manter uma forma consistente de escrever o código.

O **PEP 8** é o guia de estilo para código Python.

Ele apresenta convenções relacionadas a:

* indentação;
* espaços;
* nomes;
* organização das linhas;
* formatação geral do código.

Essas regras não alteram o comportamento do programa.

Seu objetivo é tornar o código mais consistente e legível.

### 6.1 Indentação

Python utiliza indentação como parte de sua sintaxe.

A convenção é utilizar **4 espaços por nível de indentação**:

```python
def validar_palpite(palpite: str) -> bool:
    if len(palpite) == 5:
        return True

    return False
```

### 6.2 Nomes de Variáveis e Funções

Variáveis e funções normalmente utilizam `snake_case`:

```python
palavra_secreta = "PAUSE"

def avaliar_palpite():
    ...
```

Evite nomes pouco descritivos:

```python
p = "PAUSE"
```

Prefira:

```python
palavra_secreta = "PAUSE"
```

O nome da variável também funciona como uma forma de documentação.

### 6.3 Constantes

Valores que representam constantes normalmente são escritos utilizando letras maiúsculas:

```python
MAX_TENTATIVAS = 6
TAMANHO_PALAVRA = 5
```

Por exemplo:

```python
for tentativa in range(MAX_TENTATIVAS):
    ...
```

Isso é mais expressivo do que:

```python
for tentativa in range(6):
    ...
```

### 6.4 Espaços

Prefira:

```python
resultado = a + b
```

em vez de:

```python
resultado=a+b
```

Da mesma forma:

```python
avaliar_palpite(palpite, palavra_secreta)
```

em vez de:

```python
avaliar_palpite( palpite,palavra_secreta )
```

### 6.5 Linhas em Branco

Utilize linhas em branco para separar partes logicamente distintas do código.

Por exemplo:

```python
def carregar_palavras(caminho: str) -> list[str]:
    ...


def escolher_palavra(palavras: list[str]) -> str:
    ...
```

Isso ajuda a identificar visualmente onde uma função termina e outra começa.

### 6.6 Comprimento das Linhas

O PEP 8 recomenda limitar as linhas a aproximadamente 79 caracteres.

Quando uma instrução fica muito longa, podemos quebrá-la em múltiplas linhas:

```python
def avaliar_palpite(
    palpite: str,
    palavra_secreta: str
) -> str:
    ...
```

O mais importante é manter o código legível e seguir uma convenção consistente dentro do projeto.

## 7. Aplicando ao Wordle / Termo

Podemos agora adicionar Type Hints às principais funções da aplicação:

```python
def carregar_palavras(caminho: str) -> list[str]:
    ...


def escolher_palavra(palavras: list[str]) -> str:
    ...


def validar_palpite(
    palpite: str,
    palavras: list[str]
) -> bool:
    ...


def avaliar_palpite(
    palpite: str,
    palavra_secreta: str
) -> str:
    ...


def ler_palpite() -> str:
    ...


def exibir_resultado(resultado: str) -> None:
    ...


def jogar() -> None:
    ...
```

Agora, apenas observando as assinaturas, já conseguimos obter bastante informação sobre como essas funções se relacionam:

```text
carregar_palavras()
        ↓
    list[str]
        ↓
escolher_palavra()
        ↓
       str
```

Da mesma forma:

```text
ler_palpite()
      ↓
     str
      ↓
avaliar_palpite()
      ↓
     str
      ↓
exibir_resultado()
```

Os Type Hints tornam mais explícito o **fluxo de dados** da aplicação.

## 8. Exercício

Adicione Type Hints às funções desenvolvidas para o Wordle / Termo.

Considere, por exemplo:

```python
carregar_palavras(...)
escolher_palavra(...)
validar_palpite(...)
avaliar_palpite(...)
ler_palpite(...)
exibir_resultado(...)
jogar(...)
```

Para cada função:

* identifique os tipos dos parâmetros;
* identifique seu tipo de retorno;
* utilize tipos específicos para coleções, como `list[str]`;
* utilize `-> None` quando a função não possuir retorno significativo;
* verifique se a docstring continua repetindo informações que agora já aparecem nos Type Hints.

Depois, introduza propositalmente algumas chamadas incorretas e observe como sua IDE ou o MyPy reage.

Por exemplo:

```python
escolher_palavra("palavras.txt")
```

```python
avaliar_palpite(12345, "PAUSE")
```

```python
exibir_resultado(["🟩", "⬛", "🟨"])
```
