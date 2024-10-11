# Orientação a Objetos: Construtores e Encapsulamento

## 1. O Construtor `__init__`

* O construtor `__init__` é um método especial utilizado para inicializar objetos.
* Ele permite definir valores iniciais para os atributos de uma classe e garantir que cada instância seja criada corretamente.

### Exemplo de uso:

* Imagine que estamos desenvolvendo um sistema de gerenciamento de pessoas para uma escola.
* Cada pessoa tem um nome e uma idade, que precisam ser definidos ao criar um novo registro de pessoa.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando uma instância
p1 = Pessoa("Ana", 25)
print(p1.nome)  # Saída: Ana
```

* Aqui, o método `__init__` é utilizado para inicializar cada objeto da classe Pessoa, garantindo que todas as pessoas criadas tenham um nome e uma idade.
* Ao construir um sistema mais complexo, como o de gerenciamento de alunos ou funcionários, esse tipo de controle inicial é essencial.

### Importância do Parâmetro self

* O parâmetro `self` refere-se à instância atual da classe. É uma convenção em Python e pode ser nomeado de qualquer outra forma, mas o uso de `self` é amplamente adotado e aumenta a legibilidade do código.
* Quando você usa `self.nome` dentro do método `__init__`, você está adicionando um novo atributo chamado `nome` ao objeto `self`. O objeto `self` é uma instância da classe e começará sem atributos definidos até que você os adicione no construtor.
* Isso permite que cada instância da classe tenha seus próprios valores para os atributos, diferenciando um objeto do outro.

## 2. Encapsulamento: Protegendo Dados com Modificadores de Acesso

* O encapsulamento é uma das principais características da programação orientada a objetos (POO).
* Ele permite proteger os dados dentro de uma classe, impedindo que sejam acessados ou modificados diretamente de fora da classe sem o devido controle.
* Isso é fundamental em sistemas complexos para evitar comportamentos indesejados ou dados inconsistentes.
* Por exemplo,
    - Imagine um sistema bancário. Não é seguro permitir que qualquer parte do sistema altere diretamente o saldo de uma conta bancária sem validações ou restrições.
    - O encapsulamento resolve esse problema, controlando como os dados são acessados e modificados.
* Além da proteção, o encapsulamento também fornece:
    - **bstração**: Ocultando detalhes da implementação, permitindo que os usuários interajam com a classe sem precisar entender sua lógica interna.
    - **Facilidade de Manutenção**: Alterações na implementação interna podem ser feitas sem impactar o código externo que utiliza a classe, desde que a interface permaneça a mesma.
    - **Segurança**: Restringindo o acesso a dados sensíveis, prevenindo modificações não autorizadas que podem causar inconsistências.
    - **Flexibilidade**: Permite adaptar a lógica interna de uma classe sem afetar o restante do sistema, promovendo um design mais modular.

### Níveis de privacidade

* Em Python, utilizamos convenções para marcar os atributos como públicos, protegidos ou privados:
    - **Público**: Atributos acessíveis diretamente.
    - **Protegido**: Atributos que começam com um sublinhado (`_`), sugerindo que não devem ser acessados fora da classe.
    - **Privado**: Atributos que começam com dois sublinhados (`__`), indicando que são fortemente protegidos.

### Exemplo

* No sistema bancário, um atributo como o saldo da conta não deve ser acessado diretamente:

```python
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular  # Público
        self._saldo = saldo     # Protegido (convenção)
        self.__senha = "1234"   # Privado

# Tentando acessar diretamente o saldo e a senha
conta = ContaBancaria("João", 1000)
print(conta._saldo)  # Saída: 1000 (não recomendado acessar diretamente)
print(conta.__senha)  # Erro: atributo privado
```

* No exemplo acima, o saldo é marcado como protegido (`_saldo`), indicando que o acesso direto fora da classe não é recomendado;
* Já a senha é marcada como privada (`__senha`), impedindo o acesso direto.

### Importância do Encapsulamento das Informações

* Em sistemas reais, como bancos, hospitais ou lojas online, o encapsulamento é crucial para garantir a integridade dos dados. Imagine se qualquer parte de um software de hospital pudesse modificar diretamente os dados dos pacientes sem restrições. Isso poderia resultar em erros graves, como alterar diagnósticos ou tratamentos incorretamente.
* O encapsulamento permite que esses dados sejam modificados apenas por partes autorizadas do código e com as devidas validações, garantindo segurança e consistência.
* Além disso, facilita a manutenção do código, pois você pode alterar a lógica interna sem afetar outras partes do sistema que utilizam a classe. A modularidade resultante do encapsulamento permite que desenvolvedores trabalhem em partes diferentes do sistema de forma independente, promovendo a colaboração e a eficiência.

## 3. Getters e Setters para Controle de Acesso

* Para controlar o acesso a atributos protegidos ou privados, utilizamos métodos chamados `getters` (para obter valores) e `setters` (para modificar valores). Eles garantem que os dados sejam acessados ou modificados de maneira controlada, permitindo, por exemplo, validações ou restrições.

* Continuando o exemplo do sistema bancário, vamos adicionar controle sobre o acesso ao saldo, impedindo que o saldo seja modificado para um valor negativo:

```python
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, valor):
        if valor >= 0:
            self._saldo = valor
        else:
            print("Saldo inválido")

