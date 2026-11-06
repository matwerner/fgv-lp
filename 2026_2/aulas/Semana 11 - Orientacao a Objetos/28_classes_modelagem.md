# Aula 29: Modelagem, relacionamentos entre classes e princípios de projeto

## 1. Retomando a aplicação de busca

### 1.1 Como cada dupla resolveu?

Na aula passada, cada dupla resolveu o mesmo problema: filtrar e ordenar jogos. Algumas perguntas para comparar as soluções:

```text
- Quais classes (ou funções) vocês criaram?

- Quantos lugares do código vocês precisaram alterar para o filtro novo?

- Quem cria os filtros e as ordenações: o programa principal ou outra classe?

- Qual foi a maior dificuldade?
```



### 1.2 Abordagens que costumam aparecer

```text
A. Funções soltas
   filtrar_por_tag(jogos, tag), ordenar_por_nota(jogos)...

B. Uma única classe que faz tudo
   Busca com um método grande e vários if/elif

C. Uma classe para cada filtro e cada ordenação
```

Para cada abordagem, uma pergunta ajuda a levantar as limitações:

```text
A. E se o usuário quiser combinar 3 filtros, escolhidos em tempo de execução?

B. O que acontece com o método grande quando surge um filtro novo?
   E quando alguém precisa mexer só na ordenação?

C. Quem junta as peças? Como o programa principal as conhece?
```

Ainda não vamos dar nomes às limitações. Elas voltam na seção 5.5.



## 2. Modelagem: as classes e seus detalhes

### 2.1 O diagrama de classes

Antes de programar, é útil **desenhar** o sistema. O desenho mais usado é o **diagrama de classes** (da linguagem UML). Cada classe é uma caixa com três partes:

```text
+---------------------------+
| NomeDaClasse              |
+---------------------------+
| atributos                 |
+---------------------------+
| métodos                   |
+---------------------------+
```

O primeiro passo da modelagem é responder:

```text
1. Quais são as entidades (classes) do sistema?

2. O que cada uma guarda (atributos)?

3. O que cada uma sabe fazer (métodos)?
```



### 2.2 As caixas da aplicação de busca

```text
+--------------------------+     +--------------------------+
| Jogo                     |     | Filtro (abstrata)        |
+--------------------------+     +--------------------------+
| titulo                   |     |                          |
| preco                    |     +--------------------------+
| lancamento               |     | filtrar(jogos)           |
| tags                     |     | criterio(jogo)           |
| nota                     |     +--------------------------+
| num_avaliacoes           |
+--------------------------+     +--------------------------+
                                 | Ordenacao (abstrata)     |
+--------------------------+     +--------------------------+
| Buscador                 |     | decrescente              |
+--------------------------+     +--------------------------+
| jogos                    |     | ordenar(jogos)           |
+--------------------------+     | chave(jogo)              |
| buscar(filtros,          |     +--------------------------+
|        ordenacao)        |
+--------------------------+     +--------------------------+
                                 | Exibidor                 |
                                 +--------------------------+
                                 | limite                   |
                                 +--------------------------+
                                 | exibir(jogos)            |
                                 | formatar(jogo)           |
                                 +--------------------------+
```

Só com as caixas ainda não sabemos como as peças **se conectam**. Esse é o próximo passo.



## 3. Relacionamentos entre classes

Objetos não vivem sozinhos: eles se **conhecem** e se **usam**. Existem quatro tipos principais de relacionamento.

### 3.1 Associação

Um objeto **usa** ou **conhece** o outro, sem ser dono dele.

Na nossa aplicação, o `Buscador` recebe os filtros e a ordenação apenas **durante a busca**:

```python
class Buscador:

    def buscar(self, filtros, ordenacao):
        ...
```

O `Buscador` usa os filtros e a ordenação naquele momento, mas não os guarda. Eles existem independentemente do buscador e podem ser usados em outras buscas.

Essa classificação vale para **este projeto**: filtros e ordenação chegam por parâmetro. Na seção 3.7 veremos um projeto alternativo em que essa relação muda.

Símbolo no diagrama: uma **linha** (com seta, se for só um lado que conhece o outro).

```text
Buscador ──────→ Filtro

Buscador ──────→ Ordenacao
```



### 3.2 Agregação

Relação **todo–parte**, em que a parte **existe independentemente do todo** e pode ser compartilhada.

