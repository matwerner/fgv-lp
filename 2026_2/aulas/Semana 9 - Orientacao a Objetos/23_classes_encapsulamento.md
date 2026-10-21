# Aula 24: Encapsulamento

## 1. O problema: estados inválidos

### 1.1 Onde a batalha Pokémon nos deixou

Na aula passada, construímos uma pequena batalha Pokémon:

```python
class Golpe:

    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano


class Pokemon:

    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def aprender_golpe(self, golpe):
        self.golpes.append(golpe)

    def receber_dano(self, dano):
        self.vida -= dano

    def esta_vivo(self):
        return self.vida > 0

    def atacar(self, alvo, golpe):
        print(f"{self.nome} usou {golpe.nome}!")
        alvo.receber_dano(golpe.dano)
        print(f"{alvo.nome} ficou com {alvo.vida} de vida.")
```

E deixamos duas perguntas em aberto:

> Um Pokémon não pode ficar com vida negativa. O que precisa mudar na nossa implementação?

> O que impede alguém de escrever `pikachu.vida = -50`?

Vamos começar tentando responder à primeira.



### 1.2 Reproduzindo o problema

Considere:

```python
pikachu = Pokemon("Pikachu", 100)

pikachu.receber_dano(150)

print(pikachu.vida)
```

Saída:

```text
-50
```

Podemos tentar corrigir o método `receber_dano()`, impedindo que a vida fique abaixo de zero.

Mas observe o que ainda é possível fazer de fora da classe:

```python
pikachu.vida = -50

print(pikachu.vida)
print(pikachu.esta_vivo())
```

Saída:

```text
-50
False
```

Nada impediu que o objeto fosse colocado em um estado que não faz sentido.

Corrigir `receber_dano()` não é suficiente, porque qualquer parte do programa pode **contornar** o método e modificar o atributo diretamente.

Esse é o problema que o segundo pilar da orientação a objetos, o **encapsulamento**, tenta resolver. Lembrando a pergunta associada a ele:

> Como controlar a maneira pela qual o estado de um objeto pode ser acessado e modificado?

Antes de ver **como** fazer isso em Python, vale entender **por que** isso importa. O exemplo da vida negativa é apenas um dos motivos.



## 2. Por que controlar o acesso ao estado?

Existem três motivos principais. Os dois primeiros são sobre **proteger** o objeto (regras e valores que não deveriam mudar). O terceiro é sobre **esconder** como os dados são guardados.

### 2.1 Proteger as regras do objeto

Muitos dados têm regras que fazem parte do significado deles:

```text
Pokémon     →  a vida nunca é negativa

Produto     →  o preço nunca é negativo

CPF         →  tem 11 dígitos, e os dois últimos são verificadores

Telefone    →  tem DDD, e o número segue um formato válido

E-mail      →  tem um "@" e um domínio

Idade       →  é um inteiro, e não pode ser negativa

Data        →  o dia 31 de fevereiro não existe
```

Se o atributo é público, **qualquer parte do programa** pode colocar um valor inválido nele, e o erro só será percebido muito depois, em outro lugar, quando ninguém lembra mais de onde o valor veio.

Com o acesso controlado, a regra fica em **um único lugar** e é aplicada sempre. Por exemplo, com um e-mail:

```python
class Cliente:

    def __init__(self, nome, email):
        self.nome = nome
        self.set_email(email)

    def get_email(self):
        return self._email

    def set_email(self, valor):
        valor = valor.strip().lower()
        if "@" not in valor:
            raise ValueError("e-mail inválido")
        self._email = valor
```

Testando:

```python
cliente = Cliente("Ana", "  ANA@Exemplo.com ")

print(cliente.get_email())
```

Saída:

```text
ana@exemplo.com
```

E:

```python
cliente.set_email("ana.exemplo.com")
```

produz:

```text
ValueError: e-mail inválido
```

Observe que o setter faz **duas coisas**: valida (rejeita e-mails sem `@`) e **normaliza** (remove espaços e deixa tudo em minúsculas). Assim, `ANA@Exemplo.com` e `ana@exemplo.com` passam a ser o mesmo e-mail em todo o sistema.



### 2.2 Proteger valores que não deveriam mudar

Algumas informações não têm uma regra de validade. Simplesmente **não deveriam mudar depois de definidas**:

```text
Pedido         →  número do pedido, data de criação

Pessoa         →  data de nascimento, CPF

Pokémon        →  vida máxima, espécie

Loja           →  taxa de entrega, limite de crédito, alíquota de imposto
                  (parâmetros de configuração)
```

