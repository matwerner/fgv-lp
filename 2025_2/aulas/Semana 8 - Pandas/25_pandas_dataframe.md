# Introdução ao Pandas: DataFrames

## 1. O que é um DataFrame?

* O DataFrame é uma extensão natural da estrutura de Series que vimos na última aula.
* Enquanto uma Series representa uma única coluna de dados, um DataFrame expande essa ideia para múltiplas colunas, funcionando como uma tabela de dados com várias dimensões.
* Em termos simples, um DataFrame é uma estrutura bidimensional com rótulos (índices), similar a uma tabela que encontraríamos em planilhas, onde cada linha é uma entidade e cada coluna representa um atributo ou característica dessa entidade.

### Características principais de um DataFrame:

* **Colunas e linhas rotuladas**:
    - Cada coluna em um DataFrame tem um nome (rótulo) e pode conter um tipo de dado diferente (como números, strings, ou datas).
    - Cada linha também possui um rótulo, chamado de índice, que ajuda na identificação de cada registro.

* **Heterogeneidade de dados**:
    - Diferente de um ndarray do NumPy, onde todos os elementos devem ser do mesmo tipo, um DataFrame pode armazenar diferentes tipos de dados em colunas diferentes, como números inteiros, floats, strings e até mesmo datas.

### Exemplo ilustrativo

* Para compreender melhor, imagine a tabela abaixo, que contém dados sobre vendas de jogos de videogame, algo que já vimos em outras aulas.
* Nesta tabela, cada linha corresponde a um jogo específico, e cada coluna descreve uma propriedade daquele jogo, como o nome, a plataforma, o gênero e as vendas globais.

    |    | Name                      | Platform   |   Year | Genre        | Publisher   |   Global_Sales |
    |---:|:--------------------------|:-----------|-------:|:-------------|:------------|---------------:|
    |  0 | Wii Sports                | Wii        |   2006 | Sports       | Nintendo    |          82.74 |
    |  1 | Super Mario Bros.         | NES        |   1985 | Platform     | Nintendo    |          40.24 |
    |  2 | Mario Kart Wii            | Wii        |   2008 | Racing       | Nintendo    |          35.82 |
    |  3 | Wii Sports Resort         | Wii        |   2009 | Sports       | Nintendo    |          33.00 |
    |  4 | Pokemon Red/Pokemon Blue  | GB         |   1996 | Role-Playing | Nintendo    |          31.37 |
    |  5 | Tetris                    | GB         |   1989 | Puzzle       | Nintendo    |          30.26 |
    |  6 | New Super Mario Bros.     | DS         |   2006 | Platform     | Nintendo    |          30.01 |
    |  7 | Wii Play                  | Wii        |   2006 | Misc         | Nintendo    |          29.02 |
    |  8 | New Super Mario Bros. Wii | Wii        |   2009 | Platform     | Nintendo    |          28.62 |
    |  9 | Duck Hunt                 | NES        |   1984 | Shooter      | Nintendo    |          28.31 |

* Aqui, podemos observar que:
    - Cada linha representa um jogo individual, ou seja, uma entidade.
    - Cada coluna contém informações sobre uma característica daquele jogo, como o nome, o ano de lançamento, o gênero e as vendas globais.
    - Diferentes colunas podem conter diferentes tipos de dados, como int para o ano, float para vendas globais, e str para o nome e o gênero do jogo.

* Essas características tornam o DataFrame extremamente poderoso para manipulação de dados heterogêneos em ciência de dados, sendo amplamente utilizado para análise e visualização de grandes conjuntos de dados.

## 2. Criando DataFrames

O Pandas oferece várias maneiras de criar um DataFrame, desde a criação manual a partir de listas e arrays até a importação de arquivos externos.
A seguir, exploraremos algumas dessas abordagens.

### 2.1. A partir de listas de registros ou arrays do NumPy

* Uma das maneiras mais diretas de criar um DataFrame é utilizando listas ou arrays do NumPy.
* Nessa abordagem, cada lista (ou array) representa uma coluna de dados, e podemos nomear essas colunas ao criá-lo.

```python
import pandas as pd

dados = [
    [1, 'Ana', 23],
    [2, 'Bruno', 25],
    [3, 'Carlos', 30]
]

df = pd.DataFrame(dados, columns=['ID', 'Nome', 'Idade'])
print(df)
#    ID    Nome  Idade
# 0   1     Ana     23
# 1   2   Bruno     25
# 2   3  Carlos     30

dados_array = np.array([[1, 23], [2, 25], [3, 30]])
df = pd.DataFrame(dados_array, columns=['ID', 'Idade'])
print(df)
#    ID  Idade
# 0   1     23
# 1   2     25
# 2   3     30
```

