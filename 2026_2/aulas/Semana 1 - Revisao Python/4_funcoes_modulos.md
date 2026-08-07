# Aula 3: Funções e Módulos

## 1. Motivação: Wordle

Considere uma versão simplificada do jogo **Wordle**.

O objetivo do jogo é descobrir uma palavra secreta. A cada tentativa, recebemos algumas dicas:

* 🟩 A letra está na posição correta;
* 🟨 A letra existe na palavra, mas está na posição errada;
* ⬛ A letra não aparece na palavra.

Por exemplo, considere:

```python
palavra_secreta = "termo"
palpite = "tempo"
```

Teríamos como resultado:

```text
🟩🟩🟩⬛🟩
```

> **Observação:** utilizaremos uma versão simplificada das regras do Wordle. Não trataremos de maneira especial palavras que possuem letras repetidas.

### 1.1 Implementação inicial

Utilizando apenas os recursos que vimos até agora, podemos implementar o jogo da seguinte forma:

```python
palavra_secreta = "termo"
tentativas = 6

for tentativa in range(tentativas):
    palpite = input("Digite uma palavra: ").lower()

    if len(palpite) != len(palavra_secreta):
        print("A palavra deve ter", len(palavra_secreta), "letras.")
        continue

    resultado = ""

    for i in range(len(palpite)):
        if palpite[i] == palavra_secreta[i]:
            resultado += "🟩"
        elif palpite[i] in palavra_secreta:
            resultado += "🟨"
        else:
            resultado += "⬛"

    print(resultado)

    if palpite == palavra_secreta:
        print("Você acertou!")
        break

else:
    print("Fim de jogo!")
```

O programa funciona.

Mas será que ele está bem estruturado?

Podemos começar fazendo algumas perguntas:

* Qual parte do código é responsável por comparar o palpite com a palavra secreta?
* Como poderíamos testar apenas essa comparação?
* E se precisássemos fazer essa mesma comparação em outra parte do programa?
* Como separar a lógica do jogo da leitura e exibição de informações?
* Como esse programa ficaria se adicionássemos novas funcionalidades?

Até agora escrevemos todo o comportamento diretamente no programa principal.

Uma maneira de começar a separar essas diferentes responsabilidades é utilizando **funções**.


## 2. Funções

Funções permitem definir blocos de código responsáveis por realizar tarefas específicas.

Elas ajudam principalmente na:

* **Organização**: separar um programa em partes menores e mais fáceis de compreender;
* **Reutilização**: utilizar uma mesma operação em diferentes partes do programa;
* **Separação de responsabilidades**: cada função pode ficar responsável por uma tarefa;
* **Manutenção**: alterações podem ser feitas de maneira mais localizada;
* **Testabilidade**: partes do programa podem ser verificadas isoladamente.

### 2.1 Definindo e chamando funções

Em Python, uma função é definida utilizando a palavra-chave `def`.

```python
def saudacao(nome):
    print("Olá,", nome)
```

Para executar a função, fazemos uma **chamada**:

```python
saudacao("Maria")
```

Nesse exemplo:

```python
def saudacao(nome):
```

`nome` é um **parâmetro**.

Já na chamada:

```python
saudacao("Maria")
```

`"Maria"` é um **argumento**.

De maneira geral:

* **Parâmetros** são os nomes utilizados na definição da função;
* **Argumentos** são os valores fornecidos quando chamamos a função.


### 2.2 Argumentos

Python oferece diferentes maneiras de fornecer argumentos para uma função.

#### Argumentos posicionais

A forma mais simples é associar argumentos aos parâmetros de acordo com sua posição.

```python
def exibir_divisao(num, den):
    print("Divisão:", num / den)


exibir_divisao(4, 2)
```

Nesse caso:

```text
num = 4
den = 2
```

A ordem importa.

Por exemplo:

```python
exibir_divisao(2, 4)
```

produz um resultado diferente.


#### Argumentos por palavra-chave

Também podemos indicar explicitamente qual parâmetro receberá cada argumento:

```python
def exibir_divisao(num, den):
    print("Divisão:", num / den)


exibir_divisao(num=4, den=2)
```

Nesse caso, a ordem deixa de ser importante:

```python
exibir_divisao(den=2, num=4)
```

Os dois exemplos produzem o mesmo resultado.


