# Aula 26: Herança

## 1. O problema: classes quase iguais

### 1.1 Copiar e colar

Nosso aplicativo de chat agora precisa aceitar dois tipos de mensagem: de **texto** e de **imagem**.

Uma primeira ideia é criar uma classe para cada tipo, copiando a que já temos:

```python
class MensagemTexto:

    def __init__(self, nome, data_envio, texto):
        self.nome = nome
        self.data_envio = data_envio
        self.texto = texto
        self.lida = False
        self.favorita = False

    def favoritar(self):
        self.favorita = True

    def marcar_como_lida(self):
        self.lida = True

    def exibir(self):
        print(f"{self.nome} {self.data_envio}: {self.texto}")


class MensagemImagem:

    def __init__(self, nome, data_envio, arquivo):
        self.nome = nome
        self.data_envio = data_envio
        self.arquivo = arquivo
        self.lida = False
        self.favorita = False

    def favoritar(self):
        self.favorita = True

    def marcar_como_lida(self):
        self.lida = True

    def exibir(self):
        print(f"{self.nome} {self.data_envio}: [imagem: {self.arquivo}]")
```

Funciona. Mas observe o que está **repetido**:

```text
nome, data_envio, lida, favorita      →  iguais nas duas classes

favoritar(), marcar_como_lida()       →  idênticos

exibir(), texto e arquivo             →  as únicas partes diferentes
```

Agora imagine que chegam os tipos **áudio**, **vídeo** e **localização**. Seriam cinco cópias. E se descobrirmos um erro em `favoritar()`, precisamos corrigi-lo em **todas** as classes. Se esquecermos uma, o sistema passa a se comportar de formas diferentes dependendo do tipo da mensagem.



### 1.2 A alternativa que já conhecemos

Na aula de introdução à orientação a objetos, partimos de algo parecido com um dicionário e um `if/elif`:

```python
def exibir_mensagem(mensagem):

    if mensagem["tipo"] == "texto":
        ...

    elif mensagem["tipo"] == "imagem":
        ...

    elif mensagem["tipo"] == "audio":
        ...
```

Aquela solução também não escala: cada tipo novo exige modificar a função.

Gostaríamos de uma forma de dizer:

> Uma mensagem de texto **é uma** mensagem. Uma mensagem de imagem **é uma** mensagem. O que elas têm em comum fica em um lugar só. Cada uma acrescenta apenas o que é diferente.

É exatamente isso que a **herança** permite.



## 2. Herança em Python

### 2.1 A classe base

Primeiro, colocamos em uma classe o que é comum a todas as mensagens:

```python
class Mensagem:

    def __init__(self, nome, data_envio):
        self.nome = nome
        self.data_envio = data_envio
        self.lida = False
        self.favorita = False

    def favoritar(self):
        self.favorita = True

    def marcar_como_lida(self):
        self.lida = True

    def exibir(self):
        print(f"{self.nome} {self.data_envio}")
```

Essa é a **classe base** (também chamada de superclasse ou classe pai).



### 2.2 A classe derivada

Para criar uma classe que **herda** de outra, colocamos o nome da classe base entre parênteses:

```python
class MensagemTexto(Mensagem):
    pass
```

Essa classe não tem nenhum código próprio, mas já funciona como uma `Mensagem`:

```python
m = MensagemTexto("Matheus", "2026-10-05T08:00")

m.favoritar()

print(m.favorita)
m.exibir()
```

Saída:

```text
True
Matheus 2026-10-05T08:00
```

`MensagemTexto` **herdou** o `__init__`, o `favoritar()` e o `exibir()` de `Mensagem`, sem escrever nada.

Vocabulário:

```text
Mensagem          →  classe base  /  superclasse  /  classe pai

MensagemTexto     →  classe derivada  /  subclasse  /  classe filha
```

Podemos representar:

```text
        Mensagem
   (nome, data_envio, lida, favorita
    favoritar(), marcar_como_lida(), exibir())
            ▲
            │  herda de
            │
      MensagemTexto
```



### 2.3 Acrescentando o que é específico

Uma mensagem de texto precisa de um atributo a mais: o `texto`. Então precisamos de um `__init__` próprio:

```python
class MensagemTexto(Mensagem):

    def __init__(self, nome, data_envio, texto):
        self.texto = texto
```

Mas observe o que acontece:

```python
m = MensagemTexto("Matheus", "2026-10-05T08:00", "Olá!")

m.exibir()
```

Saída:

```text
AttributeError: 'MensagemTexto' object has no attribute 'nome'
```

Ao definir um `__init__` na subclasse, ele **substitui** o da classe base. Então os atributos `nome`, `data_envio`, `lida` e `favorita` nunca foram criados.

**E se atribuíssemos, na própria subclasse, os atributos que a classe base exige?**

```python
class MensagemTexto(Mensagem):

    def __init__(self, nome, data_envio, texto):
        self.nome = nome
        self.data_envio = data_envio
        self.lida = False
        self.favorita = False
        self.texto = texto
```

Isso **funciona**: `m.exibir()` e `m.favoritar()` voltam a funcionar normalmente.

Mas observe o que fizemos: copiamos para a subclasse as linhas do `__init__` da classe base. Voltamos ao problema da seção 1:

```text
- A subclasse passa a conhecer os detalhes internos da classe base
  (acoplamento).

- Se a classe base ganhar um atributo novo (por exemplo, "editada"),
  todas as subclasses precisam ser atualizadas.

- Se esquecermos um atributo em uma das subclasses,
  o erro só aparece mais tarde, em outro lugar.
```

A forma correta é pedir à classe base que faça a parte dela, usando `super()`:

```python
class MensagemTexto(Mensagem):

    def __init__(self, nome, data_envio, texto):
        super().__init__(nome, data_envio)
        self.texto = texto
```

```text
super()              →  "a classe base, vista a partir daqui"

super().__init__()   →  executa o __init__ da classe base
                        para preparar os atributos herdados
```

**O que o `super()` dá acesso?** Aos **métodos** definidos na classe base, como `super().__init__()` e `super().exibir()`.

Os **atributos de um objeto** (`nome`, `data_envio`...) **não** ficam na classe base: ficam no próprio objeto, e continuam sendo acessados com `self`. Por isso, `super().nome` não funciona:

```python
class MensagemTexto(Mensagem):

    def mostrar_nome(self):
        return super().nome
```

produz:

```text
AttributeError: 'super' object has no attribute 'nome'
```

O correto é `self.nome`, que o objeto já possui desde o `super().__init__()`.

Fazemos o mesmo com a mensagem de imagem:

```python
class MensagemImagem(Mensagem):

    def __init__(self, nome, data_envio, arquivo):
        super().__init__(nome, data_envio)
        self.arquivo = arquivo
```

Agora, cada objeto possui os atributos comuns e os específicos:

```python
m1 = MensagemTexto("Matheus", "2026-10-05T08:00", "Olá!")

print(m1.__dict__)
```

Saída:

```text
{'nome': 'Matheus', 'data_envio': '2026-10-05T08:00', 'lida': False, 'favorita': False, 'texto': 'Olá!'}
```

E os métodos herdados continuam funcionando, sem terem sido reescritos:

```python
m1.favoritar()

print(m1.favorita)
```

Saída:

```text
True
```

Se corrigirmos um erro em `favoritar()`, a correção vale para **todos** os tipos de mensagem de uma vez. Esse era o problema da seção 1.



### 2.4 Sobrescrevendo métodos

O método `exibir()` herdado mostra apenas o nome e a data. Cada tipo de mensagem precisa mostrar também o seu conteúdo.

Uma subclasse pode **sobrescrever** (*override*) um método, escrevendo uma versão própria com o mesmo nome:

```python
class MensagemTexto(Mensagem):

    def __init__(self, nome, data_envio, texto):
        super().__init__(nome, data_envio)
        self.texto = texto

    def exibir(self):
        super().exibir()
        print(f"  {self.texto}")
```

Observe que `super().exibir()` chama a versão da classe base, e depois acrescentamos o que é específico. Assim **reaproveitamos** o que já existe em vez de reescrevê-lo.

O mesmo para a imagem:

```python
class MensagemImagem(Mensagem):

    def __init__(self, nome, data_envio, arquivo):
        super().__init__(nome, data_envio)
        self.arquivo = arquivo

    def exibir(self):
        super().exibir()
        print(f"  [imagem: {self.arquivo}]")
```

Testando:

```python
m1 = MensagemTexto("Matheus", "2026-10-05T08:00", "Olá!")
m2 = MensagemImagem("João", "2026-10-05T09:00", "foto.png")

m1.exibir()
m2.exibir()
```

