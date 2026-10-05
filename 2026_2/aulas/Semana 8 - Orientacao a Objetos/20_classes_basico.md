# Aula 21: Introdução à Programação Orientada a Objetos

## 1. De onde estamos partindo?

Até agora, utilizamos Python principalmente de forma **procedural**.

Organizamos nossos programas utilizando:

- variáveis;
- listas, tuplas e dicionários;
- funções;
- módulos;
- tratamento de erros;
- testes.

Em geral, temos **dados** armazenados em alguma estrutura e **funções** que operam sobre esses dados.

Por exemplo:

```python
produto = {
    "nome": "Livro",
    "preco": 50.0
}


def aplicar_desconto(produto, percentual):
    produto["preco"] *= 1 - percentual / 100
```

Nesse caso:

- os dados do produto estão armazenados em um dicionário;
- a função `aplicar_desconto` recebe esses dados e realiza uma operação.

Essa abordagem é perfeitamente adequada para muitos programas.

Entretanto, conforme um sistema cresce, podemos começar a ter cada vez mais dados e comportamentos relacionados entre si.

Nesta aula, vamos partir de um exemplo procedural e observar uma outra forma de organizar um programa.



## 2. Um sistema de mensagens

Imagine que queremos desenvolver uma pequena aplicação de chat.

Inicialmente, cada mensagem possui:

- o nome do remetente;
- o texto;
- a data de envio.

Como poderíamos representar uma mensagem utilizando apenas os recursos que já conhecemos?

### 2.1 Representando mensagens com dicionários

Uma possibilidade é utilizar um dicionário:

```python
m1 = {
    "nome": "Matheus",
    "texto": "Olá!",
    "data_envio": "2026-10-05T08:00"
}

m2 = {
    "nome": "João",
    "texto": "Bom dia!",
    "data_envio": "2026-10-05T09:00"
}
```

Podemos representar o histórico do chat utilizando uma lista:

```python
chat = [m1, m2]
```

E criar uma função para exibir uma mensagem:

```python
def exibir_mensagem(mensagem):
    print(
        f"{mensagem['nome']} "
        f"{mensagem['data_envio']}: "
        f"{mensagem['texto']}"
    )
```

Então:

```python
def exibir_chat(chat):
    for mensagem in chat:
        exibir_mensagem(mensagem)
```

Utilizando:

```python
exibir_chat(chat)
```

teríamos:

```text
Matheus 2026-10-05T08:00: Olá!
João 2026-10-05T09:00: Bom dia!
```

Nosso programa funciona.

Não existe nenhum problema fundamental com essa solução.



## 3. O programa começa a crescer

Com o tempo, nosso aplicativo passa a possuir mais funcionalidades.

### 3.1 Novas informações

Talvez agora queiramos saber:

- se uma mensagem já foi lida;
- se uma mensagem foi favoritada.

Podemos simplesmente adicionar novos dados:

```python
m1 = {
    "nome": "Matheus",
    "texto": "Olá!",
    "data_envio": "2026-10-05T08:00",
    "lida": False,
    "favorita": False
}
```

Isso continua funcionando.

Mas agora uma mensagem possui um pouco mais de informação.

Podemos dizer que essas informações descrevem o **estado** atual da mensagem.

Por exemplo:

```text
lida = False
favorita = False
```

indica que a mensagem ainda não foi lida nem favoritada.



### 3.2 Novas operações

Também podemos criar operações relacionadas às mensagens.

Por exemplo:

```python
def marcar_como_lida(mensagem):
    mensagem["lida"] = True
```

e:

```python
def favoritar_mensagem(mensagem):
    mensagem["favorita"] = True
```

Podemos fazer:

```python
marcar_como_lida(m1)
favoritar_mensagem(m1)
```

Depois dessas operações:

```python
print(m1["lida"])
print(m1["favorita"])
```

teríamos:

```text
True
True
```

Observe que algumas operações apenas consultam os dados:

```python
exibir_mensagem(m1)
```

enquanto outras podem modificar o estado da mensagem:

```python
favoritar_mensagem(m1)
marcar_como_lida(m1)
```

