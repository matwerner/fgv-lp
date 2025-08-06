# Orientação a Objetos: Herança

## 1. Introdução

* A herança é um dos pilares da Programação Orientada a Objetos (POO).
* Ela permite que uma classe (classe derivada ou filha) herde atributos e métodos de outra classe (classe base ou pai).
* Isso facilita a reutilização do código e promove a hierarquia na modelagem de dados.

### 1.1. Motivação

* Ao desenvolver projetos mais complexos, é comum criarmos classes parecidas. Pense, por exemplo, em um jogo de vídeo game com um personagem principal e seus inimigos.  Ambos compartilham atributos como vida, pontos de ataque e defesa. Se criarmos classes separadas para cada um, acabaríamos repetindo muito código.
* A herança nos ajuda a evitar essa duplicação. Ela permite que compartilhemos atributos e métodos idênticos em uma classe base, facilitando a criação de classes específicas para personagens diferentes sem repetir o mesmo código. Isso torna o desenvolvimento mais organizado e eficiente

### 1.2. Taxonomia

* Pode-se pensar que o objetivo da herança é criar uma taxonomia (hierarquia) de classes que reflita as relações do mundo real. Essa hierarquia ajuda a organizar e estruturar o código de forma lógica.
* Por exemplo, em um sistema de pagamento, podemos ter uma classe base `Pagamento` que encapsula os conceitos gerais de pagamento. A partir dela, podemos criar subclasses como `PagamentoDinheiro`, `PagamentoBoleto`, `PagamentoCartaoDebito`, `PagamentoCartaoCredito` e `PagamentoPix`.
* Isso permite que atributos e métodos comuns sejam definidos na classe base, evitando a duplicação e promovendo uma manutenção mais simples.

### 1.3. Generalização

* A generalização é uma maneira de criar essa taxonomia ao identificar as características comuns entre as classes que estamos desenvolvendo. Ao analisar o mundo real, podemos perceber que certos conceitos compartilham atributos ou comportamentos similares que justificam sua inclusão em uma mesma classe base.
* Por exemplo, todos os tipos de pagamento podem compartilhar atributos como `valor`, `data` e `status`. Ao generalizar essas características, conseguimos agrupar informações relevantes em uma estrutura coesa, facilitando a reutilização e a compreensão do código.

### 1.4. Regra "é um"

* A regra `"é um"` (is-a relationship) é uma maneira prática de identificar se a herança é adequada em uma situação específica. Quando dizemos que uma classe derivada "é um" tipo da classe base, estamos afirmando que ela herda suas características e comportamentos.
* Por exemplo, se PagamentoCartaoCredito herda de Pagamento, podemos afirmar que um PagamentoCartaoCredito "é um" Pagamento, o que faz sentido conceitualmente e na prática.

* No entanto, é importante ter cuidado ao aplicar essa regra, pois nem sempre a herança se justifica. Por exemplo:
    - Considerar `"Fila"` e `"Lista"` como uma hierarquia pode não ser apropriado, já que são estruturas de dados diferentes, cada uma com suas próprias características e comportamentos.
    - Da mesma forma, `"Usuário"` e `"Fornecedor"` podem não se encaixar em uma relação de herança direta, pois, apesar de ambos serem tipos de usuários, suas funções e responsabilidades podem ser distintas.
* Essa análise cuidadosa ajuda a garantir que a estrutura de classes seja lógica e eficaz.

### 1.5. Contextos de Aplicação

* **Modelagem de Dados**:
A herança é útil quando se deseja modelar uma hierarquia de classes que compartilham características comuns.
Em um sistema de pagamento, a classe base Pagamento pode conter informações comuns, enquanto as subclasses implementam comportamentos específicos.

* **Desenvolvimento de Software**:
Em projetos maiores, a herança ajuda a estruturar o código, permitindo que funcionalidades comuns sejam centralizadas em uma classe base.
A adição de novos métodos ou classes derivadas torna-se mais simples e organizada.