O `Buscador` guarda o catálogo de jogos, mas quem o carrega é quem monta o buscador:

```python
jogos = [parse_jogo(d) for d in carregar_jogos("games.jsonl")]

buscador_a = Buscador(jogos)
buscador_b = Buscador(jogos)

print(buscador_a.jogos is buscador_b.jogos)
```

Saída:

```text
True
```

Os dois buscadores usam **o mesmo** catálogo. E se um buscador deixar de existir, os jogos continuam válidos:

```python
del buscador_a
print(len(buscador_b.jogos) > 0)
```

Saída:

```text
True
```

Símbolo: **losango vazio** no lado do "todo".

```text
Buscador ◇──────→ Jogo
```



### 3.3 Composição

Também é uma relação todo–parte, mas a parte **pertence a um único dono** e **não faz sentido sem ele**: o ciclo de vida da parte acompanha o do todo.

Exemplo na aplicação: um buscador que cria o **seu próprio** exibidor, usado só por ele:

```python
class BuscadorComExibicao:

    def __init__(self, jogos, limite=10):
        self.jogos = jogos
        self.exibidor = Exibidor(limite)

    def buscar_e_exibir(self, filtros, ordenacao):
        resultado = self.jogos
        for filtro in filtros:
            resultado = filtro.filtrar(resultado)
        self.exibidor.exibir(ordenacao.ordenar(resultado))
```

Símbolo: **losango cheio** no lado do "todo".

```text
BuscadorComExibicao ◆──────→ Exibidor
```

**Atenção:** instanciar a parte dentro do `__init__` é só o sinal mais comum de composição, **não é o critério**. O que define a composição é a **posse exclusiva** e o **ciclo de vida compartilhado**. Um objeto criado fora e passado ao construtor ainda pode ser composição, se só aquele dono o usa e ele deixa de fazer sentido sem o dono.

E a mesma relação pode mudar de tipo **conforme a aplicação**. Um `Exibidor` usado por vários buscadores seria agregação; um exclusivo de um buscador seria composição.



### 3.4 Herança

Relação "**é um**": uma classe especializa outra, como vimos na aula de herança. Diferente das três anteriores ("tem um" ou "usa um"), aqui a filha **é** uma versão da base.

Símbolo: **seta com triângulo vazio**, apontando para a base.

```text
TagsFiltro ──────▷ Filtro

NotaOrdenacao ──────▷ Ordenacao
```



### 3.5 Como decidir: perguntas-critério

Para classificar uma relação entre A e B, pergunte:

```text
1. A só usa B durante uma chamada (parâmetro), ou guarda uma
   referência a B como atributo?
   → só usa: associação

2. Se A guarda B, B existe independentemente de A?
   Pode ser compartilhado com outros objetos?
   → sim: agregação

3. B pertence só a A e deixa de fazer sentido sem A?
   → sim: composição

4. A é uma versão especializada de B?
   → sim: herança
```

Ao justificar, fale de **posse** e **ciclo de vida**, e deixe claro de qual sistema você está falando: a classificação depende do contexto.



### 3.6 O mapa completo da aplicação

```text
                  +-----------+
                  | Buscador  |
                  +-----------+
                   ◇    |    |
                   |    |    |
                   v    v    v
            +------+ +--------+ +------------+
            | Jogo | | Filtro | | Ordenacao  |
            +------+ +--------+ +------------+
                          ▲            ▲
                          | (herança)  | (herança)
                  +-------------+ +---------------+
                  | TagsFiltro  | | NotaOrdenacao |
                  | NotaMinima..| | PrecoOrden..  |
                  +-------------+ +---------------+
```

Em palavras:

```text
Buscador ◇──→ Jogo             agregação (guarda o catálogo, que vem de fora)

Buscador ──→ Filtro            associação (só usa durante a busca)

Buscador ──→ Ordenacao         associação

TagsFiltro ──▷ Filtro          herança

NotaOrdenacao ──▷ Ordenacao    herança

Exibidor ──→ Jogo              associação (só recebe os jogos para exibir)
```



### 3.7 Mesma aplicação, dois projetos

Modelamos o buscador de modo que ele **guarda** o catálogo de jogos e, a cada busca, **recebe** os filtros e a ordenação. Mas existe outro projeto possível, e é provável que algumas duplas tenham feito assim na aula passada: o buscador **guarda** os filtros e a ordenação, e **recebe** os jogos a cada busca.

