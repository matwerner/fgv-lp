# Introdução ao Pandas: Visualização de Dados

O objetivo desta aula é ensinar como utilizar Pandas para criar gráficos diretamente a partir de DataFrames, cobrindo gráficos de linha, barra e dispersão.
Vamos também discutir as limitações de usar Pandas para visualização em vez do Matplotlib diretamente, além de entender como as duas bibliotecas estão integradas.

## 1. Introdução à Visualização com Pandas e Matplotlib

### O que é Matplotlib e como o Pandas o utiliza?

O **Matplotlib** é uma biblioteca amplamente utilizada para visualização de dados em Python, extremamente flexível e poderosa.
Ele permite a criação de uma ampla gama de gráficos, desde os mais simples até visualizações altamente customizadas.
Além disso, é a base para outras bibliotecas de visualização mais avançadas, como o **Seaborn**, que facilita a criação de gráficos estatísticos mais complexos e com um design visual mais refinado.

O **Pandas**, por outro lado, é uma biblioteca focada em análise de dados, e oferece funcionalidades que permitem exibir gráficos de forma muito rápida e simples, utilizando o método `.plot()`.
Essa facilidade de uso é alcançada porque o Pandas usa o Matplotlib nos bastidores para criar esses gráficos.

### Como Pandas e Matplotlib se Integram

A integração entre Pandas e Matplotlib funciona da seguinte forma:
- **Pandas**:
Fornece uma interface de alto nível que simplifica a criação de gráficos com um código mínimo, ideal para tarefas rápidas de análise exploratória de dados.
No entanto, essa simplicidade vem com uma perda de flexibilidade, tornando difícil criar gráficos altamente personalizados.
- **Matplotlib**:
Permite um controle completo sobre todos os aspectos dos gráficos, como eixos, estilos de linhas, cores e layouts.
Ao usar Matplotlib diretamente, é possível criar visualizações com um nível de customização muito maior, mas isso exige mais código e detalhes.

### Vantagens e Limitações do Pandas

- **Vantagens**:
Usar Pandas para criar gráficos é ideal para gerar rapidamente visualizações simples durante a análise de dados, especialmente quando se trabalha com DataFrames.
Isso elimina a necessidade de construir cada gráfico do zero com o Matplotlib.
- **Limitações**:
A simplicidade do Pandas sacrifica parte da flexibilidade oferecida pelo Matplotlib.
Gráficos mais avançados ou com personalizações complexas, como a criação de múltiplos subplots, escalas logarítmicas, ou estilos de linha específicos, muitas vezes requerem o uso direto de Matplotlib ou Seaborn.

### Exemplo de um Gráfico Criado com Pandas

```python
import pandas as pd
import matplotlib.pyplot as plt

# Exemplo de um gráfico de linha simples
data = {'Ano': [2018, 2019, 2020, 2021],
        'Vendas': [250, 270, 300, 330]}
df = pd.DataFrame(data)

df.plot(x='Ano', y='Vendas', kind='line')
plt.show()
```

Neste exemplo, Pandas simplifica a criação de um gráfico de linha com o método `.plot()`, permitindo que você visualize os dados rapidamente.
Para personalizações mais detalhadas, no entanto, você precisaria utilizar os recursos do Matplotlib diretamente.

### Tipos de Gráficos que Veremos Adiante

Nos próximos tópicos, exploraremos três tipos básicos de gráficos que são essenciais para a análise de dados e visualização.
Eles permitem compreender diferentes aspectos dos dados e são amplamente utilizados em diversas áreas.

* `Gráfico de Linhas`:
Ideal para representar dados contínuos ao longo do tempo, como o crescimento de vendas anuais ou mudanças de preços.
Ele é utilizado para destacar tendências e comportamentos ao longo de um período.

* `Gráfico de Barras`:
Excelente para comparar valores entre diferentes categorias ou grupos, como vendas por produto ou número de respostas em uma pesquisa.
Ele facilita a visualização de comparações entre dados discretos.

* `Gráfico de Dispersão`:
Utilizado para mostrar a relação entre duas variáveis numéricas.
Ajuda a identificar correlações, padrões ou outliers nos dados, sendo muito comum em análises de regressão e estudos de correlação entre variáveis.

Esses três tipos de gráficos cobrem a maior parte das necessidades básicas de visualização de dados e fornecem uma base sólida para a análise exploratória e a apresentação de resultados.

## 2. Gráficos de Linha com Séries Temporais

