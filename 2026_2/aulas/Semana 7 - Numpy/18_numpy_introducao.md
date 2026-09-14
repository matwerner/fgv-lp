# Aula 18: NumPy I

O **NumPy** (*Numerical Python*) é uma biblioteca voltada para computação numérica em Python, utilizada principalmente para manipulação de arrays e matrizes multidimensionais e para realização de operações matemáticas de forma eficiente.

O NumPy serve como base para diversas outras bibliotecas, como `Pandas`, `SciPy` e bibliotecas utilizadas em ciência de dados e aprendizado de máquina.

Mas por que utilizar NumPy em vez das estruturas que já conhecemos em Python?

Algumas das principais vantagens são:

* **Vetorização e desempenho:** operações podem ser aplicadas diretamente sobre arrays inteiros, evitando loops explícitos em Python.
* **Menor consumo de memória:** arrays NumPy armazenam dados homogêneos de forma mais compacta do que listas Python, que armazenam referências para objetos.
* **Controle sobre o espaço utilizado:** podemos escolher tipos como `int8`, `int32`, `float32` ou `float64`, controlando quantos bytes são utilizados para representar cada valor.

Para dar uma ideia da diferença de desempenho, considere a multiplicação de um milhão de valores por `2`:

```python id="9b1g5k"
from datetime import datetime

# Multiplicação utilizando Python
start_date = datetime.now()

my_list = list(range(10**6))
my_list2 = []

for x in my_list:
    my_list2.append(x * 2)

end_date = datetime.now()

delta = end_date - start_date

print(f"Python time: {delta.total_seconds()}")


# Multiplicação utilizando NumPy
import numpy as np

start_date = datetime.now()

my_arr = np.arange(10**6)
my_arr2 = my_arr * 2

end_date = datetime.now()

delta = end_date - start_date

print(f"NumPy time: {delta.total_seconds()}")
```

Em NumPy, a operação:

```python id="we3j3n"
my_arr * 2
```

é aplicada diretamente sobre todos os elementos do array.

Esse tipo de operação é chamado de **vetorização**.

Para grandes volumes de dados, operações vetorizadas podem ser significativamente mais rápidas e consumir menos memória do que soluções equivalentes utilizando objetos e loops Python.



## 1. `ndarray`

O `ndarray` é o principal objeto do NumPy.

Ele representa um array multidimensional e permite realizar operações matemáticas diretamente sobre conjuntos inteiros de dados.

Por exemplo:

```python id="od9qt2"
import numpy as np

data = np.array([
    [1.5, -0.1, 3],
    [0, -3, 6.5]
])

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

No primeiro caso, todos os elementos foram multiplicados por `10`.

No segundo, os valores correspondentes dos dois arrays foram somados.

### 1.1. Propriedades do `ndarray`

Um `ndarray` normalmente contém dados **homogêneos**, ou seja, os elementos possuem um mesmo tipo, de forma semelhante aos arrays que conhecemos de C.

Por conta disso, um `ndarray` possui propriedades que descrevem sua estrutura:

```python id="qykvw0"
data = np.array([
    [1.5, -0.1, 3],
    [0, -3, 6.5]
])

print(data.shape)  # Formato: (2, 3)
print(data.dtype)  # Tipo dos elementos: float64
print(data.size)   # Número total de elementos: 6
```

Nesse caso:

```text id="1uc0xy"
shape → 2 linhas e 3 colunas
dtype → tipo utilizado para armazenar os valores
size  → 6 elementos
```



## 2. Criando `ndarrays`

A forma mais comum de criar um array é utilizando `np.array`:

```python id="88cdkq"
data = [10, 20, 30]

arr = np.array(data)

print(arr)

# [10 20 30]
```

Se fornecermos uma sequência aninhada, podemos criar um array multidimensional:

```python id="gp52kz"
data = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

arr = np.array(data)

print(arr)

