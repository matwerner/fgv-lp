# Orientação a Objetos: Pilares principais

## 1. Introdução

A Programação Orientada a Objetos (POO) surgiu como resposta à crescente complexidade dos sistemas de software.
Em programas pequenos, a abordagem **procedural** (baseada em funções e estruturas de dados simples) é suficiente.
Porém, à medida que um sistema cresce, torna-se difícil manter o controle sobre como os dados e as funções interagem.
Pequenas mudanças podem causar erros em diferentes partes do código, e funções começam a se repetir ou se tornar excessivamente dependentes de detalhes internos.

A orientação a objetos foi criada para resolver esse tipo de problema.
Ela propõe organizar o código em **entidades (objetos)** que representam conceitos do mundo real e combinam **dados e comportamentos** dentro de uma mesma estrutura.

## 2. O problema: exibindo mensagens em um chat

Vamos começar com um exemplo simples.
Imagine que precisamos criar a funcionalidade `exibir_chat`, responsável por mostrar o histórico de mensagens de um aplicativo.

Cada mensagem contém três informações:
* nome do remetente,
* texto,
* data de envio.

Nosso primeiro impulso é resolver isso de forma procedural.


### 2.1 Solução procedural inicial

```python
def criar_chat(mensagens):
    return {"historico": mensagens}

m1 = {"nome": "Matheus", "texto": "Olá!", "data_envio": "2025-10-25T08:00"}
m2 = {"nome": "João", "texto": "Sextou!", "data_envio": "2025-10-25T09:00"}

chat = criar_chat([m1, m2])

def exibir_chat(chat):
    for m in chat["historico"]:
        print(f"{m['nome']} {m['data_envio']}: {m['texto']}")

exibir_chat(chat)
```

Essa versão é simples, mas já contém alguns sinais de fragilidade.


### 2.2 Analisando a solução procedural

O código funciona, mas há alguns problemas de organização:

1. As **mensagens** são apenas dicionários.
   Nada garante que sempre terão os campos corretos (`nome`, `texto`, `data_envio`).

2. A função `exibir_chat` **depende da estrutura interna** dos dicionários.
   Se uma chave mudar de nome, a função quebra.
   Essa dependência cria **acoplamento alto**: qualquer mudança na estrutura dos dados exige modificar várias funções.

3. Os **dados e os comportamentos** estão separados.
   As mensagens não “sabem” como se exibir; dependem de funções externas.

4. Além disso, o código começa a se repetir. Se quisermos alterar o formato de exibição, precisamos modificar cada função que usa os mesmos dados.

Essas fragilidades ainda não são um grande problema em um programa pequeno, mas ficam sérias à medida que o sistema cresce.


### 2.3 Evoluindo o problema: diferentes tipos de mensagens

Suponha agora que queremos permitir o envio de **mensagens de texto** e **mensagens de imagem**.
As imagens devem aparecer formatadas de forma diferente, exibindo o nome do arquivo.

Podemos tentar resolver isso adicionando uma chave `"tipo"` em cada mensagem e verificando seu valor.

```python
def exibir_msg(m):
    if m["tipo"] == "texto":
        print(f"{m['nome']} {m['data_envio']}: {m['texto']}")
    elif m["tipo"] == "imagem":
        print(f"{m['nome']} {m['data_envio']}: [imagem: {m['arquivo']}]")

def exibir_chat(chat):
    for m in chat["historico"]:
        exibir_msg(m)
```

Agora temos um código mais genérico, mas o problema não desapareceu - ele piorou.

### 2.4 Coesão, acoplamento e extensibilidade

Três conceitos ajudam a avaliar a qualidade do design de um sistema:

* **Coesão**: mede o quanto cada módulo (função, classe) tem um propósito único.
  Alta coesão significa que cada parte do código faz apenas uma coisa.

* **Acoplamento**: mede o quanto partes diferentes do código dependem umas das outras.
  Baixo acoplamento facilita mudanças, pois alterar uma parte não afeta as demais.

