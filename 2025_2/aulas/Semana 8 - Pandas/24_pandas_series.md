# Introdução ao Pandas

Pandas é uma das bibliotecas mais populares e poderosas para **análise e manipulação de dados em Python**.
Seu grande diferencial está na capacidade de lidar com **estruturas de dados tabulares e rotuladas** -- semelhantes a planilhas ou tabelas de banco de dados -- de forma simples, eficiente e intuitiva.

Com o Pandas, é possível realizar rapidamente tarefas que, em ferramentas tradicionais, seriam repetitivas ou exigiriam muito esforço manual, como **limpeza, transformação, agregação e análise de grandes volumes de dados**.
Por isso, a biblioteca é amplamente utilizada não apenas em ciência de dados, mas também em áreas como finanças, negócios, engenharia, jornalismo de dados e pesquisa acadêmica.

## 1. Por que usar Pandas?

* **Operações intuitivas**: Selecionar, filtrar, agrupar e agregar dados é direto e legível, lembrando a manipulação de planilhas ou consultas SQL.
* **Suporte a dados rotulados e tabulares**: Linhas e colunas têm rótulos, permitindo acesso e manipulação mais claros e expressivos.
* **Compatibilidade com múltiplos formatos**: Leitura e escrita nativas para CSV, Excel, JSON, SQL, entre outros.
* **Integração com o ecossistema Python**: Pandas trabalha em conjunto com bibliotecas como NumPy, Matplotlib e Scikit-learn, permitindo análises completas sem sair do ambiente Python.

## 2. Caso de uso: Sistema Bancário Simples

Para entender melhor a importância prática do Pandas, vamos imaginar um exemplo próximo ao cotidiano.

### 2.1. Situação inicial

Suponha que desenvolvemos um pequeno sistema bancário com as seguintes operações básicas:

* **Criar conta**: Gera um registro com identificador único, nome do cliente e saldo inicial igual a zero.
* **Depositar / Retirar dinheiro**: Atualiza o saldo associado à conta.
* **Salvar “estado do banco”**: Exporta as informações para um arquivo.
* Outras operações administrativas.

Esses dados são armazenados em uma **planilha no formato CSV** (Comma-Separated Values), um formato amplamente utilizado por sua simplicidade e compatibilidade.

#### Exemplo de arquivo CSV

```
identificador,nome_do_usuario,saldo
1,Rafael,0.0
2,Daniela,1000.0
3,Andreia,5000.0
4,George,2000.0
```

#### Visualização em tabela

| identificador | nome_do_usuario |  saldo |
| ------------- | --------------- | -----: |
| 1             | Rafael          |    0.0 |
| 2             | Daniela         | 1000.0 |
| 3             | Andreia         | 5000.0 |
| 4             | George          | 2000.0 |

### 2.2. Evolução do problema

Agora, imagine que queremos **armazenar não apenas o saldo atual**, mas também o **histórico de todas as transações** (depósitos e retiradas) de cada cliente.

Como poderíamos estruturar esses dados?

#### Solução A - Tabela única

Uma solução inicial poderia ser manter todas as transações em uma única tabela, repetindo informações do cliente a cada operação:

| identificador | nome_do_usuario |  valor |       data |
| ------------- | --------------- | -----: | ---------: |
| 1             | Rafael          |  100.0 | 2025-01-01 |
| 1             | Rafael          | - 50.0 | 2025-01-02 |
| 2             | Daniela         |  200.0 | 2025-01-03 |
| 1             | Rafael          |  300.0 | 2025-01-04 |

Apesar de simples, essa abordagem apresenta problemas:

* **Redundância de dados**: O nome do usuário e outros campos são repetidos a cada linha.
* **Maior uso de memória**: Mais dados armazenados desnecessariamente.
* **Manutenção trabalhosa**: Se um nome de cliente mudar, seria necessário atualizar múltiplas linhas manualmente.

#### Solução B - Duas tabelas relacionadas

Uma abordagem mais organizada seria **separar os dados em duas tabelas**:

1. **Tabela de clientes**: Contém dados fixos de cada cliente.
2. **Tabela de transações**: Registra valor e data de cada operação, associando cada transação a um cliente por meio do **identificador único**.

##### Exemplo

**Clientes**

| identificador | nome_do_usuario |
| ------------- | --------------- |
| 1             | Rafael          |
| 2             | Daniela         |
| 3             | Andreia         |
| 4             | George          |

**Transações**

| identificador_cliente | valor |       data |
| --------------------- | ----: | ---------: |
| 1                     | 100.0 | 2025-01-01 |
| 1                     | -50.0 | 2025-01-02 |
| 2                     | 200.0 | 2025-01-03 |
| 1                     | 300.0 | 2025-01-04 |