Aos poucos, começamos a ter várias operações relacionadas ao mesmo conceito:

```text
mensagem

    exibir_mensagem()
    favoritar_mensagem()
    marcar_como_lida()
```



### 3.3 Diferentes tipos de mensagem

Nosso aplicativo continua crescendo.

Agora queremos aceitar:

- mensagens de texto;
- mensagens de imagem.

Podemos continuar utilizando dicionários.

Uma mensagem de texto:

```python
m1 = {
    "tipo": "texto",
    "nome": "Matheus",
    "texto": "Olá!",
    "data_envio": "2026-10-05T08:00",
    "lida": False,
    "favorita": False
}
```

Uma mensagem de imagem:

```python
m2 = {
    "tipo": "imagem",
    "nome": "João",
    "arquivo": "foto.png",
    "data_envio": "2026-10-05T09:00",
    "lida": False,
    "favorita": False
}
```

Agora a forma de exibir uma mensagem depende de seu tipo.

```python
def exibir_mensagem(mensagem):

    if mensagem["tipo"] == "texto":
        print(
            f"{mensagem['nome']} "
            f"{mensagem['data_envio']}: "
            f"{mensagem['texto']}"
        )

    elif mensagem["tipo"] == "imagem":
        print(
            f"{mensagem['nome']} "
            f"{mensagem['data_envio']}: "
            f"[imagem: {mensagem['arquivo']}]"
        )
```

Ainda funciona.



### 3.4 E se adicionarmos novos tipos?

Imagine que nosso aplicativo passe a aceitar:

```text
texto
imagem
áudio
vídeo
localização
arquivo
```

Nossa função poderia começar a crescer:

```python
def exibir_mensagem(mensagem):

    if mensagem["tipo"] == "texto":
        ...

    elif mensagem["tipo"] == "imagem":
        ...

    elif mensagem["tipo"] == "audio":
        ...

    elif mensagem["tipo"] == "video":
        ...

    elif mensagem["tipo"] == "localizacao":
        ...

    elif mensagem["tipo"] == "arquivo":
        ...
```

Talvez outras operações também dependam do tipo da mensagem.

Por exemplo, imagine que queremos gerar uma pequena prévia:

```python
def gerar_preview(mensagem):

    if mensagem["tipo"] == "texto":
        return mensagem["texto"][:30]

    elif mensagem["tipo"] == "imagem":
        return f"[imagem: {mensagem['arquivo']}]"

    elif mensagem["tipo"] == "audio":
        return f"[áudio: {mensagem['duracao']} segundos]"
```

Nosso programa continua funcionando.

Mas começam a surgir algumas questões sobre sua organização.



## 4. O que começou a acontecer?

Vamos observar o programa antes de modificar nossa solução.

### 4.1 Dados e comportamentos relacionados estão separados

Os dados de uma mensagem estão em um dicionário:

```python
mensagem = {
    "nome": "Matheus",
    "texto": "Olá!",
    "lida": False,
    "favorita": False
}
```

Enquanto operações relacionadas à mensagem estão definidas em outros lugares:

```python
def exibir_mensagem(mensagem):
    ...


def favoritar_mensagem(mensagem):
    ...


def marcar_como_lida(mensagem):
    ...
```

Podemos visualizar aproximadamente:

```text
DADOS                         COMPORTAMENTOS

mensagem  ----------------->  exibir_mensagem()
          ----------------->  favoritar_mensagem()
          ----------------->  marcar_como_lida()
```

Essas operações possuem algo em comum:

> Todas dizem respeito ao conceito de uma mensagem.

Podemos então fazer uma pergunta:

> Seria possível manter informações e comportamentos fortemente relacionados mais próximos?

Essa ideia está relacionada ao conceito de **coesão**.

#### Coesão

Coesão está relacionada ao quanto uma parte do programa possui uma responsabilidade clara e bem definida.

Em geral, elementos fortemente relacionados tendem a ser mais fáceis de entender quando estão organizados próximos uns dos outros.



### 4.2 Várias partes conhecem a estrutura interna dos dados

Observe:

```python
def exibir_mensagem(mensagem):
    print(mensagem["texto"])
```

Outra função também pode acessar:

```python
def gerar_preview(mensagem):
    return mensagem["texto"][:30]
```

E outra:

```python
def possui_link(mensagem):
    return "http" in mensagem["texto"]
```

Todas essas funções precisam saber que o texto da mensagem está armazenado em:

```python
mensagem["texto"]
```

Para imagens, algumas funções precisam saber que existe:

```python
mensagem["arquivo"]
```

Podemos perguntar:

> Quantas partes do programa precisam conhecer exatamente como uma mensagem está representada?

Se a representação dos dados mudar, talvez várias partes do programa também precisem mudar.

Essa dependência entre partes do programa está relacionada ao conceito de **acoplamento**.

#### Acoplamento

Acoplamento está relacionado ao quanto uma parte do programa depende de detalhes de outra parte.

Quanto maior o número de partes que precisam conhecer os detalhes internos de uma estrutura, maior pode ser a dependência entre elas.



### 4.3 E quando queremos adicionar novas funcionalidades?

Imagine que amanhã adicionaremos:

```text
mensagem de áudio
```

Talvez precisemos modificar:

```python
exibir_mensagem()
gerar_preview()
```

Depois adicionamos:

```text
mensagem de vídeo
```

e novamente modificamos várias partes do programa.

Podemos então perguntar:

> Quão fácil é adicionar uma nova funcionalidade sem modificar várias partes do sistema?

Essa característica está relacionada à **extensibilidade**.

Por enquanto, não precisamos memorizar definições formais.

Queremos apenas perceber três questões:

```text
1. Existem dados e comportamentos fortemente relacionados.

2. Várias partes conhecem detalhes da representação dos dados.

3. Conforme o sistema cresce, mudanças podem se espalhar pelo programa.
```



## 5. Uma outra forma de organizar o programa

Até agora temos algo aproximadamente assim:

```text
DADOS                         COMPORTAMENTOS

mensagem  ----------------->  exibir_mensagem()
          ----------------->  favoritar_mensagem()
          ----------------->  marcar_como_lida()
```

Podemos fazer uma pergunta diferente:

> E se organizássemos juntos os dados de uma mensagem e os comportamentos relacionados a ela?

Por exemplo:

```text
Mensagem
├── dados
│   ├── nome
│   ├── texto
│   ├── data_envio
│   ├── lida
│   └── favorita
│
└── comportamentos
    ├── exibir()
    ├── favoritar()
    └── marcar_como_lida()
```

Essa é uma das ideias importantes da **Programação Orientada a Objetos**.

Em vez de organizar o programa apenas como funções que recebem estruturas de dados, podemos representar conceitos utilizando estruturas chamadas **classes**.



## 6. Classes

Uma **classe** define uma estrutura utilizada para criar objetos.

Podemos criar uma classe para representar uma mensagem:

```python
class Mensagem:

    def __init__(self, nome, texto, data_envio):
        self.nome = nome
        self.texto = texto
        self.data_envio = data_envio
        self.lida = False
        self.favorita = False
```

A classe `Mensagem` representa o conceito de uma mensagem no nosso programa.

Ela define que uma mensagem possui:

```text
nome
texto
data_envio
lida
favorita
```

Neste momento, entretanto, ainda não criamos nenhuma mensagem específica.



## 7. Objetos

A partir da classe `Mensagem`, podemos criar mensagens concretas.

```python
m1 = Mensagem(
    "Matheus",
    "Olá!",
    "2026-10-05T08:00"
)
```

E:

```python
m2 = Mensagem(
    "João",
    "Bom dia!",
    "2026-10-05T09:00"
)
```

`m1` e `m2` são dois objetos diferentes.

Ambos foram criados a partir da mesma classe:

```text
Mensagem
```

Dizemos que `m1` e `m2` são **instâncias** da classe `Mensagem`.

Podemos representar:

```text
             Mensagem
                |
          +-----+-----+
          |           |
         m1          m2
```

Ou:

```text
Mensagem → classe

m1       → objeto / instância
m2       → objeto / instância
```



