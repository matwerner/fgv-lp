# Relacionamento entre Classes: Associação, Agregação e Composição

## 0. Introdução:

* No desenvolvimento de sistemas orientados a objetos, é essencial entender **como os objetos se relacionam entre si**.
* Esses relacionamentos determinam o design do sistema, a forma como as classes interagem e como o código será mantido e expandido no futuro.
* Saber escolher entre diferentes tipos de relações ajuda a garantir que o sistema seja **modular**, **flexível** e **fácil de modificar**.

* As respostas para essas perguntas nos levam a três tipos principais de relacionamento entre classes:
    1. **Associação**: Os objetos se conhecem, mas podem se relacionar com outros objetos do mesmo tipo.
    2. **Agregação**: Um objeto "contém" outro, mas ambos podem existir de forma independente.
    3. **Composição**: Um objeto faz parte de outro e perde seu propósito de existir se o "todo" for destruído.

* Imagine três situações:
    1. **Uma pessoa e um endereço**: Uma pessoa pode ter um endereço associado a ela, mas o endereço também pode existir separadamente (`associação`).
    2. **Um carro e seu motor**: O carro depende do motor para funcionar, e sem o carro, o motor perde seu propósito (`composição`).
    3. **Um departamento e seus funcionários**: O departamento é composto por funcionários, mas se o departamento for dissolvido, os funcionários ainda podem trabalhar em outro lugar (`agregação`).
* Esses exemplos ilustram três tipos diferentes de relacionamentos: `associação`, `composição` e `agregação`.

* Vamos agora explorar cada tipo de relacionamento em detalhes.

## 1. Associação

* A **associação** é o tipo de relacionamento mais simples.
* **Objetos de classes diferentes se relacionam**, mas **podem existir de forma independente** e podem também se relacionar com outros objetos.
* Nesse cenário, um objeto apenas "conhece" ou faz uso do outro.

### Características da Associação:
- **Independência**: Os objetos podem viver separadamente.
- **Relacionamento flexível**: Um objeto pode se relacionar com outros objetos do mesmo tipo.
- **Apenas referência**: Não há posse ou controle sobre o ciclo de vida de outros objetos.

### Exemplo de Associação:
* Uma **pessoa** e seu **endereço**. A pessoa pode ter um endereço associado, mas ambos podem existir independentemente. A pessoa pode mudar de endereço, e o endereço pode ser associado a outra pessoa.

    ```python
    # Exemplo de Associação
    class Pessoa:
        def __init__(self, nome):
            self.nome = nome
            self.endereco = None  # A pessoa pode ter um endereço, mas não é obrigatório
        
        def set_endereco(self, endereco):
            self.endereco = endereco

    class Endereco:
        def __init__(self, rua, numero):
            self.rua = rua
            self.numero = numero

    # Criação de uma pessoa e um endereço, que podem existir separadamente
    pessoa = Pessoa("João")
    endereco = Endereco("Rua das Flores", 123)

    # Associando a pessoa ao endereço
    pessoa.set_endereco(endereco)

    print(f"{pessoa.nome} mora na {pessoa.endereco.rua}, número {pessoa.endereco.numero}.")utor)
    ```

### Tipo de Relacionamento:
- **Relacionamento flexível e temporário**. Cada objeto conhece o outro, mas **não depende dele** para existir ou ser destruído. Ambos podem coexistir e se associar com outros objetos.

## 2. Agregação

* A **agregação** é um tipo de associação, mas com uma estrutura de "todo-parte".
* **Um objeto é dono de outro**, mas eles **podem existir de forma independente**.
* O objeto "todo" pode agregar partes, mas a destruição do todo não implica na destruição das partes.

### Características da Agregação:
* **Independência das partes**: As partes agregadas podem existir fora do todo.
* **Relação de "todo-parte"**: O todo é dono das partes, mas as partes podem ser usadas em outros contextos.
* **Ciclo de vida independente**: As partes não são destruídas junto com o todo.