* **Extensibilidade**: mede o quanto é fácil adicionar novos comportamentos sem alterar código existente.
  Um sistema bem projetado permite estender funcionalidades sem modificar as antigas.


### 2.5 Limitações da abordagem procedural

Quando diferentes tipos de mensagens precisam ser tratados, a abordagem procedural passa a ter **problemas estruturais**.

1. **Duplicação de lógica**: funções diferentes fazem praticamente a mesma coisa.
2. **Baixa coesão**: cada função faz mais do que deveria.
3. **Alto acoplamento**: cada função precisa conhecer detalhes internos da estrutura de dados.
4. **Dificuldade de extensão**: adicionar um novo tipo de mensagem exige modificar funções existentes.
5. **Falta de invariantes**: não há garantias de que uma mensagem sempre tenha todos os campos necessários.

Percebemos que, à medida que o sistema cresce, o código procedural se torna difícil de manter e pouco extensível.
A orientação a objetos surge justamente como uma alternativa que melhora esses aspectos.

## 3. A ideia central da Orientação a Objetos

<!-- Na orientação a objetos, buscamos **combinar dados e comportamentos** em estruturas chamadas **classes**.
Cada classe representa um conceito do domínio e define como seus objetos se comportam.

Essa mudança de paradigma traz dois benefícios principais:

1. **Organização semântica**: o código reflete o mundo real.
2. **Encapsulamento**: cada entidade controla seus próprios dados e regras. -->

Na orientação a objetos (O.O) buscamos **organizar dados e comportamentos relacionados em uma mesma estrutura**, chamada **classe**.
Cada classe serve como um “molde” que define como os objetos serão criados e como se comportam.

Um **objeto** é uma instância dessa classe - uma entidade com dados próprios e métodos que sabe executar.

Nosso objetivo agora não é aprender toda a sintaxe, mas entender o raciocínio:
na O.O., cada coisa “sabe se cuidar”.
Uma mensagem sabe se exibir, um chat sabe organizar as mensagens, e assim por diante.


### 3.1 Reescrevendo o chat de forma orientada a objetos

Vamos refazer o problema utilizando classes e objetos.

A primeira etapa é identificar as **entidades** e suas **responsabilidades**.

* `Mensagem`: conceito genérico que define o comportamento comum de todas as mensagens.
* `Chat`: responsável por armazenar e exibir o histórico de mensagens.


## 3.2 Implementação orientada a objetos

```python
# Definindo uma "classe" que representa o conceito de uma Mensagem.
# Pense na classe como um "molde" para criar mensagens.
class Mensagem:
    # O método __init__ é chamado automaticamente ao criar um novo objeto.
    # Ele define o que toda mensagem deve possuir.
    def __init__(self, nome, texto, data_envio):
        self.nome = nome
        self.texto = texto
        self.data_envio = data_envio

    # Este método define o comportamento da mensagem: exibir a si mesma.
    def exibir(self):
        print(f"{self.nome} {self.data_envio}: {self.texto}")


# Agora, o Chat também se torna uma classe.
# Ele sabe armazenar e exibir mensagens, mas não precisa conhecer os detalhes de cada mensagem.
class Chat:
    def __init__(self):
        self.historico = []

    # Método para adicionar mensagens ao chat.
    def adicionar(self, mensagem):
        self.historico.append(mensagem)

    # Método para exibir o histórico.
    def exibir(self):
        for mensagem in self.historico:
            # Note que o Chat chama o método exibir() de cada mensagem,
            # sem precisar saber o que há dentro dela.
            mensagem.exibir()

# Criando objetos (instâncias) da classe Mensagem.
m1 = Mensagem("Matheus", "Olá!", "2025-10-25T08:00")
m2 = Mensagem("João", "Sextou!", "2025-10-25T09:00")

# Criando um chat e adicionando mensagens.
chat = Chat()
chat.adicionar(m1)
chat.adicionar(m2)

# Exibindo o chat.
chat.exibir()
```