**Projeto 1 (o que modelamos):** o buscador guarda o catálogo.

```python
class Buscador:

    def __init__(self, jogos):
        self.jogos = jogos

    def buscar(self, filtros, ordenacao):
        resultado = self.jogos
        for filtro in filtros:
            resultado = filtro.filtrar(resultado)
        return ordenacao.ordenar(resultado)


buscador = Buscador(jogos)

rpgs = buscador.buscar([TagsFiltro(["RPG"])], NotaOrdenacao(decrescente=True))
baratos = buscador.buscar([PrecoMaximoFiltro(50)], PrecoOrdenacao())
```

O projeto 1 se parece com uma loja de jogos: o catálogo é carregado **uma vez**, e o usuário faz várias buscas diferentes sobre ele.

**Projeto 2:** o buscador guarda a configuração da busca.

```python
class Buscador:

    def __init__(self, filtros, ordenacao):
        self.filtros = filtros
        self.ordenacao = ordenacao

    def buscar(self, jogos):
        for filtro in self.filtros:
            jogos = filtro.filtrar(jogos)
        return self.ordenacao.ordenar(jogos)


buscador = Buscador([TagsFiltro(["RPG"])], NotaOrdenacao(decrescente=True))
resultado = buscador.buscar(jogos)
```

As relações mudam:

```text
                          Projeto 1                 Projeto 2

Buscador → Jogo           agregação                 associação
                          (guarda a lista, e os     (parâmetro)
                          jogos existem sem o
                          buscador)

Buscador → Filtro         associação                agregação
                          (só usa durante a         (guarda, vem de fora,
                          busca)                    compartilhável)

Buscador → Ordenacao      associação                agregação
```

**Para discutir:** qual projeto vocês escolheriam e por quê? Anotem os argumentos: voltaremos a eles na seção 5.5, depois de conhecer os critérios.

A mesma aplicação, com os mesmos objetos, admite desenhos diferentes. **Qual é melhor?** O diagrama não responde, e esta é a pergunta da seção 5.

Uma versão com linha de comando (projeto 1) permite ver isso funcionando: o catálogo é carregado uma vez e o usuário escolhe filtros e ordenação em cada busca.



### 3.8 Para praticar: classifique e justifique

Classifique o relacionamento e justifique, dizendo em que sistema você está pensando:

```text
A. Pedido e Item de pedido

B. Pedido e Cliente

C. Time e Jogador
```

**Respostas comentadas:**

**A. Pedido e Item: composição.** Os itens existem só como parte daquele pedido. Se o pedido for apagado, os itens perdem o sentido, e nenhum outro pedido os compartilha.

**B. Pedido e Cliente: associação** (ou agregação, dependendo do sistema). O cliente existe antes e depois do pedido e tem muitos outros pedidos. O pedido apenas o conhece.

**C. Time e Jogador: depende do sistema.**
- Em um jogo em que o jogador pode ser transferido de time e continuar existindo: **agregação**.
- Em um sistema em que o jogador só existe como membro daquele time, e some junto com ele: **composição**.

O que a prova costuma avaliar é a **justificativa** (posse e ciclo de vida), não a classificação isolada.



## 4. Do diagrama ao código

O diagrama é um **mapa** do código:

```text
Caixa (classe)                →  class

Atributos da caixa            →  atributos da classe (self.x)

Métodos da caixa              →  métodos

Seta de herança               →  class Filha(Base)

Seta com losango (ou linha)   →  um atributo que referencia o outro objeto
                                 (ou um parâmetro, no caso da associação)
```

A implementação deste diagrama usa as mesmas classes `Filtro` e `Ordenacao` da construção em aula. O que muda é **quem guarda o quê** (seção 3.7).

```python
buscador = Buscador(jogos)

resultado = buscador.buscar(
    filtros=[
        TagsFiltro(["RPG"]),
        NotaMinimaFiltro(80, 1000),
        PrecoMaximoFiltro(100),
    ],
    ordenacao=NotaOrdenacao(decrescente=True),
)

Exibidor(limite=10).exibir(resultado)
```



## 5. Avaliando a modelagem

A modelagem, por si só, nos diz **como representamos** um problema com orientação a objetos: quais são as classes e como elas se relacionam. Ela **não diz nada sobre a qualidade** dessa representação. Como vimos na seção 3.7, o mesmo problema pode ser modelado de vários jeitos, todos válidos, mas com facilidades diferentes para mudar e evoluir.