### Exemplo:
* Um **departamento** e seus **funcionários**. O departamento pode ser dissolvido, mas os funcionários continuam a existir e podem trabalhar em outros departamentos.

    ```python
    # Exemplo de Agregação
    class Departamento:
        def __init__(self, nome):
            self.nome = nome
            self.funcionarios = []  # O departamento agrega funcionários
        
        def adicionar_funcionario(self, funcionario):
            self.funcionarios.append(funcionario)

    class Funcionario:
        def __init__(self, nome):
            self.nome = nome

    # Criação de um departamento e funcionários
    dep = Departamento("TI")
    func1 = Funcionario("Alice")
    func2 = Funcionario("Bob")

    # Adicionando funcionários ao departamento
    dep.adicionar_funcionario(func1)
    dep.adicionar_funcionario(func2)

    print(f"Funcionários do departamento {dep.nome}: {[f.nome for f in dep.funcionarios]}")
    ```

### Tipo de Relacionamento:
* **Relacionamento de "todo-parte"**, mas as partes mantêm **autonomia**. As partes podem existir fora do contexto do todo e se relacionar com outros objetos.

## 3. Composição

* A **composição** é o relacionamento mais forte entre classes.
* Aqui, um objeto faz **parte integrante de outro** e **não pode existir sem ele**.
* Se o objeto "todo" é destruído, as partes que o compõem também são destruídas, pois não têm razão para existir de forma isolada.

### Características da Composição:
* **Dependência forte**: As partes dependem do todo para existir.
* **Relação de "todo-parte" mais rígida**: O todo é dono absoluto das partes.
* **Ciclo de vida compartilhado**: Se o todo for destruído, as partes também são destruídas.

### Exemplo:
* Um **carro** e seu **motor**. O carro é responsável pela existência do motor, e se o carro for destruído, o motor perde sua razão de existir no contexto do sistema.

    ```python
    # Exemplo de Composição
    class Carro:
        def __init__(self, modelo):
            self.modelo = modelo
            self.motor = Motor()  # O motor faz parte integral do carro

    class Motor:
        def __init__(self):
            self.potencia = 150  # Potência fictícia do motor

    # Criação de um carro, o motor é parte integral do carro
    carro = Carro("Sedan")

    print(f"O carro modelo {carro.modelo} tem um motor com potência de {carro.motor.potencia} cavalos.")
    ```

### Tipo de Relacionamento:
* **Relação de "todo-parte" com dependência absoluta**. O objeto "parte" **não pode existir fora** do "todo" e é destruído quando o todo é destruído.

## 4. Comparação Resumida

| Tipo de Relacionamento | Descrição                                                                 | Exemplo                            | Dependência |
|------------------------|---------------------------------------------------------------------------|------------------------------------|-------------|
| **Associação**          | Objetos se conhecem e se relacionam, mas podem existir de forma independente. | Pessoa e Endereço                  | Nenhuma     |
| **Agregação**           | Um objeto contém outro, mas ambos podem viver de forma independente.        | Departamento e Funcionários         | Parcial     |
| **Composição**          | Um objeto faz parte de outro e é destruído junto com o "todo".              | Carro e Motor                      | Total       |


## 5. Quando Usar Cada Tipo de Relacionamento?

* Entender o tipo de relacionamento entre as classes é crucial para garantir que o design de software seja **flexível**, **reutilizável** e **modular**.
* Usar o relacionamento adequado facilita mudanças no sistema sem causar grandes impactos no restante do código.

    - **Associação** é ideal quando as classes precisam se comunicar, mas não devem depender uma da outra.
    - **Agregação** é útil quando o "todo" precisa controlar as "partes", mas estas podem ser compartilhadas ou reutilizadas em outros contextos.
    - **Composição** deve ser usada quando as partes são dependentes do todo e não fazem sentido fora dele.


## 6. Cenários Ambíguos

* Os cenários ambíguos são situações em que as relações entre classes podem não ser imediatamente claras, levando a diferentes interpretações.
* Vamos explorar três exemplos práticos para entender melhor essa complexidade e promover a discussão.

### Cenário 1: Vagas de Emprego e Empresas

