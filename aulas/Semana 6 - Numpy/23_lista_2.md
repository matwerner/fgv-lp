## 1. Separador de Pares e Ímpares

Gere um array de 20 números inteiros aleatórios entre 1 e 100. Escreva uma função para separar os números pares dos números ímpares, retornando dois novos arrays.

```python
# Entrada
numeros = np.array([15, 26, 33, 42, 55, 68, 71, 88, 90, 91])
# Saida
pares = [26, 42, 68, 88, 90]
ímpares = [15, 33, 55, 71, 91]
```

## 2. Normalização de Dados

Normalize um array 1D de notas de exames (números inteiros aleatórios entre 0 e 100) para uma escala de 0 a 1 usando a fórmula:
$$ \text{normalized} = \frac{x - \text{min}(x)}{\text{max}(x) - \text{min}(x)} $$

```python
# Entrada
notas = np.array([75, 40, 50, 60, 80])
# Saida
notas_normalizadas = [0.875, 0., 0.25, 0.5, 1.]
```

## 3. Distância de Manhattan

Você tem as coordenadas de cinco cidades em um plano 2D, representadas por seus valores de latitude e longitude. Escreva uma função que calcule a distância de Manhattan entre cada par de cidades.

$$ d_{\text{Manhattan}} = |x_2 - x_1| + |y_2 - y_1| $$

```python
# Entrada
cidades = np.array([[50, -120], 
                    [40,  -70]])
# Saida
distância_manhattan = 60
```

## 4. Cálculo de Média Móvel

Escreva uma função para calcular a média móvel dos preços de ações em uma janela de 5 dias. Gere um array NumPy de 30 preços de ações aleatórios (números de ponto flutuante) e retorne o array das médias móveis.

```python
# Entrada
precos = np.array([10.0, 12.5, 13.0, 14.5, 15.0, 14.0, 13.5])
# Saida
medias_moveis = [13.16, 13.75, 14.0]
```

## 5. Sumário estatístico

Crie uma função que realiza um sumário estatístico básico de um array NumPy.
Ela deve calcular e exibir o valor mínimo, o valor máximo e os quartis (25%, 50%, e 75%) de um array fornecido.

```python
# Entrada
array = np.array([10, 20, 35, 50, 70, 80, 95, 100])
# Saída:
# Sumário Estatístico do Array:
# Valor Mínimo: 10
# Valor Máximo: 100
# Quartis:
#   25%: 31.25
#   50% (Mediana): 60.0
#   75%: 83.75
```

## 6. Agrupamento por categoria

Você tem duas listas: uma com categorias e outra com os valores das transações.
Crie uma função que calcule a soma total do faturamento para cada categoria usando NumPy e retorne um dicionário onde as chaves são as categorias e os valores são as somas dos faturamentos para essas categorias.

```python
# entrada
categorias = ['Alimentação', 'Saúde', 'Alimentação', 'Educação', 'Saúde', 'Educação']
valores = [100, 200, 50, 300, 150, 100]
# Saída
resultado = {
    'Alimentação': 150,
    'Saúde': 350,
    'Educação': 400
}
```

## 7. Verificador de Vencedor do Jogo da Velha

Crie uma função que verifique o vencedor de um tabuleiro de Jogo da Velha dado (array 3x3 do NumPy).
O tabuleiro contém 1s, -1s e 0s (representando o Jogador 1, o Jogador 2 e espaços vazios, respectivamente).
A função deve detectar se algum jogador venceu ou se o jogo terminou empatado.

```python
# Entrada
tabuleiro = np.array([[ 1, -1,  1],
                      [ 0,  1, -1],
                      [-1,  1,  1]])
# Saida
vencedor = 1
```