Saída:

```text
Matheus 2026-10-05T08:00
  Olá!
João 2026-10-05T09:00
  [imagem: foto.png]
```

Uma subclasse pode também **substituir** completamente um método, sem chamar o `super()`. Usamos o `super()` quando queremos **acrescentar** algo ao comportamento original.



### 2.5 O `Chat` continua igual (uma prévia do polimorfismo)

Lembra da classe `Chat` da aula de introdução à orientação a objetos?

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

Ela não foi alterada. Mesmo assim, aceita os dois tipos:

```python
chat = Chat()

chat.adicionar(m1)
chat.adicionar(m2)

chat.exibir()
```

Saída:

```text
Matheus 2026-10-05T08:00
  Olá!
João 2026-10-05T09:00
  [imagem: foto.png]
```

O `Chat` chamou `mensagem.exibir()` sem verificar o tipo, e cada mensagem se exibiu do seu jeito. **Nenhum `if/elif` foi necessário.**

O que acabamos de ver **é** o polimorfismo: objetos de classes diferentes respondendo à mesma chamada (`exibir()`), cada um do seu jeito. A herança é uma das formas de torná-lo possível.

Hoje, o objetivo é apenas perceber que isso acontece. Na próxima aula, vamos estudar o polimorfismo com mais calma, incluindo situações em que ele funciona **sem** herança.



### 2.6 Um parêntese: as exceções customizadas

Na primeira parte da disciplina, criamos exceções customizadas, algo como:

```python
class SaldoInsuficienteError(Exception):

    def __init__(self, saldo, valor):
        super().__init__(f"saldo de {saldo} insuficiente para sacar {valor}")
        self.saldo = saldo
        self.valor = valor
```

Aquilo já era **herança**, e agora podemos entender cada peça:

```text
class SaldoInsuficienteError(Exception)
    →  nossa classe é uma subclasse de Exception

super().__init__(mensagem)
    →  executa o __init__ da classe base,
       que guarda a mensagem do erro

self.saldo, self.valor
    →  atributos específicos da nossa subclasse
```

`Exception` é a classe base de praticamente todos os erros do Python. Por isso, nossa exceção **é uma** `Exception`, e um `except Exception` a captura:

```python
try:
    raise SaldoInsuficienteError(100, 150)
except Exception as erro:
    print(erro)
    print(isinstance(erro, Exception))
    print(erro.saldo)
```

Saída:

```text
saldo de 100 insuficiente para sacar 150
True
100
```

O mesmo vale para as exceções que já existem. Se criarmos um erro como subclasse de `ValueError`, um `except ValueError` também o captura:

```python
class ValorInvalidoError(ValueError):
    pass


try:
    raise ValorInvalidoError("valor negativo")
except ValueError as erro:
    print("capturado como ValueError:", erro)
```

Saída:

```text
capturado como ValueError: valor negativo
```

Ou seja, a ordem dos `except` e a possibilidade de capturar "famílias" de erros são consequências da herança.



## 3. Como o Python encontra os métodos?

### 3.1 Atributos no objeto, métodos nas classes

Considere:

```python
m1 = MensagemTexto("Matheus", "2026-10-05T08:00", "Olá!")
```

Os **atributos** ficam no próprio objeto:

```python
print(m1.__dict__)
```

Saída:

```text
{'nome': 'Matheus', 'data_envio': '2026-10-05T08:00', 'lida': False, 'favorita': False, 'texto': 'Olá!'}
```

Os **métodos** ficam nas classes, e cada classe guarda os seus:

```python
print("favoritar" in MensagemTexto.__dict__)
print("favoritar" in Mensagem.__dict__)
print("exibir" in MensagemTexto.__dict__)
print("exibir" in Mensagem.__dict__)
```

Saída:

```text
False
True
True
True
```

Então:

```text
favoritar()   →  definido só em Mensagem

exibir()      →  definido em Mensagem e também em MensagemTexto
                 (a subclasse sobrescreveu)
```

```text
m1 (objeto)               MensagemTexto             Mensagem
───────────────           ─────────────             ────────
nome                      __init__()                __init__()
data_envio                exibir()                  exibir()
lida                                                favoritar()
favorita                                            marcar_como_lida()
texto
```



### 3.2 A busca, passo a passo

