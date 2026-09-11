# Aula 17: Closures

## 1. Funções Dentro de Funções

Até agora, já utilizamos variáveis definidas tanto dentro quanto fora de funções.

Dependendo de onde uma variável é definida, ela pertence a um escopo diferente.

```python
a = 0  # Global


def func():
    b = 1  # Local

    print(a)  # 0
    print(b)  # 1


func()

print(a)  # 0
print(b)  # NameError
```

A variável `a` foi definida fora da função e pertence ao escopo global.

Já `b` foi definida dentro de `func` e pertence ao seu escopo local. Por isso, não podemos acessá-la fora da função.

Na aula passada vimos que **funções também são objetos**.

Isso nos leva a uma pergunta:

> Podemos definir uma função dentro de outra função?

Sim.

```python
def externa():
    def interna():
        print("Função interna")
    interna()

externa()
```

Nesse caso, `interna` foi definida dentro do escopo de `externa`.

Por isso:

```python
interna()  # NameError
```

não funciona fora da função `externa`.

Uma função interna também pode utilizar variáveis definidas na função externa:

```python
def externa():
    mensagem = "Olá!"

    def interna():
        print(mensagem)

    interna()

externa()
```

A variável `mensagem` não é local de `interna`, mas está disponível no escopo da função que a contém.



## 2. Escopo Enclosing

Quando temos funções aninhadas, surge um novo nível de escopo: o **enclosing**.

Considere:

```python
mensagem = "Global"

def externa():
    mensagem = "Enclosing"

    def interna():
        mensagem = "Local"
        print(mensagem)

    interna()

externa()
```

Nesse exemplo, existem três variáveis diferentes chamadas `mensagem`:

* **local**: definida dentro de `interna`;
* **enclosing**: definida na função que contém `interna`;
* **global**: definida fora das funções.

Quando uma variável não existe no escopo local, Python procura nos escopos externos.

```python
mensagem = "Global"

def externa():
    mensagem = "Enclosing"

    def interna():
        print(mensagem)

    interna()

externa()
```

Saída:

```text
Enclosing
```

Como `mensagem` não existe no escopo local de `interna`, Python encontra a variável no escopo **enclosing**.

De forma simplificada, a procura por nomes segue:

```text
Local
  ↓
Enclosing
  ↓
Global
```



## 3. Retornando Funções

Como funções são objetos, uma função também pode retornar outra função.

```python
def criar_boasvindas():
    def boasvindas(nome):
        return f"Olá, {nome}!"

    return boasvindas
```

Ao executar:

```python
funcao = criar_boasvindas()
```

`criar_boasvindas()` é executada e retorna a função `boasvindas`.

Depois:

```python
print(funcao("Ana"))
```

Saída:

```text
Olá, Ana!
```

Observe que:

```python
return boasvindas
```

retorna a própria função.

Não estamos fazendo:

```python
return boasvindas(...)
```

Nesse caso, estamos **criando uma função durante a execução do programa e retornando esse objeto**.

Isso permite criar funções de maneira dinâmica.



## 4. Criando Funções Customizaveis

Considere:

```python
def criar_multiplicador(fator):
    def multiplicar(valor):
        return valor * fator

    return multiplicar
```

Agora podemos criar diferentes funções:

```python
dobro = criar_multiplicador(2)
triplo = criar_multiplicador(3)

print(dobro(10))   # 20
print(triplo(10))  # 30
```

As funções `dobro` e `triplo` foram criadas a partir do mesmo código:

```python
def multiplicar(valor):
    return valor * fator
```

O que muda é o contexto em que cada uma foi criada.

Para `dobro`:

```text
fator = 2
```

Para `triplo`:

```text
fator = 3
```

Isso nos leva a uma questão importante.

Quando executamos:

```python
dobro = criar_multiplicador(2)
```

acontece:

1. `criar_multiplicador` é executada;
2. `fator` recebe `2`;
3. a função `multiplicar` é criada;
4. `multiplicar` é retornada;
5. `criar_multiplicador` termina.

Mesmo assim:

```python
dobro(10)
```

continua conseguindo utilizar:

```python
fator
```

Como isso é possível?



## 5. Closures

Uma **closure** ocorre quando uma função interna mantém acesso a variáveis do contexto em que foi criada, mesmo depois que a função externa terminou.

No exemplo:

```python
def criar_multiplicador(fator):
    def multiplicar(valor):
        return valor * fator

    return multiplicar
```

a função `multiplicar` utiliza `fator`, que pertence ao escopo de `criar_multiplicador`.

Quando `multiplicar` é retornada, ela continua tendo acesso a esse contexto.

Podemos representar:

```text
criar_multiplicador(2)
        │
        ├── fator = 2
        │
        └── cria multiplicar
                  │
                  ▼
                dobro
```

Assim:

```python
dobro(10)
```

utiliza:

```text
valor = 10
fator = 2
```

mesmo que a execução de `criar_multiplicador(2)` já tenha terminado.

### 5.1. Como Esse Contexto Continua Existindo?

Normalmente, quando uma função termina, suas variáveis locais deixam de ser necessárias.

Entretanto, nesse caso, existe uma função que ainda depende de algumas dessas informações.

Por exemplo:

```python
dobro = criar_multiplicador(2)
```

A função retornada ainda depende de `fator`.

Python mantém uma referência ao contexto necessário para que essa função continue funcionando.

De forma simplificada:

```text
dobro
  │
  └── função multiplicar
          │
          └── fator → 2
```

Enquanto a closure existir, o contexto necessário para sua execução também permanece disponível.

