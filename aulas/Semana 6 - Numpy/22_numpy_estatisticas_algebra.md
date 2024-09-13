# Manipulação de Arrays, Estatística Básica e Álgebra Linear

## 1. Leitura e Escrita de Arrays

O NumPy permite salvar e carregar dados no disco em formatos de texto e binários.
Embora seja possível usar o NumPy para essas operações, na prática, muitos usuários optam por utilizar o pandas e outras ferramentas especializadas para lidar com dados em formatos de texto ou tabulares.
A principal vantagem de usar as funções do NumPy sobre as demais ferramentas é se necessitar salvar e carregar arrays diretamente em formato binário, o que é mais eficiente e adequado do que manipular textos.

### 1.1 Arrays como Texto
O `NumPy` permite salvar arrays em formato de texto usando `np.savetxt()` e carregá-los utilizando `np.loadtxt()`. 
Por exemplo:

```python
import numpy as np

# Criando um array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Salvando como arquivo de texto
np.savetxt('array.txt', arr, delimiter=',')

# Carregando o array do arquivo salvo
loaded_arr = np.loadtxt('array.txt', delimiter=',')
print(loaded_arr)
```

### 1.2 Arquivos Binários

Para uma leitura e escrita mais eficiente, usamos arquivos binários `.npy`:
```python
# Salvando como arquivo binário
np.save('array.npy', arr)

# Carregando do arquivo binário
binary_arr = np.load('array.npy')
print(binary_arr)
```

### 1.3 Múltiplos Arrays

Podemos salvar múltiplos arrays em um único arquivo `.npz` usando `np.savez()`:

```python
# Salvando múltiplos arrays
np.savez('arrays.npz', arr1=arr, arr2=np.array([7, 8, 9]))

# Carregando múltiplos arrays
data = np.load('arrays.npz')
print(data['arr1'])
print(data['arr2'])
```

## 2. Estatística Básica

Um conjunto de funções matemáticas que calculam estatísticas sobre um array inteiro ou sobre os dados ao longo de um eixo está acessível como métodos da classe de array.
Você pode usar agregações (às vezes chamadas de reduções), como `soma`, `média` e `desvio padrão (std)`.

### 2.1 Soma

A função `np.sum()` calcula a soma dos elementos de um array.
Você pode usar o parâmetro `axis` para somar ao longo de um eixo específico.
Este parâmetro é aplicável também às demais funções de agregação que veremos mais a frente.

```python
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Soma de todos os elementos
print(np.sum(arr_2d))

# Soma ao longo do eixo 0 (colunas)
print(np.sum(arr_2d, axis=0))

# Soma ao longo do eixo 1 (linhas)
print(np.sum(arr_2d, axis=1))
```

* `axis=0`: Soma ao longo das colunas, retornando um array com a soma de cada coluna.
* `axis=1`: Soma ao longo das linhas, retornando um array com a soma de cada linha.

### 2.2 Cálculo de Máximo e Mínimo

#### Valor Máximo e Mínimo

Usamos `np.max()` e `np.min()` para encontrar os valores máximos e mínimos de um array:

```python
arr = np.array([1, 3, 5, 7, 9])

# Valor máximo
print(np.max(arr))
print(arr.max())

# Valor mínimo
print(np.min(arr))
print(arr.min())
```

#### Índice do Valor Máximo e Mínimo

Para encontrar o índice do maior e menor valor, utilizamos `np.argmax()` e `np.argmin()`:

```python
# Índice do valor máximo
print(np.argmax(arr))
print(arr.argmax())

# Índice do valor mínimo
print(np.argmin(arr))
print(arr.argmin())
```

### 2.3 Percentis

Podemos calcular percentis de um array com `np.percentile()`:

```python

# Cálculo do percentil 50 (mediana)
print(np.percentile(arr, 50))

# Percentil 90
print(np.percentile(arr, 90))
```

### 2.4 Média, Mediana, Desvio Padrão e Variância

```python

# Média
print(np.mean(arr))
print(arr.mean())

# Mediana
print(np.median(arr))
print(arr.median())

# Desvio Padrão
print(np.std(arr))
print(arr.std())

# Variância
print(np.var(arr))
print(arr.var())
```

## 3. Álgebra Linear

Operações de álgebra linear, como multiplicação de matrizes, decomposições, determinantes e outras operações com matrizes quadradas, são uma parte importante de muitas bibliotecas de arrays.

### 3.1 Operações com Matrizes

#### Multiplicação de Matrizes

Podemos multiplicar duas matrizes usando `np.dot()` ou o operador `@`:

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Multiplicação de matrizes
print(np.dot(A, B))
# Ou usando o operador @
print(A @ B)
```

#### Transposição de Matrizes

Para transpor uma matriz, usamos `np.transpose()`:

```python
# Transpor a matriz A
print(np.transpose(A))
```

#### Traço de uma Matriz

O traço de uma matriz (soma dos elementos na diagonal principal) pode ser obtido com np.trace():

```python
# Traço da matriz A
print(np.trace(A))
```

#### Determinante de uma Matriz

Usamos `np.linalg.det()` para calcular o determinante de uma matriz:

```python
# Determinante de A
print(np.linalg.det(A))
```

#### Inversão de Matrizes

Para calcular a inversa de uma matriz, utilizamos `np.linalg.inv()`:

```python
# Inversa da matriz A
print(np.linalg.inv(A))
```

### 3.2 Solução de Sistemas Lineares

Para resolver sistemas de equações lineares da forma `Ax = b`, usamos `np.linalg.solve()`.
Consideremos o seguinte sistema linear:

$$
\begin{aligned}
3x + y &= 9 \\
x + 2y &= 8
\end{aligned}
$$

e sua forma matricial:

$$
A = \begin{bmatrix} 
3 & 1 \\ 
1 & 2 
\end{bmatrix}, \quad
x = \begin{bmatrix} 
x \\ 
y 
\end{bmatrix}, \quad
b = \begin{bmatrix} 
9 \\ 
8 
\end{bmatrix}
$$

```python
# Sistema: Ax = b
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])

# Resolver para x
x = np.linalg.solve(A, b)
print(x)
```