Essa estrutura é mais próxima de um **modelo relacional**: reduz redundância, melhora a consistência dos dados e facilita análises complexas.

### 2.3. Análise de dados com Pandas

Agora, imagine que o **Gerente do Banco** precisa gerar um relatório para identificar **clientes suspeitos para o Banco Central**, segundo os seguintes critérios:

* Movimentaram **acima de R$ 1.000.000,00** no último mês.
* Realizaram **mais de 50 depósitos** no mesmo período.

Para isso, ele precisa:

1. **Adicionar uma coluna** à tabela de transações para indicar se a operação é depósito ou retirada.
2. **Agrupar os dados por cliente**, somando os valores e contando o número de transações.
3. **Juntar o resultado** com as informações da tabela de clientes para obter nome e identificador.

Ferramentas como Excel, Google Sheets ou LibreOffice Calc **podem executar essas etapas**, mas exigiriam **operações manuais repetitivas** a cada nova atualização dos dados.

Com Pandas, no entanto, seria possível realizar toda essa análise com **poucas linhas de código**, de maneira **reprodutível e automatizável**, economizando tempo e reduzindo erros.

## 3. Estrutura Unidimensional: Series

### A. O que é uma `Series`?
Uma **Series** no Pandas é uma estrutura de dados **unidimensional**, semelhante a uma coluna de uma tabela ou a um array do NumPy, mas com uma característica fundamental: **cada elemento possui um índice associado**, que pode ser numérico, textual ou de outro tipo.

Essa combinação de valores e índices permite acessar e manipular dados de maneira mais intuitiva e expressiva, próxima ao funcionamento de um dicionário em Python.


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
Os índices servem como rótulos para identificar cada valor de forma única, permitindo acessos mais diretos e legíveis.

### C. Conceitos-chave:

* **Index (Índice)**
  Cada elemento da Series está associado a um índice. Esses rótulos podem ser numéricos, alfabéticos ou mesmo datas — algo que facilita muito a análise de dados reais.

* **Name (Cabeçalho)**
  A Series também pode ter um nome que funciona como um cabeçalho. Isso é útil especialmente quando se trabalha com múltiplas Series ou quando elas fazem parte de um DataFrame.

## 4. Diferenças de Series em Relação ao ndarray

### A. Índices (Index) Personalizados
Ao contrário dos arrays do NumPy, que usam posições numéricas fixas, as Series permitem **índices personalizados**, possibilitando trabalhar com dados rotulados de forma mais natural.

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
Embora uma Series tenha apenas uma “coluna”, podemos atribuir um nome a ela, tornando os resultados mais claros:


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

**Vantagens**

* **Acesso intuitivo:** É possível acessar valores por rótulo, sem depender apenas de posições numéricas.
* **Flexibilidade:** Suporta operações de filtragem, transformação e agregação de maneira simples.
* **Interoperabilidade:** Integra-se naturalmente com DataFrames, NumPy e outras bibliotecas.

**Desvantagens**

* **Desempenho numérico:** NumPy é mais rápido em operações matemáticas puras, pois trabalha com arrays homogêneos e densos.
* **Foco em dados rotulados:** Pandas é ideal para dados tabulares e não para cálculos numéricos massivos.

### D. Quando usar Pandas vs NumPy?

* `Pandas`: ideal para manipulação e análise de dados tabulares e rotulados. Use Pandas quando você precisa trabalhar com grandes datasets em formato de planilhas.
* `NumPy`: mais adequado para cálculos numéricos massivos e computação de alta performance. Ele é perfeito para operações como álgebra linear, transformações de matrizes, etc.

## 5. Operações básicas

### A. Parâmetros index e name

* `index`: Define os rótulos dos elementos na Series. Pode ser numérico ou alfabético.
* `name`: Nomeia a Series. Útil quando se trabalha com múltiplas Series ou DataFrames para identificar e distinguir entre diferentes conjuntos de dados.

```python
serie = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'], name='Valores')
print(serie)
print(serie.name)  # Saída: Valores
```

### B. Acessando Dados

As Series oferecem métodos diferentes para acessar elementos, tanto por **rótulo** quanto por **posição numérica**. Além disso, é possível fazer seleções mais complexas usando **vetores booleanos** ou **funções** para definir condições dinamicamente.

Principais métodos:

* **`at`**
  Acessa um único valor de forma rápida usando o **rótulo** do índice.
  É ideal para acesso escalar simples.

