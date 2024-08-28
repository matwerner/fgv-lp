# Aula: Testes Automatizados em Python

Testes automatizados são scripts que verificam se o código está funcionando conforme o esperado, automaticamente.
Ao invés de verificar manualmente se cada parte do código está correta, o desenvolvedor escreve testes que fazem essas verificações.

### Importância dos Testes Automatizados

- **Confiabilidade:**
Ajudam a garantir que o código funciona corretamente.
- **Eficiência:**
Economizam tempo, pois testes manuais podem ser repetitivos e propensos a erros.
- **Manutenção:**
Facilitam a manutenção do código. Se algo mudar no código, os testes automatizados podem rapidamente indicar se a mudança introduziu algum problema.
- **Documentação:**
Servem como uma forma de documentação viva, mostrando como as funções devem ser usadas e o que se espera delas.

## 2. Tipos de Testes

Os testes de software são fundamentais para garantir a qualidade e a confiabilidade de um sistema.
Eles podem ser classificados em diferentes categorias, cada uma com um propósito específico no processo de validação do software.
Aqui estão os três principais tipos de testes que você deve conhecer:

### 2.1 Testes Unitários

- **O que são?**
  - Testes unitários focam na menor unidade testável do código, geralmente funções ou métodos individuais.
  - Eles verificam se essas unidades estão funcionando corretamente de forma isolada, sem depender de outras partes do sistema.

- **Objetivo:**
  - Assegurar que cada unidade de código esteja correta em termos de comportamento esperado. 
  - Facilitar a detecção de erros precocemente no ciclo de desenvolvimento.
  
- **Características:**
  - São rápidos de executar, o que facilita sua integração em práticas de desenvolvimento contínuo.
  - Isolam as unidades de código, simulando comportamentos externos (usando mocks, stubs, etc.) quando necessário.
  - Devem cobrir tanto os casos normais quanto os casos de borda (edge cases).

- **Exemplo:**
  - Testar uma função `soma(a, b)` para verificar se ela retorna corretamente a soma dos dois números.

### 2.2 Testes de Integração

- **O que são?**
  - Testes de integração verificam a interação entre diferentes módulos ou componentes de um sistema.
  - Eles asseguram que, quando combinadas, essas unidades de código funcionam conforme esperado.

- **Objetivo:**
  - Detectar problemas na forma como diferentes partes do sistema interagem umas com as outras.
  - Validar interfaces e protocolos de comunicação entre módulos.
  
- **Características:**
  - Podem envolver múltiplas unidades de código.
  - Testam a comunicação com sistemas externos, como bancos de dados, APIs externas, ou outros serviços.
  - Normalmente, são mais lentos que os testes unitários, pois podem envolver comunicação em rede ou operações de I/O.

- **Exemplo:**
  - Testar se uma função que consulta um banco de dados retorna os dados esperados quando a conexão com o banco está ativa e se lida adequadamente com falhas de conexão.

### 2.3 Testes de Sistema

- **O que são?**
  - Testes de sistema avaliam o sistema inteiro como um todo. 
  - Eles verificam se o sistema atende aos requisitos especificados e se funciona conforme esperado em um ambiente que simula o real.

- **Objetivo:**
  - Validar o sistema em sua totalidade, incluindo interações entre subsistemas e com usuários finais.
  - Garantir que as funcionalidades oferecidas ao usuário final estejam corretas e integradas.
  
- **Características:**
  - Executam-se em um ambiente que é o mais próximo possível do ambiente de produção.
  - Incluem cenários complexos de uso do sistema, testando o fluxo de trabalho completo.
  - Envolvem todos os componentes: interface de usuário, lógica de negócio, persistência de dados, etc.

- **Exemplo:**
  - Simular uma série de ações que um usuário realizaria em um sistema de e-commerce: navegação pelo catálogo de produtos, adicionar itens ao carrinho, realizar o checkout e finalizar a compra.

## 3. Testes Unitários

No Python, existem várias bibliotecas que facilitam a escrita e execução de testes unitários. Duas das mais comuns são `doctest` e `unittest`. Ambas são incluídas na biblioteca padrão do Python, o que significa que não há necessidade de instalar pacotes adicionais para começar a usá-las.

### 3.1 `doctest`

