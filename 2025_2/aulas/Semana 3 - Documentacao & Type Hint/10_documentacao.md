# Documentação

À medida que a aplicação cresce em tamanho e complexidade, e mais desenvolvedores se envolvem no projeto, 
a documentação do código se torna essencial. Alguns motivos para priorizá-la são:

### Clareza e Compreensão

- **Facilidade de Entendimento:** Documentação clara ajuda desenvolvedores a entender rapidamente o propósito e funcionamento do código.
- **Redução de Ambiguidades:** Especifica funcionalidades, parâmetros e retornos, evitando mal-entendidos.

### Manutenção e Evolução

- **Facilidade de Manutenção:** Código bem documentado é mais fácil de atualizar e entender as mudanças.
- **Histórico de Mudanças:** Serve como registro das intenções e decisões durante o desenvolvimento.

### Colaboração e Reutilização

- **Melhoria na Colaboração:** Oferece um ponto de referência comum para equipes, facilitando a colaboração.
- **Facilidade de Reutilização:** Permite que o código seja reutilizado facilmente em outros projetos.

### Qualidade e Confiabilidade

- **Aumento da Qualidade:** Garante que o código atenda aos requisitos e expectativas.
- **Facilidade de Testes:** Ajuda na criação de testes eficazes ao fornecer uma referência clara do que deve ser testado.

A partir desses motivos, a ideia da aula de hoje é explicar brevemente as diferentes formas de documentar o código.

## Níveis de Documentação

Para garantir uma documentação eficaz e organizada, é útil dividi-la em três níveis principais:

1. **Bloco de Código:** Comentários diretos no código para explicar trechos específicos e facilitar a manutenção.
2. **Função:** Docstrings que descrevem o propósito da função, seus parâmetros e retornos, facilitando o uso e a compreensão.
3. **Módulo / Pacote:** Descrição geral do módulo e suas principais principais funcionalidades, oferecendo uma visão geral e exemplos de uso.

## Bloco de Código

Comentários inseridos diretamente no código para explicar o funcionamento de trechos específicos.
Esse tipo de documentação é voltado principalmente para desenvolvedores responsáveis pela manutenção, auxiliando na compreensão rápida do código ao identificar e corrigir bugs ou aprimorar funcionalidades existentes.

### Como Documentar Blocos de Código

- **Símbolo de Comentário (`#`):** Em Python, comentários são iniciados com `#`. Tudo o que estiver à direita desse símbolo na mesma linha será considerado um comentário e não será executado pelo interpretador.
- **Objetivo dos Comentários:** A principal função dos comentários em blocos de código é explicar a **lógica de negócio** ou **decisões de design** que não são imediatamente óbvias apenas olhando para o código. Isso inclui explicar o propósito de um trecho de código, por que uma determinada abordagem foi escolhida, ou como uma parte específica do código interage com outras partes da aplicação.
- **Localização dos Comentários:** Comentários devem ser colocados em trechos onde a lógica é complexa, onde há algum comportamento não trivial ou onde o código poderia ser difícil de entender sem uma explicação adicional.

Por exemplo, em um código que busca um elemento dentro de uma lista ordenada, você pode usar comentários para explicar como os elementos estão sendo comparados de forma eficiente.

### Boas Práticas

- **Seja Claro e Conciso:** Comentários devem ser claros, explicando o que o código faz de maneira direta e objetiva. Evite escrever comentários longos e complicados que podem confundir mais do que ajudar.
- **Explique a Lógica:** Descreva a lógica por trás de um trecho de código, especialmente se a abordagem utilizada não for trivial.
- **Evite Redundância:** Não comente coisas óbvias que já estão claras no código, como "incrementa i". Comente o que não está imediatamente evidente.

**Exemplo de Boa Prática:**