* **Jogos**:
Em jogos, a herança pode ser utilizada para definir diferentes tipos de personagens (e.g., `Personagem`, `Inimigo`, `Chefão`), permitindo que todos compartilhem métodos comuns, como `atacar()` ou `defender()`, enquanto cada um pode ter suas próprias implementações específicas.

## 2. Sintaxe das Classes Base e Derivadas 

### 2.1. Classe Base

* Vamos começar criando uma classe base `Pagamento`, que conterá atributos e métodos comuns a todos os tipos de pagamento.
* A classe base é definida da seguinte forma:
    ```python
    class Pagamento:

        def __init__(self, valor, data, status):
            self.valor = valor           # Atributo de instância
            self.data = data             # Atributo de instância
            self.status = status         # Atributo de instância

        def info(self):
            """Retorna informações básicas sobre o pagamento."""
            return f"Pagamento de R${self.valor:.2f} realizado em {self.data}. Status: {self.status}."
    ```

    * Explicação da Sintaxe:
        * `class Pagamento`: define a classe base chamada `Pagamento`.
        * `__init__` é o método construtor, que inicializa os atributos da classe.
        * `self` refere-se à instância atual da classe, permitindo acesso aos atributos e métodos.

### 2.2. Classe Derivada

* Agora, vamos criar classes derivadas que representam diferentes métodos de pagamento e que herdam da classe `Pagamento`.
* A seguir, estão exemplos de duas classes derivadas: `PagamentoBoleto` e `PagamentoCartaoCredito`.
    ```python
    class PagamentoBoleto(Pagamento):  # PagamentoBoleto herda de Pagamento

        def __init__(self, valor, data, status, numero_boleto, data_vencimento):
            super().__init__(valor, data, status)  # Chama o construtor da classe base
            self.numero_boleto = numero_boleto     # Atributo específico
            self.data_vencimento = data_vencimento # Atributo específico

    class PagamentoCartaoCredito(Pagamento):  # PagamentoCartaoCredito herda de Pagamento

        def __init__(self, valor, data, status, numero_cartao, parcelas):
            super().__init__(valor, data, status)  # Chama o construtor da classe base
            self.numero_cartao = numero_cartao     # Atributo específico
            self.parcelas = parcelas               # Atributo específico
    ```

    * Explicação da Sintaxe:
        * `class PagamentoBoleto(Pagamento)`: define PagamentoBoleto como uma classe derivada da classe base Pagamento.
        * `class PagamentoCartaoCredito(Pagamento)`: define PagamentoCartaoCredito como uma classe derivada da classe base Pagamento.
        * `super()`: é uma função que permite chamar métodos da classe base a partir da classe derivada.
        * `super().__init__(...)`: chama o construtor da classe base para inicializar os atributos herdados. Isso garante que todos os atributos comuns sejam configurados corretamente antes de adicionar atributos específicos da classe derivada.

### 2.3. Métodos Específicos

* Em nossas classes derivadas, podemos adicionar métodos que são específicos para cada tipo de pagamento.
* Esses métodos podem realizar operações que são únicas para a lógica de cada forma de pagamento.

    ```python
    class PagamentoBoleto(Pagamento):

        def __init__(self, valor, data, status, numero_boleto, data_vencimento):
            super().__init__(valor, data, status)
            self.numero_boleto = numero_boleto
            self.data_vencimento = data_vencimento
        
        def calcular_multa(self, data_pagamento):
            if data_pagamento > self.data_vencimento:
                # Lógica para calcular a multa
                return "Multa aplicada!"
            return "Sem multa."
    
    class PagamentoCartaoCredito(Pagamento):

        def __init__(self, valor, data, numero_cartao, parcelas):
            super().__init__(valor, data, "Pendente")
            self.numero_cartao = numero_cartao
            self.parcelas = parcelas
        
        def autorizar_pagamento(self):
            # Lógica para verificar a autorização do cartão
            return "Pagamento autorizado!" if self.numero_cartao else "Pagamento não autorizado."
    ```

    * Explicação da Sintaxe:
        * Em cada classe derivada, definimos novos métodos que são especificos para aquele tipo de pagamento.