- **O que é `doctest`?**
  - `doctest` é uma ferramenta que permite testar o código Python embutindo exemplos no próprio docstring do código. A ideia é escrever a especificação de como uma função deve se comportar e ao mesmo tempo incluir exemplos de uso. `doctest` então executa esses exemplos e verifica se a saída corresponde ao esperado.

- **Vantagens do `doctest`:**
  - Fácil de usar e integrar em docstrings.
  - Ideal para criar exemplos de uso que são automaticamente verificados.
  - Simples de entender, pois usa o próprio console do Python para criar os exemplos.

- **Como usar o `doctest`:**
  1. Escreva a função normalmente.
  2. Inclua exemplos de uso da função no docstring, indicando o que é esperado como saída.
  3. Use o comando `python -m doctest -v nome_do_arquivo.py` para executar os testes.

- **Exemplo de `doctest`:**

    ```python
    def soma(a, b):
        """
        Retorna a soma de a e b.
        
        Exemplo:
        >>> soma(2, 3)
        5
        >>> soma(-1, 1)
        0
        """
        return a + b
    ```

    Ao executar `python -m doctest -v nome_do_arquivo.py`, o `doctest` validará se os exemplos fornecidos na docstring produzem a saída esperada.

#### Exercícios

Para cada exercício abaixo, implemente a função detalhada e dicione um doctest para verificar o seu correto funcionamento.

1. Escreva uma função chamada `preprocessar_texto(texto)` que receba um texto como entrada e retorne uma versão pré-processada do texto.
O pré-processamento deve incluir:
    * Conversão de todas as letras para minúsculas;
    * Aceitação apenas de caracteres alfanuméricos ou espaços;
    * Troca de todos os digitos por `0`;
    * Remoção de espaços extras no início e no fim do texto.

2. Escreva uma função chamada `criar_vocabulario(textos, n)` que receba uma lista de textos já pré-processados e um número inteiro $n$, e retorne um vocabulário contendo até $n$ palavras únicas ordenadas por frequência de ocorrência.

# (Em construção)

<!-- 
### 3.2 `unittest`

- **O que é `unittest`?**
  - `unittest` é uma biblioteca mais robusta que oferece uma estrutura completa para a criação de testes unitários. Ela é baseada no conceito de criação de classes de teste, onde cada método da classe testa uma funcionalidade específica do código.

- **Vantagens do `unittest`:**
  - Suporte a criação de casos de teste mais complexos.
  - Oferece várias assertivas para verificar condições (por exemplo, `assertEqual`, `assertTrue`, `assertRaises`).
  - Facilita a organização e execução de muitos testes de uma só vez.
  - Permite configuração e limpeza de ambiente de teste com os métodos `setUp()` e `tearDown()`.

- **Como usar o `unittest`:**
  1. Importe o módulo `unittest`.
  2. Crie uma classe de teste que herda de `unittest.TestCase`.
  3. Escreva métodos de teste dentro da classe para verificar diferentes partes do código.
  4. Execute os testes usando `python -m unittest nome_do_arquivo.py`.

- **Exemplo de `unittest`:**

    ```python
    import unittest

    def soma(a, b):
        return a + b

    class TestSoma(unittest.TestCase):

        def test_soma_positivos(self):
            self.assertEqual(soma(2, 3), 5)

        def test_soma_negativos(self):
            self.assertEqual(soma(-1, -1), -2)

        def test_soma_zero(self):
            self.assertEqual(soma(0, 0), 0)

    if __name__ == '__main__':
        unittest.main()
    ```

    Neste exemplo, criamos uma classe `TestSoma` que contém métodos para testar diferentes cenários de uso da função `soma`. O método `unittest.main()` é usado para executar todos os testes definidos.

### 3.3 Quando usar `doctest` e `unittest`

- **Use `doctest` quando:**
  - Deseja fornecer exemplos de uso diretamente na documentação do código.
  - O código a ser testado é simples e os exemplos são suficientes para ilustrar a funcionalidade.
  - Prefere uma abordagem rápida e fácil de verificar pequenos comportamentos.

- **Use `unittest` quando:**
  - Precisa de uma estrutura de teste mais robusta e detalhada.
  - Está escrevendo testes para um sistema maior, com múltiplas interações e cenários.
  - Deseja separar claramente o código de produção dos testes. -->