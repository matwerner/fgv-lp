# Introdução ao Pandas

Pandas é uma das bibliotecas mais populares para análise de dados em Python.
Ele oferece estruturas de dados de alto desempenho e ferramentas para manipulação de dados tabulares e rotulados.
Essas ferramentas facilitam o processo de limpeza, transformação, e análise de grandes conjuntos de dados, tarefas comuns na ciência de dados e em outros campos.

## 1. Por que usar Pandas?

* Operações como selecionar, filtrar, agrupar e agregar dados são feitas de forma intuitiva.
* Oferece suporte a dados rotulados (com índices) e dados tabulares, facilitando a manipulação de dados semelhantes aos encontrados em planilhas ou bancos de dados.
* Ferramentas poderosas para leitura e escrita de diversos formatos de arquivos (CSV, Excel, SQL, etc.).
* Integração com outras bibliotecas populares como NumPy, Matplotlib e Scikit-learn.

### Exemplo de contexto real

* Imagine que você tem um CSV com dados de vendas de uma loja, onde cada coluna representa um aspecto (data, valor, produto).
O Pandas permite ler, manipular e analisar esse tipo de arquivo com facilidade.

## 2. Estrutura Unidimensional: Series

### A. O que é uma `Series`?
* Uma Series no Pandas é uma estrutura de dados unidimensional, semelhante a uma coluna de uma tabela ou a um array do NumPy, mas com a adição de índices personalizados.
* Esses índices permitem que você acesse os dados de maneira mais intuitiva, como se estivesse trabalhando com um dicionário Python.

### B. Exemplo básico

```python
import pandas as pd

dados = [10, 20, 30, 40]
serie = pd.Series(dados, index=['a', 'b', 'c', 'd'])
print(serie)
# a    10
# b    20
# c    30
# d    40
# dtype: int64
```
Aqui, a Series contém valores `[10, 20, 30, 40]` e tem índices personalizados `['a', 'b', 'c', 'd']`.

### C. Conceitos-chave:

* **Index**:
Cada elemento na Series possui um rótulo (ou índice), que pode ser numérico ou alfabético.
* **Header (Cabeçalho)**:
Em uma Series, o cabeçalho é o nome da própria coluna, que pode ser atribuído para facilitar a interpretação.


## 3. Diferenças de Series em Relação ao ndarray

### A. Índices (Index) Personalizados
* Ao contrário dos arrays do NumPy, as Series podem ter índices personalizados (não apenas numéricos).
* Isso facilita a manipulação de dados rotulados e permite o uso de nomes amigáveis ao invés de apenas números.

```python
# Criando uma Series com índices personalizados
cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre', 'Curitiba']
temperaturas = [30, 35, 28, 25, 27]
series_temp = pd.Series(temperaturas, index=cidades)
# Saída
print(series_temp)
# São Paulo         30
# Rio de Janeiro    35
# Belo Horizonte    28
# Porto Alegre      25
# Curitiba          27
# dtype: int64
```

### B. Cabeçalhos (Header)
* O header nas Series é o nome associado à coluna.
* Embora uma Series tenha apenas uma coluna, a presença de cabeçalhos se torna mais útil ao trabalhar com `DataFrames`.

```python
# Atribuindo um nome à Series
series_temp.name = 'Temperatura (°C)'
# Saída
print(series_temp)
# São Paulo         30
# Rio de Janeiro    35
# Belo Horizonte    28
# Porto Alegre      25
# Curitiba          27
# Name: Temperatura (°C), dtype: int64
```

### C. Vantagens e desvantagens das Series

* Vantagens:
    * Acesso Intuitivo:
    Acesso aos dados por rótulos em vez de apenas por posições.
    * Flexibilidade:
    Permite operações de filtragem, agregação e transformação de maneira mais fácil.
    * Interoperabilidade:
    Fácil integração com outras estruturas de dados e bibliotecas.

