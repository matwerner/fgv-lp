# Aula 2: Variáveis e controle de fluxo

## 1. Funções built-in

Python oferece diversas funções **built-in**, isto é, funções disponíveis diretamente na linguagem, sem que seja necessário importar um módulo ou incluir um cabeçalho para utilizá-las.

Em C, mesmo funções muito comuns da biblioteca padrão, como `printf()` e `scanf()`, dependem da inclusão do cabeçalho `stdio.h`:

```c
#include <stdio.h>
```

Em Python, funções frequentemente utilizadas, como `print()`, `input()` e `type()`, já estão disponíveis:

```python
print("Olá, mundo!")
```

Algumas das funções built-in que utilizaremos são:

| Função    | Descrição                                               | Exemplo                  |
| --------- | ------------------------------------------------------- | ------------------------ |
| `print()` | Exibe valores na tela                                   | `print("Olá")`           |
| `input()` | Lê uma entrada do usuário e a retorna como uma `str`    | `nome = input("Nome: ")` |
| `type()`  | Informa o tipo de um valor                              | `type(10)`               |
| `int()`   | Converte um valor para inteiro                          | `int("42")`              |
| `float()` | Converte um valor para número decimal                   | `float("3.5")`           |
| `str()`   | Converte um valor para texto                            | `str(42)`                |
| `len()`   | Retorna a quantidade de elementos de uma sequência      | `len("Python")`          |
| `range()` | Produz uma sequência de números inteiros                | `range(1, 6)`            |
| `ord()`   | Retorna o código numérico de um caractere               | `ord("A")`               |
| `chr()`   | Retorna o caractere correspondente a um código numérico | `chr(65)`                |

Exemplo:

```python
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print("Olá,", nome)
print("No próximo ano, você terá", idade + 1, "anos.")
```

A função `input()` sempre retorna uma string, mesmo quando o usuário digita um número:

```python
idade = input("Digite sua idade: ")

print(idade)
print(type(idade))
```

Para utilizar a entrada como um número, precisamos convertê-la:

```python
idade = int(input("Digite sua idade: "))
```



## 2. Variáveis e tipos básicos

### 2.1. Valores literais e variáveis

Um **valor literal** é um valor escrito diretamente no programa.

Exemplos:

```python
10
3.14
"Python"
True
```

Uma **variável** é um nome associado a um valor:

```python
idade = 20
altura = 1.75
nome = "Ana"
aprovado = True
```

Na instrução:

```python
idade = 20
```

o valor `20` é associado ao nome `idade`.

O valor associado a uma variável pode ser alterado durante a execução do programa:

```python
idade = 20
idade = 21
```

Diferentemente de C, não precisamos declarar previamente o tipo da variável.

Em C:

```c
int idade = 20;
```

Em Python:

```python
idade = 20
```

Python identifica o tipo a partir do valor atribuído.

Uma mesma variável também pode receber valores de tipos diferentes:

```python
valor = 10
valor = "dez"
```

Apesar de ser permitido, isso deve ser feito com cuidado, pois pode dificultar a leitura e a compreensão do programa.

### 2.2. Tipos básicos

Alguns dos tipos básicos de Python são:

| Tipo    | Descrição        | Exemplos            |
| ------- | ---------------- | ------------------- |
| `int`   | Números inteiros | `10`, `-5`, `0`     |
| `float` | Números decimais | `3.14`, `-0.5`      |
| `str`   | Textos           | `"Python"`, `"Olá"` |
| `bool`  | Valores lógicos  | `True`, `False`     |

Podemos utilizar `type()` para verificar o tipo de um valor:

```python
idade = 20
altura = 1.75
nome = "Ana"
aprovado = True

print(type(idade))
print(type(altura))
print(type(nome))
print(type(aprovado))
```

Saída:

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

Em Python, o tipo está associado ao valor, e não permanentemente ao nome da variável.

### 2.3. Nomes de variáveis

Os nomes das variáveis em Python:

