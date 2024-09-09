# Introdução ao NumPy

O NumPy (Numerical Python) é uma biblioteca essencial para computação científica em Python, usada principalmente para manipulação de arrays e matrizes multidimensionais, além de fornecer uma vasta gama de funções matemáticas de alto desempenho.
Ele se destaca por sua eficiência em comparação com as listas comuns do Python, especialmente ao lidar com grandes volumes de dados numéricos.

O NumPy serve como base para muitas outras bibliotecas, como `Pandas`, `SciPy` e `TensorFlow`, tornando-o uma peça fundamental para realizar cálculos complexos e manipulação de dados em diversas áreas, como `ciência de dados`, `aprendizado de máquina` e `simulações científicas`.

Para dar uma ideia da diferença de desempenho, considere uma matriz NumPy de um milhão de inteiros e a lista Python equivalente:
```python
from datetime import datetime

# Multiplicação via Python
start_date = datetime.now()

my_list = list(range(10**6))
my_list2 = []
for x in my_list:
    my_list2.append(x * 2)
end_date = datetime.now()
delta = end_date - start_date
print(f'Pure python time: {delta.total_seconds()}')

# Multiplicação via Numpy
import numpy as np

start_date = datetime.now()

my_arr = np.arange(10**6)
my_arr2 = my_arr * 2

end_date = datetime.now()
delta = end_date - start_date
print(f'Numpy time: {delta.total_seconds()}')
```

Algoritmos baseados em NumPy são geralmente de `10` a `100` vezes mais rápidos (ou mais) do que seus equivalentes Python puros e usam significativamente menos memória.

## 1. ndarray

O `ndarray` é o principal objeto do NumPy.
Ele representa um array multidimensional e oferece várias vantagens sobre as listas Python, como melhor desempenho e operações mais eficientes.
Com o ndarray, é possível realizar operações matemáticas em blocos inteiros de dados de forma eficiente, utilizando uma sintaxe semelhante à das operações entre elementos escalares no Python puro.

Vamos ver alguns exemplos para ilustrar melhor:

```python
import numpy as np

data = np.array([[1.5, -0.1, 3], [0, -3, 6.5]])

print(data)
# array([[ 1.5, -0.1,  3. ],
#        [ 0. , -3. ,  6.5]])
print(data * 10)
# array([[ 15.,  -1.,  30.],
#        [  0., -30.,  65.]])
print(data + data)
# array([[ 3. , -0.2,  6. ],
#        [ 0. , -6. , 13. ]])
```

No primeiro exemplo, todos os elementos foram multiplicados por 10.
No segundo exemplo, os valores correspondentes em cada célula do array foram somados entre si.

### Propriedades do ndarray

Como podemos ver, o `ndarray` é um container multidimensional para dados homogêneos, ou seja, todos os elementos devem ser do mesmo tipo, semelhante ao que ocorre em C.
Por conta dessa estrutura, um objeto `ndarray` possui propriedades especificas que descrevem seu formato, tipo e número total de elementos.

```python
import numpy as np

data = np.array([[1.5, -0.1, 3], [0, -3, 6.5]])
print(data.shape)  # Forma do array: (2, 3)
print(data.dtype)  # Tipo dos elementos: int64
print(data.size)   # Número total de elementos: 6
```

## 2. Criando ndarrays

O NumPy oferece várias maneiras de criar arrays.
A forma mais comum é utilizando a função `np.array`, passando uma sequência de elementos:

```python
data = [10, 20, 30]
arr = np.array(data)
# array([10, 20, 30])
```

Se a sequência for aninhada, como uma lista de listas de comprimento igual, será criada uma matriz multidimensional:

```python
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
# array([[1, 2, 3, 4],
#        [5, 6, 7, 8]])
```

Além de `np.array`,  há outras funções úteis para criar arrays, como:
* `np.zeros`: Criar array de zeros;
* `np.ones`: Criar array de uns;
* `np.arange`: Cria um array com uma sequência de números (similar ao `range()`).

Obs: No caso delas, é necessário informar o formato do array.

```python
print(np.zeros(10))
# array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
print(np.zeros((3, 6)))
# array([[0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0.]])
```

Outras funções incluem `asarray`, `full`, `identity`, entre muitas outras.

