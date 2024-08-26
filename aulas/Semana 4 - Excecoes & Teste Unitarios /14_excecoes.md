# Tratamento de exceções

Durante as aulas, você pode ter se deparado com a seguinte mensagem ao tentar acessar, por engano, uma posição de uma lista que excede o tamanho da lista:

```python
>>> l = [0,1,2,3]
>>> print(l[5])
Traceback (most recent call last):
  File "exemplo.py", line 2, in <module>
    print(l[5])
IndexError: list index out of range
```

Nesse exemplo, o interpretador Python encontrou um comportamento inesperado ao tentar acessar um índice inexistente, e, por isso, não pôde executar a operação solicitada.
Esse é um caso clássico de uma `exceção` em Python, um tipo de erro que ocorre durante a execução do código, interrompendo seu fluxo normal e, potencialmente, finalizando o programa.

Exceções em Python são semelhantes ao famoso `segmentation fault` da linguagem C, no qual o programa tenta acessar uma área de memória inválida.
No entanto, uma exceção em Python (e em outras linguagens modernas) fornece uma explicação muito mais detalhada sobre o que deu errado, ajudando os programadores a entender e corrigir o problema mais facilmente.

No exemplo acima, o Python fornece informações importantes:
* Em qual módulo ou arquivo Python ocorreu o erro (`exemplo.py`);
* A linha exata dentro desse arquivo onde o erro foi detectado (`line 2`);
* E o tipo específico de erro que ocorreu (`IndexError: list index out of range`).

Essas informações detalhadas são extremamente úteis para depuração, permitindo que você saiba exatamente onde procurar e o que corrigir.
Em vez de simplesmente falhar silenciosamente ou travar o sistema, como poderia ocorrer com um segmentation fault, o Python tenta explicar o problema, oferecendo uma oportunidade para tratá-lo e, assim, tornar o programa mais robusto.

Portanto, ao entender como funcionam as exceções e aprender a tratá-las corretamente, você estará desenvolvendo a habilidade de escrever códigos mais estáveis e confiáveis, capazes de lidar com uma ampla variedade de situações inesperadas.

## O que é uma Exceção?

Formalmente, uma exceção é um evento que ocorre durante a execução de um programa e interrompe o fluxo normal das instruções.
Pense em uma exceção como um erro ou uma situação inesperada que o programa encontra e não sabe como lidar.

### Tipos de exceção

Em Python, as exceções são categorizadas em diferentes tipos, permitindo que você trate erros de forma específica com base na situação.
Alguns tipos comuns incluem:

* **ValueError**: Ocorre quando uma operação recebe um argumento do tipo correto, mas com um valor inadequado.
* **IOError**: Relacionado a problemas de entrada/saída, como falhas ao tentar abrir um arquivo.
* **FileNotFoundError**: Ocorre quando um arquivo específico não pode ser encontrado.
* **TypeError**: Ocorre quando uma operação é realizada em um tipo de dado inadequado.
* **KeyError**: Ocorre quando um dicionário é acessado com uma chave que não existe.
* **ZeroDivisionError**: Ocorre quando se tenta dividir um número por zero.
* **ArithmeticError**: Exceção base para erros matemáticos.
* **RuntimeError**: Erros que não se encaixam em categorias mais específicas.
* **Exception**: Exceção base para todas as exceções internas em Python.
* ...

## Como tratar exceções

Python permite que você "intercepte" exceções e tome medidas para corrigir ou lidar com elas de forma controlada,
evitando que o programa simplesmente pare de funcionar.

Em Python, o tratamento de exceções é feito usando os blocos `try` e `except`. 
O bloco `try` contém o código que pode potencialmente causar uma exceção, enquanto o bloco `except` define como o programa deve responder a essa exceção.
Aqui está um exemplo básico de como isso funciona:

```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"O resultado é {resultado}")
except ValueError:
    print("Erro: Você precisa digitar um número válido.")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
```

### Explicação do Código:

1. Bloco `try`: 
O código dentro do bloco `try` é executado.
Se não houver erros, o bloco `except` é ignorado e o programa continua normalmente.
Se ocorrer um erro, o fluxo do programa salta para o bloco `except`.

2. Blocos `except`:
Cada bloco except trata um tipo específico de exceção.
No exemplo acima, temos dois tipos de exceções sendo tratadas:
    * **ValueError**: Esse erro ocorre se o usuário inserir algo que não pode ser convertido em um número inteiro. Nesse caso, uma mensagem é exibida pedindo um número válido.
    * **ZeroDivisionError**: Esse erro ocorre se o usuário inserir 0, pois a divisão por zero não é definida.

