# Type Hint

## 1. O que é?

Type Hint em Python é uma forma de indicar o tipo de dado que uma variável, função ou método deve receber ou retornar.
Embora não sejam obrigatórios, os Type Hints desempenham um papel importante na melhoria da legibilidade e da manutenção do código.

As ferramentas de desenvolvimento, como IDEs (por exemplo, Visual Studio Code), utilizam os Type Hints para oferecer funcionalidades como o autocomplete.
Por exemplo, ao passar uma variável como argumento em uma função, a IDE pode sugerir métodos e funções associados ao tipo de dado da variável.
No entanto, dentro do escopo da função, essa sugestão pode não ocorrer, pois, em Python, qualquer tipo de variável pode ser passado como argumento, o que dificulta a dedução do tipo pelo editor.

Os Type Hints, portanto, não só documentam o código, tornando-o mais claro para outros desenvolvedores, como também ajudam as IDEs a fornecerem dicas mais precisas, facilitando o desenvolvimento.

## 2. Sintaxe Básica

Para adicionar um Type Hint a uma variável, basta adicionar dois-pontos (:) seguido do tipo de dado após o nome da variável.
Por exemplo, para especificar que uma função recebe e retorna uma string:

```python
def preprocessamento_texto(texto: str) -> str:
    texto = texto.lower()

    char_validos = []
    for c in texto:
        if c.isalnum() or c.isspace():
            char_validos.append(c)
    texto = ''.join(char_validos)

    return texto
texto = "Hello, Matheus!!!!"
novo_texto = preprocessamento_texto(texto)
print(novo_texto)
```

Como um exercício interessante, tente remover os Type Hints da função `preprocessamento_texto` 
e observe como a sua IDE se comporta, especialmente em relação às sugestões de autocomplete.

## 3. Tipos de Dados

Os tipos de dados que você já conhece podem ser usados como Type Hints, incluindo:

- **Primitivos:** `int`, `float`, `str`, `bool`
- **Compostos:** `list`, `set`, `dict`, `tuple`

```python
def soma(a: int, b: int) -> int:
    return a + b

def pegar_valores_unicos(lista: list) -> set:
    return set(lista)
```

### Especificando Tipos em Dados Compostos

Se você quiser especificar o tipo dos elementos dentro de um tipo composto, como uma lista de inteiros, não pode simplesmente usar `list[int]`.
Isso resultará em um erro no código.

Para lidar com essa situação, o Python oferece o módulo `typing`, que expande as capacidades dos Type Hints, permitindo a especificação de tipos dentro de coleções compostas.

### Usando o Módulo typing

Com o módulo typing, você pode especificar com precisão o tipo dos elementos em listas, dicionários e outras coleções:

```python
from typing import List, Dict

def processa_lista(lista: List[int]) -> List[int]:
    return [x * 2 for x in lista]

def cria_mapa() -> Dict[str, int]:
    return {"a": 1, "b": 2}
```

Explicação:
* **Listas**: `List[int]` indica uma lista onde todos os elementos são inteiros.
* **Dicionários**: `Dict[str, int]` indica um dicionário onde as chaves são strings e os valores são inteiros.

O uso de typing não só torna seu código mais claro e robusto, mas também ajuda as ferramentas de desenvolvimento a fornecerem feedback mais detalhado e preciso.

### Optional e Union

Além dos tipos básicos que você pode especificar em Type Hints, o Python oferece funcionalidades mais avançadas para lidar com situações em que uma variável, função ou método pode aceitar ou retornar múltiplos tipos de dados ou, possivelmente, nenhum dado.
Essas funcionalidades incluem `Optional` e `Union`, que também fazem parte do módulo `typing`.
Optional

#### Optional

`Optional` é utilizado quando uma variável ou retorno de função pode ser de um tipo específico ou None.
Isso é comum em situações onde um valor pode ou não estar presente.

Vantagens de usar `Optional`:
* **Documentação Explícita**: Especifica claramente que uma variável pode ter um valor do tipo definido ou None, facilitando o entendimento do código;
* **Segurança**: Ajuda a evitar erros em tempo de execução, pois torna explícita a necessidade de verificar se o valor é None antes de usá-lo;
* **Melhor Suporte das Ferramentas**: Ferramentas de análise estática podem detectar potenciais problemas quando None não é tratado adequadamente.

```python
from typing import Optional

def buscar_valor(lista: list, indice: int) -> Optional[int]:
    if 0 <= indice < len(lista):
        return lista[indice]
    return None

resultado = buscar_valor([1, 2, 3], 5)
if resultado is None:
    print("Valor não encontrado")
else:
    print(f"Valor encontrado: {resultado}")
```

Nesse exemplo, o retorno da função `buscar_valor` pode ser um `int` ou `None`, o que é indicado claramente pelo uso de `Optional[int]`.

#### Union

`Union` é utilizado quando uma variável, parâmetro ou retorno pode ser de múltiplos tipos diferentes.
Isso é útil em funções que são projetadas para lidar com mais de um tipo de entrada ou saída.