## 3. Tipos de dados

Por padrão, ao criar um array, o NumPy tenta inferir o tipo de dado adequado.
Geralmente, ele atribui o tipo `float64`, que é um float de 8 bytes.
Contudo, o NumPy suporta diversos tipos de dados que podem ser atribuídos aos elementos do ndarray:

| **Tipo**    | **Código** | **Descrição**                                                                |
|-------------|------------|------------------------------------------------------------------------------|
| int8        | i1         | Tipos de inteiros com sinal e sem sinal de 8 bits (1 byte)                    |
| uint8       | u1         | Tipos de inteiros com sinal e sem sinal de 8 bits (1 byte)                    |
| int16       | i2         | Tipos de inteiros com sinal e sem sinal de 16 bits                           |
| uint16      | u2         | Tipos de inteiros com sinal e sem sinal de 16 bits                           |
| int32       | i4         | Tipos de inteiros com sinal e sem sinal de 32 bits                           |
| uint32      | u4         | Tipos de inteiros com sinal e sem sinal de 32 bits                           |
| int64       | i8         | Tipos de inteiros com sinal e sem sinal de 64 bits                           |
| uint64      | u8         | Tipos de inteiros com sinal e sem sinal de 64 bits                           |
| float16     | f2         | Ponto flutuante de precisão reduzida                                           |
| float32     | f4 ou f    | Ponto flutuante de precisão padrão; compatível com float do C                 |
| float64     | f8 ou d    | Ponto flutuante de precisão dupla; compatível com double do C e objeto float do Python |
| float128    | f16 ou g   | Ponto flutuante de precisão estendida                                          |
| complex64   | c8         | Números complexos representados por dois floats de 32 bits                     |
| complex128  | c16        | Números complexos representados por dois floats de 64 bits                     |
| complex256  | c32        | Números complexos representados por dois floats de 128 bits                    |
| bool        | ?          | Tipo booleano que armazena valores True e False                               |
| object      | O          | Tipo de objeto Python; um valor pode ser qualquer objeto Python               |
| string      | S          | Tipo de string com comprimento fixo em ASCII (1 byte por caractere); por exemplo, para criar um tipo de string com comprimento 10, use 'S10' |
| unicode     | U          | Tipo de string com comprimento fixo em Unicode (número de bytes específico da plataforma); mesma semântica de especificação que o tipo string_ (por exemplo, 'U10') |

Você pode especificar o tipo de dado ao criar um array:

```python
arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array([1, 2, 3], dtype=np.int32)
print(arr1.dtype) # dtype('float64')
print(arr2.dtype) # dtype('int32')
```

Também é possível converter o tipo de um array já existente:

```python
arr1 = np.array([1, 2, 3], dtype=np.float64)
print(arr1.dtype) # dtype('float64')
arr1 = arr1.astype(np.int32)
print(arr1.dtype) # dtype('int32')
```

É importante estar ciente ao manipular arrays de strings, pois o NumPy cria strings de comprimento fixo.
Isso pode resultar em truncamento de strings maiores do que o comprimento definido:

```python
arr1 = np.array(["abc", "123"])
print(arr1.dtype) # dtype('<U3')
arr1[0] = "xyzhi"
print(arr1) # array(['xyz', '123'], dtype='<U3')
```

## 4. Aritmética básica

Uma das grandes vantagens do NumPy é a sua capacidade de realizar operações aritméticas diretamente em arrays.
Com o NumPy, operações como soma, subtração, multiplicação e divisão são feitas elemento por elemento de forma rápida e eficiente.

Além dessas operações básicas, o NumPy também permite comparar arrays de mesmo tamanho, e essa comparação resulta em um array booleano, onde cada elemento indica o resultado da comparação entre os elementos correspondentes dos arrays.

Aqui estão alguns exemplos ilustrativos:

```python
# Aplicando operações matemáticas
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(x + y)  # [5 7 9]
print(x * y)  # [4 10 18]
print(x / y)  # [0.25 0.4  0.5]

# Aplicando comparação
print(x > y) # [False False False]
```