3. Vantagem do Tratamento de Exceções:
Usando `try` e `except`, o programa é capaz de lidar com entradas inesperadas e continuar funcionando, em vez de encerrar de forma abrupta.

## Mais funcionalidades

### Tratamento de Exceções Múltiplas

Em vez de tratar cada tipo de exceção em um bloco de código diferente, você pode tratar várias exceções de uma vez em um único bloco except usando uma tupla.
Isso é útil quando você deseja aplicar a mesma correção para diferentes tipos de exceções.

```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"O resultado é {resultado}")
except (ValueError, ZeroDivisionError) as e:
    print(f"Erro: {e}")
```

Nesse exemplo, tanto `ValueError` quanto `ZeroDivisionError` são tratados pelo mesmo bloco `except`, e a variável e contém a mensagem de erro gerada.

### Bloco `else`

O bloco `else` pode ser usado para definir um código que deve ser executado se o bloco try não levantar exceções.
Isso é útil para separar o código que deve ser executado quando não há erros dos que devem ser executados em caso de erro.

```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except (ValueError, ZeroDivisionError) as e:
    print(f"Erro: {e}")
else:
    print(f"O resultado é {resultado}")
```

### Bloco `finally`

O bloco `finally` é usado para definir um código que deve ser executado independentemente de uma exceção ter sido levantada ou não.
Ele é frequentemente usado para liberar recursos, como arquivos abertos ou conexões de banco de dados.

##  Boas Práticas no Tratamento de Exceções

* **Seja Específico**:
Trate exceções específicas em vez de usar um bloco except genérico. Isso ajuda a evitar esconder erros inesperados e facilita a depuração.
* **Evite Silenciar Exceções**:
Não use blocos except vazios, pois isso pode esconder erros e dificultar a identificação de problemas no código.
* **Forneça Feedback Claro**:
Ao tratar exceções, forneça mensagens de erro claras e úteis para o usuário, explicando o que deu errado e, se possível, como corrigir o problema.

## Lançando Nossas Próprias Exceções

Além de tratar exceções que ocorrem durante a execução do seu programa, você também pode lançar suas próprias exceções quando encontrar condições que não podem ser resolvidas automaticamente.
Isso é útil para criar uma comunicação mais clara sobre o que está errado e permitir que outras partes do seu código tratem essas situações de maneira adequada.

### Como Lançar Exceções

Para lançar uma exceção, você usa a palavra-chave raise, seguida pela instância da exceção que deseja lançar. Você pode lançar exceções existentes ou criar suas próprias exceções personalizadas.

```python
def verificar_idade(idade):
    if idade < 0:
        raise ValueError("Idade não pode ser negativa.")
    print(f"A idade fornecida é {idade}.")

try:
    verificar_idade(-1)
except ValueError as e:
    print(f"Erro: {e}")
```

Nesse exemplo, a função `verificar_idade` lança uma exceção ValueError se a idade fornecida for negativa.
O bloco `except` captura essa exceção e exibe uma mensagem de erro.

### Quando Lançar Exceções

* **Validação de Dados**:
Lançar exceções quando os dados fornecidos não atendem aos requisitos esperados.
* **Erros Lógicos**:
Lançar exceções quando uma operação não pode ser completada devido a um estado inválido ou erro lógico no programa.
* **Condições Específicas**:
Lançar exceções para condições que são específicas do domínio do problema que o programa está resolvendo.

### Boas Práticas para Lançar Exceções

* **Seja Claro e Específico**:
Ao criar exceções personalizadas, certifique-se de que elas são descritivas e fornecem informações úteis sobre o erro.
* **Documente Exceções**: 
Inclua documentação sobre as exceções que sua função pode lançar e o que essas exceções representam. Isso ajuda os desenvolvedores que usam seu código a entender como lidar com os erros.
* **Use Exceções Apropriadas**:
Não lance exceções para condições que podem ser tratadas de outra forma. Use exceções para erros realmente excepcionais e inesperados.


## Exercícios

1. Crie um programa que leia números de um arquivo chamado numeros.txt, um por linha, e calcule a média desses números.
Trate as exceções para os seguintes casos:
* O arquivo não existe.
* Uma linha no arquivo contém um valor que não pode ser convertido em número.
* Nenhum valor válido foi encontrado no arquivo (não é possível calcular a média).

2. Crie uma função chamada `distancia_euclidiana` que calcula a distância euclidiana entre dois vetores `v1` e `v2`.
Lance uma exceção para os seguintes casos:
* As variáveis não sejam listas de floats ou inteiros.
* As listas não possuam o mesmo tamanho.