Quando escrevemos `m1.alguma_coisa()`, o Python procura **de baixo para cima**, e **para no primeiro lugar em que encontrar**:

```text
1. no próprio objeto (m1)

2. na classe do objeto (MensagemTexto)

3. na classe base (Mensagem)

4. se não encontrou em lugar nenhum: AttributeError
```

Vamos acompanhar três chamadas.

**`m1.favoritar()`**

```text
procura em m1             →  não encontra
procura em MensagemTexto  →  não encontra
procura em Mensagem       →  encontrou! executa
```

**`m1.exibir()`**

```text
procura em m1             →  não encontra
procura em MensagemTexto  →  encontrou! executa e PARA
                             (a versão de Mensagem nem é consultada)
```

É assim que a sobrescrita funciona: a versão da subclasse é encontrada primeiro e "esconde" a da classe base.

**`m1.voar()`**

```text
procura em m1             →  não encontra
procura em MensagemTexto  →  não encontra
procura em Mensagem       →  não encontra
```

Nenhum lugar tem esse método, e o Python gera um erro:

```text
AttributeError: 'MensagemTexto' object has no attribute 'voar'
```

Esse é o mesmo erro que vimos quando esquecemos o `super().__init__()`: o Python procurou `nome` e não o encontrou.



### 3.3 E o `super()`?

O `super()` muda o ponto de partida da busca: em vez de começar pela classe do objeto, ele começa **pela classe base**.

```text
self.exibir()    →  busca começando em MensagemTexto

super().exibir() →  busca começando em Mensagem
```

É por isso que `super().exibir()` executa a versão da classe base, mesmo quando a subclasse tem uma versão própria.



### 3.4 `isinstance` e `issubclass`

Podemos perguntar de que classe um objeto é:

```python
print(isinstance(m1, MensagemTexto))
print(isinstance(m1, Mensagem))
print(isinstance(m1, MensagemImagem))
```

Saída:

```text
True
True
False
```

Um objeto de uma subclasse **também é** uma instância da classe base. E podemos comparar as classes entre si:

```python
print(issubclass(MensagemTexto, Mensagem))
print(issubclass(Mensagem, MensagemTexto))
```

Saída:

```text
True
False
```

A relação só vale em um sentido: toda mensagem de texto é uma mensagem, mas nem toda mensagem é de texto.



## 4. Prática: personagens de um jogo

Vamos aplicar a herança em um novo exemplo. Em um jogo, todos os personagens têm nome, vida e ataque, e podem atacar e receber dano. Mas o **jogador** e o **inimigo** têm características próprias.

### 4.1 O enunciado

A classe base `Personagem` já está pronta:

```python
class Personagem:

    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def receber_dano(self, dano):
        self.vida = max(0, self.vida - dano)

    def esta_vivo(self):
        return self.vida > 0

    def atacar(self, alvo):
        print(f"{self.nome} atacou {alvo.nome}!")
        alvo.receber_dano(self.ataque)
```

Crie:

- uma classe `Jogador`, que herda de `Personagem`, com o atributo `pontos` (começa em zero) e o método `ganhar_pontos(pontos)`;
- uma classe `Inimigo`, que herda de `Personagem`, com o atributo `recompensa`.

Depois, simule uma batalha entre um jogador e um inimigo. Quando o inimigo for derrotado, o jogador ganha pontos iguais à recompensa.

**Desafio:** faça o `Jogador` sobrescrever `atacar()`, imprimindo `"Golpe do herói!"` antes de executar o ataque normal.



### 4.2 Uma solução de referência

```python
class Jogador(Personagem):

    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida, ataque)
        self.pontos = 0

    def ganhar_pontos(self, pontos):
        self.pontos += pontos

    def atacar(self, alvo):
        print("Golpe do herói!")
        super().atacar(alvo)


class Inimigo(Personagem):

    def __init__(self, nome, vida, ataque, recompensa):
        super().__init__(nome, vida, ataque)
        self.recompensa = recompensa
```

A batalha:

```python
heroi = Jogador("Aria", 100, 30)
goblin = Inimigo("Goblin", 60, 10, 50)

while heroi.esta_vivo() and goblin.esta_vivo():
    heroi.atacar(goblin)

    if goblin.esta_vivo():
        goblin.atacar(heroi)

if heroi.esta_vivo():
    heroi.ganhar_pontos(goblin.recompensa)
    print(f"{heroi.nome} venceu! Pontos: {heroi.pontos}")
```