Um gráfico de linhas é uma maneira eficaz de mostrar como uma variável muda ao longo de um período ou uma sequência de dados.
Ele conecta pontos de dados com linhas, facilitando a visualização de tendências e padrões.
Esse tipo de gráfico é amplamente utilizado para acompanhar o comportamento de dados contínuos, como séries temporais ou medições em intervalos regulares.

### Exemplo 1: Criando um Gráfico de Linha Simples com `df.plot.line()`
A função `df.plot.line()` do Pandas permite criar gráficos de linhas rapidamente. Ao utilizar esse método, é importante garantir que o DataFrame esteja ordenado corretamente no eixo que representa o tempo ou sequência, para que a linha conecte os pontos de forma adequada.

Aqui, passamos os parâmetros `x` e `y` para especificar as colunas que correspondem aos eixos.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Dados de exemplo
data = {'Ano': [2018, 2019, 2020, 2021],
        'Vendas': [250, 270, 300, 330]}
df = pd.DataFrame(data)

# Ordenando o DataFrame pelo ano (essencial para séries temporais)
df = df.sort_values(by='Ano')

# Criando o gráfico de linha, especificando o eixo X e Y
df.plot.line(x='Ano', y='Vendas', title='Vendas Anuais')
plt.show()
```

### Exemplo 2: Gráfico de Múltiplas Linhas

Podemos também exibir várias séries de dados em um mesmo gráfico de linhas, útil para comparar diferentes variáveis ao longo de um mesmo eixo (por exemplo, comparar vendas e lucros ao longo dos anos).

No exemplo abaixo, mostramos como incluir duas colunas no eixo `y` para desenhar duas linhas no mesmo gráfico.

```python
# Dados de exemplo com mais de uma variável
data = {'Ano': [2018, 2019, 2020, 2021],
        'Vendas': [250, 270, 300, 330],
        'Lucro': [50, 70, 100, 120]}
df = pd.DataFrame(data)

# Ordenando o DataFrame pelo ano
df = df.sort_values(by='Ano')

# Criando o gráfico de múltiplas linhas
df.plot.line(x='Ano', y=['Vendas', 'Lucro'], title='Vendas e Lucro Anuais', ylabel='Valores')
plt.show()
```

### Observações Importantes
* `Ordem dos Dados`:
Para gráficos de linha, especialmente com séries temporais, é fundamental que o DataFrame esteja ordenado na sequência correta (por exemplo, por ano, mês ou qualquer outra variável temporal).
Se os dados não estiverem ordenados, a linha pode conectar os pontos fora de ordem, resultando em uma visualização incorreta.
* `Múltiplas Linhas`:
Quando você deseja comparar várias séries de dados no mesmo gráfico, a função `df.plot.line()` permite especificar mais de uma coluna para o eixo `y`. 
Isso facilita a comparação direta entre diferentes variáveis ao longo do mesmo eixo `x`.

## 3. Gráficos de Barra

Gráficos de barra são utilizados para comparar categorias discretas, permitindo uma visualização clara das diferenças entre diferentes grupos ou itens. 
Eles são especialmente úteis para exibir o número de vendas por produto, a distribuição de respostas em uma pesquisa ou qualquer outra métrica que envolva categorias distintas.

### Exemplo 1: Criando um Gráfico de Barra Simples com `df.plot.bar()`
No Pandas, gráficos de barra podem ser criados facilmente utilizando o método `df.plot.bar()`.
É importante escolher uma coluna para o eixo `x` que represente as categorias e outra coluna para o eixo `y` que contenha os valores a serem comparados.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Dados de exemplo
data = {'Produto': ['A', 'B', 'C'],
        'Vendas': [100, 150, 90]}
df = pd.DataFrame(data)

# Criando o gráfico de barra
df.plot.bar(x='Produto', y='Vendas', title='Vendas por Produto', color='skyblue')
plt.show()
```

### Exemplo 2: Gráfico de Barras Agrupadas

Quando você tem múltiplas séries de dados que deseja comparar em relação às mesmas categorias, um gráfico de barras agrupadas é uma boa escolha.
No Pandas, isso pode ser feito utilizando o método `df.plot.bar()` e passando um DataFrame que contém as categorias e suas respectivas séries de dados.

```python
# Dados de exemplo com múltiplas variáveis
data = {
    'Produto': ['A', 'B', 'C'],
    'Vendas_2022': [100, 150, 90],
    'Vendas_2023': [120, 160, 80],
}
df = pd.DataFrame(data)

# Criando o gráfico de barras agrupadas
df.set_index('Produto').plot.bar(title='Vendas por Produto em 2022 e 2023', color=['lightblue', 'orange'])
plt.xlabel('Produto')
plt.ylabel('Vendas')
plt.legend(title='Ano')
plt.show()
```