Esse tipo de operação direta entre arrays, sem a necessidade de loops explícitos, é conhecido como `vetorização`.
É fundamental mencionar que a principal vantagem de desempenho do NumPy em relação ao Python puro vem exatamente dessa vetorização.
Isso ocorre porque o NumPy realiza todos os cálculos internamente em C, evitando a sobrecarga de retornar os elementos do array para o Python.
Portanto, qualquer operação entre arrays que envolva loops explícitos deve ser evitada, pois o desempenho será significativamente inferior ao que se obtém com operações vetorizadas.

## 5. Indexamento Básico

O indexamento em arrays NumPy é semelhante ao indexamento em listas Python, mas com algumas diferenças notáveis devido à natureza multidimensional dos arrays NumPy.

Para acessar elementos em um array unidimensional, você usa colchetes `[]` com o índice do elemento desejado:

```python
import numpy as np

# Criando um array unidimensional
arr = np.array([10, 20, 30, 40, 50])

# Acessando elementos
print(arr[0])  # 10
print(arr[4])  # 50
```

Para arrays multidimensionais, você pode usar múltiplos índices, separados por vírgulas:

```python
# Criando um array bidimensional
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Acessando elementos
print(arr[0, 1])  # 2 (primeira linha, segunda coluna)
print(arr[2, 2])  # 9 (terceira linha, terceira coluna)
```

## 6. Fatiamento (Slicing)

O fatiamento permite extrair uma parte de um array.
Ele é realizado usando dois pontos `:` dentro dos colchetes `[]` para especificar o início e o fim do intervalo.

### 6.1 Fatiamento em Arrays Unidimensionais:

```python
# Criando um array unidimensional
arr = np.array([10, 20, 30, 40, 50])

# Fatiando o array
print(arr[1:4])  # [20 30 40] (do índice 1 ao 3)
print(arr[:3])   # [10 20 30] (do início até o índice 2)
print(arr[3:])   # [40 50] (do índice 3 até o fim)
```

### 6.2 Fatiamento em Arrays Multidimensionais:
Para arrays multidimensionais, você pode fatiar cada dimensão separadamente:

```python
# Criando um array bidimensional
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Fatiando o array
print(arr[1:, :2])  # [[4 5] [7 8]] (do índice 1 ao fim, e das primeiras duas colunas)
print(arr[:2, 1:])  # [[2 3] [5 6]] (das duas primeiras linhas, e das colunas 1 em diante)
```

### 6.3 View vs. Cópia

É importante notar que o fatiamento em NumPy cria uma `view` do array original.
Isso significa que a fatia é uma visão do array original, e modificações na fatia afetarão o array original:

```python
arr = np.array([1, 2, 3, 4, 5])
slice_arr = arr[1:4]

# Modificando a fatia
slice_arr[0] = 10

print(arr)       # [1 10  3  4  5] (o array original é alterado)
print(slice_arr) # [10  3  4]
```

## 7. Indexação Booleana

A indexação booleana usa um array de valores booleanos para selecionar elementos de um array.
Isso é útil para filtrar dados com base em uma condição.

```python
# Criando um array unidimensional
arr = np.array([10, 20, 30, 40, 50])

# Criando um array de condições booleanas
condition = arr > 25

# Aplicando a indexação booleana
print(arr[condition])  # [30 40 50]
```

Neste exemplo, `arr > 25` cria um array booleano onde cada posição é `True` ou `False`, dependendo se o elemento correspondente em `arr` atende à condição.
O resultado da indexação booleana é um novo array contendo apenas os elementos para os quais a condição é True.

### Exemplo Avançado

Agora, imagine que você tem dois arrays:
um contendo nomes e outro contendo dados associados a esses nomes.
Suponha que você queira selecionar todas as linhas de dados correspondentes ao nome `"Bob"`.
Para fazer isso, você pode comparar o array de nomes com a string `"Bob"`, gerando um array booleano que será usado para indexar o array de dados.

```python
names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])
data = np.array([[4, 7], [0, 2], [-5, 6], [0, 0], [1, 2], [-12, -4], [3, 4]])

print(names == "Bob")
print(data[names == "Bob"])
# array([[4, 7],
#        [0, 0]])
```

Neste exemplo, `names == "Bob"` gera um array booleano indicando quais posições no array names são iguais a `"Bob"`.
Esse array booleano é então usado para indexar data, resultando em um array que contém apenas as linhas associadas a `"Bob"`.

