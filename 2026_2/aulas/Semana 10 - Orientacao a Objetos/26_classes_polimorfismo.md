# Aula 27: Polimorfismo

## 1. O problema: funções que precisam conhecer todos os tipos

### 1.1 Efetuando pagamentos

Uma loja virtual aceita três formas de pagamento: Pix, boleto e cartão de crédito. Todos têm um valor, mas cada um tem **dados próprios**:

```text
Pix                →  chave

Boleto             →  código de barras

Cartão de crédito  →  número do cartão
```

Usando herança, representamos os três com uma classe base:

```python
class Pagamento:

    def __init__(self, valor):
        self.valor = valor


class PagamentoPix(Pagamento):

    def __init__(self, valor, chave):
        super().__init__(valor)
        self.chave = chave


class PagamentoBoleto(Pagamento):

    def __init__(self, valor, codigo_barras):
        super().__init__(valor)
        self.codigo_barras = codigo_barras


class PagamentoCartao(Pagamento):

    def __init__(self, valor, numero):
        super().__init__(valor)
        self.numero = numero
```

Agora precisamos de uma função que **efetue** uma lista de pagamentos. Cada tipo é efetuado de um jeito, então verificamos o tipo de cada um:

```python
def processar(pagamentos):
    for p in pagamentos:
        if isinstance(p, PagamentoPix):
            print(f"Pix de R$ {p.valor:.2f} enviado para a chave {p.chave}")
        elif isinstance(p, PagamentoBoleto):
            print(f"Boleto de R$ {p.valor:.2f} registrado: {p.codigo_barras}")
        elif isinstance(p, PagamentoCartao):
            print(f"Cartão final {p.numero[-4:]} cobrado em R$ {p.valor:.2f}")
```

Testando:

```python
lista = [
    PagamentoPix(100, "ana@email.com"),
    PagamentoBoleto(250, "34191.79001"),
    PagamentoCartao(80, "1234567812345678"),
]

processar(lista)
```

Saída:

```text
Pix de R$ 100.00 enviado para a chave ana@email.com
Boleto de R$ 250.00 registrado: 34191.79001
Cartão final 5678 cobrado em R$ 80.00
```

Funciona.



### 1.2 O que acontece quando surge um tipo novo?

Agora a loja passa a aceitar **cartão de débito**:

```python
class PagamentoDebito(Pagamento):

    def __init__(self, valor, numero):
        super().__init__(valor)
        self.numero = numero
```

E tentamos efetuar um pagamento:

```python
processar([PagamentoDebito(50, "8765432187654321")])
```

Saída:

```text

```

**Nada.** Sem erro, sem aviso: nenhum `if` foi satisfeito, e o pagamento simplesmente não foi efetuado. Isso é pior do que uma falha com mensagem, porque o cliente achou que pagou e a loja achou que recebeu.

Para corrigir, precisamos voltar ao `processar` e acrescentar mais um `elif`. E o `processar` não é o único lugar:

```text
efetuar (processar)   →  acrescentar o débito

estornar              →  acrescentar o débito

emitir recibo         →  acrescentar o débito

...qualquer função que dependa do tipo do pagamento
```

Se esquecermos uma delas, o sistema passa a se comportar de formas diferentes em partes diferentes. Esse é o mesmo problema que vimos no `if/elif` das mensagens: **cada tipo novo exige modificar o código que já existia**, e esse código precisa conhecer todos os tipos.



### 1.3 Uma pista

Na aula de herança, vimos um `Chat` que chamava `mensagem.exibir()` para cada mensagem, **sem verificar o tipo**. Texto e imagem se exibiam do seu jeito, e o `Chat` nunca precisou ser modificado.

É esse caminho que vamos seguir aqui.



## 2. Polimorfismo

### 2.1 Cada tipo sabe se efetuar

Em vez de uma função que conhece todos os tipos, fazemos com que **cada pagamento saiba se efetuar**, usando os seus próprios dados:

```python
class Pagamento:

    def __init__(self, valor):
        self.valor = valor


class PagamentoPix(Pagamento):

    def __init__(self, valor, chave):
        super().__init__(valor)
        self.chave = chave

    def efetuar(self):
        print(f"Pix de R$ {self.valor:.2f} enviado para a chave {self.chave}")


class PagamentoBoleto(Pagamento):

    def __init__(self, valor, codigo_barras):
        super().__init__(valor)
        self.codigo_barras = codigo_barras

    def efetuar(self):
        print(f"Boleto de R$ {self.valor:.2f} registrado: {self.codigo_barras}")


class PagamentoCartao(Pagamento):

    def __init__(self, valor, numero):
        super().__init__(valor)
        self.numero = numero

    def efetuar(self):
        print(f"Cartão final {self.numero[-4:]} cobrado em R$ {self.valor:.2f}")
```

E a função `processar` passa a ser muito mais simples:

```python
def processar(pagamentos):
    for p in pagamentos:
        p.efetuar()
```

Testando com a mesma `lista` de antes:

```python
processar(lista)
```

Saída:

```text
Pix de R$ 100.00 enviado para a chave ana@email.com
Boleto de R$ 250.00 registrado: 34191.79001
Cartão final 5678 cobrado em R$ 80.00
```

O resultado é idêntico ao da versão com `if/elif`. Mas observe o que mudou:

```text
Antes   →  processar() precisava conhecer todos os tipos
           e os dados de cada um (chave, código de barras, número)

Agora   →  processar() só sabe que cada pagamento
           responde a efetuar()
```

Os detalhes de cada tipo ficaram **dentro da própria classe**, onde estão os dados.



### 2.2 Acrescentando um tipo novo

Vamos acrescentar o cartão de débito:

```python
class PagamentoDebito(Pagamento):

    def __init__(self, valor, numero):
        super().__init__(valor)
        self.numero = numero

    def efetuar(self):
        print(f"Débito de R$ {self.valor:.2f} no cartão final {self.numero[-4:]}")
```

E usá-lo:

```python
processar(lista + [PagamentoDebito(50, "8765432187654321")])
```

Saída:

```text
Pix de R$ 100.00 enviado para a chave ana@email.com
Boleto de R$ 250.00 registrado: 34191.79001
Cartão final 5678 cobrado em R$ 80.00
Débito de R$ 50.00 no cartão final 4321
```

Escrevemos **uma classe nova** e **nenhuma linha** de `processar` foi alterada.

Esse é o grande benefício do polimorfismo: o sistema pode **crescer** acrescentando código novo, sem modificar o código que já funciona. Essa ideia tem um nome em projeto de software ("aberto para extensão, fechado para modificação") e voltaremos a ela quando estudarmos os princípios SOLID.



### 2.3 O que é polimorfismo?

A palavra vem do grego: *poli* (muitas) e *morfos* (formas).

> **Polimorfismo** é a capacidade de usar objetos de classes diferentes por meio da **mesma chamada**, cada um respondendo **do seu jeito**, sem que quem chama precise conhecer o tipo.

```text
p.efetuar()

    se p é Pix      →  envia para a chave

    se p é Boleto   →  registra o código de barras

    se p é Cartão   →  cobra no número do cartão
```

Quem chama escreve **uma** linha. A escolha de qual comportamento executar é feita **pelo objeto**.



### 2.4 Quem escolhe qual versão executar?

Na aula de herança, vimos como o Python procura um método: primeiro no objeto, depois na classe do objeto, depois na classe base, parando no primeiro lugar em que encontrar.

O polimorfismo usa exatamente esse mecanismo. Quando `processar` executa `p.efetuar()`, o Python **só descobre na hora da chamada** qual é a classe de `p` e procura o método a partir dela:

```text
p é um PagamentoBoleto  →  procura em PagamentoBoleto  →  encontra, executa

p é um PagamentoCartao  →  procura em PagamentoCartao  →  encontra, executa
```

A mesma linha de código, em momentos diferentes, executa métodos diferentes.



## 3. Polimorfismo sem herança: *duck typing*

### 3.1 Você já usa

Algumas funções que usamos desde o início da disciplina funcionam com tipos que **não têm nenhuma relação entre si**:

```python
print(len("abc"))
print(len([1, 2, 3]))
print(len({"a": 1, "b": 2}))
print(len((1, 2)))
```

Saída:

```text
3
3
2
2
```

Texto, lista, dicionário e tupla não herdam uns dos outros. O `len` funciona com todos eles porque **todos sabem responder ao `len`**. Com um número, a história é outra:

```python
len(10)
```

```text
TypeError: object of type 'int' has no len()
```

Outro exemplo é o `print`. Ele sabe imprimir números, textos, listas e objetos nossos, porque cada tipo sabe como se transformar em texto. Para objetos nossos, isso é feito pelo método `__str__`:

```python
class Ponto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


print(1, "texto", [1, 2], Ponto(3, 4))
```

Saída:

```text
1 texto [1, 2] (3, 4)
```

O `print` não verifica o tipo de cada objeto. Ele simplesmente pede que cada um se converta em texto. Isso também é polimorfismo.



### 3.2 Pagamento sem herdar de `Pagamento`

Em Python, para que `processar` funcione, o objeto **não precisa herdar** de `Pagamento`. Basta que ele tenha o método que `processar` usa:

```python
class PagamentoPontos:

    def __init__(self, valor, pontos):
        self.valor = valor
        self.pontos = pontos

    def efetuar(self):
        print(f"{self.pontos} pontos debitados")
```

Essa classe **não** herda de `Pagamento`:

```python
print(isinstance(PagamentoPontos(10, 1000), Pagamento))
```

Saída:

```text
False
```

Mas funciona:

```python
processar([PagamentoPix(100, "ana@email.com"), PagamentoPontos(40, 4000)])
```

Saída:

```text
Pix de R$ 100.00 enviado para a chave ana@email.com
4000 pontos debitados
```

Essa ideia é conhecida como ***duck typing*** ("tipagem de pato"), por causa do ditado:

> Se anda como um pato e grasna como um pato, então para os nossos propósitos é um pato.

Traduzindo: o que importa **não é a classe** do objeto, e sim **o que ele sabe fazer**.

```text
Herança       →  "este objeto é um Pagamento"

Duck typing   →  "este objeto sabe efetuar()"
```



### 3.3 O custo da flexibilidade

Como nada verifica o objeto **antes**, o erro só aparece **na hora da chamada**:

```python
class Fatura:

    def __init__(self, valor):
        self.valor = valor


processar([Fatura(10)])
```

Saída:

```text
AttributeError: 'Fatura' object has no attribute 'efetuar'
```

O programa só descobre o problema depois de já ter começado a processar.

Também não há como saber, olhando para a classe `PagamentoPontos`, **quais métodos ela deveria ter**. Quem decide isso é o código que a usa.

Gostaríamos de uma forma de **declarar o contrato** e de ser avisado cedo, se alguém o descumprir.



## 4. Garantindo o contrato: classes abstratas

### 4.1 Uma classe base que exige métodos

Python oferece o módulo `abc` (*abstract base classes*). Com ele, a classe base declara **quais métodos as subclasses são obrigadas a implementar**:

```python
from abc import ABC, abstractmethod


class Pagamento(ABC):

    def __init__(self, valor):
        self.valor = valor

    @abstractmethod
    def efetuar(self):
        ...
```

```text
(ABC)             →  marca a classe como abstrata

@abstractmethod   →  "toda subclasse DEVE implementar este método"
```

A base agora funciona como um **contrato**: quem herda de `Pagamento` promete oferecer `efetuar()`.

Uma subclasse que cumpre o contrato funciona normalmente:

```python
class PagamentoPix(Pagamento):

    def __init__(self, valor, chave):
        super().__init__(valor)
        self.chave = chave

    def efetuar(self):
        print(f"Pix de R$ {self.valor:.2f} enviado para a chave {self.chave}")


PagamentoPix(10, "ana@email.com").efetuar()
print(isinstance(PagamentoPix(10, "ana@email.com"), Pagamento))
```

Saída:

```text
Pix de R$ 10.00 enviado para a chave ana@email.com
True
```



### 4.2 O erro aparece cedo

Se uma subclasse esquecer o método:

```python
class PagamentoIncompleto(Pagamento):
    pass


PagamentoIncompleto(10)
```

Saída:

```text
TypeError: Can't instantiate abstract class PagamentoIncompleto without an implementation for abstract method 'efetuar'
```

O erro acontece **na criação do objeto**, e a mensagem diz exatamente o que falta. Não é preciso esperar que o `processar` chegue naquele pagamento para descobrir o problema.

A própria classe abstrata também **não pode ser instanciada**:

```python
Pagamento(10)
```

Saída:

```text
TypeError: Can't instantiate abstract class Pagamento without an implementation for abstract method 'efetuar'
```

Isso faz sentido: não existe "um pagamento genérico". Existe Pix, boleto, cartão.



### 4.3 O outro sentido de "abstração"

Na aula de abstração, avisamos que a palavra "abstração" tem outro sentido em orientação a objetos. Aqui ele aparece:

```text
Abstração (aula de abstração)    →  escolher o que representar

Classe abstrata (hoje)           →  declarar o que as subclasses
                                    devem oferecer, escondendo
                                    "como" cada uma faz
```

O `processar` usa a abstração `Pagamento` sem se preocupar com os detalhes de cada tipo.

Há ainda uma alternativa para descrever contratos sem exigir herança, chamada `Protocol`, do módulo `typing`. Não vamos estudá-la agora. Apenas saiba que ela existe, e que é útil principalmente para ferramentas que verificam o código antes de executá-lo.



## 5. Cuidados

### 5.1 Um `isinstance` em cadeia é um `if/elif` disfarçado

Se você se pegar escrevendo:

```python
if isinstance(objeto, TipoA):
    ...
elif isinstance(objeto, TipoB):
    ...
```

pare e pergunte: **isso não deveria ser um método de cada classe?** Foi exatamente a nossa situação na seção 1.

Há usos legítimos de `isinstance`, como validar o que uma função recebeu. Mas, quando a decisão é "o que fazer conforme o tipo", o polimorfismo costuma ser melhor.



### 5.2 Todos precisam respeitar o mesmo "formato"

O polimorfismo só funciona se os métodos seguem o **mesmo formato**: mesmos parâmetros e mesmo tipo de resultado. Veja o que acontece quando um tipo foge ao contrato:

```python
class PagamentoComSenha(Pagamento):

    def efetuar(self, senha):
        print("Pagamento efetuado")


processar([PagamentoComSenha(10)])
```

Saída:

```text
TypeError: PagamentoComSenha.efetuar() missing 1 required positional argument: 'senha'
```

O `processar` chama `p.efetuar()` **sem argumentos**, e a classe passou a exigir um. A classe tem o método certo, mas com um formato diferente, e o erro aparece longe da causa.

Uma regra prática: **quem chama deve poder tratar todos os objetos exatamente da mesma forma**. Se for preciso verificar qual é o tipo para saber como chamar, o contrato foi violado.



### 5.3 Nem todo `if` precisa virar polimorfismo

Se existem apenas dois tipos e eles dificilmente mudarão, um `if` simples pode ser mais claro do que criar uma hierarquia de classes. O polimorfismo compensa quando:

```text
- os tipos tendem a aumentar com o tempo;

- vários lugares do programa precisam tomar decisões
  conforme o tipo.
```



## 6. Prática: um novo tipo de pagamento

### 6.1 O ponto de partida

O código a seguir já está pronto:

```python
from abc import ABC, abstractmethod


class Pagamento(ABC):

    def __init__(self, valor):
        self.valor = valor

    @abstractmethod
    def efetuar(self):
        ...


class PagamentoPix(Pagamento):

    def __init__(self, valor, chave):
        super().__init__(valor)
        self.chave = chave

    def efetuar(self):
        print(f"Pix de R$ {self.valor:.2f} enviado para a chave {self.chave}")


class PagamentoCartao(Pagamento):

    def __init__(self, valor, numero):
        super().__init__(valor)
        self.numero = numero

    def efetuar(self):
        print(f"Cartão final {self.numero[-4:]} cobrado em R$ {self.valor:.2f}")


def processar(pagamentos):
    for p in pagamentos:
        p.efetuar()
```