```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    # Continuar a busca enquanto houver uma sublista válida
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        # Se o elemento do meio for menor que o alvo, ignorar a metade esquerda
        # Porque todos os elementos à esquerda são ainda menores
        elif arr[mid] < target:
            left = mid + 1
        # Se o elemento do meio for maior que o alvo, ignorar a metade direita
        # por motivo analago ao explicado acima
        else:
            right = mid - 1
    
    return None
```

Os comentários adicionados são úteis porque:
* **Esclarecem a Lógica**: Eles explicam por que podemos ignorar metade da lista quando `arr[mid] < target`, destacando que, devido à ordenação da lista, todos os elementos à esquerda de `mid` serão menores que o alvo.
* **Contextualizam a Decisão**: O comentário explica a eficiência da busca binária, ajudando outros desenvolvedores a entenderem não apenas o que o código faz, mas por que essa abordagem é válida e eficiente.

### Más Práticas

* **Comentários Vagamente Descritivos**: Comentários que apenas repetem o que o código faz, sem fornecer contexto ou explicação adicional, não são úteis.
* **Falta de Comentários**: Não documentar blocos de código que contenham lógica complexa ou não óbvia pode tornar o código difícil de entender e manter.
* **Comentários Desatualizados**: Comentários que não refletem mais o que o código faz, após uma mudança no código, podem ser enganosos.

Aqui, os comentários são muito genéricos e não explicam a lógica de como os elementos das listas estão sendo comparados e mesclados, o que reduz a utilidade dos comentários.

```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    # loop enquanto left <= right
    while left <= right:
        mid = (left + right) // 2
        
        # se for igual, retornar mid
        if arr[mid] == target:
            return mid
        # se for menor, ajustar left
        elif arr[mid] < target:
            left = mid + 1
        # se for maior, ajustar right
        else:
            right = mid - 1
    
    # não encontrou, retornar None
    return None
```

Os comentários acima são problemáticos porque:
* **São Redundantes**: Comentários como `loop enquanto left <= right` apenas repetem o que o código já faz, sem fornecer nenhuma explicação adicional ou contexto útil.
* **Faltam Contexto**: Comentários como `se for igual, retornar mid` não ajudam a entender a lógica do algoritmo, deixando o leitor sem uma compreensão clara de como e por que a busca binária funciona.

## Função

Docstrings que descrevem o propósito da função, seus parâmetros e retornos, facilitando o entendimento e o uso correto por outros desenvolvedores.
Com essa documentação, é possível utilizar a função adequadamente sem a necessidade de analisar detalhadamente sua implementação interna.

### O que são Docstrings

Docstrings (ou `"document strings"`) são strings de documentação que são usadas para descrever módulos e funções em Python.
Elas são colocadas logo após a definição de um módulo ou função e são envolvidas por três aspas duplas `"""`. 
As docstrings são uma maneira padrão e conveniente de documentar o código e fornecem uma forma de obter informações sobre o que uma parte do código faz sem precisar ler seu código fonte.

### PEP 257 e Estilos de Documentação

O PEP 257 é um documento que define convenções para docstrings em Python.
Ele estabelece diretrizes para a formatação e estruturação das docstrings, promovendo consistência na documentação. De acordo com o PEP 257, uma docstring deve ser uma frase ou parágrafo que explique claramente o propósito e a funcionalidade do código.
Além disso, o PEP 257 sugere que a primeira linha da docstring deve ser uma breve descrição, seguida por uma explicação mais detalhada, se necessário.

Existem vários estilos para escrever docstrings, e alguns dos mais comuns são:
* Google Style
* NumPy Style
* Sphinx Style

### O que Documentar

Em uma docstring, é importante documentar:
* **Descrição Geral**: O que a função ou módulo faz;
* **Parâmetros**: Para funções e métodos, documente os parâmetros esperados, incluindo nome, tipo e descrição;
* **Retornos**: Para funções e métodos, documente o tipo e a descrição dos valores retornados;
* **Exceções**: Liste quaisquer exceções que a função ou método possa lançar;
* **Exemplos**: Forneça exemplos de uso, quando apropriado, para ilustrar como a função ou classe deve ser usada.