# [[1 2 3 4]
#  [5 6 7 8]]
```

Além de `np.array`, existem funções para criar arrays comuns:

```python id="hpqr8b"
print(np.zeros(10))

# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]


print(np.zeros((3, 6)))

# [[0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0.]]


print(np.ones((2, 3)))

# [[1. 1. 1.]
#  [1. 1. 1.]]


print(np.arange(0, 10, 2))

# [0 2 4 6 8]
```

Algumas das principais funções são:

| Função      | Descrição                                                    |
| ----------- | ------------------------------------------------------------ |
| `np.array`  | Cria um array a partir de uma sequência                      |
| `np.zeros`  | Cria um array preenchido com zeros                           |
| `np.ones`   | Cria um array preenchido com uns                             |
| `np.arange` | Cria uma sequência de valores, de forma semelhante a `range` |

Outras funções também estão disponíveis, como `np.full`, `np.asarray` e `np.identity`.



## 3. Tipos de Dados

Ao criar um array, o NumPy tenta **inferir um tipo capaz de representar os valores fornecidos**.

```python id="7fknga"
arr1 = np.array([1, 2, 3])
arr2 = np.array([1.0, 2.0, 3.0])

print(arr1.dtype)
print(arr2.dtype)
```

Diferentemente de uma lista Python, os elementos de um `ndarray` normalmente possuem um mesmo tipo.

Alguns dos tipos mais comuns são:

| Tipo      | Descrição                  |
| --------- | -------------------------- |
| `int8`    | Inteiro de 8 bits          |
| `int32`   | Inteiro de 32 bits         |
| `int64`   | Inteiro de 64 bits         |
| `float32` | Ponto flutuante de 32 bits |
| `float64` | Ponto flutuante de 64 bits |
| `bool`    | Valor booleano             |

A escolha do tipo determina, entre outras coisas, o **espaço necessário para armazenar cada elemento**.

Por exemplo:

```text id="fly52k"
int8    → 1 byte
int32   → 4 bytes
int64   → 8 bytes
float32 → 4 bytes
float64 → 8 bytes
```

Podemos especificar o tipo ao criar um array:

```python id="javbea"
arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array([1, 2, 3], dtype=np.int32)

print(arr1.dtype)  # float64
print(arr2.dtype)  # int32
```

Também podemos converter o tipo de um array existente utilizando `astype`:

```python id="u6o99j"
arr = np.array([1, 2, 3], dtype=np.float64)

print(arr.dtype)  # float64

arr = arr.astype(np.int32)

print(arr.dtype)  # int32
```

### 3.1. Strings

Arrays de strings também possuem um tipo específico.

Por exemplo:

```python id="2ivvas"
arr = np.array(["abc", "123"])

print(arr.dtype)
```

Nesse tipo de array, o espaço reservado para as strings pode possuir tamanho fixo.

Por exemplo:

```python id="mnos29"
arr = np.array(["abc", "123"])

arr[0] = "xyzhi"

print(arr)
```

Dependendo do tipo criado para o array, a string pode ser limitada ao espaço disponível.



## 4. Aritmética Básica

Uma das principais vantagens do NumPy é a capacidade de realizar operações diretamente sobre arrays.

Soma, subtração, multiplicação e divisão são realizadas elemento por elemento:

```python id="3blakq"
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(x + y)  # [5 7 9]

print(x * y)  # [4 10 18]

print(x / y)  # [0.25 0.4  0.5]
```

Também podemos realizar operações entre um array e um único valor:

```python id="593sp4"
print(x * 10)

# [10 20 30]
```

Comparações também são aplicadas elemento por elemento:

```python id="ntx8pf"
print(x > y)

# [False False False]
```

Outro exemplo:

```python id="16v4hc"
arr = np.array([10, 20, 30, 40, 50])

print(arr > 25)

