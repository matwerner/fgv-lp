# Introdução à Programação Orientada a Objetos (POO)

## 1. Introdução à Programação Orientada a Objetos (POO)

### 1.1. O que é POO e por que usá-la?

* **Programação Orientada a Objetos (POO)**  um paradigma de programação que organiza o código em torno de objetos, que representam entidades do mundo real. Um objeto possui atributos (dados) e métodos (ações), e é uma instância de uma classe (uma espécie de molde ou modelo). Em POO:
    - O programa é estruturado em objetos que interagem entre si para realizar as funcionalidades desejadas.
    - Cada objeto possui responsabilidades e pode ser chamado para executar determinadas tarefas.
    - Os principais componentes da POO são as classes e os objetos, e as interações entre eles ocorrem por meio de chamadas a métodos.

* Até agora, utilizamos Python de forma procedural:
    - Na programação procedural, o código é organizado em funções que operam sobre variáveis globais ou locais.
    - Esse paradigma foca em executar as tarefas de forma sequencial, com o controle do fluxo de dados entre as funções.

### 1.2. Diferenças entre Paradigmas:

- Procedural:
    * Organização em torno de funções e variáveis.
    * O foco está em como as funções processam os dados diretamente, seguindo uma sequência de execução definida.

- Orientado a Objetos:
    * Estrutura o código em torno de objetos, que encapsulam tanto dados quanto comportamento.
    * O foco é em quem (qual objeto) realiza as ações, e não apenas em como elas são realizadas.

### 1.3. Vantagens da POO frente ao Paradigma Procedural:

* **Organização**: A POO promove uma organização mais clara e modular do código, permitindo uma melhor separação de responsabilidades.
* **Reutilização de Código**: As classes definidas podem ser reutilizadas em diferentes partes do programa ou em outros projetos.
* **Facilidade de Manutenção**: Com o código dividido em objetos, é mais simples fazer ajustes, adicionar novas funcionalidades ou corrigir erros sem comprometer todo o sistema.

### 1.4. Exemplo Prático: Gerenciamento de Biblioteca

Um exemplo de uso da POO seria o desenvolvimento de um sistema para gerenciar uma biblioteca.
Podemos definir uma classe para representar um livro:

```python
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

# Criando um objeto da classe Book
book1 = Book("1984", "George Orwell", 1949)
print(book1.title)  # Saída: 1984
```

Neste exemplo, a classe `Book` define a estrutura básica de um livro, com atributos como `título`, `autor` e `ano de publicação`.
O objeto `book1` representa uma instância específica dessa classe.

### 1.5. Exemplo Prático: Loja Virtual

Outro exemplo seria o de uma loja virtual, com classes para representar `Produtos` (Product), `Clientes` (Customer) e `Pedidos` (Order), onde cada classe tem suas próprias responsabilidades:

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
```

Esses exemplos ilustram como a POO facilita a organização e a modelagem de sistemas do mundo real, como uma biblioteca ou uma loja virtual, proporcionando uma estrutura mais modular e escalável.

## 2. Definição de Classes e Objetos

### 2.1. O que são Classes?

* Classes são definições que criam objetos. Elas funcionam como moldes que definem os atributos e métodos que os objetos terão.
* Em Python, uma classe é criada utilizando a palavra-chave `class`. A estrutura básica de uma classe é:

```python
class NomeDaClasse:
    def __init__(self, atributos):
        # Inicialização dos atributos
        pass

    def metodo(self):
        # Comportamento do objeto
        pass
```

### 2.2. O que são Objetos?

* Objetos são instâncias de classes. Cada objeto criado a partir de uma classe possui seus próprios dados, mas compartilha a mesma estrutura de comportamento definida pela classe.
* Um objeto pode ser considerado uma entidade do mundo real, como um carro, uma pessoa ou um livro, que tem características e ações.

### 2.3. Exemplo: Criando uma Classe

Vamos criar uma classe chamada `Produto` que tem atributos como nome, preço e quantidade, e um método para aplicar um desconto:

```python
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome           # Atributo que armazena o nome do produto
        self.preco = preco         # Atributo que armazena o preço do produto
        self.quantidade = quantidade  # Atributo que armazena a quantidade disponível

    def aplicar_desconto(self, percentual):  # Método para aplicar desconto
        desconto = self.preco * (percentual / 100)
        self.preco -= desconto
        print(f"O novo preço de {self.nome} após {percentual}% de desconto é R$ {self.preco:.2f}.")

