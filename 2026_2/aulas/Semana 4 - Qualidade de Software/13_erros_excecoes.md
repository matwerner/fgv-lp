# Aula 12: Erros e Exceções II

## 1. Propagação de Exceções

Uma função não precisa necessariamente tratar todas as exceções que ocorrem durante sua execução.

Considere:

```python
def converter_valor(valor):
    return float(valor)


def criar_transacao(campos):
    valor = converter_valor(campos[3])

    return {
        "data": campos[0],
        "descricao": campos[1],
        "categoria": campos[2],
        "valor": valor
    }
```

Ao executar:

```python
campos = [
    "2026-08-03",
    "Restaurante",
    "Alimentação",
    "oitenta"
]

criar_transacao(campos)
```

temos a seguinte sequência de chamadas:

```text
criar_transacao()
        ↓
converter_valor()
        ↓
float("oitenta")
```

A operação:

```python
float("oitenta")
```

levanta uma `ValueError`.

Entretanto, `converter_valor()` não trata essa exceção.

Nesse caso, a exceção é **propagada** para a função que realizou a chamada.

```text
criar_transacao()
        ↓
converter_valor()
        ↓
float()
        ↓
ValueError
        ↑
converter_valor()
        ↑
criar_transacao()
```

Se nenhuma função tratar a exceção, ela continua sendo propagada até chegar ao código que iniciou a sequência de chamadas.

Caso continue sem ser tratada, o programa é encerrado e um traceback é apresentado.

### 1.1. Tratando a Exceção em Outro Nível

Podemos tratar a exceção fora de `criar_transacao()`:

```python
try:
    transacao = criar_transacao(campos)
except ValueError:
    print("A transação possui um valor inválido.")
```

Isso permite separar duas responsabilidades:

* `criar_transacao()` tenta criar uma transação;
* quem chamou a função decide o que fazer caso a operação não possa ser concluída.



## 2. Onde Devemos Tratar uma Exceção?

Considere:

```python
def converter_valor(valor):
    try:
        return float(valor)
    except ValueError:
        print("Valor inválido.")
        return None
```

Essa função decidiu que, caso a conversão falhe:

1. uma mensagem será exibida;
2. `None` será retornado.

Entretanto, ela sabe o suficiente para tomar essas decisões?

Talvez quem chamou a função queira:

* solicitar novamente o valor;
* ignorar a transação;
* encerrar o programa;
* registrar o erro;
* informar ao usuário em qual linha do arquivo ocorreu o problema.

Podemos então escrever simplesmente:

```python
def converter_valor(valor):
    return float(valor)
```

Se a conversão falhar, a exceção será propagada.

Uma parte mais externa do programa pode decidir como reagir:

```python
try:
    transacao = criar_transacao(campos)
except ValueError as e:
    print(f"Não foi possível criar a transação: {e}")
```

Uma regra útil é:

> Trate uma exceção quando aquela parte do programa tiver informação suficiente para decidir o que fazer diante do problema.

Caso contrário, pode ser melhor permitir que a exceção continue sendo propagada.



## 3. Validação e Exceções

Nem toda situação inválida precisa ser descoberta utilizando `try` e `except`.

Considere novamente uma linha do arquivo de transações:

```text
2026-08-02,Aluguel,-2800.00
```

Podemos separar os campos:

```python
campos = linha.strip().split(",")
```

e verificar:

```python
if len(campos) != 4:
    print("A linha deve possuir exatamente 4 campos.")
```

Nesse caso, a condição que queremos verificar é simples.

Por outro lado, considere:

```text
2026-08-03,Restaurante,Alimentação,oitenta
```

Para descobrir se `"oitenta"` pode ser convertido para `float`, podemos simplesmente tentar realizar a conversão:

```python
try:
    valor = float(valor)
except ValueError:
    print("Valor inválido.")
```

Portanto, validações e exceções podem ser utilizadas de forma complementar.

### 3.1. Validação Explícita

Quando a condição que queremos verificar é simples:

```python
if len(campos) != 4:
    ...
```

ou:

```python
if quantidade <= 0:
    ...
```

podemos verificá-la diretamente.

### 3.2. Tentando Realizar uma Operação

Quando uma operação pode falhar naturalmente:

```python
valor = float(valor)
```

podemos utilizar a exceção produzida pela própria operação.

Não existe uma única regra que determine quando usar `if` ou `try`.

O importante é representar de forma clara as condições necessárias para que a operação seja realizada.



## 4. Lançando Exceções