#### Valores padrão

Parâmetros podem possuir valores padrão.

```python
def exibir_divisao(num, den=1):
    print("Divisão:", num / den)
```

Agora podemos chamar:

```python
exibir_divisao(4)
```

Nesse caso:

```text
den = 1
```

Também podemos fornecer explicitamente outro valor:

```python
exibir_divisao(4, 2)
```

Outro exemplo:

```python
def cumprimentar(nome="Usuário"):
    print("Olá,", nome)


cumprimentar()
cumprimentar("Maria")
```

Valores padrão permitem criar parâmetros opcionais.


#### Argumentos variáveis: `*args`

Considere algumas chamadas da função `print`:

```python
print("Olá")

print("Nome:", "Maria")

print("Nome:", "Maria", "Idade:", 20)
```

Como `print` consegue receber diferentes quantidades de argumentos?

Python permite definir funções que recebem uma quantidade arbitrária de argumentos posicionais utilizando `*`.

Por exemplo:

```python
def somar(*numeros):
    total = 0

    for numero in numeros:
        total += numero

    return total
```

Agora podemos fazer:

```python
print(somar(1, 2))

print(somar(1, 2, 3))

print(somar(1, 2, 3, 4, 5))
```

Dentro da função, `numeros` será uma **tupla** contendo os argumentos recebidos.

Por exemplo:

```python
def exibir_argumentos(*args):
    print(args)


exibir_argumentos(10, 20, 30)
```

Resultado:

```text
(10, 20, 30)
```

`args` não é uma palavra reservada. É apenas uma convenção amplamente utilizada.

Poderíamos escrever:

```python
def exibir_argumentos(*valores):
    print(valores)
```


#### Argumentos variáveis: `**kwargs`

Também podemos receber uma quantidade arbitrária de argumentos por palavra-chave.

```python
def criar_perfil(nome, **dados):
    print("Nome:", nome)
    print(dados)
```

Por exemplo:

```python
criar_perfil(
    "Maria",
    idade=20,
    cidade="Rio de Janeiro",
    curso="Economia"
)
```

Dentro da função, `dados` será um **dicionário**:

```python
{
    "idade": 20,
    "cidade": "Rio de Janeiro",
    "curso": "Economia"
}
```

Nesse caso:

* `*args` agrupa argumentos posicionais em uma tupla;
* `**kwargs` agrupa argumentos por palavra-chave em um dicionário.

Assim como `args`, `kwargs` é apenas uma convenção.


### 2.3 Retorno

Até agora, nossas funções simplesmente imprimiram seus resultados:

```python
def soma(a, b):
    print(a + b)
```

Por exemplo:

```python
soma(3, 5)
```

produz:

```text
8
```

Mas muitas vezes queremos que uma função **produza um valor que poderá ser utilizado por outras partes do programa**.

Para isso utilizamos `return`.

```python
def soma(a, b):
    resultado = a + b
    return resultado
```

Agora podemos fazer:

```python
resultado = soma(3, 5)

print(resultado)
```

Também podemos utilizar diretamente o retorno da função:

```python
print(soma(3, 5))
```

Ou utilizar o resultado em outras operações:

```python
resultado = soma(1, 2) * 10

print(resultado)
```

Também podemos combinar funções:

```python
resultado = soma(soma(1, 2), 3)

print(resultado)
```


#### Retornando múltiplos valores

Python permite escrever:

```python
def divide_e_resto(dividendo, divisor):
    quociente = dividendo // divisor
    resto = dividendo % divisor

    return quociente, resto
```

Podemos então fazer:

```python
quociente, resto = divide_e_resto(10, 3)

print("Quociente:", quociente)
print("Resto:", resto)
```

Resultado:

```text
Quociente: 3
Resto: 1
```

Mas o que a função realmente está retornando?

Vamos observar:

```python
resultado = divide_e_resto(10, 3)

print(resultado)
print(type(resultado))
```

Resultado:

```text
(3, 1)
<class 'tuple'>
```

Portanto, tecnicamente a função retorna **um único objeto do tipo tupla contendo dois valores**.

Python permite desempacotar essa tupla diretamente:

```python
quociente, resto = divide_e_resto(10, 3)
```


#### Funções sem retorno explícito

O que acontece quando uma função não possui `return`?