Vantagens de usar `Union`:
* **Flexibilidade**: Permite que uma função aceite ou retorne múltiplos tipos, sem a necessidade de sobrecarregar funções ou realizar verificações complexas de tipo.
* **Documentação**: Torna explícito que diferentes tipos de dados são aceitáveis, o que facilita a leitura e manutenção do código.
* **Verificação Estática**: As ferramentas de análise podem garantir que todos os tipos especificados em Union sejam tratados adequadamente.

```python
from typing import List, Union

def soma_tudo(valores: Union[List[int], List[List[int]]]) -> int:
    total = 0
    if isinstance(valores[0], int):
        # Caso em que valores é uma lista de inteiros
        total = sum(valores)
    elif isinstance(valores[0], list):
        # Caso em que valores é uma lista de listas de inteiros
        for sublista in valores:
            total += sum(sublista)
    return total

# Exemplos de uso
print(soma_tudo([1, 2, 3, 4]))  # Output: 10
print(soma_tudo([[1, 2], [3, 4]]))  # Output: 10
```

Explicação:

* Tipo `Union[List[int], List[List[int]]]`: Define que o parâmetro valores pode ser uma lista de inteiros (`List[int]`) ou uma lista de listas de inteiros (`List[List[int]]`).
* Verificação de Tipo:
    - A função `isinstance` é usada para verificar se uma variável é uma instância de um tipo de dados específico. A função retorna `True` se a variavel for uma instância do tipo de dados passado; caso contrário, retorna `False`.
    - Se o primeiro elemento de valores for um `int`, a função assume que valores é uma lista de inteiros e soma todos os valores diretamente.
    - Se o primeiro elemento for uma `list`, a função assume que valores é uma lista de listas de inteiros e itera sobre cada sublista, somando todos os valores contidos nela.

## 4. Verificação Estática com MyPy

A verificação estática de tipos é uma técnica usada para analisar o código-fonte sem executá-lo, a fim de encontrar erros e inconsistências, especialmente relacionados a tipos de dados. 

MyPy é uma ferramenta popular de verificação de tipos para Python que utiliza Type Hints para realizar a análise estática do código.
Ele verifica se as anotações de tipo são consistentes e se o código segue as expectativas definidas pelos Type Hints.
Embora os Type Hints não sejam obrigatórios em Python, MyPy permite que você adicione uma camada adicional de segurança e clareza ao seu código.

### Como Funciona

1. Para usar MyPy, você precisa instalá-lo. Isso pode ser feito facilmente usando `pip`:
    ```shell
    pip install mypy
    ```
2. MyPy pode ser executado diretamente a partir da linha de comando para verificar um arquivo Python. Por exemplo: 
    ```shell
    mypy meu_arquivo.py
    ```
3. O comando verifica o arquivo `meu_arquivo.py` e relata quaisquer inconsistências encontradas com base nas anotações de tipo.

### Exemplo

```python
from typing import List

def soma_lista(lista: List[int]) -> int:
    return sum(lista)

resultado = soma_lista([1, 2, '3'])  # Erro: '3' não é um int
```

Quando você executa MyPy nesse código, ele emitirá um erro indicando que o tipo `'3'` é incompatível com a anotação `List[int]`:

```shell
meu_arquivo.py:6: error: List item 2 has incompatible type "str"; expected "int"
```

### Configuração avançada

MyPy oferece diversas opções de configuração para personalizar a análise.
Você pode criar um arquivo de configuração `mypy.ini` para definir regras e opções específicas:

```ini
[mypy]
disallow_untyped_calls = True
disallow_untyped_defs = True
ignore_missing_imports = True
```

Essas opções permitem, por exemplo, desabilitar funções não tipadas e ignorar importações ausentes.

Para mais detalhes sobre todas as opçõses de verificação disponiveis, verificar a [documentação do MyPy](http://mypy-lang.org/).

## 5. Exercícios Práticos

(Continuando os exercícios da aula passada...)

Implemente e documente as seguintes funções:

* Função clean_text(text)
    - **Descrição**: Remove todos os caracteres não alfanuméricos do texto fornecido, retornando uma versão do mesmo contendo apenas letras e números.
    - **Entrada**: Uma string representando o texto a ser limpo.
    - **Saída**: Uma string contendo apenas letras e números.

* Função top_n_words(texts, n)
    - **Descrição**: Retorna as n palavras mais frequentes em um conjunto de textos fornecido.
    - **Entrada**: Uma lista de strings, onde cada string representa um texto, e um número inteiro n que define a quantidade de palavras mais frequentes a serem retornadas.
    - **Saída**: Uma lista de tuplas, onde cada tupla contém uma palavra e sua frequência, ordenadas pela frequência em ordem decrescente.

* Função generate_vocabulary(texts, n)

    * **Descrição**: Gera um vocabulário contendo as n palavras mais frequentes a partir de um conjunto de textos fornecido.
    * **Entrada**: Uma lista de strings, onde cada string representa um texto, e um número inteiro n que define o tamanho do vocabulário a ser gerado.
    * **Saída**: Um conjunto de palavras que compõem o vocabulário, ordenadas pela frequência em ordem decrescente, contendo até n palavras.