* **`iat`**
  Acessa um único valor pela **posição numérica**, semelhante a um array NumPy.

* **`loc`**
  Acessa valores usando **rótulos**, podendo selecionar:

  * Um único elemento
  * Um intervalo de índices (fatiamento)
  * Uma lista de rótulos
  * Um **vetor booleano**, para filtragem condicional
  * Uma **função**, que recebe a Series e retorna um vetor booleano

* **`iloc`**
  Acessa valores pela **posição numérica** (índices inteiros), suportando fatiamento e listas de posições.

#### Exemplos

```python
import pandas as pd

serie = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

# Acesso direto
print(serie.at['b'])   # 20
print(serie.iat[1])    # 20

# Fatiamento por rótulo e por posição
print(serie.loc['b':'d'])
# b    20
# c    30
# d    40

print(serie.iloc[1:3])
# b    20
# c    30

# Acesso por lista de rótulos
print(serie.loc[['a', 'd']])
# a    10
# d    40

# Acesso com vetor booleano
print(serie.loc[serie > 20])
# c    30
# d    40

# Acesso com função
print(serie.loc[lambda s: s % 20 == 0])
# b    20
# d    40
```

Esse conjunto de métodos permite construir **consultas expressivas e concisas**, uma das grandes forças do Pandas.

### C. Ordenação e Limpeza de Dados

Em análises reais, é comum precisar **organizar dados** (por índice ou valor) e **tratar valores ausentes**. Pandas fornece métodos específicos para essas tarefas de forma simples e eficiente.

Principais métodos:

* **`sort_values()`**: ordena os elementos com base nos valores.
* **`sort_index()`**: ordena os elementos com base no índice.
* **`fillna()`**: preenche valores ausentes (`NaN`) com um valor especificado ou com regras simples (como média, zero, valor anterior, etc.).

Tanto `sort_values()` quanto `sort_index()` possuem o parâmetro **`ascending`**, que define a direção da ordenação:

* `ascending=True` (padrão): ordem crescente
* `ascending=False`: ordem decrescente

#### Exemplos

```python
serie = pd.Series([40, None, 10, 30], index=['d', 'b', 'a', 'c'])

# Ordenação por valor (crescente)
print(serie.sort_values())
# a    10.0
# c    30.0
# d    40.0
# b     NaN

# Ordenação por valor (decrescente)
print(serie.sort_values(ascending=False))
# d    40.0
# c    30.0
# a    10.0
# b     NaN

# Ordenação por índice
print(serie.sort_index())
# a    10.0
# b     NaN
# c    30.0
# d    40.0

# Preenchendo valores ausentes com 0
serie_preenchida = serie.fillna(0)
print(serie_preenchida)
# d    40.0
# b     0.0
# a    10.0
# c    30.0
```

O uso de `ascending` é particularmente útil em análises exploratórias, onde pode ser necessário destacar maiores ou menores valores rapidamente. Já `fillna()` é fundamental em etapas de **limpeza de dados**, garantindo que valores ausentes não prejudiquem cálculos e agrupamentos posteriores.


### D. Estatísticas

Diferente do numpy, pandas já vem com uma função especifica para exibir estátisticas de uma distribuição de valores.
O mais comum é `describe()`, que fornece estatísticas como média, desvio padrão, quartis e valores mínimos/máximos.

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

## 6. Lendo uma Series de um Arquivo de Texto

Series também podem ser criadas diretamente a partir de arquivos de texto ou CSV.

### Exemplo

**Arquivo `dados_com_indice.txt`:**

```
Indice,Valor
a,10
b,20
c,30
d,40
```

**Leitura com Pandas:**

```python
import pandas as pd

serie = pd.read_csv(
    'dados_com_indice.txt',
    index_col='Indice',
    squeeze=True
)
print(serie)
```

* `index_col='Indice'` define qual coluna será usada como índice.
* `squeeze=True` garante que, se houver apenas uma coluna, o resultado seja convertido em Series ao invés de DataFrame.

## 7. Exercícios

1. Criar uma Series a partir de uma lista de dados e índices personalizados.

   ```python
   produtos = ['Caneta', 'Lápis', 'Caderno', 'Borracha', 'Estojo']
   quantidades = [150, 200, 120, 80, 60]
   ```
2. Realizar operações matemáticas e comparar com um `ndarray`.
3. Utilizar `at`, `iat`, `loc` e `iloc` para acessar elementos específicos.
4. Aplicar `describe()` a uma Series e interpretar os resultados.
5. Ordenar a Series criada com `sort_values` e `sort_index`.
6. Introduzir valores `NaN` manualmente e usar `fillna()` para tratá-los.