```python
def saudacao(nome):
    print("Olá,", nome)


resultado = saudacao("Maria")

print(resultado)
```

Toda função Python retorna um valor.

Quando nenhum valor de retorno é especificado, a função retorna automaticamente:

```python
None
```

`None` representa a ausência de um valor.


### 2.4 Refatorando o Wordle

Agora podemos voltar ao nosso Wordle.

Na implementação original, uma parte do programa possui uma responsabilidade bastante clara:

```python
resultado = ""

for i in range(len(palpite)):
    if palpite[i] == palavra_secreta[i]:
        resultado += "🟩"
    elif palpite[i] in palavra_secreta:
        resultado += "🟨"
    else:
        resultado += "⬛"
```

Esse trecho recebe duas informações:

* o palpite;
* a palavra secreta.

E produz uma informação:

* as dicas sobre o palpite.

Podemos representar essa operação utilizando uma função:

```python
def avaliar_palpite(palpite, palavra_secreta):
    resultado = ""

    for i in range(len(palpite)):
        if palpite[i] == palavra_secreta[i]:
            resultado += "🟩"
        elif palpite[i] in palavra_secreta:
            resultado += "🟨"
        else:
            resultado += "⬛"

    return resultado
```

Agora podemos fazer:

```python
resultado = avaliar_palpite("tempo", "termo")

print(resultado)
```

Resultado:

```text
🟩🟩🟩⬛🟩
```

Observe que a função:

```python
avaliar_palpite()
```

não precisa saber:

* de onde veio o palpite;
* como o resultado será exibido;
* quantas tentativas existem;
* quando o jogo termina.

Sua única responsabilidade é comparar duas palavras e retornar as dicas.

Isso facilita inclusive testar essa parte do programa:

```python
print(avaliar_palpite("tempo", "termo"))
print(avaliar_palpite("termo", "termo"))
print(avaliar_palpite("aaaaa", "termo"))
```


#### Separando a lógica do jogo

Também podemos colocar o controle das tentativas em uma função:

```python
def jogar(palavra_secreta, tentativas=6):

    for tentativa in range(tentativas):
        palpite = input("Digite uma palavra: ").lower()

        if len(palpite) != len(palavra_secreta):
            print(
                "A palavra deve ter",
                len(palavra_secreta),
                "letras."
            )
            continue

        resultado = avaliar_palpite(
            palpite,
            palavra_secreta
        )

        print(resultado)

        if palpite == palavra_secreta:
            print("Você acertou!")
            return

    print("Fim de jogo!")
```

Nosso programa principal pode agora ser simplesmente:

```python
palavra_secreta = "termo"

jogar(palavra_secreta)
```

Temos então duas funções com responsabilidades diferentes:

```python
avaliar_palpite()
```

responsável por comparar duas palavras.

E:

```python
jogar()
```

responsável por controlar as diferentes tentativas.

> **Perguntas**
>
> * Qual versão é mais fácil de compreender?
> * Qual versão é mais fácil de testar?
> * O que aconteceria se precisássemos mudar apenas a forma de avaliar um palpite?
> * O que ganhamos ao separar diferentes responsabilidades?


### 2.5 Escopo de variáveis

O **escopo** de uma variável refere-se à parte do programa onde aquele nome pode ser acessado.

Considere:

```python
def exibir():
    x = 10
    print(x)


exibir()

print(x)
```

O que acontece?

A variável `x` foi criada dentro da função.

Ela pertence ao **escopo local** de `exibir()` e não pode ser acessada fora da função.


#### Variáveis locais e globais

Considere agora:

```python
x = 10


def exibir():
    print(x)


exibir()

print(x)
```

Nesse caso, `x` foi definido fora da função.

Ele pertence ao namespace do módulo e pode ser consultado dentro da função.


#### Mesmo nome, escopos diferentes

O que você espera que seja exibido?

```python
x = 10


def exibir():
    x = 20
    print(x)


exibir()

print(x)
```

Resultado:

```text
20
10
```

O `x` definido dentro da função é local.

Ele é diferente do `x` definido fora da função.

Portanto:

```python
x = 20
```

dentro de `exibir()` não modifica o `x` externo.


#### Um caso curioso

O que acontece aqui?

```python
x = 10


def exibir():
    print(x)
    x = 20


exibir()
```

