# Closure & Decorador

Na aula passada vimos que funções em Python são objetos de primeira classe:
podem ser atribuídas a variáveis, passadas como parâmetro e até retornadas.

Hoje vamos ver duas extensões desse conceito:
* Closure → funções que lembram o contexto em que foram criadas.
* Decorador → funções que envolvem outras funções para modificar ou adicionar comportamento.

Mas antes de entrar nesses conceitos, precisamos relembrar escopo de variáveis.

## 1. Escopo

Em Python, temos três tipos principais de escopo:
* **Local** → variável criada dentro de uma função.
* **Global** → variável criada fora de todas as funções.
* **Enclosing** → variáveis da função “pai” (quando temos funções dentro de funções).

Além disso, temos as palavras-chave:
* `global` → para modificar variáveis globais.
* `nonlocal` → para modificar variáveis do escopo enclosing.

### 1.1 Exemplo: Local e Global

```python
x = 10        # Variável global
y = 'a'       # Variável global

def exibir():
    x = 20    # Variável local com mesmo nome da global
    print(x)  # Saída: 20

    global y  # Usamos a variável global 'y'
    y = 'b'
    print(y)  # Saída: 'b'

exibir()
print(x)  # Saída: 10 (global não foi alterado)
print(y)  # Saída: 'b' (foi alterado pois usamos 'global')
```

### 1.2 Exemplo: Escopo Enclosing

```python
num = 100
def func_externa():
    num = 0
    def func_interna():
        num = num + 1   # ERRO!
    func_interna()
    print(num)

func_externa()
```

* Aqui temos uma variável `num` dentro de `func_externa`.
* A função `func_interna` tenta usá-la, mas dá erro.
* Por quê? → O Python entende que `num` dentro de `func_interna` é local, mas nunca foi inicializado.

## 2. Closure

```python
num = 100                         # Variável global
def func_externa():
    num = 0                       # Variável local (no contexto da func_externa)
    def func_interna():
        nonlocal num              # Usamos a variável do contexto da func_externa
        num = num + 1
        print(f"Teste: {num}")
    func_interna()
    func_interna()
    print(num)
    return func_interna

func_retornada = func_externa()
print(num)                        # Continua sendo 100 (a variável global)
func_retornada()                  # Continua lembrando do 'num' da func_externa
```

### 2.1 O que é uma closure?

Uma closure acontece quando:
1. Temos uma função definida dentro de outra (função aninhada).
2. A função interna usa variáveis da função externa (do escopo enclosing).
3. Essa função interna é retornada ou passada adiante.
4. Mesmo depois que a função externa já terminou de rodar, a função interna continua lembrando das variáveis que estavam disponíveis no momento da sua criação.

> Em resumo: closure é uma função que carrega consigo o ambiente (variáveis) onde foi criada.

### 2.2 Dito isso, o que esta acontecendo acima?

Vamos acompanhar linha por linha:

1. Existe uma variável global `num = 100`.  
2. Quando chamamos `func_externa()`:  
    - É criada uma nova variável local `num = 0`.  
    - A função `func_interna` é definida dentro de `func_externa`.  
3. Dentro de `func_interna`, usamos `nonlocal num`:  
    - Isso indica ao Python que queremos usar o `num` da função **enclosing** (`func_externa`), e **não criar um novo local**.  
    - Assim conseguimos alterar `num`.  
4. Chamando `func_interna()` duas vezes, `num` é incrementado:  
    - 1ª vez → `num = 1`  
    - 2ª vez → `num = 2`  
5. `func_externa` imprime `num = 2` e retorna a função `func_interna`.  
6. Guardamos essa função retornada em `func_retornada`.  
7. Mesmo depois de `func_externa` terminar, `func_retornada` ainda sabe qual era o valor de `num` e continua incrementando a partir dali.  
8. A variável global `num` nunca é afetada, porque sempre trabalhamos no escopo da função externa.  

### 2.2 Por que isso é útil?

Closures permitem **guardar estado local** de uma função sem precisar de **classes** ou **variáveis globais**,
mantendo o código mais **limpo, seguro e modular**.

Algumas aplicações práticas:
* Contadores de chamadas
    - Cada closure pode manter quantas vezes foi chamada, sem interferir em outras funções.
    - **Exemplo real**: sistemas que precisam controlar limites de uso, como a OpenAI monitorando o número de chamadas ao ChatGPT.
* Caches e memoization
    - Funções que fazem cálculos pesados ou chamadas custosas podem guardar resultados anteriores.
    - Isso evita recomputação desnecessária e melhora a performance.
    - **Exemplo real**: Bibliotecas de matemática (ex.: funções recursivas de Fibonacci ou cálculos complexos) usam closures para guardar resultados já computados, evitando recomputação.

### 2.3 Exemplos

#### Contador simples

```python
def contador():
    num = 0
    def incrementar():
        nonlocal num
        num += 1
        return num
    return incrementar

c = contador()
print(c())  # 1
print(c())  # 2
print(c())  # 3
```

#### Funções configuráveis

```python
def multiplicador(fator):
    def func(x):
        return x * fator
    return func

dobro = multiplicador(2)
triplo = multiplicador(3)

print(dobro(5))   # 10
print(triplo(5))  # 15
```

## 3. Decoradores

