import numpy as np

a = 5.5 * np.ones((3, 2))
b = np.zeros((3, 2))
c = np.full((3, 2), 5.5)
d = np.identity(5)
print(a)
print(b)
print(c)
print(d)

e = [1, 2, 3, 4, 5]
f = np.array(e)
print(type(e), e)
print(type(f), f)

g = [
    [1, 2, (3.0) ** 500],
    [4, 5, 6],
]
h = np.array(g)
print(type(g), g)
print(type(h), h)
print(h.size)
print(h.shape)
print(h.dtype)

a = [
    "Joao",
    "Matheus",
    "Rafaela",
    "Bruna",
    "Igor"
]
b = np.array(a)
print(type(b), b.dtype, b)

b[1] = "abcderfghij"
print(type(b), b.dtype, b)

# Aritmetica basica

a = np.array([1, 2, 3, 4, 5, 6])
print(a + 5)
print(a - 5)
print(a * 5)
print(a / 5)
print(a ** 2)
print(a % 2)

print()
b = np.array([5, 4, 3, 4, 4, 4])
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
print(a % b)

# Vetorizacao

# Distancia euclidiana?

a = np.array([1, 2])
b = np.array([3, 5])

print("#1", b - a)
print("#2", (b - a) ** 2)
print("#3", sum((b - a) ** 2))
print("#4", (np.sum((b - a) ** 2)) ** (1/2))

# Indexacao / Busca

a = np.arange(10)
print(a)
print(a[2:4])

a = np.arange(15).reshape((5, 3))
print(a)
print(a[2:4][1])
print(a[2:4, 1])

sudoku = np.arange(81).reshape((9, 9))
print(sudoku)
print(sudoku[3:6, 3:6])

mask = sudoku > 50
print(mask)
mask2 = mask.astype(np.int8)
print(mask2)
mask3 = sudoku > 10

print(sudoku[10 < sudoku])

print(sudoku[[1, 2, 5]])

sub_conjunto = sudoku[[1, 2, 2, 2, 2]]
print(sub_conjunto)
sub_conjunto[1, 1] = -10000
print(sub_conjunto)
print(sudoku)

# Numpy: fancy index

# print(sudoku[sudoku % 9])
# Acessa os elementos: (1,2) , (2,3), (5,4)
m = sudoku[[1, 2, 5],
           [2, 3, 4]]