Para comparar modelagens, precisamos de critérios. Duas regras práticas ajudam: **SRP** e **OCP**. Vamos conhecê-las em um segundo problema e, no final, voltar à aplicação de busca para avaliar tudo o que apareceu hoje.

### 5.1 Um segundo problema

Uma loja precisa de pedidos com **itens**, **frete** (que depende do tipo de entrega) e **recibo** (que também pode ser salvo em arquivo). Uma primeira versão:

```python
class Pedido:

    def __init__(self, itens, tipo_entrega):
        self.itens = itens
        self.tipo_entrega = tipo_entrega

    def total_itens(self):
        return sum(preco for _, preco in self.itens)

    def calcular_frete(self):
        if self.tipo_entrega == "normal":
            return 10
        elif self.tipo_entrega == "expresso":
            return 25
        elif self.tipo_entrega == "retirada":
            return 0

    def gerar_recibo(self):
        linhas = [f"{nome}: R$ {preco:.2f}" for nome, preco in self.itens]
        linhas.append(f"Frete: R$ {self.calcular_frete():.2f}")
        linhas.append(f"Total: R$ {self.total_itens() + self.calcular_frete():.2f}")
        return "\n".join(linhas)

    def salvar_recibo(self, caminho):
        with open(caminho, "w", encoding="utf-8") as arquivo:
            arquivo.write(self.gerar_recibo())
```

Funciona:

```python
pedido = Pedido([("Livro", 50.0), ("Caneta", 5.5)], "expresso")
print(pedido.gerar_recibo())
```

Saída:

```text
Livro: R$ 50.00
Caneta: R$ 5.50
Frete: R$ 25.00
Total: R$ 80.50
```

Agora, três pedidos do cliente:

```text
1. "Quero um novo tipo de entrega: drone."

2. "Quero o recibo em HTML."

3. "Quero salvar o recibo em um banco de dados."
```

Em **qual classe** você mexe em cada um dos três casos? Em todos eles, na `Pedido`.



### 5.2 SRP: responsabilidade única

> Uma classe deve ter **um único motivo para mudar**.

A classe `Pedido` tem **vários motivos**: a regra de frete, o formato do recibo e a forma de armazenamento. Cada mudança de um deles mexe na mesma classe, e o risco de quebrar os outros aumenta.

Separando as responsabilidades:

```python
@dataclass(frozen=True)
class Item:
    nome: str
    preco: float


class Pedido:

    def __init__(self, itens, entrega):
        self.itens = itens
        self.entrega = entrega

    def total_itens(self):
        return sum(item.preco for item in self.itens)

    def total(self):
        return self.total_itens() + self.entrega.calcular_frete()


class ReciboTexto:

    def gerar(self, pedido):
        linhas = [f"{i.nome}: R$ {i.preco:.2f}" for i in pedido.itens]
        linhas.append(f"Frete: R$ {pedido.entrega.calcular_frete():.2f}")
        linhas.append(f"Total: R$ {pedido.total():.2f}")
        return "\n".join(linhas)


class ArquivoRecibo:

    def salvar(self, texto, caminho):
        with open(caminho, "w", encoding="utf-8") as arquivo:
            arquivo.write(texto)
```

Agora cada classe tem um único motivo para mudar:

```text
Pedido         →  muda se a regra do pedido mudar

ReciboTexto    →  muda se o formato do recibo mudar

ArquivoRecibo  →  muda se a forma de guardar mudar
```

Mesma ideia da aplicação de busca: o `Buscador` busca, o `Exibidor` exibe e o `Jogo` guarda dados.



### 5.3 OCP: aberto para extensão, fechado para modificação

> Deve ser possível **acrescentar** comportamento novo **sem editar** o código que já funciona.

O `if/elif` do frete viola isso: cada tipo de entrega novo exige **editar** `calcular_frete`. A solução é a mesma do polimorfismo:

```python
from abc import ABC, abstractmethod


class Entrega(ABC):

    @abstractmethod
    def calcular_frete(self):
        ...


class EntregaNormal(Entrega):

    def calcular_frete(self):
        return 10


class EntregaExpressa(Entrega):

    def calcular_frete(self):
        return 25


class EntregaRetirada(Entrega):

    def calcular_frete(self):
        return 0
```

Usando:

```python
pedido = Pedido([Item("Livro", 50.0), Item("Caneta", 5.5)], EntregaExpressa())

texto = ReciboTexto().gerar(pedido)
print(texto)
```

Saída:

```text
Livro: R$ 50.00
Caneta: R$ 5.50
Frete: R$ 25.00
Total: R$ 80.50
```

Para o drone, **escrevemos uma classe nova** e não editamos nenhuma que já existia:

```python
class EntregaDrone(Entrega):

    def calcular_frete(self):
        return 40


print(Pedido([Item("Livro", 50.0)], EntregaDrone()).total())
```

Saída:

```text
90.0
```

Compare com a aplicação de busca: o filtro novo do twist era exatamente isso.



### 5.4 O diagrama da segunda solução

```text
Pedido ◆──────→ Item          composição (os itens são do pedido)

Pedido ◇──────→ Entrega       agregação (a entrega vem de fora)

EntregaNormal ──▷ Entrega     herança

ReciboTexto ──────→ Pedido    associação (só usa o pedido para gerar)
```



### 5.5 Voltando à aplicação de busca

Agora que temos os critérios, vamos avaliar as abordagens do começo da aula (seção 1.2) e os dois projetos finais.

**As abordagens iniciais**

```text
A. Funções soltas, com um if/elif escolhendo qual chamar
   SRP: o trecho que decide concentra todos os critérios
   OCP: um filtro novo exige editar o if/elif

B. Uma única classe com um método grande
   SRP: filtra, ordena e (às vezes) exibe: vários motivos para mudar
   OCP: um filtro novo exige editar o método grande

C. Uma classe para cada filtro e cada ordenação, sem quem as junte
   SRP e OCP: as classes em si estão bem
   Mas alguém precisa montar a busca. Se o programa principal faz isso
   com if/elif ("se pediu tag, crie um TagsFiltro..."), o problema
   apenas mudou de lugar
```

Uma observação sobre a abordagem A: funções também são objetos. Passar as próprias funções como parâmetro, sem `if/elif`, é uma alternativa legítima, e é a mesma ideia do polimorfismo. As classes costumam organizar melhor quando cada filtro tem parâmetros e comportamento próprios.

O que faltava na abordagem C é exatamente o que os dois projetos finais resolvem: o `Buscador` é quem **junta as peças**.

**O que precisa ser editado para acrescentar um filtro novo?**

```text
A. Funções soltas com if/elif    →  o if/elif (e quem o chama)

B. Classe única                  →  o método grande

C. Classes sem um buscador       →  o programa principal

Projetos 1 e 2                   →  nada: só uma classe nova
```

É a mesma pergunta do exercício da aula passada ("em quantos lugares você mexeu?"), agora com um nome para a resposta: **OCP**.

**Os dois projetos finais**

**SRP:** vale para os dois. Cada classe tem um único motivo para mudar:

```text
Jogo         →  muda se os dados do jogo mudarem

Filtro       →  cada filtro muda se o seu critério mudar

Ordenacao    →  cada ordenação muda se o seu critério mudar

Exibidor     →  muda se o formato de saída mudar

Buscador     →  muda se a forma de buscar mudar
```

Duas observações:

- Se o `Buscador` também **lesse o arquivo** de jogos, ele teria um segundo motivo para mudar (o formato do arquivo). Por isso a leitura (`carregar_jogos` e `parse_jogo`) ficou fora dele.
- O `BuscadorComExibicao` da seção 3.3 serve para ilustrar a composição, mas **não é um bom exemplo de SRP**: ele busca *e* exibe, então muda tanto se a busca mudar quanto se a exibição mudar.

**OCP:** nos dois projetos, um filtro ou uma ordenação nova é **uma classe nova**, e nada que já existia é editado. Eles empatam.

**Então, qual é melhor?**

SRP e OCP **não separam** os dois projetos. Esses critérios avaliam **algumas** qualidades, não todas. A escolha entre os dois depende de outra pergunta: **que tipo de mudança é mais provável neste sistema?**

```text
Mudança                            Projeto 1               Projeto 2

Novo filtro                        classe nova             classe nova

Mesma busca sobre outro            criar outro buscador    passar outra lista
conjunto de jogos                  (ou atualizar a lista)  (nada a alterar)

Mesmos jogos, outra combinação     chamar buscar() com     criar outro buscador
de filtros                         outros argumentos       (ou alterar atributos)
```