Considere:

```python
class Pedido:

    def __init__(self, numero):
        self.numero = numero


pedido = Pedido(1042)

pedido.numero = 1

print(pedido.numero)
```

Saída:

```text
1
```

Python não reclamou. Um trecho do programa qualquer acabou de **mudar o número de um pedido**, e a nota fiscal, o rastreio e o histórico do cliente agora se referem a um pedido que não existe.

Os parâmetros de **configuração** são um caso especialmente perigoso. Se a taxa de entrega é um atributo público, qualquer função pode alterá-la "só para testar" e esquecer de voltar. O programa passa a se comportar de forma diferente, e ninguém sabe por quê.

O encapsulamento permite dizer: esse valor é definido na criação e **só pode ser lido** depois. Nas próximas aulas, veremos as ferramentas do Python para isso (propriedades somente leitura, `@dataclass(frozen=True)`).



### 2.3 O que acontece sem encapsulamento: cada canto tem sua lógica

Há um problema mais sutil, que aparece quando um dado é usado em muitos lugares.

Imagine um sistema com usuários, e cada usuário possui uma localização guardada em dois atributos públicos, `cidade` e `estado`:

```python
usuarios = [
    {"nome": "Ana",   "cidade": "Niterói",  "estado": "RJ"},
    {"nome": "Bruno", "cidade": None,       "estado": "SP"},
    {"nome": "Carla", "cidade": "Curitiba", "estado": None},
]
```

Uma parte do sistema, o perfil do usuário, escreve:

```python
def perfil(usuario):
    return f"{usuario['nome']} ({usuario['cidade']}, {usuario['estado']})"
```

Outra parte, a etiqueta de envio, escreve:

```python
def etiqueta(usuario):
    return f"{usuario['cidade']}/{usuario['estado']}".upper()
```

Saídas:

```text
Ana (Niterói, RJ)
Bruno (None, SP)
Carla (Curitiba, None)

NITERÓI/RJ
NONE/SP
```

Cada função decidiu, **por conta própria**, como formatar uma localização. E nenhuma delas pensou nos casos difíceis:

```text
E se só o estado foi informado?
E se só a cidade foi informada?
E se nenhum dos dois foi informado?
E se amanhã incluirmos o país?
```

Cada correção terá que ser feita em **todos os lugares** que formatam localizações. Se um deles for esquecido, o sistema passa a se comportar de formas diferentes em telas diferentes.

Com encapsulamento, a regra de formatação mora **dentro do objeto**:

```python
class Localizacao:

    def __init__(self, cidade=None, estado=None):
        self._cidade = cidade
        self._estado = estado

    def __str__(self):
        if self._cidade and self._estado:
            return f"{self._cidade}, {self._estado}"
        return self._cidade or self._estado or "local não informado"
```

Agora todos os trechos do programa simplesmente usam o objeto:

```python
print(Localizacao("Niterói", "RJ"))
print(Localizacao(estado="SP"))
print(Localizacao("Curitiba"))
print(Localizacao())
```

Saída:

```text
Niterói, RJ
SP
Curitiba
local não informado
```

E, se amanhã o país for incluído, **só a classe `Localizacao` muda**.

Esse mesmo problema aparece em muitos outros dados do dia a dia:

```text
Telefone   →  "(21) 99999-9999", "21999999999", "+55 21 99999-9999"
              Qual formato guardar? Qual exibir? Qual enviar para o SMS?

CPF        →  "123.456.789-09" ou "12345678909"?
              Quem compara dois CPFs precisa lembrar de limpar a pontuação.

Data       →  "05/10/2026", "2026-10-05", 05 de outubro de 2026,
              e o fuso horário?

Dinheiro   →  R$ 10,5? R$ 10,50? 10.5? 1050 centavos?
              E a moeda?

Nome       →  "ana silva", "ANA SILVA", "Silva, Ana"?

Distância  →  metros ou quilômetros? Milhas?
```

Sempre que a mesma decisão é tomada em vários lugares, existe risco de que sejam tomadas de formas diferentes.



### 2.4 Esconder como os dados são guardados

O terceiro motivo é o mais importante em programas grandes, e retoma o conceito de **acoplamento** da Aula 21.

Quando um dado é público, todos os trechos que o usam passam a depender de **como ele é representado**. Se essa representação mudar, todos precisam mudar.

Ao esconder a representação interna e oferecer apenas operações, quem usa o objeto só precisa saber **o que ele faz**, não **como** faz.