# Criando um objeto da classe Produto
produto1 = Produto("Camiseta", 50.00, 10)
print(produto1.nome)  # Saída: Camiseta
print(produto1.preco)  # Saída: 50.00
produto1.aplicar_desconto(10)  # Saída: O novo preço de Camiseta após 10% de desconto é R$ 45.00.
```

#### 2.4. Estrutura da Classe

1. Método `__init__`:
    * É chamado automaticamente quando um novo objeto é criado.
    * Inicializa os atributos do objeto com os valores passados como parâmetros.

2. Atributos:
    * Variáveis que armazenam dados específicos do objeto.
    * Podem ser acessados usando a notação de ponto (ex: produto1.preco).

3. Métodos:
    * Funções definidas dentro da classe que realizam ações relacionadas ao objeto.
    * Também são acessados usando a notação de ponto (ex: produto1.aplicar_desconto(10)).

4. O atributo `self`:
    * self é uma referência ao objeto atual, que permite acessar os atributos e métodos da classe.
    * É utilizada dentro dos métodos da classe para distinguir entre atributos da instância e variáveis locais.
    * Por exemplo, em self.nome, self refere-se ao objeto específico que está sendo manipulado no momento.

## 3. Atributos

Os atributos são variáveis que armazenam informações sobre um objeto.
Em Python, podemos classificar os atributos em três categorias principais: atributos de classe, atributos de objeto e variáveis de método.

### 3.1. Atributos de Classe

* Os atributos de classe são compartilhados entre todas as instâncias (objetos) da classe;
* Eles são definidos diretamente dentro da classe e são acessíveis a todos os objetos da classe;
* Isso significa que, se um atributo de classe for modificado, a alteração será refletida em todos os objetos que compartilham esse atributo;
* Ou seja, é equivalente a um variável global dentro do contexto de uma classe.

```python
class Produto:
    taxa_imposto = 0.2  # Atributo de classe

    def __init__(self, nome, preco):
        self.nome = nome  # Atributo de objeto
        self.preco = preco  # Atributo de objeto

# Acessando o atributo de classe
print(Produto.taxa_imposto)  # Saída: 0.2
```

### 3.2. Atributos de Objeto

* Os atributos de objeto são específicos de cada instância da classe;
* Cada objeto pode ter valores diferentes para esses atributos, que são definidos dentro do método `__init__` (construtor da classe);
* Quando um novo objeto é criado, esses atributos são inicializados com os valores passados.

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome  # Atributo de objeto
        self.preco = preco  # Atributo de objeto

produto1 = Produto("Livro", 30)
produto2 = Produto("Caneta", 5)

print(produto1.nome)  # Saída: Livro
print(produto2.nome)  # Saída: Caneta
```

### 3.3. Variáveis de Método

* As variáveis de método são aquelas que são definidas dentro de um método e existem apenas enquanto o método está sendo executado;
* Elas não estão associadas a uma instância específica ou à classe em si;
* Ou seja, tem o mesmo comportamento de uma variavel dentro de uma função.

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def calcular_preco_final(self):
        desconto = 0.1  # Variável de método
        return self.preco * (1 - desconto)

produto = Produto("Notebook", 1000)
print(produto.calcular_preco_final())  # Saída: 900.0
```

## 4. Métodos

Os métodos são funções que são definidas dentro de uma classe e realizam ações usando os atributos dessa classe.
Eles representam o comportamento dos objetos e são invocados para interagir com os dados que a classe encapsula.

### 4.1 O Parâmetro self

O `self` é uma referência ao objeto atual.
Ele permite que os métodos acessem os atributos e outros métodos da classe.
Em comparação com a programação procedural, onde as funções não precisam de um parâmetro para referenciar um objeto, em POO, o self é essencial para acessar o estado e o comportamento do objeto.

### 4.2. Métodos de Instância

Os métodos de instância operam em objetos específicos da classe.
Quando um método de instância é chamado, ele tem acesso ao estado (atributos) do objeto em que foi chamado.
Isso permite que o método realize operações que variam de acordo com os dados do objeto.

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        self.preco -= desconto
        print(f"Novo preço de {self.nome}: R$ {self.preco:.2f}")

# Criando um objeto da classe Produto
produto1 = Produto("Caderno", 10)
produto1.aplicar_desconto(10)  # Saída: Novo preço de Caderno: R$ 9.00
```

### 4.3. Interação entre Objetos

Um método pode interagir com outros objetos.
Isso significa que um objeto pode chamar métodos de outros objetos, permitindo um comportamento mais dinâmico e colaborativo entre as instâncias.

```python
class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def info(self):
        return f'Nome: {self.nome}, Telefone: {self.telefone}'

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def listar_contatos(self):
        for contato in self.contatos:
            print(contato.info())

# Criando contatos
contato1 = Contato("Alice", "1234-5678")
contato2 = Contato("Bob", "8765-4321")

# Criando agenda e adicionando contatos
minha_agenda = Agenda()
minha_agenda.adicionar_contato(contato1)
minha_agenda.adicionar_contato(contato2)

# Listando contatos
minha_agenda.listar_contatos()
```

## 5. Exercícios

**Exercício 1**: Crie uma classe Produto.

* Crie uma classe Produto com os atributos nome (string) e preco (float).
* Adicione um método `descricao()` que retorne uma string com o nome e o preço.
* Crie um objeto da classe Produto e exiba a descrição.

**Exercício 2**: Crie uma classe CarrinhoDeCompras.

* Crie uma classe CarrinhoDeCompras com um atributo itens (lista).
* Adicione um método `cadicionar_produto(produto)` que adiciona um produto à lista.
* Adicione um método `total_itens()` que retorna a quantidade de itens no carrinho.
* Crie alguns produtos, adicione-os ao carrinho e exiba a quantidade total.