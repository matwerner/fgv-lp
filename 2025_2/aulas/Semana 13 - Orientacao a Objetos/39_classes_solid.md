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
