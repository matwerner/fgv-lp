# Orientação a objetos: SOLID

## 1. Introdução

* Em sistemas orientados a objetos, é muito comum que, conforme o código cresce, as classes comecem a acumular muitas responsabilidades, se tornem difíceis de entender e modifiquem muitas partes do sistema quando mudam.
* Esse tipo de deterioração acontece principalmente quando OO é usado “just because OO”, porém **sem princípios de design guiando as decisões**.

### Problemas comuns

Abaixo estão alguns dos problemas comuns quando OOP cresce sem orientação clara:
* classes gigantes que fazem “mil coisas”
* cada nova feature obriga editar código já existente (e quebrar coisas antigas)
* bugs aparecem em pontos **não relacionados** com onde você mexeu
* baixa testabilidade (é difícil testar partes isoladas do sistema)
* código que ninguém tem coragem de mexer

### SOLID

> Nesse contexto, os príncipios SOLID foram desenvolvidos para atacar exatamente esse tipo de deterioração.
> SOLID é composto de $5$ princípios que guiam como estruturar classes e módulos para que o código **possa crescer sem apodrecer**.


## 2. Os princípios SOLID

* **SOLID** é um acrônimo que representa os 5 princípios que ajudam a projetar classes e módulos de forma mais **mantenível, extensível e robusta**.
* Em sistemas pequenos, qualquer solução meio bagunçada “parece funcionar”.
  Em sistemas médios e grandes, a falta de SOLID normalmente explode em:
    - dificuldade de adicionar novas features sem quebrar as antigas
    - classes enormes e confusas que fazem tudo
    - código frágil que quebra em lugares inesperados
    - baixo reaproveitamento

| Letra | Nome                            | Ideia central                                                               |
| ----- | ------------------------------- | --------------------------------------------------------------------------- |
| **S** | Single Responsibility Principle | Cada classe tem **uma única razão para mudar**                              |
| **O** | Open/Closed Principle           | Código deve ser **aberto à extensão, fechado à modificação**                |
| **L** | Liskov Substitution Principle   | Subclasses devem poder **substituir** a classe base sem quebrar o código    |
| **I** | Interface Segregation Principle | Evitar **interfaces gordas** que obrigam implementar métodos que não se usa |
| **D** | Dependency Inversion Principle  | Dependa de **abstrações**, não de implementações concretas                  |

**Nesta disciplina, vamos focar em S, O, L (e um pouco de I).**
**Não entraremos em D** visto que ele exige maturidade maior no design.

Hoje vamos começar pelo primeiro deles: **S - Single Responsibility Principle**

## 3 Single Responsibility Principle (SRP)

### 3.1 O que é “Responsabilidade”?

* Responsabilidade é aquilo que define **o motivo de mudança**.

* Se uma classe possui mais de um motivo para ser alterada, ela tem mais de uma responsabilidade.

* Exemplos de motivos de mudança:

  * Regras de negócio alteraram
  * Política de logging mudou
  * São necessários formatos diferentes de saída (HTML, CSV, JSON)
  * Banco de dados ou API externos mudaram

* Se uma classe sofre alterações por motivos diferentes em contextos diferentes → **ela está violando SRP**.

### 3.2 Exemplo de Violação do SRP

* Imagine um sistema de pedidos online. Temos a seguinte classe:

  ```python
  class PedidoService:
      def __init__(self, pedido):
          self.pedido = pedido

      def calcular_total(self):
          return sum(item.preco for item in self.pedido.itens)

      def salvar_no_banco(self):
          with open("db.txt", "a") as f:
              f.write(str(self.pedido))

      def enviar_email_confirmacao(self):
          print(f"Enviando e-mail para {self.pedido.cliente_email}")
  ```

* À primeira vista, parece prático.
* Mas observe que ela tem **três razões de mudança diferentes**:

  | Motivo de mudança                                | Onde afeta                   | Tipo de responsabilidade |
  | ------------------------------------------------ | ---------------------------- | ------------------------ |
  | Regra de negócio (ex: desconto, imposto)         | `calcular_total()`           | Cálculo do pedido        |
  | Estratégia de persistência (banco, API, arquivo) | `salvar_no_banco()`          | Armazenamento            |
  | Política de comunicação com cliente              | `enviar_email_confirmacao()` | Notificação              |