A closure não precisa manter todas as variáveis da função externa.

Ela mantém acesso às variáveis externas das quais depende.



## 6. Exemplo: Criando Filtros Configuráveis

Suponha que temos produtos representados por dicionários:

```python
produtos = [
    {"nome": "Mouse", "preco": 120, "avaliacao": 4.7},
    {"nome": "Teclado", "preco": 250, "avaliacao": 4.5},
    {"nome": "Monitor", "preco": 900, "avaliacao": 4.8},
]
```

Podemos criar uma função capaz de gerar diferentes filtros:

```python
def criar_filtro(campo, minimo, maximo):
    def filtrar(item):
        valor = item[campo]

        return minimo <= valor <= maximo

    return filtrar
```

Agora:

```python
filtrar_preco = criar_filtro("preco", 100, 300)
filtrar_avaliacao = criar_filtro("avaliacao", 4.6, 5.0)
```

Podemos utilizar:

```python
for produto in produtos:
    if filtrar_preco(produto):
        print(produto["nome"])
```

`filtrar_preco` mantém o contexto:

```text
campo = "preco"
minimo = 100
maximo = 300
```

Já `filtrar_avaliacao` mantém:

```text
campo = "avaliacao"
minimo = 4.6
maximo = 5.0
```

Closures permitem, portanto, criar **funções configuradas dinamicamente**.

Esse mesmo padrão poderia ser utilizado para criar:

* validadores;
* conversores;
* regras de desconto;
* funções de transformação;
* critérios de seleção;
* callbacks que precisam manter algum contexto.



## 7. Alterando o Estado de uma Closure

Até agora, apenas consultamos valores do escopo externo.

Mas uma closure também pode manter um estado que muda entre execuções.

Considere:

```python
def contar_chamadas(func):
    chamadas = 0

    def executar():
        chamadas = chamadas + 1

        return func()

    return executar
```

Esse código produz um erro.

A atribuição:

```python
chamadas = chamadas + 1
```

faz Python considerar `chamadas` uma variável local de `executar`.

Entretanto, o que queremos é modificar a variável existente no escopo **enclosing**.

Para isso utilizamos:

```python
nonlocal
```

Assim:

```python
def contar_chamadas(func):
    chamadas = 0

    def executar():
        nonlocal chamadas

        chamadas += 1

        resultado = func()

        print(f"Número de chamadas: {chamadas}")

        return resultado

    return executar
```

Podemos utilizar:

```python
def processar():
    print("Processando...")


processar = contar_chamadas(processar)
```

Agora:

```python
processar()
processar()
processar()
```

Saída:

```text
Processando...
Número de chamadas: 1

Processando...
Número de chamadas: 2

Processando...
Número de chamadas: 3
```

A função `executar` mantém acesso a:

```text
func
→ função original

chamadas
→ estado mantido entre diferentes execuções
```

Nesse caso, a closure não apenas mantém uma configuração, mas também mantém **estado entre chamadas**.



## 8. Relação com Decoradores

Observe novamente:

```python
processar = contar_chamadas(processar)
```

`contar_chamadas` recebe uma função e devolve outra função que adiciona um comportamento:

```text
função original
      ↓
contar_chamadas
      ↓
nova função
      ↓
função original + contagem
```

Esse tipo de mecanismo é muito comum em Python e está relacionado aos **decoradores**.

Decoradores são utilizados para adicionar comportamentos a funções já existentes.

Normalmente, eles aparecem com a sintaxe:

```python
@decorador
def funcao():
    ...
```

Por exemplo, poderíamos escrever nosso contador como:

```python
@contar_chamadas
def processar():
    print("Processando...")
```

De maneira simplificada:

```python
@contar_chamadas
```

representa a aplicação:

```python
processar = contar_chamadas(processar)
```

Decoradores são muito utilizados para adicionar comportamentos como:

* coletar estatísticas;
* medir tempo de execução;
* registrar informações;
* realizar cache;
* controlar acesso;
* validar chamadas.

Por enquanto, basta conhecer a ideia geral.



## 9. Exercício

Considere a lista:

```python
pessoas = [
    {"nome": "Ana Silva", "email": "ana@gmail.com"},
    {"nome": "Bruno Souza", "email": "bruno@fgv.br"},
    {"nome": "Mariana Costa", "email": "mariana@gmail.com"},
    {"nome": "Carlos Lima", "email": "carlos@empresa.com"},
]
```

Implemente uma função:

```python
def criar_contem(campo, texto):
    ...
```

A função deve retornar outra função capaz de verificar se o valor de `campo` contém o texto informado.

A busca deve ignorar diferenças entre letras maiúsculas e minúsculas.

Por exemplo:

```python
contem_nome_ana = criar_contem("nome", "ana")
contem_email_gmail = criar_contem("email", "gmail")
```

Depois, utilize `criar_contem` para implementar uma busca que procure o texto informado tanto no **nome** quanto no **e-mail**.

Por exemplo:

```python
query = "ana"

contem_nome = criar_contem("nome", query)
contem_email = criar_contem("email", query)

for pessoa in pessoas:
    if contem_nome(pessoa) or contem_email(pessoa):
        print(pessoa["nome"])
```

Experimente realizar diferentes buscas, como:

```text
ana
gmail
fgv
carlos
```

Responda também:

1. O que está armazenado em `contem_nome_ana`?
2. Quais variáveis do escopo externo são utilizadas pela função retornada?
3. Por que `campo` e `texto` continuam disponíveis depois que `criar_contem` termina?
4. `contem_nome_ana` e `contem_email_gmail` compartilham o mesmo contexto?