Até agora vimos situações em que o próprio Python detecta que uma operação não pode ser realizada.

Por exemplo:

```python
float("abc")
```

levanta:

```text
ValueError
```

e:

```python
10 / 0
```

levanta:

```text
ZeroDivisionError
```

Entretanto, existem situações em que o Python considera todas as operações válidas, mas **nossa aplicação sabe que alguma condição necessária não foi satisfeita**.

Nesses casos, podemos utilizar `raise` para lançar explicitamente uma exceção.

### 4.1. Pré-condições de uma Função

Considere uma busca binária.

Para que o algoritmo funcione corretamente, a lista precisa estar ordenada.

```python
def busca_binaria(valores, alvo):
    # implementação da busca
    ...
```

A seguinte chamada é válida do ponto de vista da linguagem:

```python
busca_binaria([10, 3, 8, 1], 8)
```

Python não encontra nenhum problema com essa chamada.

Entretanto, a entrada viola uma condição necessária para o funcionamento correto do algoritmo.

Podemos tornar essa condição explícita:

```python
def busca_binaria(valores, alvo):
    if valores != sorted(valores):
        raise ValueError("A busca binária requer uma lista ordenada.")

    ...
```

Uma função pode utilizar exceções para indicar que suas pré-condições não foram satisfeitas.

### 4.2. Regras da Aplicação

Muitas vezes, a operação é perfeitamente válida para Python, mas não é permitida pelas regras da aplicação.

Considere:

```python
def sacar(saldo, valor):
    return saldo - valor
```

Python permite:

```python
sacar(100, 200)
```

e retorna:

```text
-100
```

Não existe nenhum problema matemático.

Entretanto, nossa aplicação pode definir que uma conta não pode ficar com saldo negativo.

```python
def sacar(saldo, valor):
    if valor <= 0:
        raise ValueError("O valor do saque deve ser positivo.")

    if valor > saldo:
        raise ValueError("Saldo insuficiente.")

    return saldo - valor
```

A função agora sinaliza que a operação não pode ser realizada segundo as regras da aplicação.

### 4.3. Uma Validação Anterior Pode Não Ser Suficiente

Considere uma loja virtual.

Quando um usuário adiciona um produto ao carrinho, podemos verificar:

```python
if produto["estoque"] > 0:
    adicionar_ao_carrinho(produto)
```

Também podemos verificar um cupom:

```python
if cupom_valido(cupom):
    aplicar_cupom(cupom)
```

Entretanto, algum tempo pode passar entre essas verificações e a finalização da compra.

Nesse intervalo:

* outro cliente pode comprar a última unidade;
* o cupom pode expirar;
* uma promoção pode terminar;
* alguma condição necessária para a compra pode mudar.

Por isso, as condições precisam ser verificadas novamente quando a operação é efetivamente realizada:

```python
def finalizar_compra(produto, cupom):
    if produto["estoque"] <= 0:
        raise ValueError("O produto não possui mais estoque.")

    if not cupom_valido(cupom):
        raise ValueError("O cupom não é mais válido.")

    ...
```

Uma validação feita anteriormente não garante necessariamente que uma condição continue válida no momento em que uma operação é executada.

### 4.4. Quando Lançar uma Exceção?

Algumas situações comuns incluem:

#### Argumentos Inválidos

Uma função recebe um valor que não consegue processar corretamente.

```python
def repetir(texto, quantidade):
    if quantidade < 0:
        raise ValueError("A quantidade não pode ser negativa.")

    return texto * quantidade
```

Outros exemplos:

* quantidade negativa;
* índice ou limite inválido;
* uma lista não ordenada fornecida para uma busca binária;
* um valor fora do domínio esperado pela função.

#### Violação de Regras da Aplicação

Uma operação viola regras definidas pelo sistema.

Exemplos:

* tentar sacar mais dinheiro do que existe na conta;
* tentar acessar uma funcionalidade sem permissão;
* utilizar um cupom expirado;
* matricular um aluno em uma turma cheia;
* finalizar uma compra sem estoque.

#### Operação Não Pode Ser Concluída

Algum recurso necessário não está disponível.

Exemplos:

* um arquivo necessário não existe;
* uma conexão com banco de dados falha;
* um serviço externo está indisponível;
* um recurso necessário para a operação deixa de existir.

Em muitos desses casos, a exceção original já pode ser levantada por outra operação.

Por exemplo:

```python
open("arquivo_inexistente.csv")
```

já levanta:

```text
FileNotFoundError
```

Nossa aplicação decide se deve tratar, propagar ou transformar essa exceção.