# [False False  True  True  True]
```

Esse tipo de operação direta sobre arrays é conhecido como **vetorização**.

Grande parte do ganho de desempenho do NumPy vem do fato de essas operações serem implementadas de forma eficiente em código de baixo nível, evitando a sobrecarga de executar um loop Python para cada elemento.

Quando existir uma operação vetorizada equivalente, normalmente devemos preferi-la em vez de escrever explicitamente:

```python id="itwcm0"
for valor in arr:
    ...
```



## 5. Indexamento Básico

O indexamento de arrays NumPy é semelhante ao de listas Python.

Em um array unidimensional:

```python id="p0rbex"
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])  # 10
print(arr[4])  # 50
```

Para arrays multidimensionais, podemos informar um índice para cada dimensão:

```python id="fgu5qf"
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(arr[0, 1])  # 2
print(arr[2, 2])  # 9
```

Podemos pensar:

```text id="h5rox1"
arr[linha, coluna]
```



## 6. Fatiamento (*Slicing*)

Assim como em listas Python, podemos utilizar `:` para selecionar uma parte do array.

### 6.1. Arrays Unidimensionais

```python id="r4ibqx"
arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])  # [20 30 40]

print(arr[:3])   # [10 20 30]

print(arr[3:])   # [40 50]
```

### 6.2. Arrays Multidimensionais

Para arrays multidimensionais, podemos fazer slicing separadamente em cada dimensão:

```python id="l9uq6u"
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(arr[1:, :2])

# [[4 5]
#  [7 8]]

print(arr[:2, 1:])

# [[2 3]
#  [5 6]]
```

Por exemplo:

```python id="sw8n2c"
arr[1:, :2]
```

significa:

```text id="7brga8"
linhas  → da posição 1 até o final
colunas → do início até a posição 2
```

### 6.3. View × Cópia

Existe uma diferença importante entre o slicing de listas Python e o slicing de arrays NumPy.

O slicing de um `ndarray` normalmente cria uma **view** dos dados originais.

```python id="y13b4f"
arr = np.array([1, 2, 3, 4, 5])

slice_arr = arr[1:4]

slice_arr[0] = 10

print(arr)
print(slice_arr)
```

Saída:

```text id="v08nis"
[ 1 10  3  4  5]

[10  3  4]
```

A alteração realizada em `slice_arr` também aparece no array original.

Isso ocorre porque os dois objetos estão acessando os mesmos dados.

Quando quisermos uma cópia independente, podemos utilizar:

```python id="hxchc1"
slice_arr = arr[1:4].copy()
```



## 7. Indexação Booleana

A indexação booleana utiliza um array de valores `True` e `False` para selecionar elementos.

Considere:

```python id="8i0hlg"
arr = np.array([10, 20, 30, 40, 50])
```

Podemos criar uma condição:

```python id="gj52nr"
condition = arr > 25

print(condition)

# [False False  True  True  True]
```

E utilizar esse resultado para indexar o próprio array:

```python id="jazcic"
print(arr[condition])

# [30 40 50]
```

Também podemos escrever diretamente:

```python id="pqchfr"
print(arr[arr > 25])
```

A indexação booleana permite, portanto, **filtrar dados utilizando condições vetorizadas**.

### 7.1. Exemplo com Dados Relacionados

Considere dois arrays:

```python id="utwj4q"
names = np.array([
    "Bob",
    "Joe",
    "Will",
    "Bob",
    "Will",
    "Joe",
    "Joe"
])

data = np.array([
    [4, 7],
    [0, 2],
    [-5, 6],
    [0, 0],
    [1, 2],
    [-12, -4],
    [3, 4]
])
```

Podemos verificar quais posições correspondem a `"Bob"`:

```python id="wlsvaf"
print(names == "Bob")
```

E utilizar o resultado para selecionar as linhas correspondentes de `data`:

```python id="tc4syh"
print(data[names == "Bob"])
```

Resultado:

```text id="kguhm4"
[[4 7]
 [0 0]]