## 8. Atributos

As informações associadas a um objeto são chamadas de **atributos**.

Na nossa classe:

```python
class Mensagem:

    def __init__(self, nome, texto, data_envio):
        self.nome = nome
        self.texto = texto
        self.data_envio = data_envio
        self.lida = False
        self.favorita = False
```

temos os atributos:

```text
nome
texto
data_envio
lida
favorita
```

Podemos acessar os atributos utilizando a notação de ponto:

```python
print(m1.nome)
print(m1.texto)

print(m2.nome)
print(m2.texto)
```

Saída:

```text
Matheus
Olá!
João
Bom dia!
```

Observe que:

```python
m1.nome
```

e:

```python
m2.nome
```

podem possuir valores diferentes.

Os dois objetos foram criados pela mesma classe, mas cada objeto possui seus próprios dados.

Também podemos observar:

```python
print(m1.favorita)
print(m2.favorita)
```

Saída:

```text
False
False
```

Cada objeto possui seu próprio estado.



## 9. Métodos

Objetos também podem possuir comportamentos.

Esses comportamentos são definidos através de **métodos**.

Podemos fazer com que uma mensagem saiba como se exibir:

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
```

Agora podemos escrever:

```python
m1.exibir()
m2.exibir()
```

Em vez de:

```python
exibir_mensagem(m1)
exibir_mensagem(m2)
```



### 9.1 Métodos que modificam o objeto

Também podemos criar:

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
```

Podemos observar o estado inicial:

```python
print(m1.favorita)
print(m1.lida)
```

Saída:

```text
False
False
```

Agora fazemos:

```python
m1.favoritar()
m1.marcar_como_lida()
```

E novamente:

```python
print(m1.favorita)
print(m1.lida)
```

Saída:

```text
True
True
```

Um método pode, portanto, operar utilizando os dados de um objeto e também modificar seu estado.



## 10. O que mudou?

Antes tínhamos:

```python
exibir_mensagem(m1)
favoritar_mensagem(m1)
marcar_como_lida(m1)
```

Agora temos:

```python
m1.exibir()
m1.favoritar()
m1.marcar_como_lida()
```

Na primeira versão, tínhamos aproximadamente:

```text
mensagem
   +
funções externas
```

Na segunda:

```text
Mensagem
├── atributos
│   ├── nome
│   ├── texto
│   ├── data_envio
│   ├── lida
│   └── favorita
│
└── métodos
    ├── exibir()
    ├── favoritar()
    └── marcar_como_lida()
```

Dados e comportamentos relacionados ao conceito de mensagem passaram a estar organizados juntos.

Isso não significa que todo programa deva ser orientado a objetos.

Também não significa que utilizar funções e dicionários esteja errado.

Estamos estudando uma **outra forma de organizar programas**.



## 11. O parâmetro `self`

Observe novamente:

```python
def favoritar(self):
    self.favorita = True
```

O parâmetro `self` representa o **objeto sobre o qual o método está sendo executado**.

Quando fazemos:

```python
m1.favoritar()
```

dentro do método:

```python
self
```

se refere ao objeto:

```python
m1
```

Portanto:

```python
self.favorita = True
```

modifica:

```python
m1.favorita
```

Agora considere:

```python
m2.favoritar()
```

Nesse caso, durante a execução do método:

```python
self
```

representa:

```python
m2
```

Por isso, o mesmo método pode operar sobre objetos diferentes.

Podemos visualizar:

```text
m1.favoritar()
      ↓
self = m1


m2.favoritar()
      ↓
self = m2
```

Por enquanto, basta entender:

> `self` permite que um método acesse os dados do objeto sobre o qual está operando.

Voltaremos a esse conceito com mais detalhes nas próximas aulas.



## 12. Objetos diferentes possuem estados diferentes

Considere:

```python
m1 = Mensagem(
    "Matheus",
    "Olá!",
    "2026-10-05T08:00"
)

m2 = Mensagem(
    "João",
    "Bom dia!",
    "2026-10-05T09:00"
)
```

Inicialmente:

```python
print(m1.favorita)
print(m2.favorita)
```