* podem começar com uma letra ou underscore (`_`);
* podem conter letras, números e underscores;
* não podem começar com um número;
* diferenciam letras maiúsculas de minúsculas;
* não podem utilizar palavras reservadas da linguagem.

Exemplos válidos:

```python
idade = 20
nome_completo = "Ana Silva"
_total = 100
aluno2 = "Carlos"
```

Exemplos inválidos:

```python
2aluno = "Carlos"
nome-completo = "Ana Silva"
```

Devemos utilizar nomes que indiquem o significado do valor armazenado.

Evite:

```python
x = 1500
```

Prefira:

```python
salario_mensal = 1500
```

A convenção mais utilizada para nomes de variáveis em Python é `snake_case`:

```python
nome_do_usuario = "Ana"
quantidade_de_itens = 10
```

Outra convenção comum em diferentes linguagens é `camelCase`:

```python
nomeDoUsuario = "Ana"
quantidadeDeItens = 10
```

Em Python, utilizaremos preferencialmente `snake_case`.

### 2.4. Operadores aritméticos

Python oferece os seguintes operadores aritméticos:

| Operador | Descrição        | Exemplo  |
| -------- | ---------------- | -------- |
| `+`      | Adição           | `5 + 3`  |
| `-`      | Subtração        | `5 - 3`  |
| `*`      | Multiplicação    | `5 * 3`  |
| `/`      | Divisão          | `5 / 3`  |
| `//`     | Divisão inteira  | `5 // 3` |
| `%`      | Resto da divisão | `5 % 3`  |
| `**`     | Exponenciação    | `5 ** 3` |

Exemplo:

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

A divisão `/` sempre produz um valor do tipo `float`:

```python
resultado = 10 / 2

print(resultado)
print(type(resultado))
```

Saída:

```text
5.0
<class 'float'>
```

Assim como em C, Python permite combinar uma operação com uma atribuição:

```python
contador = 10

contador += 1
contador -= 2
contador *= 3
contador /= 2
```

Python não possui os operadores `++` e `--`.

Em C:

```c
contador++;
```

Em Python:

```python
contador += 1
```

### 2.5. Ordem de avaliação

Python segue regras de precedência semelhantes às utilizadas na matemática.

Uma ordem simplificada é:

1. parênteses;
2. exponenciação;
3. multiplicação, divisão, divisão inteira e módulo;
4. adição e subtração.

Exemplo:

```python
resultado = 2 + 3 * 4
print(resultado)
```

O resultado será `14`, pois a multiplicação é realizada antes da adição.

Podemos utilizar parênteses para alterar a ordem:

```python
resultado = (2 + 3) * 4
print(resultado)
```

O resultado será `20`.

Considere também:

```python
x = 2
resultado = 3.9 * x * (1 + x)

print(resultado)
```

Primeiro, o lado direito da atribuição é avaliado. Em seguida, o resultado é associado à variável `resultado`.

Quando houver dúvida, utilize parênteses para tornar a intenção do código mais clara.

### 2.6. Conversão de tipos

#### 2.6.1. Conversão implícita

Em algumas situações, Python converte automaticamente um valor para outro tipo.

```python
inteiro = 2
decimal = 3.5

resultado = inteiro + decimal

print(resultado)
print(type(resultado))
```

Saída:

```text
5.5
<class 'float'>
```

O valor inteiro foi convertido para `float` para que a operação pudesse ser realizada.

#### 2.6.2. Conversão explícita

Também podemos solicitar uma conversão explicitamente:

```python
texto = "42"
numero = int(texto)

print(numero)
print(type(numero))
```

Outros exemplos:

```python
numero_inteiro = int("10")
numero_decimal = float("3.5")
texto = str(100)
```

Nem toda conversão é possível:

```python
numero = int("Python")
```

Esse código gera um erro, pois `"Python"` não representa um número inteiro.

#### 2.6.3. Conversão de entradas do usuário

Como `input()` retorna uma string, entradas numéricas normalmente precisam ser convertidas:

```python
primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

soma = primeiro_numero + segundo_numero

print("Resultado:", soma)
```

Sem a conversão:

```python
primeiro_numero = input("Digite o primeiro número: ")
segundo_numero = input("Digite o segundo número: ")

print(primeiro_numero + segundo_numero)
```

Caso o usuário digite `10` e `20`, o resultado será:

```text
1020
```

Isso acontece porque as duas entradas são strings. Nesse caso, o operador `+` realiza a concatenação dos textos.



## 3. Condicionais

As estruturas condicionais permitem executar diferentes blocos de código de acordo com uma condição.

Python utiliza as palavras-chave `if`, `elif` e `else`.

### 3.1. Sintaxe e estrutura

A estrutura básica de uma condicional é:

```python
if condição:
    # executado se a condição for verdadeira
elif outra_condição:
    # executado se a segunda condição for verdadeira
else:
    # executado caso nenhuma condição anterior seja verdadeira
```

Exemplo:

```python
idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Idade inválida")
elif idade < 18:
    print("Menor de idade")
else:
    print("Maior de idade")
```

Somente um desses blocos será executado.

Em Python, a indentação define quais instruções pertencem a cada bloco:

```python
if idade >= 18:
    print("Maior de idade")
    print("Entrada permitida")

print("Fim do programa")
```

As duas primeiras chamadas de `print()` pertencem a blocos diferentes.

### 3.2. Operadores de comparação

Os operadores de comparação produzem valores booleanos, ou seja, `True` ou `False`.

| Operador | Descrição        | Exemplo  |
| -------- | ---------------- | -------- |
| `==`     | Igual a          | `a == b` |
| `!=`     | Diferente de     | `a != b` |
| `<`      | Menor que        | `a < b`  |
| `>`      | Maior que        | `a > b`  |
| `<=`     | Menor ou igual a | `a <= b` |
| `>=`     | Maior ou igual a | `a >= b` |

Exemplo:

```python
idade = 20

print(idade >= 18)
print(idade == 20)
print(idade != 30)
```

Não confunda o operador de atribuição `=` com o operador de comparação `==`:

```python
idade = 20       # atribuição
idade == 20      # comparação
```

Python também permite encadear comparações.

Em C:

```c
x > 5 && x < 15
```

Em Python:

```python
5 < x < 15
```

As duas expressões verificam se `x` está entre `5` e `15`.

### 3.3. Operadores lógicos

Os operadores lógicos permitem combinar ou negar condições.

| Operador | Descrição                                              |
| -------- | ------------------------------------------------------ |
| `and`    | Verdadeiro quando as duas condições são verdadeiras    |
| `or`     | Verdadeiro quando pelo menos uma condição é verdadeira |
| `not`    | Inverte o resultado de uma condição                    |

Em C, os operadores equivalentes são `&&`, `||` e `!`.

#### 3.3.1. Operador `and`

O operador `and` produz `True` apenas quando as duas condições são verdadeiras.

| A       | B       | A `and` B |
| ------- | ------- | --------- |
| `False` | `False` | `False`   |
| `False` | `True`  | `False`   |
| `True`  | `False` | `False`   |
| `True`  | `True`  | `True`    |

Exemplo:

```python
idade = 20
possui_documento = True

if idade >= 18 and possui_documento:
    print("Entrada permitida")
```

#### 3.3.2. Operador `or`

O operador `or` produz `True` quando pelo menos uma das condições é verdadeira.

| A       | B       | A `or` B |
| ------- | ------- | -------- |
| `False` | `False` | `False`  |
| `False` | `True`  | `True`   |
| `True`  | `False` | `True`   |
| `True`  | `True`  | `True`   |

Exemplo:

```python
idade = 70

if idade < 18 or idade >= 60:
    print("Possui direito à meia-entrada")
```

#### 3.3.3. Operador `not`

O operador `not` inverte o resultado de uma condição.

| A       | `not` A |
| ------- | ------- |
| `False` | `True`  |
| `True`  | `False` |

Exemplo:

```python
possui_ingresso = False

if not possui_ingresso:
    print("É necessário comprar um ingresso")
```