A saída será:

```
Matheus 2025-10-25T08:00: Olá!
João 2025-10-25T09:00: Sextou!
```


## 3.3 Utilizando as classes

Esse código faz exatamente o que o anterior fazia, mas de uma forma muito mais organizada.

* Cada **mensagem** sabe se exibir.
* O **chat** não precisa conhecer os detalhes de como as mensagens são estruturadas.
* É possível criar facilmente novos tipos de mensagem (imagem, áudio, etc.) sem alterar o código do chat.

A principal mudança aqui é de **organização de responsabilidades**:
em vez de termos funções que manipulam dados genéricos, agora temos objetos que sabem agir sobre si mesmos.

## 3.4 Comparando com a solução procedural

Na versão procedural:
* Os dados (dicionários) e os comportamentos (funções) estavam separados.
* O código era fortemente acoplado.
* A manutenção seria difícil conforme o sistema crescesse.

Na versão orientada a objetos:
* Cada classe tem uma função clara e bem definida.
* As responsabilidades estão distribuídas.
* O código se torna mais próximo do mundo real e mais fácil de entender.


## 4. Fundamentos da Orientação a Objetos

A O.O. se apoia em quatro princípios fundamentais que tornam o código mais organizado, extensível e fácil de manter.

## 4.1 Como a O.O. melhora o design

Quando passamos a organizar o código em classes:

1. A **coesão** aumenta:
   cada classe tem uma única responsabilidade.
   `MensagemTexto` trata apenas de mensagens de texto, `Chat` apenas organiza o histórico.

2. O **acoplamento** diminui:
   O `Chat` não conhece os detalhes internos das mensagens.
   Ele apenas chama `exibir()`, independentemente do tipo.

3. A **extensibilidade** melhora:
   Para criar uma nova mensagem, basta criar uma nova classe.
   O sistema cresce por **adição**, não por **modificação**.

Essas propriedades reduzem erros, aumentam o reuso e tornam o sistema mais previsível.

## 4.2 Os quatro pilares da O.O.

A orientação a objetos se apoia em quatro princípios fundamentais.

**Abstração**
Foca no que o objeto faz, não em como faz.
A classe `Mensagem` define o que é essencial para qualquer mensagem, escondendo detalhes de implementação.

**Encapsulamento**
Protege os dados dentro de uma classe.
Os atributos e métodos ficam agrupados e controlados, reduzindo dependências externas.

**Herança**
Permite criar novas classes baseadas em outras, reutilizando e estendendo comportamentos.
Por exemplo, `MensagemImagem` poderia herdar de `Mensagem`.

**Polimorfismo**
Permite tratar objetos diferentes de forma uniforme.
O `Chat` pode chamar `exibir()` em qualquer tipo de mensagem, sem precisar saber qual é.


## 4.3 Benefícios práticos

* Código mais legível e coerente com o domínio do problema.
* Facilidade para adicionar novas funcionalidades.
* Menor risco de regressões ao evoluir o sistema.
* Reuso de código por herança e abstração.
* Melhor isolamento de erros e validações.
* Estrutura mais previsível e escalável.


## 5. Exercício

1. Copie o código da classe `Mensagem` mostrado.
2. Crie uma nova classe chamada `MensagemImagem`, semelhante à `Mensagem`, mas que possua um atributo `arquivo` e um método `exibir` que mostre:

   ```
   [imagem: nome_arquivo]
   ```
3. Adicione uma instância de `MensagemImagem` ao `Chat` e chame o método `exibir()`.
4. Responda, em texto:

   * Qual foi a principal diferença entre o código procedural e o código orientado a objetos?
   * Por que o `Chat` não precisou ser alterado quando criamos um novo tipo de mensagem?
   * O que significa dizer que “cada objeto sabe cuidar de si mesmo”?

Essas perguntas ajudam a consolidar o entendimento conceitual da orientação a objetos e dos motivos pelos quais ela é usada.
