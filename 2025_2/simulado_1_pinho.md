# Questão 1

## (a)  
Analise o código abaixo e escreva exatamente o que é impresso no console (linha a linha), seguido do valor final impresso por `print(somar(3, 4))`. Em seguida, explique por que essa é a ordem correta.

```python
def trace(func):
    def wrapper(*args, **kwargs):
        print(f"enter:{func.__name__}")
        result = func(*args, **kwargs)
        print(f"exit:{func.__name__} -> {result}")
        return result
    return wrapper

def double(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        return value * 2
    return wrapper

@trace
@double
def somar(a, b):
    return a + b

print(somar(3, 4))
```

## (b)  
Implemente `call_limit(max_calls)` que retorna um decorator. Esse decorator, ao ser aplicado a qualquer função, permite apenas `max_calls` execuções; a partir da `(max_calls + 1)`-ésima tentativa, levante `RuntimeError("limite de chamadas excedido")`.

```python
@call_limit(2)
def somar_valores(left, right):
    return left + right

print(somar_valores(1, 2)) # ok
print(somar_valores(2, 3)) # ok
print(somar_valores(3, 4)) # deve levantar RuntimeError
```

## (c)
1. No item (a), é possível que `func.__name__` impresso seja `"wrapper"` (e não `"somar"`). Explique por que isso pode acontecer e como corrigir de forma conceitual (não é necessário escrever o código completo).  
2. Explique o impacto de inverter a ordem dos decorators, ou seja, usar `@double` mais externo e `@trace` mais interno.


# Questão 2

## (a)
```python
functions = []
for index in range(3):
    functions.append(lambda number: number + index)

computed_values = [fn(10) for fn in functions]
print(computed_values)
```

- O que é impresso?  
- Explique tecnicamente por que esse resultado acontece.  
- Mostre uma forma correta de obter o resultado `[10, 11, 12]` usando o mesmo laço.

## (b)  
Implemente apenas a função `make_filter` que recebe critérios opcionais e retorna uma função de filtro (`True`/`False` para um nome de produto).

**Regras:**
- `min_length`: se fornecido, o nome deve ter comprimento ≥ `min_length`.  
- `starts_with`: se fornecido, o nome deve começar com esse prefixo (case sensitive).  
- `forbidden_substrings`: coleção de substrings proibidas; se qualquer uma aparecer no nome, rejeite.

**Esqueleto e exemplo:**

```python
def make_filter(min_length=None, starts_with=None, forbidden_substrings=()):
    # retorne uma função filter_fn(product_name) -> bool
    # utilize as variáveis de make_filter dentro de filter_fn
    ...

product_names = ["arroz", "açúcar", "azeite", "sal", "salmarinho", "salada"]

filter_fn = make_filter(min_length=4, starts_with="a", forbidden_substrings=("ç", "zite"))
filtered = [name for name in product_names if filter_fn(name)]
```

## (c)  
Implemente `compose(*functions)` que devolve uma função que aplica as funções em ordem da esquerda para a direita:

```python
g = compose(f1, f2, f3)
# g(x) == f3(f2(f1(x))) ← observe a ordem
```

Dado o mapeamento de operações:

```python
operations = {
    "double": lambda number: number * 2,
    "square": lambda number: number * number,
    "negate": lambda number: -number,
}
```

### (i)  
Construa, com `compose`, um pipeline equivalente a “dobrar e depois elevar ao quadrado” e calcule o resultado para `input_value = 3`.

### (ii)  
Implemente `choose_and_apply(program_steps, operation_map, initial_value)` que:
- recebe `program_steps` como lista de strings (chaves presentes em `operation_map`),  
- busca as funções correspondentes em `operation_map`,  
- compõe na ordem fornecida e  
- aplica ao valor `initial_value`.  

Se algum nome não existir no mapeamento, levante `KeyError`.

**Esqueleto de código:**

```python
def compose(*functions):
    ...

def choose_and_apply(program_steps, operation_map, initial_value):
    ...

# Exemplo:
result_value = choose_and_apply(["double", "square", "negate"], operations, 2)
```
