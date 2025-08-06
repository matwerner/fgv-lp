# Orientação a Objetos: Polimorfismo

## 1. O que é Polimorfismo?

* Polimorfismo é um dos conceitos fundamentais da Programação Orientada a Objetos (POO). Ele permite que diferentes classes sejam tratadas como se fossem instâncias de uma classe comum, mesmo que essas classes não compartilhem uma hierarquia direta.
* Essa característica promove a flexibilidade e a extensibilidade do código, pois objetos de classes diferentes podem ser manipulados de maneira intercambiável.

### Exemplo

* Considere um cenário em que você tem uma classe base chamada `Pagamento`, que define um método `processar()`. Várias subclasses, como `CartaoCredito` e `TransferenciaBancaria`, implementam esse método de maneiras diferentes. Assim, você pode chamar `processar()` em qualquer objeto do tipo `Pagamento`, e o comportamento será adaptado de acordo com a forma específica de pagamento.
    ```python
    class Pagamento:
        def processar(self):
            pass

    class CartaoCredito(Pagamento):
        def processar(self):
            return "Processando pagamento com cartão de crédito."

    class TransferenciaBancaria(Pagamento):
        def processar(self):
            return "Processando transferência bancária."

    def realizar_pagamento(pagamento: Pagamento):
        print(pagamento.processar())

    # Exemplo de uso
    pagamento_cartao = CartaoCredito()
    pagamento_transferencia = TransferenciaBancaria()

    realizar_pagamento(pagamento_cartao)       # Saída: Processando pagamento com cartão de crédito.
    realizar_pagamento(pagamento_transferencia) # Saída: Processando transferência bancária.
    ```

* Neste exemplo, mesmo que `CartaoCredito` e `TransferenciaBancaria` sejam classes diferentes, ambos podem ser tratados como um `Pagamento`. Ao chamar o método `processar()`, cada classe fornece sua própria implementação, demonstrando como o polimorfismo permite que métodos operem de maneira consistente em diferentes tipos de objetos.

## 2. Tipos de Polimorfismo

* Existem duas formas principais de polimorfismo em Programação Orientada a Objetos (POO):
    * **Polimorfismo por Sobrescrita de Métodos**:
    Ocorre quando uma subclasse fornece uma nova implementação de um método já definido na classe base, permitindo comportamentos diferentes para o mesmo método em subclasses.
    * **Polimorfismo por Subtipagem (Interfaces)**:
    É alcançado por meio de interfaces ou classes abstratas que definem métodos que devem ser implementados pelas subclasses, garantindo que diferentes classes sigam o mesmo contrato e possam ser usadas de forma intercambiável.


### 2.1 Polimorfismo por Sobrescrita de Métodos (Override):

* O polimorfismo por sobrescrita de métodos ocorre quando uma `subclasse` redefine um método herdado da sua `superclasse`, mantendo o mesmo nome e assinatura, mas alterando o comportamento.
* Esse tipo de polimorfismo está diretamente ligado ao conceito de `herança`, onde uma `subclasse` herda atributos e métodos de uma `superclasse`, mas pode especializar o comportamento de certos métodos.

#### Exemplo

    ```python
    class Animal:
    def fazer_som(self):
        return "Algum som"

    class Cachorro(Animal):
        def fazer_som(self):
            return "Latido"

    class Gato(Animal):
        def fazer_som(self):
            return "Miau"

    def emitir_som(animal: Animal):
        print(animal.fazer_som())

    # Ambos os animais respondem ao mesmo método, mas com comportamentos diferentes
    emitir_som(Cachorro())  # Saída: Latido
    emitir_som(Gato())      # Saída: Miau
    ```

* Explicação:
    * `Animal` é a superclasse que define um método `fazer_som()`, que retorna um som genérico.
    * As classes `Cachorro` e `Gato` são subclasses de `Animal` e sobrescrevem o método `fazer_som()` para fornecer sons específicos.
    * A função `emitir_som()` aceita um objeto do tipo `Animal`, mas o polimorfismo garante que o método correto (`fazer_som()`) será chamado com base no tipo real do objeto passado, seja um `Cachorro` ou um `Gato`.
* *Aqui, o polimorfismo por sobrescrita permite que a função `emitir_som()` trate objetos de diferentes classes (`Cachorro` e `Gato`) de forma intercambiável, chamando o método adequado com base no tipo específico do objeto, mesmo que ambos sejam referenciados como `Animal`.

### 2.2 Polimorfismo por Subtipagem (Interfaces)

* O polimorfismo por subtipagem, também conhecido como polimorfismo por interfaces, é uma abordagem que permite que diferentes classes implementem os mesmos métodos definidos em uma interface ou classe abstrata.
* Esse tipo de polimorfismo assegura que todas as classes que implementam a interface cumpram um "contrato" específico, ou seja, devem fornecer suas próprias versões dos métodos definidos.

#### Exemplo

```python
class Forma:
    def area(self):
        raise NotImplementedError("Este método deve ser implementado pela subclasse")

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * (self.raio ** 2)

def calcular_area(forma: Forma):
    print(f"A área da forma é: {forma.area()}")

# Exemplo de uso
retangulo = Retangulo(5, 3)
circulo = Circulo(2)

calcular_area(retangulo)  # Saída: A área da forma é: 15
calcular_area(circulo)     # Saída: A área da forma é: 12.56
```

* Explicação:
    * `Forma` é uma classe abstrata que define o método `area()`, que deve ser implementado por qualquer classe que herde dela.
    * `Retangulo` e `Circulo` são subclasses que implementam o método `area()` de maneiras específicas, calculando a área conforme sua forma geométrica.
    * A função `calcular_area()` aceita um objeto do tipo Forma e chama o `método area()`, que é definido de forma consistente em todas as subclasses.