```

O mesmo array booleano pode, portanto, ser utilizado para selecionar posições correspondentes em outro array.



## 8. Indexação Avançada (*Fancy Indexing*)

Além de slices e condições booleanas, NumPy permite selecionar elementos utilizando diretamente uma coleção de índices.

### 8.1. Exemplo Unidimensional

```python id="x3pc28"
arr = np.array([10, 20, 30, 40, 50])

indices = [1, 3, 4]

print(arr[indices])

# [20 40 50]
```

Nesse caso, estamos solicitando os valores que ocupam as posições:

```text id="6ao90v"
1, 3 e 4
```

### 8.2. Arrays Multidimensionais

Também podemos fornecer índices para linhas e colunas:

```python id="jf09ve"
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

row_indices = [0, 2]
col_indices = [1, 2]

print(arr[row_indices, col_indices])
```

Resultado:

```text id="07dbct"
[2 9]
```

Isso seleciona os elementos nas posições:

```text id="ospx7o"
(0, 1)
(2, 2)
```

Uma diferença importante é que, enquanto o slicing básico normalmente retorna uma **view**, a indexação avançada retorna uma **cópia** dos dados.



## 9. Exercícios

### A. Matriz de Matrículas

Uma universidade representa as matrículas de seus alunos utilizando uma matriz.

Cada **linha** representa um aluno e cada **coluna** representa uma disciplina.

```python
alunos = np.array([
    "Ana",
    "Bruno",
    "Carla",
    "Daniel"
])

disciplinas = np.array([
    "Cálculo",
    "Programação",
    "Álgebra",
    "Estatística"
])

matriculas = np.array([
    [1, 1, 0, 1],
    [1, 1, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 1]
])
```

Na matriz `matriculas`:

```text
1 → aluno está matriculado na disciplina
0 → aluno não está matriculado na disciplina
```

Por exemplo:

```python
matriculas[0, 1]
```

indica se Ana está matriculada em Programação.

Utilizando NumPy:

1. Obtenha todas as disciplinas cursadas por Ana.
2. Obtenha todos os alunos matriculados em Programação.
3. Obtenha as matrículas de Bruno em todas as disciplinas.
4. Obtenha a submatriz contendo apenas Ana e Carla e as disciplinas Programação e Estatística.
5. Matricule Carla em Álgebra alterando diretamente a matriz.
6. Determine quais disciplinas Daniel cursa.

Evite percorrer manualmente os arrays quando for possível utilizar indexação ou indexação booleana.

### B. Distância entre Vetores

Diferentes métricas podem ser utilizadas para medir a distância ou a similaridade entre dois vetores.

Considere:

```python
a = np.array([1, 2, 3])
b = np.array([4, 2, 1])
```

#### Distância Euclidiana

A distância euclidiana entre dois vetores é dada por:

```text
d(a, b) = √((a₁ - b₁)² + (a₂ - b₂)² + ... + (aₙ - bₙ)²)
```

Implemente:

```python
def distancia_euclidiana(a, b):
    ...
```

utilizando operações NumPy.

Evite utilizar um `for` explícito.

#### Distância de Cosseno

A similaridade de cosseno entre dois vetores é definida por:

```text
                    a · b
cos(a, b) = ───────────────────
             ||a|| × ||b||
```

A **distância de cosseno** pode ser definida como:

```text
d(a, b) = 1 - cos(a, b)
```

Implemente:

```python
def distancia_cosseno(a, b):
    ...
```

Novamente, utilize operações NumPy em vez de percorrer manualmente os elementos.

Teste as duas funções utilizando:

```python
a = np.array([1, 2, 3])
b = np.array([4, 2, 1])
```

Depois compare também:

```python
a = np.array([1, 2, 3])
b = np.array([2, 4, 6])
```

e:

```python
a = np.array([1, 0])
b = np.array([0, 1])
```

Analise:

1. Em qual dos exemplos a distância de cosseno é menor?
2. Dois vetores podem estar distantes pela distância euclidiana e, ao mesmo tempo, muito próximos segundo a distância de cosseno?
3. O que cada uma das métricas parece estar medindo?
