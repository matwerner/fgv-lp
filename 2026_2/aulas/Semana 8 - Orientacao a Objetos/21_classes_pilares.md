# Aula 22: Classes e Objetos por Dentro + Visão Geral dos Pilares

## 1. De onde estamos partindo?

### 1.1 O que construímos na aula anterior

Na última aula, partimos de uma solução procedural (dicionários e funções) e chegamos a uma classe `Mensagem` e a uma classe `Chat`:

```python
class Mensagem:

    def __init__(self, nome, texto, data_envio):
        self.nome = nome
        self.texto = texto
        self.data_envio = data_envio
        self.lida = False
        self.favorita = False

    def exibir(self):
        print(
            f"{self.nome} "
            f"{self.data_envio}: "
            f"{self.texto}"
        )

    def favoritar(self):
        self.favorita = True

    def marcar_como_lida(self):
        self.lida = True


class Chat:

    def __init__(self):
        self.historico = []

    def adicionar(self, mensagem):
        self.historico.append(mensagem)

    def exibir(self):
        for mensagem in self.historico:
            mensagem.exibir()
```

Vimos que:

- uma **classe** define uma estrutura utilizada para criar objetos;
- um **objeto** (ou instância) é criado a partir de uma classe;
- **atributos** armazenam o estado de cada objeto;
- **métodos** definem os comportamentos de um objeto;
- `self` representa o objeto sobre o qual um método está sendo executado.



### 1.2 O que ainda não explicamos

Na aula anterior, usamos algumas coisas "porque funcionam".

Por exemplo:

```python
m1 = Mensagem("Matheus", "Olá!", "2026-10-05T08:00")
```

Podemos fazer algumas perguntas:

> Qual é o papel do `__init__`?

> De onde vem o `self`? Nós não passamos nenhum argumento para ele.

> Onde ficam os dados de cada objeto? E os métodos?

> O que acontece se atribuirmos um objeto a outra variável?

Nesta aula, vamos responder a essas perguntas e, em seguida, apresentar uma visão geral das ideias que organizam a orientação a objetos: os chamados **pilares**.



## 2. O que acontece quando criamos um objeto?

### 2.1 Criando um objeto

Considere novamente:

```python
m1 = Mensagem("Matheus", "Olá!", "2026-10-05T08:00")
```

Ao criarmos uma nova `Mensagem`, o Python executa o método:

```python
__init__
```

para inicializar o estado daquele objeto.

Podemos pensar aproximadamente:

```text
Mensagem("Matheus", "Olá!", "2026-10-05T08:00")
                ↓
          novo objeto
                ↓
            __init__
                ↓
      estado inicial definido
```

Observe que o `__init__` **não cria** o objeto: quando ele começa a executar, o objeto já existe. O papel do `__init__` é **inicializar** esse objeto. Também não o chamamos diretamente: o Python faz isso por nós.

Podemos verificar que o `self` do `__init__` é o próprio objeto criado, utilizando `id`, que retorna um número que identifica cada objeto enquanto ele existe:

```python
class Mensagem:

    def __init__(self, nome, texto, data_envio):
        print("self dentro do __init__:", id(self))
        self.nome = nome
        self.texto = texto
        self.data_envio = data_envio
        self.lida = False
        self.favorita = False


m1 = Mensagem("Matheus", "Olá!", "2026-10-05T08:00")

print("m1 fora da classe:   ", id(m1))
```

Saída (os números mudam a cada execução):

```text
self dentro do __init__: 140126774844480
m1 fora da classe:    140126774844480
```

Os dois números são iguais: o `self` do `__init__` e `m1` são **o mesmo objeto**.

O `__init__` será executado novamente sempre que criarmos outro objeto:

```python
m1 = Mensagem("Matheus", "Olá!", "2026-10-05T08:00")
m2 = Mensagem("João", "Bom dia!", "2026-10-05T09:00")
```

Assim, objetos criados a partir da mesma classe podem possuir estados diferentes.



### 2.2 De onde vem o `self`?

O `self` representa o **objeto sobre o qual o método está sendo executado**.

Considere:

```python
m1.favoritar()
```

Nesse caso, dentro de `favoritar()`, `self` representa `m1`.

Se fizermos:

```python
m2.favoritar()
```

o mesmo método será executado, mas agora `self` representa `m2`:

```text
m1.favoritar()
      ↓
self = m1


m2.favoritar()
      ↓
self = m2
```

É por isso que o mesmo método consegue operar sobre objetos diferentes.

Podemos pensar na chamada `m1.favoritar()` aproximadamente como:

```python
Mensagem.favoritar(m1)
```

Podemos inclusive testar:

```python
m1 = Mensagem("Matheus", "Olá!", "2026-10-05T08:00")

Mensagem.favoritar(m1)

print(m1.favorita)
```

Saída:

```text
True
```

Isso explica um detalhe que pode ter causado estranhamento.

O método foi definido com um parâmetro:

```python
def favoritar(self):
    self.favorita = True
```

mas normalmente o chamamos sem informar explicitamente esse argumento:

```python
m1.favoritar()
```

O objeto antes do ponto é fornecido automaticamente como `self`.

O mesmo vale para métodos que possuem outros parâmetros.

Considere:

```python
class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual):
        self.preco *= 1 - percentual / 100
```

Quando fazemos:

```python
produto.aplicar_desconto(10)
```

podemos pensar aproximadamente em:

```python
Produto.aplicar_desconto(produto, 10)
```

Nesse caso:

```text
self        → produto
percentual  → 10
```

Note a semelhança com a versão procedural da Aula 21, em que `aplicar_desconto` era uma função que recebia o produto como argumento:

```python
aplicar_desconto(produto, 10)             # procedural (Aula 21)

Produto.aplicar_desconto(produto, 10)     # chamada pela classe

produto.aplicar_desconto(10)              # forma habitual
```

É a mesma ideia. Uma diferença importante é onde a função está definida: agora ela faz parte da classe, junto com os comportamentos relacionados àquele tipo de objeto.



## 3. Onde ficam os dados e os comportamentos?

### 3.1 Cada objeto possui seu próprio estado

Já vimos que objetos criados a partir da mesma classe possuem estados independentes:

```python
m1 = Mensagem("Matheus", "Olá!", "2026-10-05T08:00")
m2 = Mensagem("João", "Bom dia!", "2026-10-05T09:00")

m1.favoritar()

print(m1.favorita)
print(m2.favorita)
```

Saída:

```text
True
False
```

Cada objeto possui seu próprio estado.



### 3.2 Métodos ficam na classe

E os métodos?

Não precisamos criar uma nova cópia de `favoritar()`, `exibir()` ou `marcar_como_lida()` para cada mensagem.

Esses métodos são definidos uma única vez na classe:

```text
                 Mensagem
                 ├── exibir()
                 ├── favoritar()
                 └── marcar_como_lida()
                        ▲
              ┌─────────┴─────────┐
              │                   │
         m1 (objeto)         m2 (objeto)

         nome=Matheus        nome=João
         texto=Olá!          texto=Bom dia!
         lida=False          lida=False
         favorita=True       favorita=False
```

O **código dos métodos** é comum aos objetos.

O que muda de um objeto para outro são seus **dados**.

É justamente aí que entra `self`: ele informa ao método **de qual objeto** os dados devem ser utilizados ou modificados.

Podemos resumir:

```text
CLASSE   → comportamentos comuns

OBJETO   → estado particular

self     → indica sobre qual objeto
           o método está operando
```



## 4. Identidade e referências

### 4.1 Variáveis guardam referências

O que acontece quando atribuímos um objeto a outra variável?

```python
m1 = Mensagem("Matheus", "Olá!", "2026-10-05T08:00")

m3 = m1
```

A instrução:

```python
m3 = m1
```

não cria uma nova `Mensagem`.

Agora `m1` e `m3` se referem ao mesmo objeto:

```text
m1 ─┐
    ├──→ [ objeto Mensagem ]
m3 ─┘
```

Por isso:

```python
m3.favoritar()

print(m1.favorita)
```

produz:

```text
True
```

Alteramos o objeto utilizando o nome `m3`, mas `m1` continua apontando para esse mesmo objeto.

Podemos verificar isso utilizando `is`:

```python
print(m1 is m3)
```

Saída:

```text
True
```

Agora considere:

```python
a = Mensagem("Matheus", "Olá!", "2026-10-05T08:00")
b = Mensagem("Matheus", "Olá!", "2026-10-05T08:00")
```

Mesmo tendo os mesmos valores:

```python
print(a is b)
```

produz:

```text
False
```

Isso acontece porque foram criados **dois objetos diferentes**.

```text
Identidade → são o mesmo objeto? → is
```

Se testarmos `a == b`, o resultado também será `False`. Por padrão, o Python considera dois objetos "iguais" apenas se forem o mesmo objeto. Nas próximas aulas, veremos como mudar esse comportamento.



### 4.2 Objetos dentro de outros objetos

Essa característica é importante quando um objeto contém outros objetos.

Na aula anterior, criamos um `Chat` que guarda mensagens:

```python
chat = Chat()

chat.adicionar(m1)
chat.adicionar(m2)
```

O `Chat` guarda referências para os mesmos objetos representados por `m1` e `m2`.

```text
m1 ──────→ [ Mensagem ] ←──── chat.historico[0]

m2 ──────→ [ Mensagem ] ←──── chat.historico[1]
```

Então:

```python
m2.favoritar()

print(chat.historico[1].favorita)
```

produz:

```text
True
```

Modificamos `m2` fora do chat e a mudança aparece quando acessamos a mensagem através do chat, pois estamos tratando do mesmo objeto.

Isso também responde a uma das perguntas do exercício do carrinho de compras.

Considere (utilizando as classes `Produto` e `Carrinho` do exercício):

```python
produto = Produto("Livro", 50.0)

carrinho = Carrinho()
carrinho.adicionar(produto)

print(carrinho.total())

produto.aplicar_desconto(10)

print(carrinho.total())
```

Saída:

```text
50.0
45.0
```

O carrinho guarda uma referência para o objeto `produto`, e não uma cópia.

Portanto, quando `carrinho.total()` é executado, é utilizado o preço **atualizado** do produto, mesmo sem termos modificado o carrinho.



## 5. Os pilares da orientação a objetos

### 5.1 O que a orientação a objetos tenta resolver?

Na aula anterior, observamos algumas questões que surgiram ao fazer o programa crescer:

```text
1. Dados e comportamentos relacionados estavam separados.

2. Várias partes do programa conheciam detalhes
   de como os dados eram representados.

3. Adicionar novas funcionalidades poderia exigir
   modificar várias partes do sistema.
```

Costuma-se dizer que a orientação a objetos "modela o mundo real".

Essa ideia pode ser útil como intuição inicial, mas não é o principal objetivo.

Nem toda classe precisa representar alguma coisa física. O nosso `Chat`, por exemplo, não é um objeto do mundo real: é uma ideia que escolhemos representar.

O critério mais importante é:

> Essa classe ajuda a organizar o programa, deixando-o mais fácil de entender e modificar?

Tradicionalmente, a orientação a objetos é associada a quatro ideias:

```text
Abstração

Encapsulamento

Herança

Polimorfismo
```

Nesta aula não vamos estudá-las em profundidade.

O objetivo é apenas entender **qual pergunta está associada a cada uma delas**.



### 5.2 Abstração

> Quais informações e operações realmente importam para o problema que queremos resolver?

Ao criar a classe `Mensagem`, decidimos representar:

```text
nome
texto
data_envio
lida
favorita
```

Poderíamos representar muitas outras informações, mas nem todas são relevantes para o nosso problema.

Em um sistema de correios, por exemplo, uma "mensagem" (uma carta) seria representada de forma bem diferente: teria endereço, peso e tipo de envio.

A escolha depende do problema que queremos resolver. Essa questão está relacionada à **abstração**.

Na próxima aula, estudaremos essa ideia com mais detalhes.



### 5.3 Encapsulamento

Considere:

```python
produto.preco = -100

print(produto.preco)
```

Saída:

```text
-100
```

Nada impede que qualquer parte do programa coloque o objeto em um estado inválido.

Isso gera a pergunta:

> Como controlar a maneira pela qual o estado de um objeto pode ser acessado e modificado?

Essa questão está relacionada ao **encapsulamento**.

Voltaremos a esse problema em uma aula posterior.



### 5.4 Herança

Considere diferentes tipos de mensagem:

```text
Mensagem
├── MensagemTexto
├── MensagemImagem
└── MensagemAudio
```

Esses tipos possuem várias características em comum (nome, data de envio, estado de lida e favorita), mas também características específicas (texto, arquivo, duração).

Uma possibilidade seria copiar a classe `Mensagem` para cada tipo. Mas então qualquer correção feita em uma das cópias precisaria ser repetida nas outras.

Isso gera a pergunta:

> Como representar tipos relacionados que compartilham características?

Essa questão está relacionada à **herança**.



### 5.5 Polimorfismo

Lembre-se do `if/elif` que crescia a cada novo tipo de mensagem na Aula 21:

```python
def exibir_mensagem(mensagem):

    if mensagem["tipo"] == "texto":
        ...

    elif mensagem["tipo"] == "imagem":
        ...

    elif mensagem["tipo"] == "audio":
        ...
```

Agora observe o método `exibir` da nossa classe `Chat`:

```python
for mensagem in chat.historico:
    mensagem.exibir()
```

Imagine que o histórico contenha:

```text
MensagemTexto
MensagemImagem
MensagemAudio
```

Todos esses objetos podem responder à mesma operação:

```python
exibir()
```

mas cada um pode executá-la de maneira diferente. Quem chama o método não precisa verificar o tipo da mensagem.

Isso gera a pergunta:

> Como utilizar objetos diferentes através das mesmas operações?

Essa questão está relacionada ao **polimorfismo**.



### 5.6 Mapa das próximas aulas

Podemos fechar o ciclo aberto no início da seção, associando cada questão observada na aula anterior a uma ideia:

```text
Dados e comportamentos separados
→ classes (o que vimos hoje)

Detalhes internos expostos
→ encapsulamento

Mudanças espalhadas pelo programa
→ herança e polimorfismo
```

E resumir os pilares pelas perguntas que cada um responde:

```text
Abstração
→ O que é relevante representar?


Encapsulamento
→ Como controlar o estado?


Herança
→ Como representar e especializar tipos relacionados?


Polimorfismo
→ Como utilizar objetos diferentes
  através das mesmas operações?
```

Esses pilares não são regras independentes. Em programas reais, eles aparecem **juntos**.



## 6. Exercícios

### 6.1 Prevendo a saída

Sem executar o código, diga o que será impresso:

```python
class Contador:

    def __init__(self):
        self.valor = 0

    def incrementar(self):
        self.valor += 1


a = Contador()
b = Contador()
c = a

a.incrementar()
a.incrementar()

b.incrementar()

c.incrementar()

print(a.valor)
print(b.valor)
print(c.valor)

print(a is c)
print(a is b)
```

Depois, execute o código e compare com sua previsão.

**Para pensar:**

1. Quantos objetos `Contador` foram criados?
2. Por que `a.valor` e `c.valor` possuem o mesmo valor?
3. Quando `c.incrementar()` é executado, qual objeto `self` representa?



### 6.2 Contas bancárias

Crie uma classe `Conta` com os atributos:

- `titular`;
- `saldo`, inicialmente com o valor informado na criação da conta.

A classe deve possuir os métodos:

- `depositar(valor)`, que adiciona o valor ao saldo;
- `sacar(valor)`, que reduz o saldo;
- `transferir(destino, valor)`, que transfere um valor para outra conta.

Exemplo:

```python
c1 = Conta("Ana", 1000)
c2 = Conta("Bruno", 500)

c1.transferir(c2, 200)

print(c1.saldo)
print(c2.saldo)
```

Saída esperada:

```text
800
700
```

**Dicas:**

- Um método pode chamar outros métodos do mesmo objeto, utilizando `self`. Por exemplo, `self.sacar(valor)`.
- Por enquanto, você pode ignorar o caso de saldo insuficiente.

**Desafio extra:** faça `sacar()` gerar um `ValueError` caso o saldo seja insuficiente. O que acontece com `transferir()` nesse caso?

**Para pensar:**

1. No método `c1.transferir(c2, 200)`, quem é `self` e quem é `destino`?
2. Quantos objetos `Conta` existem nesse exemplo?
3. Por que alterar o saldo de `c2` dentro do método `transferir()` altera a própria conta representada por `c2`?