* Dessa forma:
  > Se o cálculo mudar, mexemos aqui.\
  > Se trocarmos o banco, mexemos aqui.\
  > Se mudar o texto do e-mail, mexemos aqui.
  >
  > **Três motivos distintos de mudança = três responsabilidades.**

### 3.3 Aplicando SRP

* A separação natural é dividir cada “motivo de mudança” em sua própria classe:

  ```python
  class CalculadoraPedido:
      def total(self, pedido):
          return sum(item.preco for item in pedido.itens)

  class PedidoRepository:
      def salvar(self, pedido):
          with open("db.txt", "a") as f:
              f.write(str(pedido))

  class NotificadorEmail:
      def enviar_confirmacao(self, pedido):
          print(f"Enviando e-mail para {pedido.cliente_email}")
  ```

* E um **orquestrador** pode coordenar o fluxo, sem violar SRP:

  ```python
  class PedidoService:
      def __init__(self, repo, calculadora, notificador):
          self.repo = repo
          self.calc = calculadora
          self.notif = notificador

      def processar_pedido(self, pedido):
          total = self.calc.total(pedido)
          self.repo.salvar(pedido)
          self.notif.enviar_confirmacao(pedido)
          return total
  ```

* Cada classe agora:
  - muda por um único motivo
  - tem propósito singular
  - reduz a chance de quebrar outros comportamentos

### 3.4 Benefícios Diretos

* **Código mais testável**
  Testa-se cálculo sem depender de I/O, e vice-versa.

* **Código mais flexível**
  Podemos mudar a persistência (banco, csv, api) sem tocar no cálculo.

* **Código mais legível**
  Facilita entender rapidamente “o que cada classe faz”.

* **Menos efeito borboleta**
  Alterar uma parte não gera consequências imprevisíveis.

### 3.5 SRP não é “uma classe precisa ter 1 método”

* Um dos erros mais comuns ao estudar o *Single Responsibility Principle* é confundir **“responsabilidade” com “quantidade de métodos”**.

  > SRP **não significa** que uma classe deve ter apenas um método,
  > e sim que ela deve ter **uma única razão para mudar**.

* Em outras palavras:
  - uma classe pode ter **vários métodos**,
  - contanto que todos sirvam **a um mesmo propósito**,
  - e mudem **pelas mesmas razões** dentro do sistema.


#### Exemplo: uma classe coesa com múltiplos métodos

```python
class GeradorDeFaturas:
    def gerar_fatura(self, pedido):
        itens = self._filtrar_itens_validos(pedido)
        total = self._calcular_total(itens)
        impostos = self._calcular_impostos(itens)
        valor_final = total + impostos
        return {
            "cliente": pedido.cliente,
            "itens": itens,
            "total": total,
            "impostos": impostos,
            "valor_final": valor_final,
        }

    def _filtrar_itens_validos(self, pedido):
        return [item for item in pedido.itens if item.ativo]

    def _calcular_total(self, itens):
        return sum(item.preco for item in itens)

    def _calcular_impostos(self, itens):
        return sum(item.preco * 0.1 for item in itens)  # 10% de imposto
```

  * Essa classe possui quatro métodos, mas todos trabalham juntos para **cumprir uma única responsabilidade**:

    > “Gerar uma fatura a partir de um pedido.”

  * Ela **muda apenas por um motivo**:

    > Se a regra de cálculo de faturas mudar (ex: política de imposto, desconto, arredondamento, etc.).

#### Exemplo de violação

* Agora veja uma classe parecida, mas que mistura preocupações diferentes:

  ```python
  class GeradorDeFaturas:
      def gerar_fatura(self, pedido):
          fatura = self._montar_dados(pedido)
          self._salvar_no_banco(fatura)
          self._enviar_email_cliente(fatura)

      def _montar_dados(self, pedido): ...
      def _salvar_no_banco(self, fatura): ...
      def _enviar_email_cliente(self, fatura): ...
  ```