Continuando a ideia de closure, um **decorador** é uma função que recebe outra função como parâmetro e retorna uma nova função com comportamento adicional, sem modificar o código original.
Ou seja, é uma forma elegante de “envolver” funções para adicionar funcionalidades.

Closures são tão úteis que existe uma forma mais elegante de usá-las: os decoradores.

Um decorador é simplesmente uma função que:
1. Recebe outra função como argumento;
2. Retorna uma nova função (normalmente um wrapper).

### 3.1 O que é um decorador?

Um decorador permite:
* Receber uma função `f` como entrada.
* Criar uma função interna que adiciona comportamento extra.
* Retornar essa função interna, que substitui ou complementa a original.

> Em outras palavras: decoradores são closures que adicionam funcionalidades a funções existentes.

### 3.2 Passo a passo conceitual

1. Definimos uma função que receberá outra função como argumento (`func`).
2. Dentro dela, definimos uma função interna (`wrapper`) que:
3. Executa ações antes ou depois de chamar `func`.
    * Pode alterar argumentos, resultados ou controlar quando `func` é executada.
    * A função externa retorna a função interna.
4. A função interna fecha sobre o contexto da função original (closure), permitindo acessar variáveis do escopo externo.

### 3.3 Ilustrando...

```python
def meu_decorador(func):
    def wrapper():
        print("Antes da execução")
        func()
        print("Depois da execução")
    return wrapper

def diga_ola():
    print("Olá!")

diga_ola = meu_decorador(diga_ola)
diga_ola()
# Saída esperada:
# Antes da execução
# Olá!
# Depois da execução
```

* `wrapper` é uma closure: lembra de `func` mesmo após `meu_decorador` terminar.
* Decorador adiciona comportamento sem alterar `diga_ola`.

### 3.4 Sintaxe “Pythonica” com @

Python permite aplicar decoradores de forma direta:

```python
@meu_decorador
def diga_ola():
    print("Olá!")

diga_ola()
```

* O `@meu_decorador` é equivalente a `diga_ola = meu_decorador(diga_ola)`.
* Torna o código mais limpo e legível.

### 3.5 Por que decoradores são úteis?

* **Adicionar funcionalidades** (logging, autenticação, validação, monitoramento) sem alterar código existente.
* **Reutilização e modularidade**: o mesmo decorador pode ser aplicado a várias funções.
* **Privacidade e encapsulamento**: a função original permanece inalterada, estado e contexto são gerenciados internamente.
* **Frameworks e bibliotecas**: muito usados em Flask, Django, FastAPI, testes unitários e sistemas de caching.

### 3.6 Exemplo: Medição de tempo

#### Algoritmo

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()                              # Marca o tempo antes da execução
        resultado = func(*args, **kwargs)                 # Chama a função original com todos os argumentos
        fim = time.time()                                 # Marca o tempo após a execução
        print(f"Tempo de execução: {fim - inicio:.4f}s")  # Exibe o tempo gasto
        return resultado                                  # Retorna o resultado da função original
    return wrapper

@timer
def soma_grande():
    return sum(range(10**6))

soma_grande()
```

#### O que esta acontecendo?

1. **Decorador `timer`**  
   - Recebe uma função `func` como argumento.  
   - Define uma função interna `wrapper` que adiciona comportamento: medir o tempo de execução.  
   - Retorna `wrapper`, que substituirá a função original.

2. **`*args` e `**kwargs`**  
   - `*args` → captura **todos os argumentos posicionais** passados para a função.  
   - `**kwargs` → captura **todos os argumentos nomeados** (keywords) passados para a função.  
   - Dessa forma, o decorador funciona para qualquer função, **independentemente da assinatura**.

3. **Dentro do `wrapper`**  
   - `inicio = time.time()` → registra o tempo antes da execução.  
   - `resultado = func(*args, **kwargs)` → chama a função original com todos os argumentos recebidos.  
   - `fim = time.time()` → registra o tempo após a execução.  
   - `print(f"Tempo de execução: {fim - inicio:.4f}s")` → exibe o tempo gasto.  
   - `return resultado` → devolve o resultado da função original, garantindo que o comportamento principal não seja alterado.

4. **Uso do `@timer`**  
   - Aplicando `@timer` antes da definição de `soma_grande`, Python faz:  
     ```
     soma_grande = timer(soma_grande)
     ```  
   - Ou seja, a função `soma_grande` agora **é a função `wrapper`** que mede o tempo e depois chama a original.

5. **Execução**  
   - Ao chamar `soma_grande()`, o decorador mede o tempo da soma de `range(10**6)` e imprime o resultado.


## 4. Exercícios

### 4.1 Closure: Média acumulada
Crie uma função `media_acumulada()` que retorna uma função interna capaz de:
- Adicionar cada número recebido a uma lista interna.
- Retornar a **média atualizada** a cada chamada.
- A função interna deve manter **todo o histórico de números recebidos** usando closure.

### 4.2 Decorador: Números não-negativos
Crie um decorador `@nao_negativo` que impede a execução de uma função caso algum dos argumentos numéricos seja negativo.  
- Se todos os argumentos forem `≥ 0`, a função deve rodar normalmente.  
- Caso contrário, a função não deve ser executada e deve exibir um aviso na tela indicando que existem valores negativos.