### 6.2 O enunciado

Crie a classe `PagamentoParcelado`, que:

- herda de `Pagamento`;
- recebe, além do `valor`, o `numero` do cartão e o número de `parcelas`;
- ao ser efetuado, mostra o final do cartão e o valor de cada parcela, no formato abaixo.

Depois, teste:

```python
processar([
    PagamentoPix(100, "ana@email.com"),
    PagamentoParcelado(200, "1234567812345678", 3),
])
```

Saída esperada:

```text
Pix de R$ 100.00 enviado para a chave ana@email.com
Cartão final 5678: 3x de R$ 66.67
```

**Observação:** a função `processar` **não pode ser modificada**.

**Desafios:**

1. Crie uma classe `PagamentoPontos` que **não herde** de `Pagamento`, e verifique que `processar` continua funcionando.
2. Remova o método `efetuar()` de uma das suas classes que herdam de `Pagamento`. Em que momento o erro aparece?



### 6.3 Uma solução de referência

```python
class PagamentoParcelado(Pagamento):

    def __init__(self, valor, numero, parcelas):
        super().__init__(valor)
        self.numero = numero
        self.parcelas = parcelas

    def efetuar(self):
        print(f"Cartão final {self.numero[-4:]}: {self.parcelas}x de R$ {self.valor / self.parcelas:.2f}")
```

**Para pensar:**

1. Quantas linhas de `processar` foram alteradas?
2. Por que o `__init__` de `PagamentoParcelado` chama `super().__init__(valor)`?
3. Em qual momento o Python decide qual `efetuar()` executar?



## 7. Exercícios

### 7.1 Áreas de formas geométricas

Crie uma classe abstrata `Forma` com o método abstrato `area()`. Depois, crie as classes:

- `Retangulo`, com `largura` e `altura`;
- `Circulo`, com `raio` (use `math.pi`);
- `Triangulo`, com `base` e `altura`.

Escreva uma função que receba uma lista de formas e devolva a **soma das áreas**, sem verificar o tipo de nenhuma delas.

Exemplo:

```python
formas = [Retangulo(5, 3), Circulo(2), Triangulo(4, 3)]

print(round(somar_areas(formas), 2))
```

Saída esperada:

```text
33.57
```

**Para pensar:**

1. O que acontece se você tentar criar uma `Forma()` diretamente?
2. O que precisaria mudar em `somar_areas` para aceitar um novo tipo, como `Trapezio`?



### 7.2 Duck typing

Crie duas classes que **não tenham relação de herança**, por exemplo `Cachorro` e `Robo`, ambas com um método `falar()` que devolve um texto diferente.

Escreva uma função que receba uma lista de objetos e imprima o resultado de `falar()` de cada um.

Depois, teste a função com a lista contendo também um número inteiro.

**Para pensar:**

1. Em que momento o erro aparece?
2. Como uma classe abstrata ajudaria a descobrir o problema mais cedo? E o que seria necessário mudar nas classes `Cachorro` e `Robo`?



### 7.3 Refatorando um `if/elif`

Considere o código abaixo, que calcula o frete de um pedido conforme o tipo de entrega:

```python
class PedidoNormal:
    pass


class PedidoExpresso:
    pass


class PedidoRetirada:
    pass


def calcular_frete(pedido):
    if isinstance(pedido, PedidoNormal):
        return 10
    elif isinstance(pedido, PedidoExpresso):
        return 25
    elif isinstance(pedido, PedidoRetirada):
        return 0
```

Refatore o código para usar polimorfismo:

- cada classe deve ter o método `calcular_frete()`;
- escreva uma função `total_fretes(pedidos)` que some os fretes de uma lista, sem usar `isinstance`.

Exemplo:

```python
print(total_fretes([PedidoNormal(), PedidoExpresso(), PedidoRetirada()]))
```

Saída esperada:

```text
35
```

**Para pensar:**

1. O que você precisaria fazer para acrescentar um `PedidoDrone` (frete 40)? Quantas funções existentes precisariam ser alteradas?
2. Nessa versão, a herança é necessária? Você usaria uma classe base? Por quê?