### 3.4. Ordem de avaliação

Os operadores lógicos seguem esta ordem de precedência:

1. `not`;
2. `and`;
3. `or`.

Considere:

```python
x = 25

if x > 20 or x > 10 and x < 15:
    print("Opção A")
else:
    print("Opção B")
```

Como `and` é avaliado antes de `or`, a condição é interpretada como:

```python
if x > 20 or (x > 10 and x < 15):
```

A mensagem exibida será:

```text
Opção A
```

Mesmo conhecendo a precedência dos operadores, podemos utilizar parênteses para melhorar a legibilidade:

```python
if x > 20 or (10 < x < 15):
    print("Opção A")
```

### 3.5. Exemplo: classificação de uma nota

O programa abaixo recebe uma nota entre `0` e `100` e exibe sua classificação:

```python
nota = float(input("Digite uma nota entre 0 e 100: "))

if nota < 0 or nota > 100:
    print("Nota inválida")
elif nota >= 80:
    print("A")
elif nota >= 65:
    print("B")
elif nota >= 40:
    print("C")
elif nota >= 30:
    print("D")
else:
    print("F")
```

A ordem das condições é importante. Assim que uma condição verdadeira é encontrada, os demais blocos não são avaliados.

Por exemplo, uma nota igual a `85` também é maior que `65`, mas o programa executa apenas o primeiro bloco cuja condição é verdadeira.



## 4. Laços de repetição

Laços de repetição permitem executar um mesmo bloco de código várias vezes.

Python possui dois laços principais:

* `while`;
* `for`.

### 4.1. Laço `while`

O laço `while` executa um bloco enquanto uma condição for verdadeira.

Sua estrutura básica é:

```python
while condição:
    # bloco de código
```

Exemplo:

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
```

Saída:

```text
1
2
3
4
5
```

É importante que alguma instrução altere a condição do `while`.

O código abaixo gera um loop infinito:

```python
contador = 1

while contador <= 5:
    print(contador)
```

Como o valor de `contador` nunca muda, a condição permanece verdadeira.

Python não possui um laço `until`, mas podemos obter um comportamento semelhante negando a condição do `while`:

```python
while not terminou:
    print("Executando...")
```

### 4.2. Laço `for`

O laço `for` de Python percorre os elementos de uma sequência ou de outro objeto iterável.

Exemplo com uma string:

```python
palavra = "Python"

for letra in palavra:
    print(letra)
```

Saída:

```text
P
y
t
h
o
n
```

Exemplo com uma lista:

```python
cores = ["vermelho", "verde", "azul"]

for cor in cores:
    print(cor)
```

Em C, o `for` normalmente é definido por uma inicialização, uma condição e uma atualização:

```c
for (int i = 1; i <= 5; i++) {
    printf("%d\n", i);
}
```

Em Python, o `for` percorre uma sequência de valores:

```python
for i in range(1, 6):
    print(i)
```

### 4.3. Função `range()`

A função `range()` produz uma sequência de números inteiros.

Ela pode ser utilizada de três formas:

```python
range(fim)
range(inicio, fim)
range(inicio, fim, passo)
```

O valor final não é incluído na sequência.

#### 4.3.1. `range(fim)`

```python
for i in range(5):
    print(i)
```

Saída:

```text
0
1
2
3
4
```

#### 4.3.2. `range(inicio, fim)`

```python
for i in range(1, 6):
    print(i)
```

Saída:

```text
1
2
3
4
5
```

#### 4.3.3. `range(inicio, fim, passo)`

```python
for i in range(0, 11, 2):
    print(i)
```

Saída:

```text
0
2
4
6
8
10
```

Também podemos utilizar um passo negativo:

```python
for i in range(5, 0, -1):
    print(i)

print("Fim!")
```

Saída:

```text
5
4
3
2
1
Fim!
```

### 4.4. Interrompendo o fluxo

Dentro de um laço, podemos utilizar `break` e `continue` para alterar o fluxo normal de execução.

#### 4.4.1. `break`

A instrução `break` encerra imediatamente o laço.

```python
for numero in range(1, 6):
    if numero == 3:
        break

    print(numero)