* Desvantagens:
    * Operações Matemáticas mais Lentas:
    O NumPy é otimizado para operações numéricas em larga escala devido ao seu uso de arrays densos e homogêneos, enquanto o Pandas foi projetado para a manipulação de dados heterogêneos e rotulados.
    * Foco em Dados Tabulares:
    O Pandas foi projetado para manipulação de planilhas e dados rotulados, não sendo a melhor escolha para operações matemáticas puras, onde o NumPy é mais eficiente.

### D. Quando usar Pandas vs NumPy?

* `Pandas`: ideal para manipulação e análise de dados tabulares e rotulados. Use Pandas quando você precisa trabalhar com grandes datasets em formato de planilhas.
* `NumPy`: mais adequado para cálculos numéricos massivos e computação de alta performance. Ele é perfeito para operações como álgebra linear, transformações de matrizes, etc.

## 4. Operações básicas

### Parâmetros index e name

* `index`: Define os rótulos dos elementos na Series. Pode ser numérico ou alfabético.
* `name`: Nomeia a Series. Útil quando se trabalha com múltiplas Series ou DataFrames para identificar e distinguir entre diferentes conjuntos de dados.

```python
serie = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'], name='Valores')
print(serie)
print(serie.name)  # Saída: Valores
```

### Acessando Dados

Os métodos abaixo são essenciais para acessar valores de uma Series de maneira eficiente e controlada:
* `at`: Acessa um único valor pela etiqueta do índice (rótulo).
* `iat`: Acessa um único valor pela posição numérica (como em um array).
* `loc`: Acessa um ou mais valores pela etiqueta.
* `iloc`: Acessa um ou mais valores pela posição numérica.

```python
serie = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

# Usando at e iat para acessar elementos individuais
print(serie.at['b'])   # Saída: 20
print(serie.iat[1])    # Saída: 20

# Usando loc e iloc para acessar múltiplos elementos
print(serie.loc['b':'d'])  # Saída: b 20, c 30, d 40
print(serie.iloc[1:3])     # Saída: b 20, c 30
```

### Estatísticas

* Diferente do numpy, pandas já vem com uma função especifica para exibir estátisticas de uma distribuição de valores 
* O método `describe()` do Pandas é uma maneira rápida e eficiente de obter estatísticas descritivas de uma Series, como `média`, `desvio padrão`, `valor mínimo`, `máximo`, `etc`.

```python
serie = pd.Series([10, 20, 30, 40, 50, 60])
estatisticas = serie.describe()
print(estatisticas)
# Saída:
# count     6.000000
# mean     35.000000
# std      18.708287
# min      10.000000
# 25%      22.500000
# 50%      35.000000
# 75%      47.500000
# max      60.000000
```

## 5. Lendo uma Series de um Arquivo de Texto

* Criar um arquivo `dados_com_indice.txt` com o seguinte conteúdo:
    ```python
    Indice,Valor
    a,10
    b,20
    c,30
    d,40
    ```
* Ler o arquivo e criar uma Series com índices personalizados:
    ```python
    import pandas as pd

    # Lendo o arquivo txt com cabeçalhos e índices
    serie = pd.read_csv('dados_com_indice.txt', index_col='Indice', squeeze=True)
    print(serie)
    ```
* Explicação:
    * `index_col='Indice'` define a coluna que será usada como índice para a Series.
    * `squeeze=True` é usado para garantir que o DataFrame seja convertido em uma Series, se houver uma única coluna.

## 6. Exercícios

1. Criar uma Series a partir de uma lista de dados e índices personalizados.
    ```python
    produtos = ['Caneta', 'Lápis', 'Caderno', 'Borracha', 'Estojo']
    quantidades = [150, 200, 120, 80, 60]
    ```
2. Realizar operações matemáticas com a Series e comparar com um ndarray.
3. Utilizar `at`, `iat`, `loc` e `iloc` para acessar elementos específicos da Series.
4. Aplicar o método `describe()` em uma Series criada e interpretar os resultados.