### 2.2. A partir de um dicionário de listas

* Outra forma comum de criar um DataFrame é utilizando um dicionário.
* As chaves representam os nomes das colunas, e os valores são listas contendo os dados para essas colunas.
* Isso permite construir DataFrames de maneira muito flexível e estruturada.

```python
dados_dict = {
    'Nome': ['Ana', 'Bruno', 'Carlos'],
    'Idade': [23, 25, 30],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Curitiba']
}

df = pd.DataFrame(dados_dict)
print(df)
#      Nome  Idade          Cidade
# 0     Ana     23       São Paulo
# 1   Bruno     25  Rio de Janeiro
# 2  Carlos     30        Curitiba
```

* Outra variação é criar o DataFrame a partir de uma lista de dicionários, onde cada dicionário representa uma linha de dados.

```python
dados_lista_dicts = [
    {'Nome': 'Ana', 'Idade': 23},
    {'Nome': 'Bruno', 'Idade': 25, 'Cidade': 'Rio de Janeiro'},
    {'Nome': 'Carlos', 'Idade': 30}
]

df = pd.DataFrame(dados_lista_dicts)
print(df)
#      Nome  Idade          Cidade
# 0     Ana     23             NaN
# 1   Bruno     25  Rio de Janeiro
# 2  Carlos     30             NaN
```

### 2.3 A partir de arquivos externos (CSV, JSON)

* Em aplicações práticas, os dados geralmente vêm de arquivos externos, como arquivos CSV, planilhas Excel ou formatos JSON.
* O Pandas oferece métodos convenientes para carregar esses arquivos diretamente em um DataFrame.

```python
# O CSV (Comma Separated Values) é um dos formatos mais comuns para armazenamento de dados tabulares.
df = pd.read_csv('dados.csv', sep=',')
print(df.head())  # Exibe as primeiras 5 linhas do DataFrame

# Com o Pandas, também é possível carregar planilhas Excel diretamente.
df = pd.read_excel('dados.xlsx', sheet_name='Planilha1')
print(df.head())

# Para trabalhar com arquivos JSON, o Pandas oferece suporte à sua leitura e conversão para DataFrame.
df = pd.read_json('dados.json')
print(df.head())
```

## 3. Atributos Básicos do DataFrame

* Assim como o Series, o DataFrame também possui alguns atributos básicos:
    - **shape**: Retorna as dimensões do DataFrame (número de linhas e colunas).
    - **columns**: Lista os nomes das colunas.
    - **index**: Lista os índices (rótulos das linhas).
    - **dtypes**: Tipos de dados de cada coluna.

```python
print(df.shape)
# (10, 6)

print(df.columns)
# Index(['Name', 'Platform', 'Year', 'Genre', 'Publisher', 'Global_Sales'],

#       dtype='object')

print(df.index)
# RangeIndex(start=0, stop=10, step=1)

print(df.dtypes)
# Name             object
# Platform         object
# Year            float64
# Genre            object
# Publisher        object
# Global_Sales    float64
# dtype: object
```

## 4. Acessando e Filtrando Dados

O Pandas oferece diversas formas de acessar dados em um DataFrame, seja para visualizar, manipular ou realizar operações específicas. Vamos explorar as principais formas de acesso:

### 4.1. Acessando colunas

* Para acessar uma coluna de um DataFrame, podemos tratá-la como uma chave de dicionário ou usar o atributo com o nome da coluna.

```python
# Acessando uma única coluna
print(df['Name'])
# 0                   Wii Sports
# 1            Super Mario Bros.
# 2               Mario Kart Wii
# 3            Wii Sports Resort
# 4     Pokemon Red/Pokemon Blue
# 5                       Tetris
# 6        New Super Mario Bros.
# 7                     Wii Play
# 8    New Super Mario Bros. Wii
# 9                    Duck Hunt
# Name: Name, dtype: object
```

#### Acessando múltiplas colunas:

* Para acessar mais de uma coluna ao mesmo tempo, passamos uma lista de nomes de colunas.

```python
print(df[['Name', 'Platform']])
#                         Name Platform
# 0                 Wii Sports      Wii
# 1          Super Mario Bros.      NES
# 2             Mario Kart Wii      Wii
# 3          Wii Sports Resort      Wii
# 4   Pokemon Red/Pokemon Blue       GB
# 5                     Tetris       GB
# 6      New Super Mario Bros.       DS
# 7                   Wii Play      Wii
# 8  New Super Mario Bros. Wii      Wii
# 9                  Duck Hunt      NES
```

### 3.2. Acessando linhas com iloc e loc

* O Pandas usa os métodos `iloc` e `loc` para acessar linhas de forma mais específica:
    - `iloc`: acessa dados baseados na posição das linhas (index numérico).
    - `loc`: acessa dados baseados nos rótulos dos índices (não necessáriamente numéricos).

