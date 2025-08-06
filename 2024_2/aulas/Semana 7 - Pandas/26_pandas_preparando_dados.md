# Introdução ao Pandas: Limpeza e Preparação de Dados

## 1. Introdução

* A limpeza e preparação de dados são etapas fundamentais na análise de dados.
* Dados reais raramente estão perfeitos; eles contêm valores ausentes, inconsistências, duplicatas e ruídos que podem comprometer a qualidade das análises e dos modelos de machine learning.
* De fato, estima-se que até $80%$ do tempo de um cientista de dados é gasto preparando e limpando dados.
* Dominar essas técnicas permite que você lide com desafios complexos e transforme dados brutos em informações valiosas para tomada de decisões.
    ```
     Exemplo prático: Considere uma empresa de e-commerce que está analisando as compras de seus clientes. Os dados podem conter transações duplicadas, valores ausentes em campos como "idade" e "renda", e diferentes formatos para datas. Antes que qualquer análise significativa, como identificar os produtos mais populares ou clientes com maior valor de vida (lifetime value), seja feita, é essencial garantir que os dados estejam corretos e completos.
    ```

## 2. Limpeza de Dados com Pandas

### 2.1 Lidando com Dados Ausentes (NA)

* Dados ausentes podem distorcer os resultados da análise, levando a conclusões erradas.
* Isso pode acontecer porque a ausência de dados pode não ser aleatória e pode refletir problemas específicos em partes do conjunto de dados, como falhas no processo de coleta de dados.

    ```
    Exemplo prático: Em uma pesquisa de saúde, se muitos pacientes não preencheram suas idades, preencher com a média ou mediana pode enviesar a distribuição.
    Se for um problema recorrente em uma faixa etária específica, simplesmente ignorar esses valores pode eliminar dados críticos.
    ```

* Detecção de valores ausentes:
    ```python
    df.isnull().sum()  # Contagem de valores nulos por coluna
    ```
* Remoção de dados ausentes:
    ```python
    df_clean = df.dropna()  # Remove todas as linhas que contêm pelo menos um valor nulo
    ```
* Preenchimento de valores ausentes:
    ```python
    df_filled = df.fillna(df.mean())  # Preenche valores nulos com a média da coluna
    ```

### 2.2 Remover Duplicatas

* Duplicatas podem inflacionar resultados, criando uma percepção errada sobre os dados.
* Por exemplo, em uma análise de compras, duplicatas podem fazer parecer que a receita foi maior do que realmente foi.

    ```
    Exemplo prático: Um banco analisa suas transações diárias, mas percebe duplicatas devido a falhas no sistema.
    Sem a remoção dessas duplicatas, o banco não teria uma visão precisa de suas operações financeiras.
    ```

* Remoção de duplicatas:

    ```python
    df_unique = df.drop_duplicates()  # Remove duplicatas baseando-se em todas as colunas
    ```

## 3. Transformação de Dados

### 3.1 Trocar Valores

* Certos valores podem estar incorretos ou mal formatados.
* Por exemplo, ao lidar com nomes de cidades, abreviações ou grafias erradas podem comprometer a consistência da análise.

    ```python
    Exemplo prático: Em um conjunto de dados sobre pedidos online, algumas entradas estão listadas como “SP” e outras como “São Paulo”, criando dois valores distintos para a mesma cidade. Substituir essas inconsistências ajuda a unificar os dados.
    ```

* Uso de `replace()`:
    ```python
    df.replace({'old_value': 'new_value'})
    ```

### 3.2  Transformação com Apply, Applymap e Map

* Esses métodos permitem aplicar funções a colunas, linhas ou até células individuais, facilitando a transformação em massa de dados.
* Isso é útil para tarefas como conversões de unidade, padronizações de textos ou cálculos personalizados.

    ```
    Exemplo prático: Imagine que você está analisando um conjunto de dados financeiros onde os preços estão em dólares, mas deseja convertê-los para euros. Usar apply pode facilitar a aplicação dessa conversão em todas as linhas da coluna de preços.
    ```

* Diferença entre os métodos:

    * Apply: Aplica uma função ao longo de uma coluna ou linha.
        ```python
        df['preco_euro'] = df['preco_dolar'].apply(lambda x: x * 0.85)
        ```
    * Map: Aplica uma função a cada elemento elemento do dataframe (Anteriormente, apenas para Series).
        ```python
        df['category'].map({'A': 'Categoria 1', 'B': 'Categoria 2'})
        ```
    * Applymap (Descontinuado): Aplica uma função a cada elemento de um DataFrame.
        ```python
        df.applymap(str.upper)  # Converte todos os valores para maiúsculas
        ```

## 4. Discretização e Binning