### Exemplos de Estilos

#### Google Style

```python
def add_numbers(a, b):
    """
    Adiciona dois números.

    Args:
        a (int): O primeiro número.
        b (int): O segundo número.

    Returns:
        int: A soma de `a` e `b`.

    Examples:
        >>> add_numbers(2, 3)
        5
        >>> add_numbers(-1, 1)
        0
    """
    return a + b
```

Características:
* Usa palavras-chave como `Args`, `Returns`, e `Examples`.
* Descrições claras e diretas dos parâmetros e retornos.

#### NumPy Style

```python
def add_numbers(a, b):
    """
    Adiciona dois números.

    Parameters
    ----------
    a : int
        O primeiro número.
    b : int
        O segundo número.

    Returns
    -------
    int
        A soma de `a` e `b`.

    Examples
    --------
    >>> add_numbers(2, 3)
    5
    >>> add_numbers(-1, 1)
    0
    """
    return a + b
```

Características:
* Usa seções como `Parameters`, `Returns`, e `Examples`.
* Seções formatadas com cabeçalhos e descrições detalhadas.

#### Sphinx Style

```python
def add_numbers(a, b):
    """
    Adiciona dois números.

    :param a: O primeiro número.
    :type a: int
    :param b: O segundo número.
    :type b: int
    :return: A soma de `a` e `b`.
    :rtype: int

    **Exemplos**:

    >>> add_numbers(2, 3)
    5
    >>> add_numbers(-1, 1)
    0
    """
    return a + b
```

Características:
* Usa diretivas como `:param`, `:type`, `:return`, e `:rtype`.
* Formatação baseada em diretivas que podem ser processadas pelo Sphinx para gerar documentação.

## Módulo / Pacote

A documentação de um módulo ou pacote deve oferecer uma visão geral clara e concisa de seu propósito e funcionalidades principais.
Ela deve descrever o que o módulo ou pacote faz, como ele se encaixa no projeto e fornecer exemplos básicos de uso para facilitar a compreensão e a integração.

Na prática, a documentação de um módulo tende a ser sucinta, focando em uma breve explicação do seu propósito.
No entanto, para maior clareza e utilidade, a documentação pode incluir detalhes adicionais, como principais atributos e funções, exemplos de uso, e informações sobre o autor e a licença de uso.


### Exemplo de Documentação de Módulo

Para um módulo chamado data.py, a documentação pode ser estruturada da seguinte forma:

```python
"""
Este módulo é responsável por carregar e salvar arquivos e dados utilizados na aplicação.

Attributes
----------
PI : float
    Valor de PI até a 5ª casa decimal.

Functions
---------
load(filepath)
    Carrega dados a partir do caminho especificado.
save(filepath, data)
    Salva os dados no caminho especificado.

Exemples
--------
    >>> import data
    >>> data.load("dados.csv")
    >>> data.save("saida.csv", data_to_save)

Author
-----_
    Seu Nome <seu.email@example.com>

License:
--------
    MIT License
"""
```

### Exemplo de Documentação de Pacote

Para um pacote chamado `analytics`, a documentação pode ser assim:

```python
"""
analytics

Este pacote fornece ferramentas para análise e visualização de dados.

Modules
-------
data_loader
    Responsável por carregar e pré-processar dados.
statistics
    Contém funções para cálculos estatísticos.
visualization
    Fornece utilitários para criar gráficos e visualizações.

Exemples
--------
    >>> import analytics

    >>> # Carregar dados
    >>> data = analytics.data_loader.load("dados.csv")

    >>> # Calcular estatísticas
    >>> stats = analytics.statistics.calculate_mean(data)

    >>> # Visualizar dados
    >>> analytics.visualization.plot(data)

Author
------
    Seu Nome <seu.email@example.com>

License
-------
    MIT License
"""
```