Saída:

```text
Golpe do herói!
Aria atacou Goblin!
Goblin atacou Aria!
Golpe do herói!
Aria atacou Goblin!
Aria venceu! Pontos: 50
```

**Para pensar:**

1. Onde está definido o método `esta_vivo()` usado em `heroi.esta_vivo()`?
2. O que aconteceria se o `__init__` de `Jogador` não chamasse `super().__init__()`?
3. No método `heroi.atacar(goblin)`, quem é `self` e quem é `alvo`?



## 5. Quando usar herança, e quando não usar

### 5.1 A regra "é um"

Um bom teste para decidir se a herança faz sentido é perguntar:

> A subclasse **é um** tipo da classe base?

```text
MensagemTexto  é uma  Mensagem        →  faz sentido

Jogador        é um   Personagem      →  faz sentido

Inimigo        é um   Personagem      →  faz sentido
```

E alguns casos em que **não** faz sentido:

```text
Fila  é uma  Lista?        →  em geral, não: uma lista permite inserir e remover
                              em qualquer posição, e uma fila não deveria permitir

Carrinho  é um  Produto?   →  não: o carrinho TEM produtos
```

O último exemplo mostra o outro lado: quando a relação é **"tem um"** (um carrinho *tem* produtos), usamos um objeto dentro de outro, como já fizemos com `Chat` e `Mensagem`. Esse é o tema de uma aula futura (composição).

**E há casos em que a resposta depende do sistema.**

Considere `Fornecedor` e `Usuario`. Será que um fornecedor **é um** usuário?

**Sistema A: um marketplace.** Os fornecedores fazem login, têm e-mail e senha, recebem as mesmas notificações que qualquer usuário e usam as mesmas telas de perfil. Em todos os lugares em que o sistema espera um `Usuario`, poderíamos colocar um `Fornecedor` sem problemas. Aqui, `Fornecedor` herdar de `Usuario` pode fazer sentido.

**Sistema B: um sistema de compras interno.** O fornecedor é apenas um cadastro de empresa (CNPJ, contato, prazo de entrega). Ele **nunca** acessa o sistema. Se herdasse de `Usuario`, receberia `senha`, `login()` e outras coisas que não fazem sentido para ele. Aqui, a herança é uma má ideia.

A palavra "fornecedor" é a mesma nos dois casos, mas a resposta é diferente. Isso acontece porque a regra "é um" **não é uma verdade sobre o mundo real**. É uma afirmação sobre **o nosso sistema**. Lembra da abstração? A resposta depende do problema que estamos resolvendo.

Uma pergunta mais precisa para fazer é:

> Em **todo lugar** em que o programa espera um objeto da classe base, eu aceitaria um objeto da subclasse sem problemas?

Se a resposta for "sim", a herança tende a ser adequada. Se houver lugares em que a subclasse "quebraria" o que se espera da classe base, é um sinal de alerta.



### 5.2 Cuidados

A herança é uma ferramenta poderosa, mas é muito mal usada por quem está começando. Alguns cuidados:

```text
- Reaproveitar código não é motivo suficiente.
  Se o "é um" não vale, a herança provavelmente é a ferramenta errada.

- Subclasses dependem da classe base (acoplamento).
  Uma mudança na classe base pode afetar todas as subclasses.

- Hierarquias muito profundas ficam difíceis de entender.
  Duas ou três camadas costumam ser o suficiente.

- Os atributos "protegidos" (_atributo) continuam acessíveis
  na subclasse. O encapsulamento precisa ser pensado
  também para quem herda.
```



### 5.3 Quando o "tipo" muda

Considere um jogo em que existem os tipos de personagem **Mago**, **Guerreiro** e **Arqueiro**. À primeira vista, parece uma boa hierarquia:

```text
Personagem
├── Mago
├── Guerreiro
└── Arqueiro
```

Mas e se o jogador puder **trocar de classe** durante o jogo? Um objeto criado como `Guerreiro` não pode se transformar em `Mago`. Teríamos que criar um objeto novo e copiar os dados.

Nesse caso, a classe do personagem seria melhor como um **atributo** (`personagem.classe = "Mago"`), e não como uma subclasse.

A pergunta para sempre fazer é:

> Esse "tipo" vai mudar durante a vida do objeto? Se sim, provavelmente não deveria ser herança.



