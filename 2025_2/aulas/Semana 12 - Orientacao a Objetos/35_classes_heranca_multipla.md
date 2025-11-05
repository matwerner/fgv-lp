# [RASCUNHO] Orientação a Objetos: Herança Múltipla

## 1. Introdução

Anteriormente, vimos que uma classe pode herdar os atributos e métodos de uma outra classe.
Nesse contexto, chamamos a primeira classe de *derivada* e a segunda de *base*.
Naturalmente, isso nos leva a uma pergunta que costuma aparecer em todas as turmas:

> **Uma classe pode herdar de mais de uma classe ao mesmo tempo?**

Em Python, a resposta é sim.

Quer dizer… **“sim”**.

As aspas existem porque, embora Python permita herança múltipla nativamente, isso não é comum ou padrão em todas as linguagens orientadas a objetos.
Por exemplo: Java **não** permite herança múltipla de classes - mas oferece *interfaces*, que são uma forma de suprir parte da necessidade. C# idem. C++ permite.

Ou seja: Python, nesse ponto, é mais flexível. Mas essa flexibilidade vem com um preço:

> Herança múltipla pode ser poderosa, mas deve ser usada com cuidado e responsabilidade.

Por quê?

Porque herdar de várias classes ao mesmo tempo aumenta as chances de conflito:
de comportamento, de sentido semântico (ontologia), de ordem de resolução de métodos, de dependência de inicialização, etc.

Então o objetivo dessa aula é:
* explicar quando faz sentido usar herança múltipla
* como Python resolve conflitos
* qual é a regra de ouro para fazer isso de forma correta

## 2. Herança múltipla

Quando herdamos de múltiplas classes em Python, é comum que exista **uma classe principal** e outras classes **satélite**.

Ou seja: na maioria dos casos de uso corretos, teremos:

* uma classe mãe que representa o *conceito* que estamos modelando (classe de domínio)
* outras classes menores, que adicionam comportamentos específicos (normalmente chamadas de **mixins**)

Essa distinção é crucial para evitar abusos.

### 2.1 A classe principal (domínio)

A classe principal é a que define o “tipo” do objeto.

Ela responde a pergunta: **“o que essa classe é?”**

Ex: `Pedido`, `Conta`, `Personagem`, `Pagamento`.
Ela carrega o significado semântico do objeto.

### 2.2 As classes satélites (funcionalidades extras)

As classes satélites não representam um novo tipo de coisa.
Elas representam um *comportamento utilitário* que pode ser plugado em vários tipos distintos.

Exemplos comuns:

* log
* serialização
* validação
* auditoria
* métricas
* timestamp

Essas classes satélite são chamadas de **mixins**.

Elas não fazem sentido se usadas sozinhas.
Elas só fazem sentido quando combinadas com uma classe principal.

### 2.3 O anti-padrão fatal

O maior erro que alunos podem cometer ao usar herança múltipla é tentar herdar de duas classes de domínio ao mesmo tempo.

Exemplo ruim:

```python
class Diretor(Pessoa, ContaBancaria):
    ...
```

Diretor **não é** uma ContaBancaria.
Diretor **tem** uma conta bancária.
→ este caso deveria ser modelado com **composição**, não com herança.

### 2.4 Method Resolution Order (MRO)

Mas se podemos herdar de duas ou mais classes, então surge uma dúvida inevitável:

> Se duas classes possuírem o mesmo método, qual delas será usada?

Para responder isso, precisamos entender o **MRO** - Method Resolution Order.
O MRO é a ordem que o Python segue para procurar métodos e atributos quando chamamos algo via `self`.

E aqui existe uma armadilha pedagógica:
O MRO se parece “mais ou menos com uma DFS” (depth first search), porém **isso não é verdade.**

Às vezes o MRO *parece* uma DFS.
Mas não é DFS.
E você não deve raciocinar como se fosse.

#### C3 linearization

O Python usa o algoritmo chamado **C3 linearization**.
Esse algoritmo tenta criar uma ordem linear para busca considerando **toda a hierarquia** de forma consistente, preservando:
1. a ordem local declarada dos pais
2. a monotonicidade: uma classe filha não pode quebrar a ordem entre ancestrais
3. a ausência de duplicações (um pai só aparece uma vez na sequência final)

Quando essas 3 condições não podem ser satisfeitas ao mesmo tempo, o Python não tenta “forçar” uma linearização - ele simplesmente dá erro.

Para inspecionar o MRO de uma classe, usamos:

```python
ClasseX.mro()
# ou
ClasseX.__mro__
# ou
help(ClasseX)
```

E esse hábito de olhar o MRO **é essencial** quando trabalhamos com herança múltipla.

### 2.5 a importância do `super()`

Se uma classe participa de herança múltipla, ela precisa “cooperar”.

Se ela não chamar `super()`, ela interrompe a cadeia.
E isso vai quebrar o fluxo de inicialização.

Por isso, o `super()` não deve ser visto como “pai direto”.
Ele deve ser visto como “o próximo da sequência do MRO”.

Então em herança múltipla, todos os `__init__` envolvidos precisam:

* aceitar `*args, **kwargs` (ou combinar assinaturas)
* chamar `super().__init__(...)` no final

É assim que todas as classes conseguem executar seu pedaço.