* Essa versão tem **três razões distintas para mudar**:

  | Motivo de mudança | Responsabilidade |
  | ----------------- | ---------------- |
  | Regra de cálculo  | Negócio          |
  | Persistência      | Infraestrutura   |
  | Envio de e-mail   | Comunicação      |

* Portanto, ela **viola o SRP** - porque reúne **decisões de natureza diferente** dentro de uma mesma classe.

#### Responsabilidade é relativa ao contexto

* O termo *responsabilidade* pode ser interpretado em **diferentes níveis de granularidade**, dependendo da complexidade e do propósito do sistema:

  | Nível                | Exemplo                 | Responsabilidade (nível adequado)                     |
  | -------------------- | ----------------------- | ----------------------------------------------------- |
  | Projeto pequeno      | `GeradorDeFaturas`      | gerar fatura completa                                 |
  | Sistema corporativo  | `ServicoDeFaturamento`  | coordenar múltiplos módulos de cálculo e persistência |
  | Microserviço isolado | `ModuloDeCalculoFiscal` | apenas aplicar regras tributárias                     |

> O que conta como “uma única responsabilidade” **depende da escala**.
> O que é coeso num sistema pequeno pode ser uma “bola de lama” em um sistema distribuído.

### 3.6 Dicas práticas

* Pergunta prática para ser usada como teste de SRP:

    > “Se eu mudar ‘X’ no sistema, preciso alterar esta classe?”

    Se a resposta for “depende do que você mexer”, é sinal de que ela está acumulando responsabilidade.

* Outra frase útil:

    > “Classe boa tem nome que indica a responsabilidade.
    > Se o nome começa a ficar genérico (Manager, Helper, Utils) → cheiro de violação de SRP.”

### 3.7 Exercícios Práticos

1. Analise o código abaixo. Há violação do SRP? Justifique **quais são os motivos distintos de mudança**.

    ```python
    class UsuarioService:
        def cadastrar(self, usuario):
            self.validar(usuario)
            self.salvar(usuario)
            self.enviar_email_boas_vindas(usuario)

        def validar(self, usuario): ...
        def salvar(self, usuario): ...
        def enviar_email_boas_vindas(self, usuario): ...
    ```

2. Pegue o exemplo `PedidoService` e:
    * Escreva um teste unitário **antes da refatoração**. O que é difícil de isolar?
    * Depois refatore aplicando SRP e tente novamente. O que ficou mais simples de testar?

3. Dado o bloco de código abaixo:

    * Quais são as responsabilidades?
    * Que classes/objetos poderiam ser extraídos?

    ```python
    class PedidosController:
        def listar(self): ...
        def criar(self, dados): ...
        def validar_formato(self, dados): ...
        def enviar_email_confirmacao(self, dados): ...
    ```

    > Dica: controladores **devem coordenar**, não **fazer tudo**.

4. Imagine uma classe `RelatorioVendas` de 400 linhas que:

    * lê CSV de vendas,
    * calcula estatísticas,
    * gera gráficos,
    * exporta para PDF,
    * envia o relatório por e-mail.

    Liste as **responsabilidades distintas** e desenhe um possível conjunto de classes mais coesas.

Aqui está a **continuação natural** da sua aula — mantendo exatamente o mesmo tom, profundidade, estrutura e estilo.
O texto está pronto para virar **slide, PDF ou leitura de apoio**.
Ele segue diretamente após a seção do **SRP**, como você pediu.

## 4 Open/Closed Principle (OCP)

### 4.1 O que é OCP?

> **Uma classe deve estar aberta para extensão, mas fechada para modificação.**
> Ou seja: você deve poder adicionar novos comportamentos *sem precisar editar código já existente*.

A ideia é simples:

* quando surge um novo caso de uso,
* **você cria código novo** (ou novos dados/configurações), ao invés de
* editar código antigo (e correr risco de quebrar o sistema inteiro).

Muitas vezes isso é feito com polimorfismo, mas também pode ser feito
com **modelagem por dados**: em vez de encher o código de `if`, você
transforma variações em *configuração* (por exemplo, cupons diferentes).

### 4.2 Mau exemplo: violando OCP com ifs infinitos