**Exemplo 1: a vida do Pokémon.**

Hoje a vida é um número. Se amanhã quisermos guardar vida atual e vida máxima (para mostrar uma barra de vida), todo trecho que faz `pikachu.vida -= 20` precisaria ser reescrito. Se existir apenas `pikachu.receber_dano(20)`, só a classe muda.

**Exemplo 2: um grafo.**

Um grafo pode ser guardado como **lista de adjacência** (um dicionário que associa cada vértice aos seus vizinhos) ou como **matriz de adjacência** (uma matriz de verdadeiro/falso). Cada uma é melhor em situações diferentes.

Versão com dicionário:

```python
class Grafo:

    def __init__(self):
        self._vizinhos = {}

    def adicionar_aresta(self, a, b):
        self._vizinhos.setdefault(a, set()).add(b)
        self._vizinhos.setdefault(b, set()).add(a)

    def vizinhos(self, v):
        return set(self._vizinhos.get(v, set()))

    def tem_aresta(self, a, b):
        return b in self._vizinhos.get(a, set())
```

Versão com matriz:

```python
class GrafoMatriz:

    def __init__(self, vertices):
        self._vertices = list(vertices)
        self._indice = {v: i for i, v in enumerate(vertices)}
        n = len(vertices)
        self._matriz = [[False] * n for _ in range(n)]

    def adicionar_aresta(self, a, b):
        i, j = self._indice[a], self._indice[b]
        self._matriz[i][j] = self._matriz[j][i] = True

    def vizinhos(self, v):
        i = self._indice[v]
        return {self._vertices[j] for j, ok in enumerate(self._matriz[i]) if ok}

    def tem_aresta(self, a, b):
        return self._matriz[self._indice[a]][self._indice[b]]
```

Para quem usa, as duas são **indistinguíveis**:

```python
g.adicionar_aresta("A", "B")
g.adicionar_aresta("A", "C")

print(sorted(g.vizinhos("A")))
print(g.tem_aresta("A", "B"))
print(g.tem_aresta("B", "C"))
```

Saída (nas duas versões):

```text
['B', 'C']
True
False
```

Se o programa inteiro só usa `adicionar_aresta`, `vizinhos` e `tem_aresta`, podemos trocar uma versão pela outra (por exemplo, porque o grafo ficou denso e a matriz passou a ser mais eficiente) **sem alterar nenhuma linha** do código que usa o grafo.

Se, em vez disso, vários trechos acessassem `g.vizinhos["A"]` diretamente, a troca quebraria todos.

**Exemplo 3: o tabuleiro de Sudoku.**

Um tabuleiro de Sudoku é naturalmente uma matriz 9×9. Mas também poderia ser uma lista com 81 números, ou até um texto com 81 caracteres (um formato comum para compartilhar tabuleiros).

```python
class Tabuleiro:

    def __init__(self):
        self._celulas = [[0] * 9 for _ in range(9)]

    def get(self, linha, coluna):
        return self._celulas[linha][coluna]

    def colocar(self, linha, coluna, valor):
        if not 0 <= valor <= 9:
            raise ValueError("valor deve estar entre 0 e 9")
        self._celulas[linha][coluna] = valor
```

A versão com texto teria exatamente os mesmos métodos:

```python
class TabuleiroTexto:

    def __init__(self):
        self._celulas = "0" * 81

    def get(self, linha, coluna):
        return int(self._celulas[linha * 9 + coluna])

    def colocar(self, linha, coluna, valor):
        if not 0 <= valor <= 9:
            raise ValueError("valor deve estar entre 0 e 9")
        i = linha * 9 + coluna
        self._celulas = self._celulas[:i] + str(valor) + self._celulas[i + 1:]
```

O código que resolve o Sudoku, desenha o tabuleiro ou verifica as regras usa apenas `get` e `colocar`. A conta `linha * 9 + coluna` nunca aparece fora da classe. Além disso, a regra de validação (valores de 0 a 9) também está em um único lugar.

**Exemplo 4: dinheiro.**

Números com vírgula (`float`) têm uma imprecisão conhecida:

```python
print(0.1 + 0.2)
```

Saída:

```text
0.30000000000000004
```

Por isso, sistemas financeiros costumam guardar dinheiro como um número **inteiro de centavos**. Se o preço for um atributo público `preco = 10.5`, todo o programa passa a depender de que ele seja um `float`. Se o dado estiver encapsulado em um objeto `Dinheiro`, a representação pode ser trocada sem afetar ninguém:

```python
class Dinheiro:

    def __init__(self, reais):
        self._centavos = round(reais * 100)

    def somar(self, outro):
        resultado = Dinheiro(0)
        resultado._centavos = self._centavos + outro._centavos
        return resultado

    def __str__(self):
        return f"R$ {self._centavos // 100},{self._centavos % 100:02d}"
```

Testando:

```python
print(Dinheiro(0.1).somar(Dinheiro(0.2)))
```

Saída:

```text
R$ 0,30
```

Ninguém de fora da classe precisa saber que existe um número inteiro de centavos lá dentro.

Podemos resumir:

```text
Encapsulamento

    proteger o estado do objeto
        (regras e valores que não deveriam mudar)
            +
    reduzir a dependência de detalhes internos
        (a representação pode mudar sem quebrar quem usa)
```

Em vez de permitir que qualquer parte do programa modifique os dados livremente, o objeto passa a oferecer **operações bem definidas** para acessá-los e modificá-los.



### 2.5 Centralizar também ajuda a revisar mudanças

Há um benefício menos óbvio, que aparece no trabalho em equipe.

Imagine que a regra de negócio muda: agora o dano máximo de um golpe é 100.

**Sem encapsulamento**, a regra está espalhada pelo programa. A mudança aparece em dezenas de trechos, misturada com outras alterações, e é fácil que algum passe despercebido.

**Com encapsulamento**, a regra está em um único método. A mudança aparece em um único lugar, e é fácil de enxergar em uma revisão:

```diff
 def receber_dano(self, dano):
-    if dano < 0:
-        raise ValueError("dano não pode ser negativo")
+    if not 0 <= dano <= 100:
+        raise ValueError("dano deve estar entre 0 e 100")
     self._vida = max(0, self._vida - dano)
```

Em um sistema de controle de versões (como o Git/GitHub), isso significa:

```text
- quem revisa o código vê exatamente a regra que mudou;

- o histórico (git log, git blame) mostra quem mudou a regra, quando e por quê;

- se alguém alterar um valor importante "por fora" da classe,
  a mudança fica evidente: o atributo deveria ser acessado
  apenas por dentro da classe.
```

Um bônus: **testar** fica mais fácil. Em vez de testar a regra em cada lugar que a usa, testamos a classe uma vez.



## 3. Como o Python lida com isso?

### 3.1 Atributos públicos e a convenção `_`

Até agora, todos os atributos que criamos eram **públicos**: qualquer parte do programa pode lê-los e modificá-los.

Em Python, quando queremos indicar que um atributo é um **detalhe interno**, usamos um sublinhado no início do nome:

```python
class Pokemon:

    def __init__(self, nome, vida):
        self.nome = nome
        self._vida = vida
        self._golpes = []
```

O sublinhado significa:

> "Este atributo é um detalhe interno da classe. Não mexa nele de fora."

Mas observe que **nada impede** o acesso:

```python
pikachu = Pokemon("Pikachu", 100)

pikachu._vida = -50
```

O Python não gera nenhum erro. A convenção `_` é apenas um **aviso** para outros programadores.



### 3.2 O `__` e o *name mangling*

Python também possui uma forma mais "forte" de marcar atributos internos: dois sublinhados no início do nome.

```python
class Pokemon:

    def __init__(self, nome, vida):
        self.nome = nome
        self.__vida = vida
```

Agora:

```python
pikachu = Pokemon("Pikachu", 100)

print(pikachu.__vida)
```

Saída:

```text
AttributeError: 'Pokemon' object has no attribute '__vida'
```

Parece privacidade de verdade. Mas observe o `__dict__` do objeto:

```python
print(pikachu.__dict__)
```

Saída:

```text
{'nome': 'Pikachu', '_Pokemon__vida': 100}
```

O Python apenas **renomeou** o atributo para `_Pokemon__vida` (esse processo se chama *name mangling*). Basta usar o nome novo:

```python
print(pikachu._Pokemon__vida)
```

Saída:

```text
100
```

O `__` serve principalmente para evitar conflitos de nomes em herança. **Não é um mecanismo de segurança.** Na maior parte dos casos, o `_` é suficiente.



### 3.3 Um contrato entre programadores

Em linguagens como Java e C++, existem modificadores como `private`, que o compilador **impõe**.

Em Python, a filosofia é diferente:

```text
Python:   somos todos adultos responsáveis.
          Marcamos o que é interno e confiamos que ninguém vai mexer.
```