# Usando os getters e setters
conta = ContaBancaria("João", 1000)
print(conta.get_saldo())  # Saída: 1000

conta.set_saldo(-500)  # Saída: Saldo inválido
print(conta.get_saldo())  # Saída: 1000
```

* Aqui, usamos `get_saldo()` para acessar o saldo e `set_saldo()` para alterá-lo. O método `set_saldo()` inclui uma validação para garantir que o saldo nunca seja negativo. Isso é fundamental para sistemas reais, onde erros de lógica podem resultar em falhas críticas, como permitir que uma conta tenha um saldo negativo em um sistema bancário.

## 4. Funções Especiais Simples

* Algumas funções especiais permitem personalizar o comportamento de objetos em situações comuns, como exibir e comparar objetos.
* Essas funções são especialmente úteis quando criamos classes que precisam ser usadas em interações mais complexas no sistema.

### 4.1. `__str__`: Representação de Objetos

* O método __str__ define como um objeto será representado como uma string, útil quando queremos exibir um objeto de forma legível.

#### Exemplo:

* No sistema de gerenciamento de pessoas da escola, podemos implementar `__str__` para exibir uma pessoa de forma mais amigável:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Pessoa: {self.nome}, Idade: {self.idade}"

p1 = Pessoa("Ana", 25)
print(p1)  # Saída: Pessoa: Ana, Idade: 25
```

* Isso facilita a leitura e interpretação dos dados quando imprimimos uma instância da classe.

### 4.2. `__eq__`: Comparação de Objetos

O método `__eq__` permite comparar se dois objetos são iguais com base em seus atributos.

#### Exemplo:

* No sistema escolar, podemos querer comparar se duas pessoas são iguais, baseando-se no nome e idade:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __eq__(self, outra_pessoa):
        return self.nome == outra_pessoa.nome and self.idade == outra_pessoa.idade

p1 = Pessoa("Ana", 25)
p2 = Pessoa("Bruno", 30)
print(p1 == p2)  # Saída: False
```

* Essa função é útil em situações onde precisamos verificar se dois objetos representam a mesma entidade no sistema, como verificar se dois registros no banco de dados são iguais.

## 5. Práticas Recomendadas de Encapsulamento

* **Evitar Expor Atributos Diretamente**:
Proteja os dados importantes da classe usando `_` ou `__`, e forneça métodos de acesso (getters e setters) para garantir que os dados sejam tratados de forma segura e controlada.

* **Validação nas Alterações de Atributos**:
Use setters para garantir que alterações nos atributos de uma classe sejam válidas.
Isso evita que o estado interno da classe se torne inconsistente.

* **Facilitar a Manutenção do Código**:
O encapsulamento permite que o comportamento interno de uma classe seja alterado sem modificar o código que utiliza essa classe, facilitando a manutenção e evolução do sistema.

## 6. Exercícios Práticos

### 6.1. Conta bancária

1. Crie uma classe simples que represente uma conta bancária com atributos como `titular` e `saldo`, garantindo que o `saldo` só possa ser acessado e modificado por meio de getters e setters.
2. Faça com que implementem o método `__str__` para retornar uma string amigável que descreva o objeto.
3. Peça para implementar o método `__eq__` em uma classe para comparar objetos e verificar se são iguais.

### 6.2. Match 3


1. Crie uma classe chamada `Peca` que represente uma peça do jogo com atributos como `tipo` e `cor`.
Implemente os seguintes métodos:
    * O método `__init__` para inicializar os atributos.
    * O método `__str__` para retornar uma string amigável que descreva a peça.
    * O método `__eq__` para comparar objetos e verificar se são iguais com base no atributo tipo.
2. Implemente uma função chamada `combinar_pecas` que aceite uma lista de peças e identifique combinações de duas peças que podem ser "jogadas" (ou seja, peças do mesmo tipo). A função deve retornar uma lista de combinações encontradas.
3. Crie algumas instâncias da classe `Peca` e teste a lógica de combinação. Exiba as combinações encontradas de maneira amigável.