## 8. Indexação Avançada (Fancy Indexing)

A indexação avançada, também conhecida como "fancy indexing", é uma técnica que permite selecionar elementos de um array utilizando um array de índices. 
Ao contrário do fatiamento, que retorna uma view do array original, a indexação avançada retorna uma cópia dos dados.
Isso significa que alterações na cópia não afetam o array original.

### Exemplo Simples

Vamos considerar um array unidimensional e um array de índices para demonstrar a indexação avançada:

```python
# Criando um array unidimensional
arr = np.array([10, 20, 30, 40, 50])

# Criando um array de índices
indices = [1, 3, 4]

# Aplicando a indexação avançada
print(arr[indices])  # [20 40 50]
```

Aqui, o array indices especifica quais elementos do array `arr` devem ser selecionados.
O resultado é um novo array contendo os elementos nos índices fornecidos.

### Exemplo em Arrays Multidimensionais

A indexação avançada também pode ser aplicada a arrays multidimensionais, permitindo a seleção de elementos de maneira flexível:

```python
# Criando um array bidimensional
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Índices para linhas e colunas
row_indices = [0, 2]
col_indices = [1, 2]

# Aplicando a indexação avançada
print(arr[row_indices, col_indices])  # [2 9]
```

Neste exemplo, `row_indices` e `col_indices` são usados para selecionar elementos específicos das linhas e colunas indicadas.
O resultado é um array com os valores localizados nas posições especificadas pelos índices.

## 9. Exercícios

### A. Criação e Propriedades de Arrays
* Crie um array NumPy unidimensional contendo os números de `1` a `10`.
Em seguida, imprima o array e verifique suas propriedades (shape, dtype, size).
* Crie um array NumPy bidimensional com `3` linhas e `4` colunas, preenchido com zeros.
Imprima o array e verifique suas propriedades.

### B. Indexação e Fatiamento
* Crie um array NumPy bidimensional `4x4` contendo números de `1` a `16`.
Selecione e imprima a submatriz que contém as 2 primeiras linhas e as 3 primeiras colunas.
* Dado o array bidimensional a seguir:
    ```python
    arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
    ```
    - a) Selecione e imprima a segunda coluna.
    - b) Selecione e imprima os elementos da última linha.
    - c) Selecione e imprima uma submatriz que compreende a segunda e terceira linhas e a primeira e segunda colunas.

### C. Indexação Booleana
* Crie um array NumPy contendo os números de `1` a `20`.
Use a indexação booleana para selecionar e imprimir todos os números pares.
* Dado o array de nomes e o array de dados a seguir:
    ```python
    names = np.array(["Alice", "Bob", "Charlie", "Bob", "Alice"])
    data = np.array([[5, 7], [8, 10], [1, 3], [4, 6], [7, 8]])
    ```
    - a) Use a indexação booleana para selecionar todas as linhas onde o nome é `"Alice"`.
    - b) Use a indexação booleana para selecionar todas as linhas onde o nome é `"Bob"` e calcule a média dos valores em cada linha selecionada.

### D. Indexação Avançada (Fancy Indexing)
* Crie um array unidimensional de `15` elementos e use um array de índices para selecionar os elementos nas posições 3, 7 e 10.
Imprima o resultado.
* Dado o array bidimensional a seguir:
    ```python
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    ```
    - a) Selecione e imprima os elementos nas posições (0, 1), (1, 2) e (3, 0) usando indexação avançada.
    - b) Crie dois arrays de índices para linhas e colunas e use-os para selecionar elementos específicos.
    Por exemplo, selecione os elementos das linhas 1 e 3 e das colunas 0 e 2.

### E. Slicing e Views
* Crie um array NumPy unidimensional com `12` elementos.
Use o fatiamento para selecionar os elementos das posições `3` a `8`.
Modifique os valores selecionados e observe como a modificação afeta o array original.
* Crie um array bidimensional `5x5` com números de `1` a `25`.
Use o fatiamento para selecionar a submatriz composta pelas 3 primeiras linhas e 3 primeiras colunas.
Em seguida, modifique todos os elementos da submatriz para zero e observe o impacto no array original.
