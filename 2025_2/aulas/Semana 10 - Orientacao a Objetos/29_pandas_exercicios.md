# Lista de Exercícios: Análise de Dados com Pandas


## 1. Estatísticas básicas

1. Carregue o dataset `netflix_titles.csv`.
2. Exiba as cinco primeiras linhas e as informações gerais sobre o dataset.
3. Liste todas as colunas disponíveis e seus respectivos tipos de dados.
4. Quantos filmes existem no dataset? Considere apenas as linhas com `type == 'Movie'`.
5. Verifique se existem filmes duplicados. Quais colunas devem ser consideradas para definir duplicidade?
6. Verifique se há valores ausentes nas colunas e apresente um resumo da quantidade de valores nulos.
7. Analise a distribuição das colunas `duration`, `listed_in` e `release_year` (**Não fazer nenhum processamento**).

## 2. Pré-processamento de dados

1. Realize o parsing da coluna `duration`, extraindo apenas o valor numérico da duração em minutos.
2. Crie uma nova coluna `duration_movie` com as seguintes categorias:
    * Menos que 90 minutos → **Curto**
    * Entre 90 e 150 minutos → **Ideal**
    * Mais que 150 minutos → **Longo**
    * Em caso de `type == 'TV Show'` → **None**

3. Converta a coluna `date_added` para o formato de data e crie as colunas:
    * `date_added_day`
    * `date_added_month`
    * `date_added_year`

4. Transforme a coluna `listed_in`, originalmente armazenada como string, em uma lista (array) de gêneros para cada linha.

## 3. Visualização de dados

1. Exiba o número de filmes adicionados ao catálogo por ano.
2. Mostre os dez atores ou atrizes que mais aparecem em filmes.
3. Crie um gráfico de dispersão entre o ano de lançamento (`release_year`) e a duração (`duration`) dos filmes.

## 4. Análise exploratória

1. Quais países possuem mais produções na Netflix?
2. Quais são os gêneros mais produzidos?
3. Quantos filmes foram lançados por ano com base na coluna `release_year`?
5. Quantos dias seriam necessários para assistir todos os filmes?

## 5. Análise focada no Brasil

1. Quantos filmes brasileiros estão disponíveis no catálogo da Netflix?
2. Quais são os gêneros mais comuns entre os filmes brasileiros?
3. Quantos filmes brasileiros foram adicionados por ano ao catálogo?