print("Fim!")
```

Saída:

```text
1
2
Fim!
```

O laço é encerrado quando `numero` recebe o valor `3`.

Também podemos utilizar `break` para controlar um laço que inicialmente não possui uma condição de término:

```python
while True:
    comando = input("Digite 'q' para sair: ")

    if comando == "q":
        break

    print("Você digitou:", comando)

print("Programa encerrado.")
```

#### 4.4.2. `continue`

A instrução `continue` ignora o restante da iteração atual e inicia a próxima iteração.

```python
for numero in range(1, 6):
    if numero % 2 == 0:
        continue

    print(numero)
```

Saída:

```text
1
3
5
```

Quando o número é par, o `continue` impede a execução do `print()` naquela iteração.



## 5. Exercícios

### 5.1. Menu de comandos

Escreva um programa que leia repetidamente comandos digitados pelo usuário.

#### Regras

* Ao receber `"a"`, exiba `"Hello"`;
* ao receber `"b"`, exiba `"world!"`;
* ao receber `"q"`, encerre o programa;
* para qualquer outra entrada, exiba `"Entrada inválida"`.

O programa deve continuar solicitando comandos até que o usuário digite `"q"`.

#### Entrada

Uma sequência de comandos digitados pelo usuário.

#### Saída

A mensagem correspondente a cada comando.

#### Exemplo

```text
Digite uma opção: a
Hello

Digite uma opção: x
Entrada inválida

Digite uma opção: b
world!

Digite uma opção: q
Programa encerrado
```

### 5.2. Cifra de César

A Cifra de César é uma técnica de criptografia que substitui cada letra de uma mensagem por outra letra localizada algumas posições à frente no alfabeto.

Por exemplo, para um deslocamento igual a `3`:

```text
a → d
b → e
c → f
x → a
y → b
z → c
```

Escreva um programa que criptografe uma mensagem utilizando a Cifra de César.

#### Regras

* a mensagem conterá apenas letras minúsculas sem acentos, espaços e sinais de pontuação;
* cada letra deve ser deslocada pela quantidade informada pelo usuário;
* depois da letra `z`, o deslocamento deve continuar a partir da letra `a`;
* espaços e sinais de pontuação devem permanecer inalterados;
* o deslocamento será um número inteiro.

#### Entrada

O programa deve receber:

1. uma mensagem;
2. um valor inteiro de deslocamento.

#### Saída

A mensagem criptografada.

#### Exemplo 1

```text
Digite a mensagem: atacar ao amanhecer
Digite o deslocamento: 3
Mensagem criptografada: dwdfdu dr dpdqkhfhu
```

#### Exemplo 2

```text
Digite a mensagem: zebra!
Digite o deslocamento: 2
Mensagem criptografada: bgdtc!
```

#### Desafios adicionais

* preservar letras maiúsculas;
* permitir deslocamentos negativos;
* implementar a descriptografia;
* permitir que o usuário processe várias mensagens.

### 5.3. Termo simplificado

Implemente uma versão simplificada do jogo Termo.

O programa deve possuir uma palavra secreta de cinco letras. O jogador terá no máximo seis tentativas para descobri-la.

#### Regras

Em cada tentativa, o jogador deve informar uma palavra de cinco letras.

Para cada letra da tentativa, o programa deve exibir:

* `🟩` quando a letra estiver na palavra secreta e na posição correta;
* `🟨` quando a letra estiver na palavra secreta, mas em outra posição;
* `⬛` quando a letra não estiver na palavra secreta.

O jogo deve terminar quando:

* o jogador descobrir a palavra secreta; ou
* o jogador utilizar as seis tentativas.

Para esta primeira versão:

* a palavra secreta e as tentativas devem conter exatamente cinco letras;
* devem ser utilizadas apenas letras minúsculas sem acentos;
* não é necessário verificar se a tentativa corresponde a uma palavra existente;
* uma tentativa com quantidade incorreta de letras não deve ser avaliada;
* letras repetidas podem seguir a regra simplificada: uma letra será amarela sempre que existir em alguma posição da palavra secreta.

#### Entrada

Até seis palavras de cinco letras, informadas uma por vez pelo jogador.

#### Saída

Após cada tentativa válida, o programa deve exibir uma sequência de cinco símbolos indicando o resultado da comparação.

Caso o jogador acerte, deve ser exibida uma mensagem de vitória.

Caso as seis tentativas sejam utilizadas, deve ser exibida uma mensagem de derrota e a palavra secreta.

#### Exemplo de execução

Considere a palavra secreta:

```text
casal
```

Uma possível execução seria:

```text
Tentativa 1 de 6: canto
🟩🟩🟨⬛⬛