### 2.4. Sobrescrita de Métodos

* A sobrescrita de métodos (ou overriding) ocorre quando uma classe derivada fornece uma implementação específica para um método que já está definido na classe base. Isso é útil quando a lógica do método precisa ser ajustada ou personalizada para a classe derivada.
* Vamos adicionar um exemplo de sobrescrita no método info na classe PagamentoCartaoCredito, para ilustrar essa prática:

    ```python
    class PagamentoCartaoCredito(Pagamento):

        def __init__(self, valor, data, numero_cartao, parcelas):
            super().__init__(valor, data, "Pendente")
            self.numero_cartao = numero_cartao
            self.parcelas = parcelas

        def info(self):
            """Sobrescreve o método info para incluir informações sobre parcelamento."""
            return f"{super().info()} | Pagamento em {self.parcelas} parcelas."
    ```

    * Explicação da Sintaxe:
        * Aqui, estamos sobrescrevendo o método `info()` na classe `PagamentoCartaoCredito`. A nova implementação inclui detalhes sobre o número de parcelas.
        * Utilizamos `super().info()` para chamar a implementação original do método na classe base, garantindo que as informações comuns ainda sejam incluídas na saída.

## 3. Vantagens e Desvantagens da Herança

### Vantagens

* **Reutilização de Código**: Permite usar código existente de classes base, reduzindo duplicação e facilitando a manutenção.
* **Organização**: Cria uma estrutura hierárquica que reflete relações do mundo real, tornando o código mais legível.
* **Facilidade de Extensão**: Novas funcionalidades podem ser adicionadas rapidamente com subclasses, sem reescrever código.

### Desvantagens

* **Acoplamento**: Subclasses dependem da classe base; mudanças na base podem afetar todas as subclasses.
* **Reutilização Difícil**: Às vezes, a herança pode não ser a melhor forma de reutilizar código, especialmente se as classes não têm uma relação "é um".
* **Sobrescrita Confusa**: Sobrescrita de métodos pode causar confusão se não for bem documentada, levando a comportamentos inesperados.

## 4. Exercícios

### 4.1. Criar um sistema de catalogação de livros usando herança.

* **Classe Base**: Crie uma classe base chamada Livro que contenha atributos comuns como `titulo`, `autor`, `ano_publicacao` e métodos como `info()` para retornar informações sobre o livro.
* **Classes Derivadas**: Desenvolva subclasses para diferentes tipos de livros, como `LivroFisico` e `EBook`.
    - LivroFisico pode ter um atributo adicional, como `peso`.
    - EBook pode ter atributos como `formato` e `tamanho`.
* **Métodos Específicos**: Adicione métodos exclusivos, como `download()` para EBook e `informar_localizacao()` para LivroFisico.
* **Desafio**: Implementar um método na classe EBook que sobrescreva o método `info()` da classe base, fornecendo informações adicionais sobre o download.

### 4.2. Desenvolver um sistema básico para gerenciar personagens em um jogo.

* **Classe Base**: Crie uma classe base chamada Personagem com atributos como `nome`, `vida`, `pontos_ataque` e métodos como `atacar()` e `info()`.
* **Classes Derivadas**: Desenvolva subclasses para diferentes tipos de personagens, como `Heroi` e `Inimigo`.
    - Heroi pode ter atributos adicionais, como `poder_especial`.
    - Inimigo pode incluir atributos como `nivel_de_perigo`.
* **Métodos Específicos**: Adicione métodos exclusivos, como `usar_poder()` para Heroi e `fugir()` para Inimigo.
* **Desafio**: Implementar a lógica de combate entre um Heroi e um Inimigo, utilizando os métodos de ataque e uma condição para verificar quem ganha.