```python
# Exemplo com iloc:

print(df.iloc[0])
# Name            Wii Sports
# Platform               Wii
# Year                2006.0
# Genre               Sports
# Publisher         Nintendo
# Global_Sales         82.74
# Name: 0, dtype: object
# Acessando as três primeiras linhas

print(df.iloc[:3])
#                 Name Platform    Year Publisher  Global_Sales
# 0         Wii Sports      Wii  2006.0  Nintendo         82.74
# 1  Super Mario Bros.      NES  1985.0  Nintendo         40.24
# 2     Mario Kart Wii      Wii  2008.0  Nintendo         35.82

# Exemplo com loc
df2 = df.set_index('Name')
df2.loc['Mario Kart Wii']
# Platform             Wii
# Year              2008.0
# Publisher       Nintendo
# Global_Sales       35.82
# Name: Mario Kart Wii, dtype: object

print(df2.loc[['Wii Sports', 'Mario Kart Wii']])
#                 Name Platform    Year Publisher  Global_Sales
# 0         Wii Sports      Wii  2006.0  Nintendo         82.74
# 2     Mario Kart Wii      Wii  2008.0  Nintendo         35.82
```

### 3.3. Acessando elementos específicos com at e iat

* Quando precisamos acessar elementos individuais de forma eficiente, podemos usar `at` e `iat`, que funcionam como atalhos para acessar dados rapidamente.
    - `at`: para acessar elementos baseados em rótulos de índice e nome de coluna.
    - `iat`: para acessar elementos baseados na posição.

```python
print(df.iat[0, 2])
# 2006.0

print(df2.at['Wii Sports', 'Year'])
# 2006.0
```

### 3.4. Filtrando

* Assim como no NumPy e nas Series do Pandas, é possível aplicar filtros em DataFrames utilizando máscaras booleanas.
* Um filtro cria uma lista de valores booleanos (True/False) com base em uma condição aplicada aos dados, permitindo selecionar apenas as linhas que atendem a essa condição.

```python
print(df[df['Genre'] == 'Platform'])
                        Name Platform    Year     Genre Publisher  Global_Sales
1          Super Mario Bros.      NES  1985.0  Platform  Nintendo         40.24
6      New Super Mario Bros.       DS  2006.0  Platform  Nintendo         30.01
8  New Super Mario Bros. Wii      Wii  2009.0  Platform  Nintendo         28.62
```

## 4. Adição e Remoção de Linhas e Colunas

Ao trabalhar com DataFrames, é comum precisar adicionar ou remover dados de maneira eficiente.
O Pandas facilita essas operações com métodos diretos.

### 4.1. Adicionando Colunas

* Para adicionar uma nova coluna a um DataFrame, basta atribuir uma lista, array, ou um valor escalar a uma nova coluna.

```python
# Adicionando uma nova coluna 'Region' com valores padrão
df['Region'] = 'Global'
print(df.head())

# Exemplo com cálculo baseado em outra coluna:
df['Sales_Millions'] = df['Global_Sales'] * 1e6
print(df.head())
```

### 4.2. Removendo Colunas

* O método `drop()` é utilizado para remover colunas.
* Por padrão, é necessário especificar o eixo como 1 para indicar que queremos remover uma coluna.

```python
df.drop('Region', axis=1, inplace=True)
print(df.head())
```

### 4.3. Adicionando Linhas

* Para adicionar novas linhas a um DataFrame, podemos usar o método `append()` com um dicionário ou outro DataFrame.

```python
new_row = {
    'Name': 'New Game', 
    'Platform': 'PC', 
    'Year': 2023, 
    'Genre': 'Action',
    'Publisher': 'Indie',
    'Global_Sales': 1.5
}
# Depreciado -> Não mais utilizado oficialmente
df = df.append(new_row, ignore_index=True)
print(df.tail())

# Novo método
row_df = df.DataFrame([new_row])
df = df.concat([df, row_df], ignore_index=True)
```

### 4.4. Removendo Linhas

* Assim como as colunas, podemos remover linhas utilizando o método `drop()` e especificando o índice da linha que queremos remover.
Exemplo:

```python
# Removendo a linha de índice 0
df.drop(0, axis=0, inplace=True)
print(df.head())
```

## 5. Estatísticas Descritivas e Operações em DataFrames

### 5.1. Função describe()

* A função `describe()` gera estatísticas descritivas para colunas numéricas em um DataFrame, como contagem, média, desvio padrão, valores mínimos, máximos e percentis.
* No entanto, ela é mais adequada para colunas numéricas.
* Para colunas categóricas, que contêm valores como rótulos ou nomes, outras abordagens são necessárias.