temos:

```text
False
False
```

Agora:

```python
m1.favoritar()
```

Se verificarmos novamente:

```python
print(m1.favorita)
print(m2.favorita)
```

temos:

```text
True
False
```

Por quê?

Porque `m1` e `m2` são objetos diferentes.

Eles foram criados a partir da mesma classe, mas possuem estados independentes.



## 13. Representando o próprio chat

Também podemos representar o chat através de uma classe.

Um chat possui um conjunto de mensagens.

```python
class Chat:

    def __init__(self):
        self.historico = []

    def adicionar(self, mensagem):
        self.historico.append(mensagem)

    def exibir(self):
        for mensagem in self.historico:
            mensagem.exibir()
```

Agora podemos utilizar:

```python
m1 = Mensagem(
    "Matheus",
    "Olá!",
    "2026-10-05T08:00"
)

m2 = Mensagem(
    "João",
    "Bom dia!",
    "2026-10-05T09:00"
)

chat = Chat()

chat.adicionar(m1)
chat.adicionar(m2)

chat.exibir()
```

Temos agora dois conceitos representados no programa:

```text
Mensagem
Chat
```

Cada classe possui uma responsabilidade diferente.

`Mensagem` representa uma mensagem.

`Chat` organiza um conjunto de mensagens.

Podemos visualizar:

```text
Chat
 |
 +-- Mensagem
 |
 +-- Mensagem
 |
 +-- Mensagem
```

Um objeto também pode utilizar outros objetos.

Exploraremos esse tipo de relação com mais detalhes posteriormente.



## 14. Procedural × Orientado a Objetos

Compare as duas abordagens.

### Abordagem procedural

```python
mensagem = {
    "nome": "Matheus",
    "texto": "Olá!",
    "favorita": False
}


def exibir_mensagem(mensagem):
    print(mensagem["texto"])


def favoritar_mensagem(mensagem):
    mensagem["favorita"] = True


exibir_mensagem(mensagem)
favoritar_mensagem(mensagem)
```

Temos:

```text
dados          → dicionário

comportamentos → funções
```



### Abordagem orientada a objetos

```python
class Mensagem:

    def __init__(self, nome, texto):
        self.nome = nome
        self.texto = texto
        self.favorita = False

    def exibir(self):
        print(self.texto)

    def favoritar(self):
        self.favorita = True


mensagem = Mensagem("Matheus", "Olá!")

mensagem.exibir()
mensagem.favoritar()
```

Temos:

```text
Mensagem
├── atributos
│   ├── nome
│   ├── texto
│   └── favorita
│
└── métodos
    ├── exibir()
    └── favoritar()
```

Como podemos notar a diferença principal está na forma como organizamos as responsabilidades do programa.



## 15. Exercícios

### 15.1 Produto

Crie uma classe `Produto` com os atributos:

- `nome`
- `preco`

A classe deve possuir os métodos:

- `exibir()`: exibe o nome e o preço do produto;
- `aplicar_desconto(percentual)`: reduz o preço pelo percentual informado.

Exemplo:

```python
produto = Produto("Livro", 50.0)

produto.exibir()
produto.aplicar_desconto(10)
produto.exibir()
```

Saída esperada:

```text id="7tfmyr"
Livro - R$ 50.00
Livro - R$ 45.00
```

### 15.2 Carrinho de compras

Crie uma classe `Carrinho` que:

- armazene uma lista de produtos;
- possua um método `adicionar(produto)`;
- possua um método `total()`, que retorna a soma dos preços dos produtos.

Exemplo:

```python
livro = Produto("Livro", 50.0)
caneta = Produto("Caneta", 5.0)

carrinho = Carrinho()

carrinho.adicionar(livro)
carrinho.adicionar(caneta)

print(carrinho.total())
```

Saída esperada:

```text id="l0z68o"
55.0
```

**Para pensar:**

- O que está armazenado em `self.produtos`?
- Quem deve ser responsável por calcular o total: `Produto` ou `Carrinho`?
- Se o preço de um produto mudar, o valor retornado por `total()` também muda?