Tentativa 2 de 6: cabra
🟩🟩⬛⬛🟨

Tentativa 3 de 6: casal
🟩🟩🟩🟩🟩

Parabéns! Você descobriu a palavra.
```

#### Exemplo de entrada inválida

```text
Tentativa 1 de 6: casa
A palavra deve possuir exatamente cinco letras.

Tentativa 1 de 6: casal
🟩🟩🟩🟩🟩
```

A tentativa inválida não deve consumir uma das seis tentativas disponíveis.

#### Exemplo de derrota

```text
Você não descobriu a palavra.
A palavra secreta era: casal
```

#### Desafios adicionais

* tratar corretamente a quantidade de ocorrências de letras repetidas;
* aceitar letras maiúsculas;
* escolher a palavra secreta entre várias opções;
* informar quais letras já foram utilizadas;
* permitir que dois jogadores definam e descubram palavras alternadamente.

### 5.4. Verificador de força de senha

Escreva um programa que receba uma senha e avalie sua força de acordo com um conjunto de critérios.

> Este exercício representa uma avaliação simplificada. Sistemas reais de segurança utilizam critérios mais complexos para analisar senhas.

#### Critérios

A senha recebe um ponto para cada critério atendido:
1. possuir pelo menos oito caracteres;
2. possuir pelo menos uma letra minúscula;
3. possuir pelo menos uma letra maiúscula;
4. possuir pelo menos um número;
5. possuir pelo menos um caractere especial, como `!`, `@`, `#`, `$`, `%` ou `&`.

#### Classificação

A senha deve ser classificada de acordo com sua pontuação:
* de 0 a 2 pontos: `Senha fraca`;
* 3 ou 4 pontos: `Senha média`;
* 5 pontos: `Senha forte`.

#### Entrada

Uma senha digitada pelo usuário.

#### Saída

A classificação da senha e a quantidade de critérios atendidos.

#### Exemplo 1

```text
Digite uma senha: casa
Critérios atendidos: 1 de 5
Senha fraca
```

#### Exemplo 2

```text
Digite uma senha: Python123
Critérios atendidos: 4 de 5
Senha média
```

#### Exemplo 3

```text
Digite uma senha: Python@123
Critérios atendidos: 5 de 5
Senha forte
```

#### Observações

* a senha pode conter letras, números, espaços e símbolos;
* a verificação deve percorrer os caracteres da senha;
* um mesmo critério deve acrescentar no máximo um ponto, mesmo que apareça várias vezes;
* o programa não deve modificar a senha digitada.

Para verificar os diferentes tipos de caracteres, podem ser utilizados os seguintes métodos de strings:

| Método                | Descrição                                     |
| --------------------- | --------------------------------------------- |
| `caractere.islower()` | Verifica se o caractere é uma letra minúscula |
| `caractere.isupper()` | Verifica se o caractere é uma letra maiúscula |
| `caractere.isdigit()` | Verifica se o caractere é um dígito           |

#### Desafios adicionais

* informar quais critérios não foram atendidos;
* rejeitar senhas que contenham espaços;
* impedir que a senha contenha o nome do usuário;
* considerar senhas com doze ou mais caracteres como mais seguras;
* rejeitar sequências muito comuns, como `"123456"`, `"abcdef"` ou `"qwerty"`.
