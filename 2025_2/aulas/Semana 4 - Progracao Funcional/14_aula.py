import time


def fabrica_funcs():
    def exibir():
        print("a")
    return exibir()


def fabrica_de_conversores(moeda, cotacao):  # Closure
    def conversor(valor):
        print(f"Valor em {moeda}: {valor * cotacao}")
    return conversor


conversor_dolar = fabrica_de_conversores("US$", 5.40)
conversor_euro = fabrica_de_conversores("£", 7.10)

print(conversor_dolar(10))
print(conversor_euro(10))

num_chamadas = 0


def contar_chamadas():
    num_chamadas = 0

    def func():
        nonlocal num_chamadas
        print(f"#{num_chamadas} Chamou minha funcao")
        num_chamadas += 1

    return func


f1 = contar_chamadas()
f1()  # 0
f1()  # 1
f1()  # 2
f1()  # 3

print(f1.__code__.co_freevars)
print(f1.__closure__[0].cell_contents)

f2 = contar_chamadas()
f2()  # 0
f2()  # 1

print(f2.__code__.co_freevars)
print(f2.__closure__[0].cell_contents)

f2.__closure__[0].cell_contents = 1000
f2()

f1()  # 4

# O que acontece?
# A) da erro
# B) Dá sempre 0
# C) Conta em sequencia (0, 1, 2, 3, ...)


def fabrica_fib():
    memoria = dict()

    def fib(n):
        nonlocal memoria
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n in memoria:
            return memoria[n]
        resultado = fib(n-1) + fib(n-2)
        memoria[n] = resultado
        return resultado
    return fib


fib1 = fabrica_fib()
print(fib1(100))


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(args)
        print(kwargs)
        resultado = func(*args, **kwargs)
        delta = time.time() - start
        print(f"Minha funcao levou {delta} segundos")
        return resultado
    return wrapper


@timer  # Equivalente calculo_super_complexo = timer(calculo_super_complexo)
def calculo_super_complexo(n):
    total = 0
    for i in range(n):
        total += i
    return total


@timer  # equivalente a soma = timer(soma)
def soma(a, b):
    return a + b


# calculo_super_complexo()
# soma()

def test_args(a, b, c, *args, **kwargs):
    print(args)
    print(kwargs)


test_args(1, 2, 3, "a", "b", n=10)

res = soma(2, 3)
print(res)