### 4.1 Cut e qcut

* Discretizar dados contínuos permite agrupá-los em categorias, facilitando a análise de distribuições.
* Por exemplo, ao categorizar a idade em faixas, podemos entender melhor o comportamento de diferentes grupos etários.

    ```
    Exemplo prático: Um banco pode querer agrupar a renda dos clientes em "baixa", "média" e "alta" para criar estratégias de marketing específicas para cada grupo.
    ```

* Uso de `cut()`:
    ```python
    bins = [0, 18, 35, 60, 100]
    labels = ['Adolescente', 'Jovem Adulto', 'Adulto', 'Idoso']
    df['faixa_etaria'] = pd.cut(df['idade'], bins=bins, labels=labels)
    ```
* uso de `qcut()`:
    ```python
    df['quantile_bins'] = pd.qcut(df['renda'], q=4)
    ```

### 4.2 Dados Categóricos (Categories)

* Ao discretizar dados ou ao trabalhar com colunas categóricas, o Pandas oferece uma forma eficiente de armazenar e manipular esses dados usando o tipo category.
* Isso não só economiza memória, como também permite que você atribua códigos a categorias específicas.
* Essa abordagem é extremamente útil em grandes conjuntos de dados que contêm muitos valores categóricos repetidos.

    ```
    Exemplo prático: Suponha que você esteja analisando um conjunto de dados sobre clientes de um banco, onde a variável "estado civil" tem valores como "solteiro", "casado" e "divorciado". Ao converter essa coluna para o tipo category, podemos associar códigos numéricos a cada estado civil, melhorando a eficiência da análise e do processamento de dados.
    ```

* Atributos principais:
    * `codes`: Retorna os códigos numéricos associados a cada categoria.
    * `categories`: Retorna as categorias distintas.

```python
# Exemplo de uso
df['faixa_etaria'] = pd.cut(df['idade'], bins=[0, 18, 35, 60, 100], labels=['Adolescente', 'Jovem Adulto', 'Adulto', 'Idoso'])
df['faixa_etaria'] = df['faixa_etaria'].astype('category')

# Acessando os atributos
df['faixa_etaria'].cat.codes  # Retorna os códigos numéricos
df['faixa_etaria'].cat.categories  # Retorna as categorias
```

## 5. Exercícios

Seção de Exercícios Práticos

* Limpeza de Dados

    1. Tratamento de Dados Ausentes:
        Dado um conjunto de dados de vendas com valores ausentes nas colunas de "preço" e "desconto", preencha os valores ausentes com a mediana dos preços e, para os descontos, preencha com zero.
        ```python
        data = {
            'produto': ['A', 'B', 'C', 'D'],
            'preço': [10, np.nan, 25, 30],
            'desconto': [0.1, np.nan, 0.2, np.nan]
        }
        df = pd.DataFrame(data)
        ```

    2. Remoção de Duplicatas:
        Em um conjunto de dados de clientes de uma loja, remova as duplicatas de clientes que fizeram múltiplas compras no mesmo dia, garantindo que apenas uma compra por dia por cliente seja considerada.
        ```python
        data = {
            'cliente': ['João', 'Ana', 'João', 'Ana'],
            'data': ['2024-09-01', '2024-09-01', '2024-09-01', '2024-09-01'],
            'valor': [100, 150, 100, 200]
        }
        df = pd.DataFrame(data)
        ```

* Transformação de Dados

    3. Substituição de Valores:
        Em uma coluna de cidades, substitua todas as ocorrências de "SP" por "São Paulo" e "RJ" por "Rio de Janeiro". Verifique a consistência após a transformação.
        ```python
        data = {'cidade': ['SP', 'RJ', 'SP', 'MG']}
        df = pd.DataFrame(data)
        ```

    4. Aplicação de Funções (apply e map):
        Em uma tabela de produtos, aplique uma função `apply` para aumentar o preço de todos os produtos em 10%. Depois, use `map` para padronizar todas as strings da tabela em letras maiúsculas.
        ```python
        data = {
            'produto': ['a', 'b', 'c'],
            'preço': [10, 15, 20]
        }
        df = pd.DataFrame(data)
        ```

* Discretização e Binning

    5. Discretização com cut():
        Dado um conjunto de dados de rendas, crie uma nova coluna que divida os dados em três faixas de idade: 'Adolescente', 'Adulto', 'Idoso'.
        ```python
        data = {'idade': [10, 20, 30, 40, 50]}
        df = pd.DataFrame(data)
        ```

    6. Estrutura de Dados Categóricos:
        Transforme a coluna de faixas de renda criada no exercício anterior em uma coluna do tipo category.
        Acesse e imprima os valores de codes e categories.