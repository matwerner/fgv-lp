# Aula 19: NumPy II

## 1. Funções Universais (*ufuncs*)

Na aula anterior, vimos que o NumPy permite realizar operações diretamente sobre arrays:

```python
a = np.array([1, 2, 3])

print(a * 2)
print(a ** 2)
```

Além dos operadores básicos, o NumPy fornece diversas funções que também operam de forma **vetorizada**, aplicando determinada operação elemento por elemento sobre um array.

Muitas dessas funções são chamadas de **funções universais** (*universal functions* ou **ufuncs**).

Por exemplo:

```python
a = np.array([1, 4, 9, 16])

print(np.sqrt(a))
```

Saída:

```text
[1. 2. 3. 4.]
```

A função `np.sqrt` foi aplicada a cada elemento do array, sem a necessidade de escrever um `for`.

Algumas ufuncs comuns são:

| Função             | Operação                               |
| ------------------ | -------------------------------------- |
| `np.abs(a)`        | Valor absoluto                         |
| `np.sqrt(a)`       | Raiz quadrada                          |
| `np.square(a)`     | Quadrado                               |
| `np.exp(a)`        | Exponencial                            |
| `np.log(a)`        | Logaritmo natural                      |
| `np.floor(a)`      | Arredondamento para baixo              |
| `np.ceil(a)`       | Arredondamento para cima               |
| `np.sin(a)`        | Seno                                   |
| `np.cos(a)`        | Cosseno                                |
| `np.maximum(a, b)` | Máximo entre elementos correspondentes |
| `np.minimum(a, b)` | Mínimo entre elementos correspondentes |

Algumas recebem apenas um array:

```python
a = np.array([1, 4, 9])

print(np.sqrt(a))
print(np.square(a))
```

Outras operam sobre dois arrays:

```python
a = np.array([1, 5, 3])
b = np.array([4, 2, 6])

print(np.maximum(a, b))
```

Saída:

```text
[4 5 6]
```

Assim como as operações aritméticas vistas anteriormente, as ufuncs permitem realizar operações sobre arrays inteiros utilizando **vetorização**.

## 2. Gerador de Números Aleatórios

O NumPy possui ferramentas para geração de números pseudoaleatórios.

Essas operações são úteis em situações como:

* simulações;
* experimentos estatísticos;
* testes;
* amostragem;
* geração de dados.

Primeiro, criamos um gerador:

```python
rng = np.random.default_rng()
```

A partir dele, podemos gerar diferentes tipos de valores.

Números reais no intervalo `[0, 1)`:

```python
print(rng.random(5))
```

Uma matriz de números reais:

```python
print(rng.random((2, 3)))
```

Números inteiros:

```python
print(rng.integers(1, 11, size=5))
```

Uma matriz de inteiros:

```python
print(rng.integers(1, 11, size=(3, 3)))
```

Também podemos gerar valores seguindo uma distribuição normal:

```python
print(
    rng.normal(
        loc=0,
        scale=1,
        size=5
    )
)
```

Nesse caso:

```text
loc   → média
scale → desvio padrão
size  → quantidade/formato dos valores
```

### Reprodutibilidade

Podemos fornecer uma **semente** ao gerador:

```python
rng = np.random.default_rng(10)
```

Executando novamente o programa com a mesma semente, a mesma sequência de números será produzida.

Isso pode ser útil, por exemplo, quando queremos repetir exatamente um experimento ou teste.

## 3. Operações sobre Arrays

Além das operações elemento por elemento, o NumPy fornece diversas operações para resumir, comparar e reorganizar os dados armazenados em arrays.

### 3.1. Operações de Agregação

Algumas operações recebem vários elementos de um array e produzem um valor que os resume.

Considere:

```python
valores = np.array([10, 20, 30, 40])
```

Podemos calcular:

```python
print(valores.sum())   # 100
print(valores.mean())  # 25.0
print(valores.min())   # 10
print(valores.max())   # 40
print(valores.std())   # Desvio padrão
```

Algumas operações comuns são:

| Operação     | Descrição          |
| ------------ | ------------------ |
| `arr.sum()`  | Soma dos elementos |
| `arr.mean()` | Média              |
| `arr.min()`  | Menor valor        |
| `arr.max()`  | Maior valor        |
| `arr.std()`  | Desvio padrão      |

Essas operações também podem ser utilizadas em arrays multidimensionais.

Considere uma matriz na qual cada linha representa um aluno e cada coluna representa uma avaliação:

```python
notas = np.array([
    [8, 7, 9],
    [6, 5, 7],
    [9, 9, 10]
])
```

A média de todas as notas é:

```python
print(notas.mean())
```

Podemos também realizar a operação ao longo de uma determinada dimensão utilizando `axis`.

Média por coluna:

```python
print(notas.mean(axis=0))
```

Resultado:

```text
[7.66666667 7.         8.66666667]
```

Média por linha:

```python
print(notas.mean(axis=1))
```

Resultado:

```text
[8. 6. 9.33333333]
```

Podemos interpretar:

```text
axis=0 → reduz as linhas → um resultado para cada coluna

axis=1 → reduz as colunas → um resultado para cada linha
```

O mesmo princípio pode ser utilizado com outras operações:

```python
print(notas.max(axis=1))
print(notas.min(axis=0))
print(notas.sum(axis=1))
```

### 3.2. Operações Booleanas

Na aula anterior vimos que uma comparação produz um array booleano:

```python
arr = np.array([1, 2, 3, 4, 5])

condition = arr > 2

print(condition)
```

Saída:

```text
[False False  True  True  True]
```

Além de utilizar esse resultado para indexação, podemos realizar outras operações sobre condições.

#### `np.where`

`np.where` permite escolher valores de acordo com uma condição:

```python
result = np.where(
    arr > 2,
    arr,
    -1
)

print(result)
```

Saída:

```text
[-1 -1  3  4  5]
```

Para cada elemento:

```text
condição verdadeira → utiliza arr

condição falsa      → utiliza -1
```

Outro exemplo:

```python
notas = np.array([8.0, 4.5, 7.0, 3.0])

situacoes = np.where(
    notas >= 6,
    "Aprovado",
    "Reprovado"
)

print(situacoes)
```

Saída:

```text
['Aprovado' 'Reprovado' 'Aprovado' 'Reprovado']
```

#### `np.all` e `np.any`

Podemos verificar se **todos** os elementos satisfazem uma condição:

```python
arr = np.array([1, 2, 3, 4, 5])

print(np.all(arr > 0))
```

Saída:

```text
True
```

Ou se **pelo menos um** satisfaz:

```python
print(np.any(arr > 4))
```

Saída:

```text
True
```

Assim:

```text
np.all → todas as posições precisam ser True

np.any → pelo menos uma posição precisa ser True
```

### 3.3. Operações com Conjuntos

O NumPy também fornece operações úteis quando queremos tratar os valores dos arrays como conjuntos.

Considere:

```python
a = np.array([1, 2, 3, 4, 5])
b = np.array([3, 4, 5, 6, 7])
```

Algumas operações são:

| Função                 | Operação                                        |
| ---------------------- | ----------------------------------------------- |
| `np.unique(a)`         | Valores únicos                                  |
| `np.intersect1d(a, b)` | Interseção                                      |
| `np.union1d(a, b)`     | União                                           |
| `np.isin(a, b)`        | Verifica quais elementos de `a` aparecem em `b` |

Por exemplo:

```python
print(np.intersect1d(a, b))
```

Saída:

```text
[3 4 5]
```

```python
print(np.union1d(a, b))
```

Saída:

```text
[1 2 3 4 5 6 7]
```

A função `np.isin` retorna um array booleano:

```python
print(np.isin(a, b))
```

Saída:

```text
[False False  True  True  True]
```

Esse resultado também pode ser utilizado para indexação:

```python
print(a[np.isin(a, b)])
```

Saída:

```text
[3 4 5]
```

#### Valores Únicos e Contagem

`np.unique` também pode ser utilizado para contar quantas vezes cada valor aparece.

```python
valores = np.array([1, 2, 2, 3, 3, 3, 4])

unicos, contagens = np.unique(
    valores,
    return_counts=True
)

print(unicos)
print(contagens)
```

Saída:

```text
[1 2 3 4]

[1 2 3 1]
```

### 3.4. Ordenação de Arrays

Podemos ordenar arrays utilizando:

```python
np.sort(...)
```

ou:

```python
arr.sort()
```

Considere:

```python
arr = np.array([5, 1, 9, 3, 7])
```

`np.sort` retorna um novo array:

```python
sorted_array = np.sort(arr)

print(sorted_array)
print(arr)
```

Saída:

```text
[1 3 5 7 9]

[5 1 9 3 7]
```

Já:

```python
arr.sort()

print(arr)
```

modifica o próprio array:

```text
[1 3 5 7 9]
```

Portanto:

```text
np.sort(arr)
→ retorna um array ordenado

arr.sort()
→ ordena o próprio array
```

## 4. Exercícios

### A. Análise de Notas

Considere:

```python
notas = np.array([
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 4.5],
    [9.5, 8.5, 10.0],
    [6.0, 7.0, 6.5]
])
```

Cada linha representa um aluno e cada coluna representa uma avaliação.

Utilizando operações NumPy:

1. calcule a média geral das notas;
2. calcule a média de cada aluno;
3. calcule a média de cada avaliação;
4. determine a maior nota de cada aluno;
5. determine quais alunos possuem média maior ou igual a `7`;
6. verifique se existe alguma nota menor que `5`;
7. verifique se todas as notas estão entre `0` e `10`.

Evite utilizar loops quando houver uma operação NumPy equivalente.

### B. Validação de Sudoku

Implemente uma função que verifica se uma solução de Sudoku é válida.

Uma solução é válida se:

* cada linha contém todos os números de `1` a `9`, sem repetição;
* cada coluna contém todos os números de `1` a `9`, sem repetição;
* cada subgrade `3 × 3` contém todos os números de `1` a `9`, sem repetição.

Algumas operações que podem ser úteis:

```python
np.unique(...)
np.all(...)
```

Para transformar uma região bidimensional em um vetor:

```python
regiao.flatten()
```

Teste utilizando:

```python
valid_sudoku = np.array([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
])
```

e:

```python
invalid_sudoku = np.array([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 1, 9]
])
```