### Observações Importantes:

* `Comparação de Categorias`:
Gráficos de barra são particularmente úteis quando se deseja comparar diferentes categorias de forma visual.
Eles são fáceis de interpretar e permitem que o espectador compreenda rapidamente as diferenças entre os valores representados.
* `Personalização`:
O método `df.plot.bar()` oferece opções para personalizar cores, estilos de linha e rótulos, permitindo que você adapte a visualização às suas necessidades específicas.

## 4. Gráficos de Dispersão

Gráficos de dispersão são utilizados para mostrar a relação entre duas variáveis numéricas.
Eles ajudam a identificar padrões, tendências e possíveis correlações entre os dados.
Cada ponto no gráfico representa uma observação, com a posição no eixo `x` correspondente a uma variável e a posição no eixo `y` correspondente a outra.

### Exemplo 1: Criando um Gráfico de Dispersão com `df.plot.scatter()`
No Pandas, gráficos de dispersão podem ser criados utilizando o método `df.plot.scatter()`. É importante escolher as colunas apropriadas para os eixos `x` e `y`, que representem as variáveis a serem comparadas.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Dados de exemplo
data = {
    'Altura': [1.60, 1.75, 1.80, 1.65, 1.70],
    'Peso': [50, 70, 80, 60, 75]
}
df = pd.DataFrame(data)

# Criando o gráfico de dispersão
df.plot.scatter(x='Altura', y='Peso', title='Relação entre Altura e Peso', xlabel='Altura (m)', ylabel='Peso (kg)')
plt.show()
```

### Exemplo 2: Gráfico de Dispersão com Cores e Tamanhos Personalizados

Você pode adicionar outra dimensão aos dados, utilizando cores ou tamanhos de marcadores diferentes. Isso é útil para incluir informações adicionais, como categorias ou outra variável numérica.

```python
# Dados de exemplo com categoria
data = {
    'Altura': [1.60, 1.75, 1.80, 1.65, 1.70],
    'Peso': [50, 70, 80, 60, 75],
    'Idade': [25, 30, 22, 28, 35]  # Variável adicional para o tamanho dos pontos
}
df = pd.DataFrame(data)

# Criando o gráfico de dispersão com tamanho dos marcadores baseado na idade
scatter = df.plot.scatter(x='Altura', y='Peso', title='Relação entre Altura e Peso com Idade', 
                          s=df['Idade']*10, xlabel='Altura (m)', ylabel='Peso (kg)')
plt.show()
```

### Observações Importantes:

* `Identificação de Padrões`:
Gráficos de dispersão são úteis para identificar correlações entre variáveis, como a relação entre altura e peso, permitindo observar se existe uma tendência de que à medida que uma variável aumenta, a outra também tende a aumentar ou diminuir.
* `Ajustes de Visualização`:
O método `df.plot.scatter()` permite diversas personalizações, como cores, tamanhos dos marcadores e transparência (alpha), que podem ser utilizadas para representar informações adicionais ou tornar o gráfico mais legível.

## 5. Salvando Gráficos

O comando `plt.show()` é utilizado para exibir os gráficos na tela. No entanto, também é possível salvar as imagens diretamente utilizando `plt.savefig()`.
Essa função permite que você escolha o formato de saída (como `PNG`, `JPEG`, `SVG`, etc.) e defina a resolução da imagem com o parâmetro dpi (dots per inch).

```python

# Criando um gráfico de exemplo
data = {'Produto': ['A', 'B', 'C'],
        'Vendas': [100, 150, 90]}
df = pd.DataFrame(data)
df.plot.bar(x='Produto', y='Vendas', title='Vendas por Produto')

# Exibindo o gráfico
plt.show()

# Salvando a imagem
plt.savefig('vendas_por_produto.png', format='png', dpi=300)
```

### Observações Importantes

* `Formatos de Saída`:
Você pode salvar gráficos em diversos formatos, como PNG, PDF, SVG, etc.
* `DPI`:
A configuração de dpi é importante para garantir a qualidade da imagem ao ser impressa ou exibida em alta resolução.

## Referências

* [Documentação do Pandas - Gráficos de Linhas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.line.html)
* [Documentação do Pandas - Gráficos de Barra](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.bar.html)
* [Documentação do Pandas - Gráficos de Dispersão](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.scatter.html)