* Neste exemplo, o polimorfismo por contratos permite que a função `calcular_area()` trate diferentes formas (retângulos e círculos) de forma intercambiável, garantindo que todos os objetos sigam o contrato estipulado pela classe abstrata `Forma`. Isso proporciona flexibilidade no código, facilitando a adição de novas formas sem a necessidade de alterar a função de cálculo.

## 3. Classes Abstratas e Protocols

* Como já comentamos, no polimorfismo por subtipagem, as classes fornecem um contrato de métodos e atributos que devem ser implementados ou seguidos por outras classes, garantindo que elas possam ser usadas de forma intercambiável, mesmo que não compartilhem uma hierarquia de herança direta.
* Existem duas formas principais de implementar esse tipo de polimorfismo em Python: `Classes Abstratas` e `Protocols`.

### 3.1 Classes Abstratas

* As Classes Abstratas definem métodos que devem ser implementados pelas subclasses, fornecendo um contrato explícito. Elas garantem que toda classe que herda de uma classe abstrata tenha uma implementação para os métodos marcados como abstratos. Em Python, isso é feito através do módulo abc e do decorador @abstractmethod.

    * **Quando usar**: Quando você deseja que as subclasses implementem obrigatoriamente certos métodos, assegurando que sigam um comportamento definido.

#### Exemplo

```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

# Verificando se a classe segue o contrato da classe abstrata
retangulo = Retangulo(3, 4)
print(isinstance(retangulo, Forma))  # Saída: True
```

* Aqui, a classe `Forma` define o método `area()`, e qualquer subclasse (como `Retangulo`) é obrigada a implementar esse método. Se não o fizer, será impossível instanciar a subclasse.

### 3.2. Protocols

* Os **Protocols**, introduzidos em Python com o módulo **typing**, permitem que você defina um contrato de métodos e atributos sem forçar as classes a herdar explicitamente de uma classe base. Um protocolo apenas verifica se um objeto segue esse contrato, ou seja, se possui os métodos ou atributos esperados, mesmo que não tenha uma relação de herança direta.

    * **Quando usar**: Quando você quer verificar se um objeto segue um conjunto de comportamentos (contrato) sem exigir herança formal. Protocols oferecem maior flexibilidade, pois a classe que os implementa não precisa explicitamente herdar de uma classe base.

#### Exemplo

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Desenhavel(Protocol):
    def desenhar(self) -> None:
        ...

class Circulo:
    def desenhar(self) -> None:
        print("Desenhando um círculo")

def desenhar_forma(forma: Desenhavel):
    forma.desenhar()

circulo = Circulo()
desenhar_forma(circulo)  # Saída: Desenhando um círculo

# Verificando se o objeto segue o contrato do protocolo em tempo de execução
print(isinstance(circulo, Desenhavel))  # Saída: True
```

* Neste caso, `Circulo` não herda de `Desenhavel`, mas segue o contrato ao implementar o método `desenhar()`. Protocols garantem que o comportamento esperado seja seguido sem exigir uma relação formal de herança.

### 3.3. Diferenças entre Classes Abstratas e Protocols

* **Classes Abstratas**: Exigem herança direta e forçam a implementação dos métodos abstratos nas subclasses. O uso de `isinstance` verifica se o objeto é uma instância da classe abstrata.
* **Protocols**: Não exigem herança direta e verificam se o objeto implementa os métodos necessários, sem impor uma relação de hierarquia. Quando decorados com `@runtime_checkable`, permitem o uso de `isinstance` para verificar a conformidade do contrato em tempo de execução.

## 6. Exercício Prático

### 4.1. 4.1 Polimorfismo por Sobrescrita de Métodos

Crie uma classe `Personagem` com um método `atacar()`. Depois, crie as subclasses `Guerreiro` e `Mago`, onde cada uma deve sobrescrever o método `atacar()` para implementar seu próprio estilo de ataque.

1. A classe `Personagem` deve ter o método `atacar()`.
2. A classe `Guerreiro` deve sobrescrever `atacar()` para exibir um ataque físico.
3. A classe `Mago` deve sobrescrever `atacar()` para exibir um ataque mágico.
4. Crie uma função que receba um personagem e chame seu método `atacar()`.

### 4.2. Polimorfismo por Subtipagem com Classes Abstratas

Crie uma classe abstrata Usuario com um método `acessar_conteudo()`. Em seguida, crie as subclasses `UsuarioGratuito` e `UsuarioPremium`, onde cada uma implementa o método `acessar_conteudo()` de maneira diferente, conforme as regras do seu plano.

1. A classe `Usuario` deve ter o método abstrato `acessar_conteudo()`.
2. A classe `UsuarioGratuito` deve implementar `acessar_conteudo()` com restrições de acesso.
3. A classe `UsuarioPremium` deve implementar `acessar_conteudo()` com acesso completo ao conteúdo.
4. Crie uma função que receba um usuário e permita acessar o conteúdo de acordo com seu tipo.

### 4.3. Polimorfismo por Subtipagem com Protocols

Defina um protocolo `Pagavel` com um método `realizar_pagamento()`. Crie as classes `CartaoDeCredito` e `PayPal`, que implementam o protocolo de maneiras diferentes para processar pagamentos.

1. Defina um protocolo `Pagavel`  que tenha o método `realizar_pagamento()`.
2. A classe `CartaoDeCredito` deve implementar `realizar_pagamento()` para processar um pagamento via cartão.
3. A classe `PayPal` deve implementar `realizar_pagamento()` para processar um pagamento via PayPal.
4. Crie uma função que receba qualquer tipo de método de pagamento e chame `realizar_pagamento()`.