* Uma empresa oferece várias vagas de emprego. Cada vaga pode ser preenchida por um candidato, mas um candidato pode se inscrever em várias vagas de diferentes empresas.

    * **Pergunta**: Como podemos classificar o relacionamento entre a classe Empresa e a classe Vaga?
    * **Reflexão**: Este cenário sugere uma associação, onde cada empresa pode ter várias vagas, e cada vaga pode ser associada a diferentes empresas. O que acontece se considerarmos que uma vaga específica deve estar vinculada a uma única empresa?

### Cenário 2: Posts e Comentários

* Um usuário pode criar vários posts em uma plataforma de redes sociais. Cada post pode ter vários comentários feitos por diferentes usuários, mas um comentário específico pertence a apenas um post.
    * **Pergunta**: Qual é a relação entre as classes Post e Comentario?
    * **Reflexão**: Esse relacionamento pode ser considerado uma composição, onde um comentário existe dentro do contexto de um post. O que implicaria se um post fosse deletado? Os comentários também seriam deletados, reforçando a ideia de que eles não podem existir independentemente de um post.

### Cenário 3: Carrinho de Compras e Produtos

* Um carrinho de compras pode conter vários produtos, mas cada produto pode ser adicionado a diferentes carrinhos de compras em diferentes momentos.
    * **Pergunta**: Como classificar a relação entre a classe Carrinho e a classe Produto?
    * **Reflexão**: Este cenário sugere uma agregação, onde o carrinho de compras "possui" produtos, mas esses produtos podem existir independentemente em outros carrinhos. Se um carrinho for esvaziado, os produtos ainda permanecerão disponíveis para serem adicionados a outros carrinhos.

## 6. Exercícios Práticos

1. **Desafio 1: Sistema de Biblioteca**
   Modele um sistema de gerenciamento de uma biblioteca. Defina as classes **Livro**, **Biblioteca**, **Autor** e **Usuário**. Decida onde aplicar associação, composição e agregação, justificando suas escolhas.

2. **Desafio 2: Sistema de e-commerce**
   Modele um sistema de pedidos em um site de e-commerce. Um **Pedido** contém **Itens** e está associado a um **Cliente**. Determine como modelar os relacionamentos e explique se usaria composição ou agregação.

3. **Desafio 3: Jogo Snake**
   Modele um jogo simples como **Snake**. Considere que o **jogo** contém a **cobra** e a **comida**. Defina como esses objetos devem se relacionar. Se o **jogo** for encerrado, a cobra e a comida continuam existindo? Como você modelaria esses relacionamentos?

4. **Desafio 4: Sistema de Saúde**
   Modele um sistema para gerenciamento de **consultas médicas**. Defina as classes **Paciente**, **Médico**, **Recepcionista** e **Consulta**. Explore como esses objetos devem se relacionar, pensando na dependência entre eles. Como você organizaria o ciclo de vida de cada objeto?

5. **Desafio 5: Sistema de Herança**
   Introduza um quarto tipo de relacionamento, a **herança**. Modele uma hierarquia de veículos, onde **Veículo** é a classe base e suas subclasses são **Carro**, **Moto** e **Caminhão**. Como a herança impacta o design dos sistemas? Além disso, discuta como a herança se relaciona ou se combina com associação, agregação e composição.

6. **Desafio 6: Sistema Escolar**
   Modele um sistema de gerenciamento de uma **escola**. Defina as classes **Professor**, **Aluno**, **Turma** e **Disciplina**. Analise como organizar esses relacionamentos: **professores** pertencem a **turmas** e **alunos** se inscrevem em **disciplinas**. Como você usaria associação, agregação e composição para modelar essas interações?

### Notas para os exercícios:

- Em todos os desafios, o objetivo é entender **quando e por que** escolher um tipo de relacionamento. 
- Em alguns casos, é possível que você tenha que combinar **associação** com **composição** ou **agregação** para um design robusto.
- No desafio de herança, considere como as subclasses podem adicionar ou modificar comportamentos sem quebrar a estrutura do código.