O código produz um erro.

Como existe uma atribuição:

```python
x = 20
```

dentro da função, Python considera `x` uma variável local daquela função.

Por isso:

```python
print(x)
```

tenta acessar uma variável local antes que ela tenha recebido um valor.


#### Blocos criam escopo?

Considere:

```python
if True:
    mensagem = "Olá"

print(mensagem)
```

Funciona?

E:

```python
for i in range(5):
    numero = i

print(numero)
```

Também funciona.

Em Python, estruturas como:

```text
if
for
while
```

não criam um novo escopo de variáveis.

Funções, por outro lado, criam.


#### Observando os namespaces

> **Curiosidade**

Python permite observar os nomes existentes durante a execução.

Por exemplo:

```python
def teste():
    x = 10
    y = 20

    print(locals())


teste()
```

`locals()` permite observar os nomes existentes no namespace local.

Também podemos utilizar:

```python
print(globals())
```

para observar os nomes pertencentes ao namespace global do módulo.

Python disponibiliza durante a execução diversas informações sobre seus objetos.

Na realidade, já utilizamos mecanismos desse tipo:

```python
print(type(10))
print(type("Python"))
```

Também podemos perguntar quais atributos estão disponíveis em um objeto:

```python
print(dir("Python"))
```

Essa capacidade de um programa examinar informações sobre seus próprios objetos durante a execução é chamada de **introspecção**.

Não precisamos conhecer todos esses mecanismos agora. O importante é perceber que Python disponibiliza várias dessas informações durante a execução do programa.


## 3. Modularização

### 3.1 Motivação

Depois da nossa refatoração, o programa possui uma estrutura semelhante a:

```python
def avaliar_palpite(...):
    ...


def jogar(...):
    ...


palavra_secreta = "termo"

jogar(palavra_secreta)
```

As funções permitiram organizar as diferentes responsabilidades do programa.

Mas ainda temos tudo dentro de um único arquivo.

À medida que um programa cresce, podemos acabar tendo:

```text
100 linhas
500 linhas
1.000 linhas
10.000 linhas
...
```

em um mesmo arquivo.

Além disso, algumas funções podem ser úteis em diferentes partes de um programa ou até em diferentes programas.

Por exemplo, poderíamos querer utilizar:

```python
avaliar_palpite()
```

em:

* nosso jogo;
* um programa de testes;
* outra interface;
* outro projeto.

Para facilitar a organização e reutilização de código, Python permite dividir programas em **módulos**.


### 3.2 Módulos

Um **módulo** Python é, de maneira simplificada, um arquivo `.py` contendo definições que podem ser utilizadas por outros arquivos.

Considere nosso Wordle.

Poderíamos organizar:

```text
wordle/
│
├── main.py
└── jogo.py
```

No arquivo:

```text
jogo.py
```

podemos colocar as funções relacionadas ao jogo:

```python
# jogo.py

def avaliar_palpite(palpite, palavra_secreta):
    resultado = ""

    for i in range(len(palpite)):
        if palpite[i] == palavra_secreta[i]:
            resultado += "🟩"
        elif palpite[i] in palavra_secreta:
            resultado += "🟨"
        else:
            resultado += "⬛"

    return resultado


def jogar(palavra_secreta, tentativas=6):

    for tentativa in range(tentativas):
        palpite = input("Digite uma palavra: ").lower()

        if len(palpite) != len(palavra_secreta):
            print(
                "A palavra deve ter",
                len(palavra_secreta),
                "letras."
            )
            continue

        resultado = avaliar_palpite(
            palpite,
            palavra_secreta
        )

        print(resultado)

        if palpite == palavra_secreta:
            print("Você acertou!")
            return

    print("Fim de jogo!")
```

Nosso outro arquivo pode então utilizar essas funções.


#### Importando um módulo

No arquivo:

```text
main.py
```

podemos escrever:

```python
import jogo


jogo.jogar("termo")
```

A instrução:

```python
import jogo
```

importa o módulo definido no arquivo:

```text
jogo.py
```

Podemos acessar suas definições através de:

```python
jogo.jogar
jogo.avaliar_palpite
```

Por exemplo:

```python
import jogo


resultado = jogo.avaliar_palpite(
    "tempo",
    "termo"
)

print(resultado)
```


#### Namespaces