Suponha um e-commerce com produtos e cupons simples (OFF10, OFF20, etc):

```python
class Produto:
    def __init__(self, nome, categoria, preco):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
```

Uma primeira implementação “ingênua” para aplicar cupons:

```python
def aplicar_cupom(produto: Produto, cupom: str) -> float:
    preco = produto.preco

    if cupom == "OFF10":
        # 10% em qualquer coisa
        return preco * 0.90

    elif cupom == "OFF20_ELETRONICOS":
        # 20% só para eletrônicos
        if produto.categoria == "ELETRONICOS":
            return preco * 0.80
        else:
            return preco

    elif cupom == "OFF15_LIVROS":
        # 15% só para livros
        if produto.categoria == "LIVROS":
            return preco * 0.85
        else:
            return preco

    # ...

    return preco
```

Problemas:

* cada novo cupom → você **edita a função** e adiciona mais um `elif`
* a função cresce sem parar e fica difícil de entender
* a regra de validação fica espalhada em `if`/`else`
* é difícil testar um cupom isoladamente
* qualquer alteração num cupom pode quebrar outro caso sem querer

Aqui o código está **fechado para extensão** e **aberto para sofrimento**:
qualquer mudança na política de cupons obriga mexer no miolo dessa função.

### 4.3 Boa solução: OCP com polimorfismo

Em vez de encher a função de regras específicas, podemos:

* modelar o cupom como um **objeto de dados** com regras genéricas
* fazer a função de cálculo trabalhar **sempre da mesma forma**
* criar/alterar cupons apenas instanciando objetos (ou via banco/config)

```python
class Cupom:
    def __init__(
        self,
        codigo: str,
        desconto_percentual: float,
        categorias_permitidas: list[str] | None = None,
        produtos_permitidos: list[str] | None = None,
    ):
        self.codigo = codigo
        self.desconto_percentual = desconto_percentual
        self.categorias_permitidas = categorias_permitidas or []
        self.produtos_permitidos = produtos_permitidos or []

    def eh_valido_para(self, produto: Produto) -> bool:
        if self.categorias_permitidas and produto.categoria not in self.categorias_permitidas:
            return False
        if self.produtos_permitidos and produto.nome not in self.produtos_permitidos:
            return False
        return True

    def aplicar(self, produto: Produto) -> float:
        if not self.eh_valido_para(produto):
            return produto.preco
        fator = 1 - (self.desconto_percentual / 100.0)
        return produto.preco * fator
```

Função que usa o cupom:

```python
def calcular_preco_com_cupom(produto: Produto, cupom: Cupom | None) -> float:
    if cupom is None:
        return produto.preco
    return cupom.aplicar(produto)
```

Como ficam os cupons?

```python
OFF10 = Cupom(
    codigo="OFF10",
    desconto_percentual=10.0,
)

OFF20_ELETRONICOS = Cupom(
    codigo="OFF20_ELETRONICOS",
    desconto_percentual=20.0,
    categorias_permitidas=["ELETRONICOS"],
)

OFF15_LIVROS = Cupom(
    codigo="OFF15_LIVROS",
    desconto_percentual=15.0,
    categorias_permitidas=["LIVROS"],
)
```

Na vida real esses cupons poderiam vir de:

* uma tabela no banco
* um arquivo de configuração
* uma API de administração

Mas o ponto central é:

* a função `calcular_preco_com_cupom` **não precisa mudar**
* a lógica de aplicação de cupom **não precisa mudar**
* novos cupons são criados **sem modificar o código existente**, apenas adicionando novos dados/instâncias

Isso é OCP aplicado de forma simples:

> O comportamento varia porque adicionamos **novos cupons**,
> não porque mexemos na função de cálculo.

### 4.4 Na prática, quando OCP vale a pena?

Use OCP quando:

* **variações são naturais** (ex.: cupons, promoções, filtros, ordenações)
* **novos comportamentos surgem com frequência**
* você quer que a regra geral do sistema **continue estável**, enquanto só adiciona “peças” na borda (cupons, plugins, estratégias, etc.)

Não use OCP quando:

* você só quer evitar meia dúzia de `if` simples
* não é esperado que essa parte do código mude tanto
* a solução “genérica” deixaria tudo mais confuso que o problema

> OCP não tem a ver com “remover todos os `if` do mundo”.
> Tem a ver com **fazer o código crescer por adição**, e não por remendo.

## 5 Liskov Substitution Principle (LSP)

### 5.1 O que é LSP?

> **Subtipos devem ser substituíveis pela classe base sem quebrar o sistema.**

Isso significa:

* Se `B` herda `A`,
* então `B` **não pode diminuir** o que `A` promete fazer,
* nem **alterar drasticamente** como `A` se comporta,
* nem **exigir mais do que `A` exige**.

Em termos mais simples:

> Se uma função aceita um `A`, deve funcionar perfeitamente se eu enviar um `B`.

### 5.2 Violando LSP na prática

#### Superclasse

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False
```

Contrato implícito:

* `withdraw` nunca dá exceção
* sempre retorna True/False
* saque é permitido se houver saldo

#### Subclasse problemática

```python
class FrozenAccount(BankAccount):
    def withdraw(self, amount):
        raise Exception("Account is frozen")
```

**Isso viola LSP**, porque:

* mudou a *forma* de responder
* comportamento esperado (retornar bool) virou exceção
* código que usa `BankAccount` quebra

Por exemplo:

```python
def process_withdraw(account: BankAccount, amount):
    if account.withdraw(amount):
        print("OK")
    else:
        print("Saldo insuficiente")
```

Passar uma `FrozenAccount` faz o sistema explodir.

### 5.3 Por que isso viola LSP formalmente?

Quando você herda uma classe, você herda o “contrato comportamental” dela:

* pré-condições não podem ser mais restritas
  (não pode aceitar menos)
* pós-condições não podem ser mais fracas
  (não pode devolver algo menos útil)
* invariantes devem ser mantidos
  (estado essencial deve permanecer válido)

`FrozenAccount` quebra tudo isso.

### 5.4 Solução correta (em vez de herança)

Herança foi a escolha errada. O correto é **composição**:

```python
class WithdrawalBlocker:
    def __init__(self, base_account):
        self.base = base_account

    def withdraw(self, amount):
        raise Exception("Blocked")

    def deposit(self, amount):
        return self.base.deposit(amount)
```

Agora você não mente:
**WithdrawalBlocker NÃO é um tipo de BankAccount.**

### 5.5 Outro exemplo

```python
class User:
    def access(self):
        return "acesso básico"

class Admin(User):
    def access(self):
        return "acesso avançado"
```

Isso é OK.

Mas se alguém fizer:

```python
class Guest(User):
    def access(self):
        raise Exception("Guests cannot access")
```

→ Violou LSP
→ Subclasse que não substitui o pai
→ Composição seria mais apropriada

## 6 Interface Segregation Principle (ISP)

### 6.1 O que é ISP?

> “Não obrigue ninguém a depender de métodos que não usa.”

Ou:
Interfaces devem ser **pequenas**, **focadas**, **específicas**.

Quando uma interface tem 12 métodos, todo mundo vira refém dela.

### 6.2 Mau exemplo: interface “polvo”

```python
class Repository:
    def save(self): ...
    def update(self): ...
    def delete(self): ...
    def search(self): ...
```

Se você só quer buscar dados, é obrigado a implementar tudo.

### 6.3 Boa solução: interfaces pequenas e precisas

```python
class Searchable:
    def search(self): ...

class Writable:
    def save(self): ...
    def update(self): ...
```

Benefícios:

* classes implementam só o que precisam
* testabilidade melhora
* evita “interfaces de 20 métodos”
* reduz acoplamento

Em Python, isso pode ser feito naturalmente via **Protocols**:

```python
from typing import Protocol

class Searchable(Protocol):
    def search(self): ...
```

### 6.4 ISP na vida real

ISP fica evidente quando:

* você tem repositórios que leem e escrevem,
  mas alguns serviços só devem ler
* APIs externas onde nem tudo faz sentido para todos
* quando misturar responsabilidades em interfaces força gambiarras
