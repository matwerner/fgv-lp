from datetime import datetime
import time

# CLOSURE & DECORADOR


def contador_chamadas():
    count = 0

    def exibir():
        nonlocal count
        print(f"Chamada #{count}")
        count += 1
    return exibir


f1 = contador_chamadas()
f1()
f1()

f2 = contador_chamadas()
f2()
f2()


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        resultado = func(*args, **kwargs)
        delta = time.time() - start
        print(f"Demorou {delta} segundos")
        return resultado
    return wrapper


def stats(n_repeticoes):
    def timer(func):
        def wrapper(*args, **kwargs):
            tempos_de_execucao = []
            for i in range(n_repeticoes):
                start = time.time()
                resultado = func(*args, **kwargs)
                delta = time.time() - start
                tempos_de_execucao.append(delta)
                print(f"#{i} Demorou {delta} segundos")
            media = sum(tempos_de_execucao) / len(tempos_de_execucao)
            print(f"A media de {n_repeticoes} foi: {media} segundos")
            print(f"Tempo total: {sum(tempos_de_execucao)}")
            return resultado
        return wrapper
    return timer


stats_100 = stats(200)
# @stats_100  # calculo_complexo = timer(calculo_complexo)


@stats(100)  # @
def calculo_complexo(n: int) -> int:
    total = 0
    for i in range(n):
        total += i
    return total


calculo_complexo(10000)
# f = stats_100(calculo_complexo)
# print(f(100))


# PROGRAMACAO FUNCIONAL

l = [1, 2, 3, 4, 5]

# Imperativa

s = []
# V1
for i in range(len(l)):
    if l[i] > 3:
        s.append(l[i])

# V2
s = []
for i in l:
    if i > 3:
        s.append(i)

# V3
s = [i for i in l if i > 3]  # List comprehsion

# Funcional


def greater_than_3(x):
    return x > 3


s = list(filter(lambda x: x > 3, l))

print(s)


def greetings_inpure(name):
    today = datetime.now()
    if today.hour < 12:
        print(f"Bom dia, {name}")
    else:
        print(f"Oi, {name}")


def greetings_pure(name, date):
    if date.hour < 12:
        return f"Bom dia, {name}"
    else:
        return f"Oi, {name}"


greetings_inpure("matheus")
greetings_pure("matheus", datetime.today())
