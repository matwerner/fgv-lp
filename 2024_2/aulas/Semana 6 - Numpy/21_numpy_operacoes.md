# Operações com ndarrays

Nesta aula, vamos continuar explorando o poder do NumPy, focando em funções universais (ufuncs), geração de números aleatórios, operações com arrays booleanos e de conjuntos, além de ordenação de arrays.
O objetivo é entender como essas funcionalidades podem tornar o trabalho com grandes volumes de dados eficiente, substituindo o uso de loops e outras operações que, em Python puro, seriam mais lentas.

## 1. Funções Universais (ufuncs)

As `funções universais` são uma das principais funcionalidades do NumPy.
Elas permitem aplicar operações matemáticas diretamente aos arrays, operando elemento por elemento de maneira muito eficiente.
Em vez de escrever loops para processar cada item do array, as ufuncs permitem realizar operações em massa.

Exemplos de ufuncs incluem operações matemáticas como:
* `np.abs`: Calcula o valor absoluto de cada elemento.
* `np.sqrt`: Calcula a raiz quadrada de cada elemento.
* `np.square`: Eleva ao quadrado.
* `np.log`: Logaritmo natural.
* `np.floor, np.ceil`: Arredondamento para baixo ou para cima.
* `np.cos, np.sin, np.tan`: Funções trigonométricas.
* `np.maximum, np.minimum`: Retorna o valor máximo ou mínimo entre dois arrays.
* `np.exp`: Exponencial de cada elemento.

Essas funções são vetorizadas, o que significa que são aplicadas a todos os elementos de um array de uma só vez, sem a necessidade de laços explícitos.

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Soma dos arrays
c = np.maximum(a, b)
print("Máximo: ", c)

# Exponencial de cada elemento
exp = np.exp(a)
print("Exponencial: ", exp)
```

Neste exemplo, `np.maximum` compara os elementos correspondentes de `a` e `b` e retorna o maior valor.
Já `np.exp` calcula o valor de $e^x$ para cada elemento de `a`.

## 2. Gerador de Números Aleatórios

O NumPy oferece o módulo `random`, que facilita a geração de números aleatórios de diferentes distribuições estatísticas.
Isso é extremamente útil em simulações, experimentos estatísticos e testes.
O gerador de números aleatórios do NumPy é muito mais eficiente e poderoso do que a função random padrão do Python.

Principais funções:
* `np.random.rand()`:
Gera números aleatórios de uma distribuição uniforme no intervalo `[0, 1)`.
* `np.random.randn()`:
Gera números aleatórios de uma distribuição normal (média 0 e desvio padrão 1).
* `np.random.randint(low, high)`:
Gera números inteiros aleatórios em um intervalo específico.

```python
# Gera uma matriz 3x3 de números aleatórios uniformes
random_array = np.random.rand(3, 3)
print("Matriz de números aleatórios:\n", random_array)

# Gera números inteiros aleatórios de 1 a 10
integers = np.random.randint(1, 10, size=(3, 3))
print("Números inteiros aleatórios:\n", integers)
```

Neste exemplo, utilizamos o `np.random.rand()` para gerar uma matriz de números aleatórios entre `0` e `1`,
e `np.random.randint()` para gerar uma matriz de inteiros dentro do intervalo de `1` a `10`.

## 3. Operações sobre Arrays

### 3.1 Operações Booleanas

Arrays booleanos são extremamente úteis em análises condicionais.
O NumPy permite aplicar operações como `np.where`, `np.all`, e `np.any`, que facilitam a seleção, filtragem e análise de dados.

* `np.where(condition, x, y)`:
Retorna elementos de x onde a condição é verdadeira e de y onde é falsa.
* `np.all(a)`:
Verifica se todos os elementos do array são verdadeiros.
* `np.any(a)`:
Verifica se pelo menos um elemento é verdadeiro.

Essas operações são rápidas e podem ser aplicadas a arrays inteiros de forma vetorizada, o que melhora o desempenho quando comparado a loops comuns.

```python
arr = np.array([1, 2, 3, 4, 5])

# Condição: valores maiores que 2
condition = arr > 2
result = np.where(condition, arr, -1)  # Substitui por -1 onde a condição é falsa
print("Resultado com where:", result)

# Verifica se todos os elementos são maiores que 0
all_positive = np.all(arr > 0)
print("Todos maiores que 0:", all_positive)
```

Aqui usamos `np.where` para substituir valores menores ou iguais a `2` por `-1`, e `np.all` para verificar se todos os elementos do array são maiores que zero.

### 3.2 Operações com Conjuntos

O NumPy fornece funções para realizar operações de conjunto, como `np.unique`, `np.intersect1d`, `np.union1d` e `np.in1d`.
Estas funções são úteis para comparar e manipular arrays, tratando-os como conjuntos matemáticos.
* `np.unique(a)`: Retorna os valores únicos do array.
* `np.intersect1d(a, b)`: Interseção entre dois arrays.
* `np.union1d(a, b)`: União de dois arrays.
* `np.in1d(a, b)`: Verifica se os elementos de a estão presentes em b.

```python
a = np.array([1, 2, 3, 4, 5])
b = np.array([3, 4, 5, 6, 7])

# Elementos únicos
unique_values = np.unique(a)
print("Valores únicos:", unique_values)

# Interseção de a e b
intersection = np.intersect1d(a, b)
print("Interseção:", intersection)

# União de a e b
union = np.union1d(a, b)
print("União:", union)
```

Essas operações facilitam a comparação de arrays como se fossem conjuntos.
A função `np.unique` elimina elementos duplicados, enquanto `np.intersect1d` e `np.union1d` permitem encontrar interseções e uniões entre arrays.

### 3.3 Ordenação de Arrays

Ordenar arrays no NumPy pode ser feito com as funções `np.sort()` ou `arr.sort()`.
A principal diferença entre elas é que `np.sort` retorna uma cópia ordenada do array, enquanto `arr.sort` modifica o array original.

```python
arr = np.array([5, 1, 9, 3, 7])

# Ordena o array
sorted_array = np.sort(arr)
print("Array ordenado:", sorted_array)

# Ordena in-place
arr.sort()
print("Array ordenado in-place:", arr)
```

Aqui, `np.sort` cria um novo array com os elementos ordenados, enquanto `arr.sort` altera o array original.

## 4. Exercícios

* A. Implemente as seguintes métricas utilizando NumPy:
    - a) Distância Euclideana:
        $$
        \text{distância} = \sqrt{\sum_{i} (a_i - b_i)^2}
        $$

    - b) Similaridade de cossenos:
        $$
        \text{similaridade} = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \|\mathbf{b}\|}
        $$

* B. Implemente uma função para verificar se uma solução de Sudoku é válida.
    * Uma solução é válida se:
        * Cada linha contém todos os números de `1` a `9`, sem repetição.
        * Cada coluna contém todos os números de `1` a `9`, sem repetição.
        * Cada subgrade 3x3 contém todos os números de `1` a `9`, sem repetição.
    * Para facilitar, buscar na documentação do numpy as funções: `np.all`, `np.flatten` e `np.unique`
    * Para testar:
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

        invalid_sudoku = np.array([
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 1, 9]  # Repetição de 1 na última linha
        ])
        ```