## 6. Exercícios

### 6.1 Catálogo de livros

Crie um sistema de catalogação de livros usando herança.

- **Classe base:** `Livro`, com os atributos `titulo`, `autor` e `ano_publicacao`, e o método `info()`, que **retorna** uma frase com os dados do livro.
- **Classes derivadas:**
  - `LivroFisico`, com o atributo adicional `peso`;
  - `EBook`, com os atributos `formato` e `tamanho`.
- **Sobrescrita:** faça o `EBook` sobrescrever `info()`, acrescentando o formato e o tamanho, e reaproveitando o `info()` da classe base com `super()`.

Exemplo:

```python
ebook = EBook("Dom Casmurro", "Machado de Assis", 1899, "epub", 2)

print(ebook.info())
```

Saída esperada:

```text
Dom Casmurro, de Machado de Assis (1899) | epub, 2 MB
```

**Para pensar:**

1. Quais atributos `EBook` herda de `Livro`? Quais são só dele?
2. O que aconteceria se `EBook` não chamasse `super().__init__()`?



### 6.2 A herança faz sentido aqui?

Para cada situação abaixo, diga se usaria herança e justifique. Use estas três perguntas como guia:

```text
1. A regra "é um" vale NESTE sistema?
   (em todo lugar em que a classe base é usada, a subclasse serviria?)

2. O "tipo" muda enquanto o objeto existe?
   (como no exemplo do Mago e do Guerreiro)

3. A subclasse herdaria algo que não deveria ter?
```

**Situação A: locadora de veículos.**
O sistema registra veículos (placa, ano, valor da diária) e permite alugá-los. Existem carros e motos, que têm características próprias.
Faz sentido `Carro` herdar de `Veiculo`?

**Situação B: biblioteca de estruturas de dados.**
Uma classe `Lista` permite inserir e remover elementos em qualquer posição. Uma `Pilha` só permite empilhar e desempilhar no topo.
Faz sentido `Pilha` herdar de `Lista`?

**Situação C: sistema acadêmico.**
Os alunos se matriculam em disciplinas. Em alguns semestres, certos alunos passam a ser monitores de uma disciplina, e deixam de ser no semestre seguinte.
Faz sentido `Monitor` herdar de `Aluno`?

**Situação D: sistema de RH.**
Uma empresa tem funcionários (nome, matrícula, salário). Gerentes são funcionários que também aprovam férias e acompanham equipes.
Faz sentido `Gerente` herdar de `Funcionario`?
Aqui, a resposta pode não ser apenas "sim" ou "não". Se for o caso, diga **do que ela depende**.

Tente responder antes de ler as respostas.



#### Respostas comentadas

**A. Locadora: sim.**
Um carro **é um** veículo, o tipo não muda e tudo o que o sistema faz com veículos (alugar, devolver, consultar a placa) também serve para carros. É um caso clássico em que a herança funciona bem.

**B. Pilha e Lista: em geral, não.**
Se `Pilha` herdasse de `Lista`, ela receberia o método de inserir em qualquer posição e quebraria a garantia de que só se mexe no topo. Falha a pergunta 3: herdaria algo que não deveria ter. Uma alternativa é a pilha guardar uma lista dentro dela e oferecer apenas as operações permitidas. Voltaremos a essa ideia em uma aula futura.

**C. Aluno e Monitor: provavelmente, não.**
A mesma pessoa é aluno o tempo todo e é monitor só durante um período. Falha a pergunta 2: o "tipo" muda enquanto o objeto existe. Seria preciso criar um objeto novo e copiar os dados. Uma alternativa é guardar a monitoria como informação do aluno (por exemplo, um atributo indicando a disciplina que ele monitora).



**D. Gerente e Funcionário: depende.**
Um gerente **é um** funcionário, e a herança parece natural. Mas a resposta depende de **como o sistema vai ser usado**. Se as promoções acontecem com frequência, o mesmo funcionário passaria de `Funcionario` para `Gerente`, e voltamos ao problema da situação C. Se, por outro lado, o gerente é cadastrado como gerente desde o início e não muda de cargo no sistema, a herança funciona bem.



Observe o padrão: o nome das classes quase nunca decide sozinho. O que decide é o que **o sistema precisa fazer** com elas e se o tipo do objeto **muda** ao longo do tempo.