```text
Projeto 1
   + o catálogo é carregado uma vez e várias buscas podem ser feitas
   + filtros e ordenação são escolhidos a cada busca, o que combina com
     um programa interativo (como uma loja de jogos)
   - o buscador fica preso a um catálogo: se a lista mudar, é preciso
     atualizá-la (e quem pode alterá-la?)

Projeto 2
   + o buscador configurado funciona como uma "busca salva", reutilizável
     (ex.: um alerta "RPG até R$ 50")
   - os jogos precisam ser passados a cada busca
```

Não existe "o melhor" sem conhecer o contexto. O que a modelagem e os critérios nos dão é um vocabulário para **justificar** a escolha.



### 5.6 Cuidados

- **OCP não significa nunca editar uma classe.** Um bug ou uma regra errada pode e deve ser corrigido onde está. O princípio fala de **acrescentar** comportamento sem editar o que já funciona.
- **SRP não significa uma classe com um único método.** Significa um único *motivo* para mudar.
- Nem todo programa precisa disso. Se só existem duas entregas e nunca vão mudar, o `if` pode ser mais simples. O princípio compensa quando o sistema **cresce**.



## 6. Exercícios

### 6.1 Notificações da EMAp

A instituição **EMAp** está criando um sistema simples para enviar **notificações** aos alunos sobre comunicados relacionados a **eventos acadêmicos**.

Cada **aluno** possui: **nome**, **telefone**, **e-mail** e **curso** (ex.: "Matemática Aplicada", "Ciência de Dados").

Uma **notificação** possui: **mensagem**, **curso alvo** e um **canal de envio**. Os canais possíveis são **E-mail** e **SMS**.

Ao enviar uma notificação, o sistema deve enviá-la **apenas para os alunos cujo curso coincide exatamente** com o **curso alvo** informado.

O sistema deve permitir:

- **(i)** o cadastro e armazenamento de alunos;
- **(ii)** o envio de notificações direcionadas a um curso específico;
- **(iii)** a seleção dos alunos cujo curso coincide exatamente com o curso alvo informado.

**Importante:** assuma que os dados fornecidos são sempre válidos (não é necessário tratar casos de contorno como curso inexistente, canal inválido ou lista vazia).

Implemente:

**(a)** As classes principais, com seus atributos e métodos. Deve existir ao menos uma classe responsável por armazenar e gerenciar os alunos.

**(b)** As relações adequadas entre as classes (associação, agregação, composição, herança). Indique-as diretamente no código, por meio de comentários curtos.

**(c)** Um **exemplo de uso**, simulando o envio de notificações (ao menos uma por e-mail e uma por SMS) para cursos diferentes, exibindo no console quais alunos receberam cada notificação.

**(d)** Examine sua implementação com base nos princípios **SRP** e **OCP**. Para cada um, analise sua aplicação na estrutura do código, indicando trechos específicos que fundamentem sua avaliação. Caso identifique limitações ou violações, descreva uma alteração concreta no design que poderia melhorar a solução.

**Dica:** comece pelo diagrama de classes (as caixas e as setas) antes de escrever código.



### 6.2 Classifique e justifique

Para cada par abaixo, classifique o relacionamento (associação, agregação, composição ou herança) e justifique, dizendo em que sistema você está pensando:

1. Biblioteca e Livro
2. Carro e Motor
3. Playlist e Música
4. Funcionário e Gerente
5. Turma e Aluno



### 6.3 Refatorando uma classe com muitos motivos para mudar

A classe abaixo guarda uma lista de produtos, calcula descontos conforme o tipo de cliente e imprime um relatório:

```python
class Loja:

    def __init__(self, produtos):
        self.produtos = produtos

    def desconto(self, tipo_cliente, valor):
        if tipo_cliente == "comum":
            return valor
        elif tipo_cliente == "vip":
            return valor * 0.9
        elif tipo_cliente == "funcionario":
            return valor * 0.7

    def imprimir_relatorio(self, tipo_cliente):
        for nome, preco in self.produtos:
            print(f"{nome}: R$ {self.desconto(tipo_cliente, preco):.2f}")
```

1. Quais são os **motivos para mudar** dessa classe?
2. O que você precisaria editar para acrescentar um tipo de cliente novo?
3. Refatore o código para respeitar SRP e OCP, e desenhe o diagrama de classes da sua solução.