#### Evitando Falhas Silenciosas

Considere:

```python
def sacar(saldo, valor):
    if valor > saldo:
        return None

    return saldo - valor
```

Se quem chamou esquecer de verificar o retorno:

```python
novo_saldo = sacar(100, 200)

saldo_final = novo_saldo + 50
```

o erro aparecerá posteriormente:

```text
TypeError
```

Entretanto, o problema real aconteceu antes: o saque não pôde ser realizado.

Podemos sinalizar a falha no momento em que ela ocorre:

```python
def sacar(saldo, valor):
    if valor > saldo:
        raise ValueError("Saldo insuficiente.")

    return saldo - valor
```

### 4.5. Quando Não Lançar uma Exceção?

Nem toda situação diferente do caso principal representa um erro.

Exceções não devem substituir indiscriminadamente `if` e `else`.

#### Quando o Resultado Faz Parte do Fluxo Normal

Considere:

```python
def buscar_usuario(usuarios, email):
    for usuario in usuarios:
        if usuario["email"] == email:
            return usuario

    return None
```

Se não encontrar um usuário for um resultado esperado da busca, retornar `None` pode fazer parte normalmente do contrato da função.

#### Quando Existem Diferentes Caminhos Normais

```python
if idade >= 18:
    print("Maior de idade.")
else:
    print("Menor de idade.")
```

Ser menor de idade não representa necessariamente um erro.

É apenas outro possível estado do programa.

#### Quando uma Condição Pode Ser Tratada Naturalmente

Considere uma interface de uma loja:

```python
if produto["estoque"] > 0:
    mostrar_botao_comprar()
else:
    mostrar_produto_indisponivel()
```

Não precisamos lançar uma exceção para decidir o que mostrar.

Por outro lado:

```python
finalizar_compra(produto)
```

pode precisar lançar uma exceção se o estoque acabar no momento da finalização.

A mesma condição pode representar um fluxo normal em um contexto e impedir uma operação em outro.



## 5. Complementos ao Tratamento de Exceções

Além de `try` e `except`, Python permite utilizar os blocos `else` e `finally`.

### 5.1. `else`

O bloco `else` é executado somente quando nenhuma exceção ocorre no bloco `try`.

```python
try:
    numero = int(input("Digite um número: "))

except ValueError:
    print("Número inválido.")

else:
    print(f"Número informado: {numero}")
```

Se o usuário fornecer:

```text
10
```

o bloco `else` é executado.

Se fornecer:

```text
abc
```

o bloco `except` é executado e o `else` é ignorado.

O `else` também pode ajudar a manter o bloco `try` restrito somente às operações que podem gerar as exceções que desejamos tratar:

```python
try:
    transacao = criar_transacao(linha)

except ValueError as e:
    print(f"Transação inválida: {e}")

else:
    transacoes.append(transacao)
```

Nesse exemplo, uma possível exceção produzida por:

```python
transacoes.append(transacao)
```

não será confundida com uma exceção produzida por `criar_transacao()`.

### 5.2. `finally`

O bloco `finally` é executado independentemente de uma exceção ter ocorrido.

```python
try:
    numero = int(input("Digite um número: "))

except ValueError:
    print("Número inválido.")

finally:
    print("Operação finalizada.")
```

A mensagem:

```text
Operação finalizada.
```

será exibida tanto para uma entrada válida quanto para uma entrada inválida.

Um uso comum de `finally` é garantir que determinados recursos sejam liberados:

```python
arquivo = open("dados.txt")

try:
    conteudo = arquivo.read()
finally:
    arquivo.close()
```

Mesmo que uma exceção ocorra durante a leitura, `arquivo.close()` será executado.

Para arquivos, entretanto, normalmente utilizamos:

```python
with open("dados.txt") as arquivo:
    conteudo = arquivo.read()
```

O `with` já garante que o arquivo seja fechado corretamente.

O `finally` é um mecanismo mais geral para situações nas quais determinada ação precisa acontecer independentemente do resultado da operação.



## 6. Exceções Personalizadas

As exceções existentes em Python, como:

```python
ValueError
```

```python
TypeError
```

```python
FileNotFoundError
```

são suficientes para muitas situações.

Entretanto, algumas aplicações possuem situações de erro específicas do seu próprio domínio.

### 6.1. Acesso Negado

Considere uma aplicação na qual apenas administradores podem remover usuários.

Podemos criar:

```python
class AcessoNegadoError(Exception):
    pass
```

e utilizar:

```python
def remover_usuario(usuario_atual, usuario):
    if not usuario_atual["administrador"]:
        raise AcessoNegadoError("Apenas administradores podem remover usuários.")

    ...
```

Podemos então tratar especificamente essa situação:

```python
try:
    remover_usuario(usuario_atual, usuario)

except AcessoNegadoError as e:
    print(e)
```

### 6.2. Saldo Insuficiente

Também podemos criar:

```python
class SaldoInsuficienteError(Exception):
    pass
```

e escrever:

```python
def sacar(saldo, valor):
    if valor <= 0:
        raise ValueError("O valor do saque deve ser positivo.")

    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente.")

    return saldo - valor
```

Agora existem duas situações conceitualmente diferentes.

```python
sacar(100, -20)
```

representa um argumento inválido.

Já:

```python
sacar(100, 200)
```

representa uma situação específica do domínio bancário: não existe saldo suficiente para realizar a operação.

Podemos tratá-las separadamente:

```python
try:
    saldo = sacar(saldo, valor)

except ValueError as e:
    print(f"Valor inválido: {e}")

except SaldoInsuficienteError as e:
    print(f"Não foi possível realizar o saque: {e}")
```

### 6.3. Por que Criar Exceções Próprias?

Considere:

```python
except ValueError:
```

Esse bloco pode representar inúmeros problemas diferentes.

Já:

```python
except SaldoInsuficienteError:
```

expressa diretamente uma situação específica da aplicação.

Exceções personalizadas ajudam a comunicar **qual tipo de operação falhou** sem obrigar quem utiliza uma função a conhecer todos os detalhes de sua implementação.

A definição:

```python
class SaldoInsuficienteError(Exception):
    pass
```

utiliza classes e herança.

Por enquanto, basta entender que estamos criando um novo tipo de exceção baseado em `Exception`.

Esses conceitos serão estudados em mais detalhes posteriormente.



## 7. Separando Quem Detecta de Quem Trata

Considere:

```python
def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente.")

    return saldo - valor
```

A função sabe que a operação não pode ser realizada.

Entretanto, ela não precisa saber como o restante do programa deve reagir.

Podemos ter:

```python
try:
    saldo = sacar(saldo, valor)

except SaldoInsuficienteError:
    print("Você não possui saldo suficiente.")
```

ou:

```python
try:
    saldo = sacar(saldo, valor)

except SaldoInsuficienteError:
    registrar_tentativa_de_saque()
```

Portanto, podemos separar:

```text
Detectar o problema
        ↓
Lançar uma exceção
        ↓
Propagar a exceção
        ↓
Tratar onde existe informação suficiente
```

Essa separação está relacionada aos princípios de responsabilidade e coesão.



## 8. Exercício: Intervalo entre Datas

Implemente um programa que calcule a quantidade de dias entre duas datas.

Para simplificar o problema, considere que:

* todos os meses possuem exatamente 30 dias;
* todos os anos possuem exatamente 360 dias.

As datas serão fornecidas como strings no formato:

```text
DD/MM/AAAA
```

Por exemplo:

```text
15/08/2026
```

Implemente a função:

```python
def converter_data(data):
    ...
```

responsável por converter uma string para uma tupla:

```python
(dia, mes, ano)
```

A função deve lançar uma exceção caso:

* a entrada não possua exatamente três componentes separados por `/`;
* dia, mês ou ano não possam ser convertidos para `int`;
* o dia não esteja entre `1` e `30`;
* o mês não esteja entre `1` e `12`.

Implemente também:

```python
def calcular_dias(data_inicio, data_fim):
    ...
```

A função deve retornar a quantidade de dias entre as duas datas.

Caso `data_inicio` ocorra depois de `data_fim`, a função deve lançar uma exceção.

Por fim, escreva um programa que:

1. solicite a data inicial;
2. solicite a data final;
3. converta as duas entradas;
4. calcule a quantidade de dias;
5. trate adequadamente as possíveis exceções;
6. apresente o resultado somente quando a operação for realizada com sucesso.

Considere entradas como:

```text
10/08/2026
```

```text
10-08-2026
```

```text
dez/08/2026
```

```text
35/08/2026
```

```text
20/08/2026
10/08/2026
```

Pense também:

* Quais erros já produzem naturalmente uma exceção do Python?
* Em quais situações nosso próprio código precisa utilizar `raise`?
* Faz sentido utilizar apenas `ValueError` ou criar exceções específicas?
* Em qual parte do programa cada exceção deve ser tratada?
