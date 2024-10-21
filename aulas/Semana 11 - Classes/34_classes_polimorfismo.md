# (EM CONSTRUÇÃO) Orientação a Objetos: Polimorfismo

## 1. Conceito e Definição

- **Definição de Polimorfismo:**
  - Polimorfismo é um conceito central em programação orientada a objetos que permite que métodos em diferentes classes tenham o mesmo nome, mas diferentes implementações.
  - Ele provê uma interface comum para objetos de classes diferentes, permitindo que eles sejam tratados de forma intercambiável.

- **Importância do Polimorfismo:**
  - O polimorfismo é fundamental para a abstração e a encapsulação, pois permite que você escreva código que pode trabalhar com objetos de diferentes tipos de maneira uniforme.
  - Quando você chama um método em um objeto, não precisa saber qual implementação específica será executada; isso é decidido em tempo de execução, tornando o código mais flexível e extensível.


## 2. Exemplo Prático

### 2.1. Hierarquia de Classes

- **Cenário: Personagens de RPG:** Vamos criar uma hierarquia de classes que inclui diferentes tipos de personagens que implementam um método comum chamado `ataque()`.

  ```python
    class Personagem:
        def ataque(self) -> str:
            raise NotImplementedError("Este método deve ser implementado por subclasses.")

    class Guerreiro(Personagem):
        def ataque(self) -> str:
            return "Guerreiro ataca com espada!"

    class Mago(Personagem):
        def ataque(self) -> str:
            return "Mago lança um feitiço!"

    class Arqueiro(Personagem):
        def ataque(self) -> str:
            return "Arqueiro dispara uma flecha!"
  ```

  - **Explicação:** A classe `Personagem` define um método `ataque()` que levanta `NotImplementedError`, indicando que as subclasses devem fornecer sua própria implementação. Essa abordagem é simples e acessível para alunos iniciantes.

### 2.2. Utilização do Polimorfismo

- **Implementando o Polimorfismo:**
  - Vamos criar uma função que aceita qualquer objeto da classe `Personagem` e chama o método `ataque()`.
  - A função deve demonstrar como diferentes instâncias de personagens respondem ao mesmo método, evidenciando o conceito de polimorfismo.

  ```python
    def realizar_ataque(personagem: Personagem) -> None:
        """Chama o método ataque() de um personagem."""
        print(personagem.ataque())

    # Testando a função com diferentes tipos de personagens
    guerreiro = Guerreiro()
    mago = Mago()
    arqueiro = Arqueiro()

    realizar_ataque(guerreiro)  # "Guerreiro ataca com espada!"
    realizar_ataque(mago)       # "Mago lança um feitiço!"
    realizar_ataque(arqueiro)   # "Arqueiro dispara uma flecha!"
  ```

  - **Explicação:** A função `realizar_ataque` aceita um parâmetro do tipo `Personagem`. Isso significa que você pode passar qualquer instância de `Personagem` ou de suas subclasses, e o método apropriado será chamado, demonstrando o polimorfismo.



## 3. Discussão sobre Abstração e Métodos Abstratos

- **Conceito de Abstração:** A abstração é um dos pilares da Programação Orientada a Objetos (POO) e refere-se à ideia de ocultar os detalhes de implementação e mostrar apenas a funcionalidade essencial de um objeto. Isso permite que os desenvolvedores interajam com objetos em um nível mais alto, sem se preocupar com a complexidade interna.

- **Métodos Abstratos:** Um método abstrato é um método que é declarado, mas não implementado na classe base. As subclasses devem fornecer suas próprias implementações para esses métodos. Isso estabelece um contrato que garante que todas as subclasses implementem comportamentos específicos, promovendo a consistência no design do sistema.

- **Comparação: `NotImplementedError` vs. `@abstractmethod`:**
  - **`raise NotImplementedError`:**
  Essa abordagem é simples e direta, ideal para iniciantes. Ao definir um método na classe base e levantar NotImplementedError, você indica que a implementação deve ser feita nas subclasses.

    ```python
    class Animal:
        def fazer_som(self):
            raise NotImplementedError("Este método deve ser implementado por subclasses.")

    class Cachorro(Animal):
        def fazer_som(self):
            return "Au Au!"

    class Gato(Animal):
        def fazer_som(self):
            return "Miau!"
    ```

    - **Explicação:** Nesta abordagem, a classe base `Animal` define o método `fazer_som()` e levanta um `NotImplementedError`. As subclasses Cachorro e Gato devem implementar este método. Se alguém tentar instanciar `Animal` ou chamar `fazer_som()` sem uma implementação, receberá um erro.

  - **`@abstractmethod`:** 
  O uso de `@abstractmethod` dentro de uma classe abstrata (definida com `ABC`) fornece uma maneira mais formal de definir métodos que devem ser implementados pelas subclasses. O Python não permitirá que você instancie a classe base, garantindo que todas as subclasses implementem os métodos necessários. Essa abordagem é recomendada para projetos maiores ou mais complexos.

    ```python
    from abc import ABC, abstractmethod

    class Animal(ABC):
        @abstractmethod
        def fazer_som(self):
            pass

    class Cachorro(Animal):
        def fazer_som(self):
            return "Au Au!"

    class Gato(Animal):
        def fazer_som(self):
            return "Miau!"
    ```

    - **Explicação:** Aqui, `Animal` é definida como uma classe `abstrata` que utiliza o decorador `@abstractmethod` para declarar `fazer_som()`. Essa abordagem não permite a instância da classe base `Animal`, garantindo que todas as subclasses implementem o método antes de serem utilizadas.

- **Quando Usar Cada Abordagem:**
    - **`NotImplementedError`:** Melhor para projetos simples ou para alunos iniciantes, facilitando a compreensão dos conceitos de herança e polimorfismo.
    - **`@abstractmethod`:** Recomendado para projetos mais complexos, onde a estrutura e a segurança são importantes. Essa abordagem ajuda a prevenir erros de implementação.


## 4. Polimorfismo com Herança

- **Sobrescrita de Métodos:** Quando uma classe filha fornece uma implementação específica de um método que já foi definido na classe pai, dizemos que ela está sobrescrevendo o método.

- **Exemplo de Sobrescrita:** Considere a classe `Animal` com o método `fazer_som()`, onde cada tipo de animal implementa seu próprio som.

    ```python
    class Animal:
        def fazer_som(self) -> str:
            raise NotImplementedError("Este método deve ser implementado por subclasses.")

    class Cachorro(Animal):
        def fazer_som(self) -> str:
            return "Au Au!"

    class Gato(Animal):
        def fazer_som(self) -> str:
            return "Miau!"
    ```

## 5. Exemplos do Mundo Real

- **Discussão sobre Aplicações:** O polimorfismo pode ser encontrado em muitos contextos do dia a dia, como métodos de pagamento que implementam um método comum `processar_pagamento()` e dispositivos de impressão com um método `imprimir()`.

    ```python
    class Dispositivo:
        def imprimir(self) -> str:
            raise NotImplementedError("Este método deve ser implementado por subclasses.")

    class Impressora(Dispositivo):
        def imprimir(self) -> str:
            return "Imprimindo em papel."

    class Scanner(Dispositivo):
        def imprimir(self) -> str:
            return "Escaneando documento."
    ```



## 6. Exercício Prático

- **Tarefa:** Implemente uma hierarquia de classes para veículos. Cada tipo de veículo (carro, moto, caminhão) deve implementar um método comum chamado `dirigir()` que retorna uma string descritiva. Em seguida, eles devem demonstrar o uso do polimorfismo chamando `dirigir()` em diferentes instâncias de veículos.