```python
print(df.describe())
#               Year  Global_Sales
# count    10.000000     10.000000
# mean   1999.800000     36.939000
# std      10.282672     16.517351
# min    1984.000000     28.310000
# 25%    1990.750000     29.267500
# 50%    2006.000000     30.815000
# 75%    2007.500000     35.115000
# max    2009.000000     82.740000
```

### 5.2. Tratando colunas categóricas com value_counts()

* Para colunas categóricas (como o gênero de um jogo ou o nome de uma plataforma), em vez de calcular média ou desvio padrão, é mais útil contar a frequência de cada categoria.
* Para isso, usamos a função `value_counts()`, que retorna a contagem de ocorrências de cada valor único.

```python
# Contagem de ocorrências de cada gênero de jogo
print(df['Genre'].value_counts())
# Genre
# Platform        3
# Sports          2
# Racing          1
# Role-Playing    1
# Puzzle          1
# Misc            1
# Shooter         1
# Name: count, dtype: int64
```

### 5.3. Estatísticas específicas

* Além do describe(), outras operações matemáticas e estatísticas podem ser realizadas nas colunas numéricas de um DataFrame, tais como:
    - Soma de valores: `df['Global_Sales'].sum()`
    - Média dos valores: `df['Global_Sales'].mean()`
    - Valor máximo: `df['Global_Sales'].max()`
    - Valor mínimo: `df['Global_Sales'].min()`

```python
# Somando as vendas globais
print(df['Global_Sales'].sum())
# 369.39

print(df['Global_Sales'].mean())
# 36.939
```

## 6. Aplicação de Funções e Mapeamento

O Pandas oferece três formas principais de aplicar funções em DataFrames e Series, cada uma com um propósito específico:
* `apply()` funciona em uma linha ou coluna inteira de um DataFrame.
* `applymap()` funciona de forma elemento por elemento em um DataFrame.
* `map()` funciona de forma elemento por elemento em uma Series.


### 6.1. Aplicando funções com apply()

* O método `apply()` permite aplicar uma função a uma:
    * coluna (quando axis=0, valor padrão).
    * linha (quando axis=1) de um DataFrame.
* Isso é útil para agregar ou transformar dados em uma dimensão específica.

```python
df['Sales_Category'] = df.apply(lambda row: 'High' if row['Global_Sales'] > 30 else 'Low', axis=1)
print(df[['Name', 'Global_Sales', 'Sales_Category']].head())
```

* Aqui, categorizamos as vendas globais dos jogos em `"High"` (vendas superiores a 30 milhões) e `"Low"` (vendas inferiores a esse valor), percorrendo linha por linha.

### 6.2. Mapeando valores com map()

* O método `map()` permite substituir valores em uma coluna com base em uma correspondência,
* útil para aplicar transformações ou substituir categorias.

```python
platform_mapping = {
    'Wii': 'Retro', 
    'NES': 'Retro',
    'GB': 'Retro',
    'PS4': 'Modern',
    'PC': 'Modern'
}
df['Platform_Type'] = df['Platform'].map(platform_mapping)
print(df[['Name', 'Platform', 'Platform_Type']].head())
```

### 6.3. Aplicando funções em todos os elementos com applymap()

* Se quisermos aplicar uma função a todos os elementos de um DataFrame, usamos applymap().
Exemplo:

```python
# Aplicando uma função de formatação a todas as colunas numéricas
df_num = df[['Year', 'Global_Sales']].applymap(lambda x: f'{x:.2f}')
print(df_num.head())
```

## 7. Exercícios

* Exercício 1: Adicionando e Removendo Colunas
    - Crie uma nova coluna no DataFrame chamada `'Profit'`, onde o valor é a multiplicação das vendas globais por 1.2.
    - Em seguida, remova a coluna `'Profit'`.

* Exercício 2: Filtragem e Aplicação de Funções
    - Filtre o DataFrame para exibir apenas os jogos lançados após o ano 2000 e que têm vendas globais maiores que 30 milhões.
    - Crie uma nova coluna chamada `'Adjusted Sales'`, onde as vendas globais são ajustadas para milhões com base na função `apply()`.

* Exercício 3: Estatísticas Descritivas
    - Calcule o resumo estatístico (`describe()`) para as vendas globais e o ano de lançamento.
    - Use `value_counts()` para contar a frequência de cada gênero de jogo no DataFrame.

* Exercício 4: Função Customizada com apply()
    - Crie uma função que classifica os jogos em três categorias com base nas vendas globais: `'Baixo'`, `'Médio'` e `'Alto'`.
    - Aplique essa função à coluna `'Global_Sales'` e crie uma nova coluna `'Sales_Category'` no DataFrame.