### 2.6 Dois pais que inicializam estado (construtores múltiplos)

Esse é o ponto mais delicado quando falamos de herança múltipla:

> se duas classes base possuem parâmetros próprios no `__init__`, como passá-los corretamente?

O primeiro impulso do aluno costuma ser:

```python
class C(A, B):
    def __init__(self, x, y):
        super().__init__(x=x, y=y)   # isso não funciona diretamente
```

Esse código gera um erro assim:

```
TypeError: A.__init__() got an unexpected keyword argument 'y'
```

**Por que deu erro?**

Porque o `super()` vai seguir o MRO e chamar primeiro o `A.__init__`.

Mas o construtor de `A` só aceita `x`.
Ele não sabe o que fazer com `y`.
Então o Python reclama.

Em herança múltipla cooperativa a regra é:

> cada classe base deve consumir somente os parâmetros que são dela, e repassar o restante para o próximo na cadeia via `**kwargs`.

Assim:

```python
class A:
    def __init__(self, *, x, **kwargs):
        super().__init__(**kwargs)  # passa o resto adiante
        self.x = x

class B:
    def __init__(self, *, y, **kwargs):
        super().__init__(**kwargs)  # passa o resto adiante
        self.y = y

class C(A, B):
    def __init__(self, x, y):
        super().__init__(x=x, y=y)
```

Agora funciona.

Fluxo real quando fazemos `C(10, 20)`:

1. C chama `super()` → cai em A (por causa do MRO)
2. A consome o `x=10` e repassa `y=20` para o próximo `super()`
3. próximo `super()` cai em B
4. B consome o `y=20` e repassa vazio para o próximo `super()`
5. próximo cai em `object.__init__`, que aceita vazio → fim

Resultado: ambos A e B inicializam seus estados.

### Inicialização alternativa (não cooperativa)

Muita gente faz assim:

```python
class C(A, B):
    def __init__(self, x, y):
        A.__init__(self, x)
        B.__init__(self, y)
```

Sim, isso “funciona” para este exemplo simples.
O problema é que esse padrão **ignora totalmente o MRO**.
Se amanhã você colocar outro mixin no meio da hierarquia, esse código manual simplesmente pula aquele construtor.

### Sobre `self.__init__`

Outro erro comum é achar que chamar:

```python
self.__init__(...)
```

vai chamar “os dois pais”.

Não vai.

`self.__init__` é simplesmente o `__init__` da classe selecionada pelo MRO atual.
É **um** método.
Não todos.

Em herança múltipla, o único mecanismo que faz todos os pais cooperarem é:

* usar `super()`
* cada classe consumir só seu pedaço
* e repassar o resto via `**kwargs`

Isso é a base técnica que faz herança múltipla funcionar corretamente em Python.

## 3. Aplicações

Agora que entendemos a base teórica da herança múltipla em Python, vamos falar sobre quando queremos usar isso.

### 3.1 Mixins

Este é o principal caso de uso real.
Mixins são classes pequenas, que implementam **um comportamento específico**, e que não representam um “tipo” de objeto.
Um mixin sozinho não faz sentido.
Ele só existe para ser combinado com uma classe de domínio.

Exemplos típicos:

* `LoggingMixin` (fornece método `log`)
* `SerializableMixin` (fornece método `to_dict`)
* `RetryableMixin` (fornece método `retry`)
* `TimestampMixin` (fornece método `timestamp`)

Isso é herança múltipla com propósito **claro**.

A classe principal continua definindo a identidade do objeto.
Os mixins adicionam ferramentas a esse objeto.

### 3.2 Interfaces (comentário breve)

Linguagens que não possuem herança múltipla normalmente introduzem **interfaces**.

Interfaces existem para definir “contratos” de comportamento:

* “essa classe *pode ser usada* como Autenticável”
* “essa classe *pode ser usada* como Pagável”
* etc.

Em Python, nós *podemos* criar contratos sem depender de herança múltipla, via abstract classes e via `Protocol`.

Mas isso será tema da próxima aula.
Hoje queremos apenas que fique claro que herança múltipla **não** é a única forma de adicionar capacidades a uma classe.

E, inclusive, em muitos casos, preferimos o uso de interfaces ou protocolos porque eles reduzem acoplamento.

## 4. Exercícios

### **Exercício 1**: Mixins

Crie uma classe `Pedido` e duas classes mixins:
* `LoggingMixin`
* `TimestampMixin`

Depois crie uma classe `PedidoRegistrado` que herde de `Pedido`, `LoggingMixin` e `TimestampMixin`.

Faça o método `registrar()` mostrar um log com timestamp.

### **Exercício 2**: Investigando MRO

Crie uma hierarquia em diamante (A → B e C → D)
e obtenha o MRO de D usando `D.mro()`.

Explique por escrito por que a ordem não é apenas DFS.

### **Exercício 3**: dois construtores

Crie duas classes base que inicializam atributos diferentes, use `super()` cooperativo, e mostre que a classe final herdada inicializa ambos os atributos corretamente.

Escreva em 2 frases porque isso só funcionou com `super()`.

### **Exercício 4**: anti-pattern

Dado o exemplo ruim:

```python
class Diretor(Pessoa, ContaBancaria):
    pass
```

Refatore usando composição.