Isso significa que, em Python, o encapsulamento é um **contrato entre programadores**, e não uma barreira de segurança.

Isso também significa que **não devemos guardar segredos** em atributos "privados". Uma senha em `__senha` continua acessível para quem quiser.

O que o encapsulamento nos dá é:

```text
- um lugar único onde as regras do objeto são aplicadas;

- liberdade para mudar a representação interna
  sem quebrar quem usa a classe;

- um sinal claro do que faz parte da "interface"
  e do que é detalhe de implementação.
```



## 4. Controlando o acesso ao estado

### 4.1 Peça ao objeto para fazer, não mexa nos dados

A primeira forma de proteger o estado é oferecer **operações** em vez de deixar que os dados sejam modificados de fora.

Em vez de:

```python
pikachu.vida -= 20      # quem chama decide tudo
```

preferimos:

```python
pikachu.receber_dano(20)    # o objeto decide como aplicar
```

Assim, as regras ficam em **um único lugar**:

```python
class Pokemon:

    def __init__(self, nome, vida):
        self.nome = nome
        self._vida = vida
        self._golpes = []

    def receber_dano(self, dano):
        if dano < 0:
            raise ValueError("dano não pode ser negativo")
        self._vida = max(0, self._vida - dano)

    def esta_vivo(self):
        return self._vida > 0
```

Testando:

```python
pikachu = Pokemon("Pikachu", 100)

pikachu.receber_dano(150)

print(pikachu.esta_vivo())
```

Saída:

```text
False
```

E:

```python
pikachu.receber_dano(-5)
```

produz:

```text
ValueError: dano não pode ser negativo
```

Observe que, nesse caso, estamos reaproveitando o tratamento de erros que já estudamos: uma operação inválida **levanta uma exceção** em vez de ser aceita silenciosamente.

Esse princípio costuma ser resumido assim:

```text
Tell, don't ask

Diga ao objeto o que fazer.
Não pergunte pelos dados para decidir por ele.
```



### 4.2 Getters e setters

Algumas vezes, precisamos permitir a leitura ou a alteração direta de um valor, mas **com controle**.

Uma forma tradicional de fazer isso, em outras linguagens, é com métodos chamados **getters** (que leem o valor) e **setters** (que modificam o valor, com validação).

Antes de escrevê-los, vale lembrar **para que eles servem de verdade**. O valor de um getter ou setter está em ser um **ponto único de passagem** por onde todo acesso ao dado precisa passar. Isso permite, em um único lugar:

```text
- validar o valor (vida >= 0, e-mail com "@");

- normalizar o valor (remover espaços, deixar em minúsculas);

- calcular o valor em vez de guardá-lo (total do carrinho);

- registrar quem mudou o dado (log, auditoria);

- avisar outras partes do sistema que algo mudou;

- trocar a representação interna sem afetar quem usa (seção 2.4).
```

Mas há um alerta importante. Na **maior parte dos casos**, um getter e um setter que apenas devolvem e atribuem o valor, sem nenhuma dessas funções, são **puro código repetitivo** (*boilerplate*):

```python
def get_nome(self):
    return self._nome

def set_nome(self, valor):
    self._nome = valor
```

Esse par de métodos não protege nada: tem o mesmo efeito de um atributo público, só que mais longo. Em linguagens como Java, esse padrão é muito comum, porque trocar um atributo público por um método depois obrigaria a reescrever todo o código que o usa. Em Python, veremos na próxima aula que essa troca é possível sem quebrar ninguém, e por isso **só criamos getters e setters quando existe um motivo real** (uma das funções da lista acima).

Dito isso, o getter e o setter de `vida` abaixo têm um motivo real: a validação.

```python
class Pokemon:

    def __init__(self, nome, vida):
        self.nome = nome
        self._vida = vida

    def get_vida(self):
        return self._vida

    def set_vida(self, valor):
        if valor < 0:
            raise ValueError("vida não pode ser negativa")
        self._vida = valor
```

Agora:

```python
pikachu = Pokemon("Pikachu", 100)

pikachu.set_vida(80)
print(pikachu.get_vida())
```

Saída:

```text
80
```

E uma tentativa de usar um valor inválido:

```python
pikachu.set_vida(-50)
```

produz:

```text
ValueError: vida não pode ser negativa
```

Esse código funciona, mas apresenta dois inconvenientes.

**Inconveniente 1: o construtor pode contornar a validação.**

Observe:

```python
pikachu = Pokemon("Pikachu", -10)

print(pikachu.get_vida())
```