Por que utilizamos:

```python
jogo.avaliar_palpite()
```

em vez de simplesmente:

```python
avaliar_palpite()
```

?

Um **namespace** pode ser entendido como um contexto que associa nomes a objetos.

Ao escrever:

```python
import jogo
```

as definições existentes em `jogo.py` ficam associadas ao namespace `jogo`.

Por isso podemos acessar:

```python
jogo.avaliar_palpite
jogo.jogar
```

Isso também evita conflitos de nomes.

Considere dois módulos.

```python
# matematica.py

def soma(a, b):
    return a + b
```

E:

```python
# texto.py

def soma(a, b):
    return a + " " + b
```

Os dois possuem uma função chamada:

```python
soma
```

Mas podemos utilizar ambos:

```python
import matematica
import texto


print(matematica.soma(2, 3))

print(texto.soma("Olá", "mundo"))
```

Como cada função pertence a um namespace diferente, não existe conflito.


#### Importando elementos específicos

Também podemos importar diretamente uma função:

```python
from jogo import avaliar_palpite
```

Nesse caso podemos fazer:

```python
resultado = avaliar_palpite(
    "tempo",
    "termo"
)
```

sem precisar escrever:

```python
jogo.avaliar_palpite(...)
```

Também podemos importar vários elementos:

```python
from jogo import avaliar_palpite, jogar
```

As duas formas são válidas:

```python
import jogo
```

ou:

```python
from jogo import avaliar_palpite
```

A primeira forma deixa explícito de qual módulo determinada função veio:

```python
jogo.avaliar_palpite(...)
```


### 3.3 Execução e importação de módulos

Existe um detalhe importante sobre módulos Python.

Considere:

```python
# jogo.py

print("Carregando jogo...")


def avaliar_palpite(palpite, palavra_secreta):
    ...
```

E:

```python
# main.py

import jogo
```

Ao executar:

```text
main.py
```

o que será exibido?

```text
Carregando jogo...
```

Isso acontece porque o código existente no nível do módulo é executado quando ele é importado.

Agora considere:

```python
# jogo.py

def jogar():
    print("Executando o jogo...")


jogar()
```

Ao executar diretamente:

```bash
python jogo.py
```

temos:

```text
Executando o jogo...
```

Mas o que acontece se outro arquivo fizer:

```python
import jogo
```

?

O jogo também será iniciado.

Isso nem sempre é o comportamento que desejamos.

Queremos distinguir duas situações:

1. executar `jogo.py` diretamente;
2. importar `jogo.py` para utilizar suas funções.


#### `__name__`

Todo módulo Python possui uma variável especial chamada:

```python
__name__
```

Podemos observar seu valor:

```python
print(__name__)
```

Considere um arquivo:

```python
# jogo.py

print(__name__)
```

Se executarmos diretamente:

```bash
python jogo.py
```

o resultado será:

```text
__main__
```

Por outro lado, se tivermos:

```python
# main.py

import jogo
```

dentro de `jogo.py`, `__name__` terá o valor:

```text
jogo
```

Portanto:

* arquivo executado diretamente → `__name__ == "__main__"`;
* arquivo importado → `__name__` recebe o nome do módulo.


#### `if __name__ == "__main__"`

Podemos utilizar esse comportamento para decidir quando executar determinada parte do programa:

```python
def jogar():
    print("Executando o jogo...")


if __name__ == "__main__":
    jogar()
```

Agora:

```bash
python jogo.py
```

executará:

```python
jogar()
```

Mas:

```python
import jogo
```

não iniciará automaticamente o jogo.

Uma estrutura bastante comum é:

```python
def main():
    jogar()


if __name__ == "__main__":
    main()
```

Aplicando ao nosso Wordle:

```python
def avaliar_palpite(palpite, palavra_secreta):
    resultado = ""

    for i in range(len(palpite)):
        if palpite[i] == palavra_secreta[i]:
            resultado += "🟩"
        elif palpite[i] in palavra_secreta:
            resultado += "🟨"
        else:
            resultado += "⬛"

    return resultado


def jogar(palavra_secreta, tentativas=6):
    # lógica do jogo
    ...


def main():
    jogar("termo")


if __name__ == "__main__":
    main()
```

O mesmo arquivo agora pode ser utilizado de duas maneiras.

Como programa:

```bash
python jogo.py
```

ou como módulo:

```python
import jogo


resultado = jogo.avaliar_palpite(
    "tempo",
    "termo"
)
```


### 3.4 Pacotes

Funções ajudam a organizar operações.

Módulos ajudam a organizar funções e outras definições.

Mas, conforme nossos programas crescem, podemos também ter muitos módulos.

Por exemplo:

```text
wordle/
│
├── main.py
├── regras.py
├── interface.py
├── palavras.py
└── estatisticas.py
```

Python permite agrupar módulos relacionados em **pacotes**.

Podemos reorganizar nosso projeto como:

```text
wordle/
│
├── main.py
│
└── jogo/
    ├── __init__.py
    ├── regras.py
    └── interface.py
```

Aqui:

```text
jogo/
```

representa um pacote.

E:

```text
regras.py
interface.py
```

são módulos pertencentes ao pacote.

Podemos então importar:

```python
from jogo.regras import avaliar_palpite
```

ou:

```python
import jogo.regras
```

e acessar:

```python
jogo.regras.avaliar_palpite(...)
```


#### `__init__.py`

Tradicionalmente, pacotes Python possuem um arquivo chamado:

```text
__init__.py
```

Por exemplo:

```text
jogo/
├── __init__.py
├── regras.py
└── interface.py
```

Para nossos primeiros programas, esse arquivo pode simplesmente estar vazio.

```python
# __init__.py
```

Ele também pode conter código executado quando o pacote é importado.

Por exemplo:

```python
# __init__.py

print("Inicializando pacote jogo")
```

Neste momento, não precisamos explorar todos os detalhes de pacotes.

O importante é compreender a ideia geral:

```text
Função
   ↓
organiza uma tarefa

Módulo
   ↓
organiza funções e outras definições
em um arquivo

Pacote
   ↓
organiza módulos relacionados
em uma estrutura de diretórios
```


## 4. Exercícios

### 4.1. Informações de usuário

Escreva uma função chamada:

```python
exibir_info
```

que recebe três parâmetros:

```text
nome
idade
cidade
```

Os parâmetros devem possuir como valor padrão uma string vazia.

A função deve imprimir:

```text
Nome: [nome], Idade: [idade], Cidade: [cidade]
```

Teste a função utilizando argumentos posicionais e argumentos por palavra-chave.

### 4.2. Área e perímetro

Escreva uma função:

```python
calcular_propriedades_retangulo
```

que recebe:

```text
comprimento
largura
```

A função deve calcular e retornar:

* a área;
* o perímetro.

Utilize desempacotamento para receber os dois resultados:

```python
area, perimetro = calcular_propriedades_retangulo(10, 5)
```


### 4.3. Refatorando o Wordle

Considere novamente nossa implementação inicial.

Separe o programa nas seguintes funções.

#### A. `avaliar_palpite`

```python
avaliar_palpite(palpite, palavra_secreta)
```

Deve receber duas palavras e retornar uma string contendo as dicas:

```text
🟩🟨⬛...
```


#### B. `ler_palpite`

```python
ler_palpite(tamanho)
```

Deve solicitar uma palavra ao usuário.

Se a palavra possuir tamanho incorreto, deve solicitar novamente.

A função deve retornar apenas quando receber uma palavra com o tamanho esperado.


#### C. `jogar`

```python
jogar(palavra_secreta, tentativas=6)
```

Deve controlar as diferentes rodadas do jogo.

Utilize as funções anteriores sempre que possível.


#### D. Modularizando o Wordle

Depois de implementar as funções, organize o programa em:

```text
wordle/
├── main.py
└── jogo.py
```

O arquivo:

```text
jogo.py
```

deve conter as funções relacionadas ao jogo.

O arquivo:

```text
main.py
```

deve importar o módulo `jogo` e iniciar uma nova partida.

Por exemplo:

```python
# main.py

import jogo


jogo.jogar("termo")
```

#### Para pensar

Depois dessa reorganização:

* Qual parte do programa é mais fácil de testar?
* Quais funções poderiam ser reutilizadas por outro programa?
* Qual é a vantagem de manter `main.py` pequeno?
* O que aconteceria se quiséssemos criar uma interface gráfica para o mesmo jogo?
* A lógica responsável por avaliar um palpite precisaria mudar?