Saída:

```text
-10
```

O `__init__` atribuiu diretamente a `self._vida`, sem passar pelo setter. Para corrigir, o `__init__` precisa **utilizar o setter**:

```python
def __init__(self, nome, vida):
    self.nome = nome
    self.set_vida(vida)
```

Agora:

```python
pikachu = Pokemon("Pikachu", -10)
```

produz:

```text
ValueError: vida não pode ser negativa
```

Um erro muito comum é validar apenas em um lugar e esquecer dos outros caminhos pelos quais o dado entra no objeto.

**Inconveniente 2: o uso fica pesado.**

Compare:

```python
pikachu.set_vida(pikachu.get_vida() - 20)    # com getter e setter

pikachu.vida -= 20                           # com atributo público
```

O segundo é muito mais natural de ler.

Isso gera uma pergunta:

> Seria possível ter a **sintaxe simples** de um atributo público, mas com o **controle** de um setter?

Em Python, sim. Para isso, precisamos de uma ferramenta chamada **decorador**, que será o tema da próxima aula.



### 4.3 Cuidado com estruturas mutáveis

Há um segundo caminho pelo qual o estado de um objeto pode "vazar".

Considere uma classe que protege a lista de golpes e oferece um método para acessá-la:

```python
class Pokemon:

    def __init__(self, nome, vida):
        self.nome = nome
        self._vida = vida
        self._golpes = []

    def aprender_golpe(self, golpe):
        self._golpes.append(golpe)

    def get_golpes(self):
        return self._golpes
```

Agora:

```python
pikachu = Pokemon("Pikachu", 100)
pikachu.aprender_golpe(Golpe("Choque do Trovão", 20))

pikachu.get_golpes().clear()

print(len(pikachu.get_golpes()))
```

Saída:

```text
0
```

Apagamos todos os golpes do Pokémon **sem passar por nenhum método da classe**.

Isso acontece porque `get_golpes()` devolveu uma **referência** para a mesma lista que está dentro do objeto. Esse é exatamente o mesmo tema da Aula 22: dois nomes se referindo ao mesmo objeto.

Existem duas formas de resolver:

**Devolver uma cópia:**

```python
def get_golpes(self):
    return list(self._golpes)
```

Agora, `pikachu.get_golpes().clear()` limpa apenas a cópia, e o Pokémon continua com seus golpes (o `len` imprime `1`).

**Devolver uma estrutura imutável:**

```python
def get_golpes(self):
    return tuple(self._golpes)
```

Agora, `pikachu.get_golpes().clear()` gera:

```text
AttributeError: 'tuple' object has no attribute 'clear'
```

Podemos resumir:

```text
Se um método devolve uma estrutura mutável que está dentro do objeto,
quem chamou passa a ter acesso ao estado interno.

Devolva uma cópia ou uma estrutura imutável.
```



## 5. Exercícios

### 5.1 Protegendo o preço

Considere a classe `Produto`:

```python
class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
```

Modifique a classe para que o preço:

- seja guardado em um atributo interno (`_preco`);
- possa ser lido com `get_preco()`;
- possa ser alterado com `set_preco(valor)`, que levanta `ValueError` se o valor for negativo.

Depois, teste:

```python
Produto("Livro", -10)
```

**Para pensar:**

1. O que acontece se o `__init__` atribuir diretamente a `self._preco`?
2. O que acontece com o método `aplicar_desconto()` que escrevemos na Aula 21? Ele também precisa passar pelo setter?



### 5.2 Vazamento no carrinho

Considere:

```python
class Carrinho:

    def __init__(self):
        self._produtos = []

    def adicionar(self, produto):
        self._produtos.append(produto)

    def get_produtos(self):
        return self._produtos
```

1. Escreva um código **externo** à classe que esvazie o carrinho sem usar nenhum método dela.
2. Corrija `get_produtos()` de duas formas diferentes (cópia e `tuple`).
3. Qual das duas você escolheria? Por quê?



### 5.3 Curando um Pokémon

Adicione à classe `Pokemon`:

- um atributo `_vida_maxima`, definido na criação;
- um método `curar(quantidade)`, que aumenta a vida **sem ultrapassar** a vida máxima.

Depois, responda:

1. O que impede alguém de escrever `pikachu._vida = 9999`?
2. Isso é um problema da nossa classe ou do Python?
3. O que mudaria se `_vida` e `_vida_maxima` fossem guardadas de outra forma (por exemplo, como porcentagem)? Quem precisaria ser modificado?