# Aula 14: Testes Automatizados II

## 1. Exercício: Calculando o Valor Final de uma Compra

Uma loja virtual utiliza a função:

```python
def calcular_total(valor_produtos, regiao, cupom=None):
    ...
```

para calcular o valor final de uma compra.

### 1.1. Regras

O cálculo deve obedecer às seguintes regras:

1. O valor dos produtos deve ser maior que zero.

2. São aceitas apenas as regiões: `sudeste`, `sul` e `nordeste`

3. O frete depende da região:

    | Região   | Frete |
    | -------- | ----: |
    | Sudeste  | R$ 15 |
    | Sul      | R$ 20 |
    | Nordeste | R$ 30 |

4. Compras com valor dos produtos **acima de R$ 200** possuem frete grátis.

5. Existem dois cupons:

    * `DESCONTO10`: Aplica 10% de desconto sobre o valor dos produtos.
    * `DESCONTO20`: Aplica 20% de desconto sobre o valor dos produtos, mas somente pode ser utilizado em compras de pelo menos R$ 150.

6. O desconto não é aplicado sobre o frete.

7. As regras de desconto e frete grátis devem considerar o **valor original dos produtos**, antes da aplicação do desconto.

8. Devem gerar `ValueError`:
    * valor dos produtos menor ou igual a zero;
    * região inválida;
    * cupom desconhecido;
    * uso de `DESCONTO20` em compras abaixo de R$ 150.

### 1.2. Implementação

Você recebeu a seguinte implementação:

```python
def calcular_total(valor_produtos, regiao, cupom=None):
    if valor_produtos < 0:
        raise ValueError("Valor inválido")

    if cupom == "DESCONTO10":
        valor_produtos *= 0.90
    elif cupom == "DESCONTO20":
        valor_produtos *= 0.80

    if valor_produtos >= 200:
        frete = 0
    elif regiao == "sudeste":
        frete = 15
    elif regiao == "sul":
        frete = 20
    else:
        frete = 30

    return valor_produtos + frete
```

Não assuma que a implementação está correta.

### 1.3. Atividade

1. Entenda as regras do problema.
2. Analise a implementação fornecida.
3. Proponha casos de teste que considere relevantes.
4. Determine previamente o comportamento esperado para cada caso.
5. Execute os casos propostos.
6. Compare o comportamento observado com o esperado.
7. Caso encontre um problema, indique:

   * qual entrada revelou o problema;
   * qual era o comportamento esperado;
   * qual comportamento foi observado.

Não é necessário corrigir a implementação neste momento.

Procure considerar diferentes situações discutidas nas aulas anteriores:

```text
casos típicos
casos de borda
entradas inválidas
diferentes regras
diferentes caminhos
combinações entre regras
```



## 2. Discussão do Exercício

Quais casos foram utilizados para avaliar a implementação?

Podemos organizar os resultados encontrados:

| Situação               | Entrada | Esperado | Obtido |
| ---------------------- | ------- | -------- | ------ |
| Compra normal          |         |          |        |
| Limite do frete grátis |         |          |        |
| Cupom de 10%           |         |          |        |
| Cupom de 20%           |         |          |        |
| Cupom + frete grátis   |         |          |        |
| Região inválida        |         |          |        |
| Valor inválido         |         |          |        |

Algumas perguntas:

* Testamos somente valores diferentes ou situações diferentes?
* Os limites das regras foram testados?
* Testamos cada regra isoladamente?
* Existem regras que podem interagir?
* Algum teste encontrou um comportamento incorreto?
* Seria possível uma implementação passar por vários testes e ainda possuir bugs?

Até agora, estamos realizando essas verificações manualmente.

Como podemos automatizar esse processo?



## 3. Do Teste Manual ao `assert`

Considere um teste escrito utilizando apenas os recursos vistos até agora:

```python
resultado = calcular_total(100, "sudeste")
esperado = 115

if resultado == esperado:
    print("Teste passou")
else:
    print(
        f"Teste falhou: "
        f"esperado {esperado}, obtido {resultado}"
    )
```

O objetivo desse código é verificar uma condição:

```text
resultado obtido == resultado esperado
```

Python possui o comando `assert` para expressar diretamente esse tipo de expectativa.

```python
assert calcular_total(100, "sudeste") == 115
```

De forma geral:

```python
assert condicao
```

significa que esperamos que `condicao` seja verdadeira.

Por exemplo:

```python
assert 2 + 2 == 4
```

não produz erro.

Entretanto:

```python
assert 2 + 2 == 5
```

produz:

```text
AssertionError
```

Podemos então escrever:

```python
assert calcular_total(100, "sudeste") == 115
assert calcular_total(100, "sul") == 120
assert calcular_total(100, "nordeste") == 130
```

O `assert` simplifica nossas verificações.

Entretanto, ainda existem algumas questões:

* como organizar dezenas ou centenas de testes?
* como executar todos os testes automaticamente?
* como saber rapidamente quais testes falharam?
* como repetir todos os testes depois de modificar o programa?

Para isso, podemos utilizar um **framework de testes**.



## 4. Testes com Pytest

`pytest` é um framework utilizado para escrever, organizar e executar testes em Python.

Ele permite, entre outras coisas:

* encontrar testes automaticamente;
* executar uma suíte de testes;
* identificar quais testes passaram ou falharam;
* apresentar informações sobre as falhas;
* testar exceções esperadas.

### 4.1. Instalando o Pytest

`pytest` não faz parte da biblioteca padrão de Python.

Python possui um grande ecossistema de bibliotecas externas, que podem ser instaladas utilizando ferramentas como o `pip`.

Para instalar `pytest`:

```bash
python -m pip install pytest
```

Podemos verificar a instalação:

```bash
python -m pytest --version
```

Não vamos aprofundar neste momento questões relacionadas a gerenciamento de pacotes.

Para esta aula, basta observar:

```text
pip
 ↓
instala bibliotecas externas
```

### 4.2. Adaptando nossos Testes ao Framework

Até agora, nossos testes eram scripts Python comuns.

Para que um framework consiga encontrar, organizar e executar automaticamente nossos testes, precisamos escrevê-los seguindo o **formato esperado pelo framework**.

No caso do `pytest`, as convenções básicas são simples.

Os arquivos de teste normalmente seguem o padrão:

```text
test_*.py
```

Por exemplo:

```text
compra.py
test_compra.py
```

Além disso, as funções de teste devem começar com:

```text
test_
```

Por exemplo:

```python
def test_compra_sudeste():
    ...
```

Assim, uma possível organização seria:

```text
projeto/
├── compra.py
└── test_compra.py
```

Essas convenções permitem que o `pytest` descubra automaticamente quais testes devem ser executados.

### 4.3. Nosso Primeiro Teste

Em `compra.py`:

```python
def calcular_total(valor_produtos, regiao, cupom=None):
    ...
```

Em `test_compra.py`:

```python
from compra import calcular_total


def test_compra_sudeste():
    assert calcular_total(100, "sudeste") == 115
```

Podemos acrescentar outros testes:

```python
def test_compra_sul():
    assert calcular_total(100, "sul") == 120


def test_compra_nordeste():
    assert calcular_total(100, "nordeste") == 130
```

Observe que não precisamos executar manualmente:

```python
test_compra_sudeste()
test_compra_sul()
test_compra_nordeste()
```

O framework encontra essas funções utilizando as convenções apresentadas anteriormente.

### 4.4. Executando os Testes

Podemos executar:

```bash
python -m pytest
```

Um possível resultado é:

```text
==================== test session starts ====================

collected 4 items

test_compra.py ...F

========================= FAILURES ==========================
_____________________ test_limite_frete __________________

    def test_limite_frete():
>       assert calcular_total(200, "sudeste") == 215
E       assert 200 == 215

================== 1 failed, 3 passed ======================
```

O framework informa:

* quantos testes foram encontrados;
* quais passaram;
* quais falharam;
* em qual teste ocorreu a falha;
* qual comparação não produziu o resultado esperado.

Isso é mais conveniente do que implementar manualmente mensagens como:

```python
if resultado == esperado:
    print("Teste passou")
else:
    print("Teste falhou")
```

Além disso, após modificar a implementação podemos simplesmente executar novamente:

```bash
python -m pytest
```

e verificar toda a suíte.

### 4.5. Testando Exceções

Alguns testes não esperam um valor retornado.

Considere a regra:

> `valor_produtos <= 0` deve lançar `ValueError`.

Para verificar esse comportamento com `pytest`, podemos utilizar `pytest.raises()`.

```python
import pytest

from compra import calcular_total


def test_valor_negativo():
    with pytest.raises(ValueError):
        calcular_total(-10, "sudeste")
```

Também podemos testar:

```python
def test_valor_zero():
    with pytest.raises(ValueError):
        calcular_total(0, "sudeste")
```

Nesse caso:

```text
nenhuma exceção
→ teste falha

ValueError
→ teste passa

outra exceção
→ teste falha
```

Portanto, uma exceção não representa necessariamente uma falha do teste.

Se ela faz parte do comportamento especificado para a função, sua ocorrência é justamente aquilo que queremos verificar.

### 4.6. Outra Opção: `unittest`

`pytest` não é o único framework de testes utilizado em Python.

Python possui também o módulo:

```python
unittest
```

que faz parte da biblioteca padrão e, portanto, não precisa ser instalado.

Um teste semelhante poderia ser escrito como:

```python
import unittest

from compra import calcular_total


class TestCompra(unittest.TestCase):

    def test_compra_sudeste(self):
        self.assertEqual(
            calcular_total(100, "sudeste"),
            115
        )
```

E uma exceção poderia ser testada utilizando:

```python
def test_valor_negativo(self):
    with self.assertRaises(ValueError):
        calcular_total(-10, "sudeste")
```

`unittest` é bastante utilizado, mas sua estrutura é baseada em conceitos como:

```text
classes
métodos
herança
```

que ainda estudaremos posteriormente.

Por esse motivo, neste momento utilizaremos `pytest`, cuja estrutura básica exige menos conceitos novos:

```python
def test_alguma_coisa():
    assert ...
```



## 5. Cobertura de Testes

Suponha que escrevemos dez testes e todos passaram.

Podemos concluir que todas as partes da nossa implementação foram exercitadas?

Não necessariamente.

**Cobertura de testes**, ou *test coverage*, mede quais partes do programa foram executadas durante os testes.

Podemos utilizar a biblioteca `coverage` para obter essa informação.

### 5.1. Instalando o Coverage

A biblioteca pode ser instalada utilizando:

```bash
python -m pip install coverage
```

Temos então duas ferramentas diferentes:

```text
pytest
→ encontra e executa nossos testes

coverage
→ observa quais partes do código foram executadas
```

As duas podem ser utilizadas em conjunto.

### 5.2. Executando os Testes com Coverage

Normalmente executaríamos:

```bash
python -m pytest
```

Para executar os mesmos testes enquanto o `coverage` coleta informações:

```bash
coverage run -m pytest
```

Depois podemos gerar um relatório:

```bash
coverage report
```

Por exemplo:

```text
Name             Stmts   Miss  Cover
------------------------------------
compra.py           18      5    72%
test_compra.py      12      0   100%
------------------------------------
TOTAL               30      5    83%
```

Podemos também visualizar quais linhas não foram executadas:

```bash
coverage report -m
```

Por exemplo:

```text
Name        Stmts   Miss  Cover   Missing
-----------------------------------------
compra.py      18      5    72%   8, 12-14, 20
```

Isso permite fazer uma nova pergunta:

> Por que essas linhas nunca foram executadas pelos nossos testes?

Talvez exista algum comportamento importante para o qual ainda não criamos um caso de teste.

### 5.3. Relatório HTML

Também podemos gerar um relatório mais detalhado em HTML:

```bash
coverage html
```

A ferramenta cria um relatório no qual podemos visualizar diretamente quais linhas foram:

```text
executadas
```

e quais linhas:

```text
não foram executadas
```

Isso pode ajudar a identificar partes da implementação ainda não exercitadas pela suíte de testes.

### 5.4. Coverage e Escolha de Casos

Na aula anterior, vimos que podemos olhar para os diferentes caminhos da implementação ao projetar testes.

Coverage fornece uma ferramenta adicional para fazer essa análise.

Por exemplo, se nunca testamos:

```text
regiao == "sul"
```

é possível que o trecho correspondente ao frete da região Sul nunca seja executado.

Se nunca testamos:

```text
cupom == "DESCONTO20"
```

as instruções relacionadas a esse cupom podem permanecer sem cobertura.

Coverage pode, portanto, revelar **lacunas na suíte de testes**.

### 5.5. 100% de Coverage Significa Código Correto?

Considere:

```python
def test_classificar():
    classificar(10)
    classificar(-10)
    classificar(0)
```

Talvez essas chamadas executem todas as linhas de:

```python
def classificar(x):
    if x > 0:
        return "positivo"
    elif x < 0:
        return "negativo"
    else:
        return "zero"
```

Entretanto, o teste não verifica nenhum resultado.

Não existe:

```python
assert ...
```

A função poderia retornar valores incorretos e ainda assim todas as linhas serem executadas.

Portanto:

> Coverage indica quais partes do código foram executadas pelos testes. Ele não indica se o comportamento foi verificado corretamente.

Uma cobertura de:

```text
100%
```

não garante:

```text
programa correto
```

Coverage complementa a escolha de bons casos de teste.

Ele não substitui essa escolha.



## 6. Exercício: Avaliando uma Implementação de CPF

Considere a seguinte função:

```python
def cpf_valido(cpf):
    if len(cpf) != 11:
        return False

    if not cpf.isdigit():
        return False

    numeros = [int(digito) for digito in cpf]

    soma = 0

    for i in range(9):
        soma += numeros[i] * (10 - i)

    resto = soma % 11

    if resto < 2:
        primeiro = 0
    else:
        primeiro = 11 - resto

    soma = 0

    for i in range(9):
        soma += numeros[i] * (11 - i)

    soma += primeiro * 2

    resto = soma % 11

    if resto < 2:
        segundo = 0
    else:
        segundo = 11 - resto

    return (
        primeiro == numeros[9]
        or segundo == numeros[10]
    )
```

Não assuma que a implementação está correta.

### 6.1. Regras

A função deve obedecer às seguintes regras:

1. O CPF deve ser fornecido como uma `str`.
2. A string deve possuir exatamente 11 caracteres.
3. Todos os caracteres devem ser dígitos.
4. O primeiro dígito verificador deve ser calculado a partir dos nove primeiros dígitos.
5. O segundo dígito verificador deve ser calculado a partir dos nove primeiros dígitos e do primeiro dígito verificador.
6. Os dois dígitos verificadores precisam estar corretos para que o CPF seja considerado válido.
7. Sequências formadas pelo mesmo dígito repetido onze vezes, como:
    ```text
    00000000000
    11111111111
    22222222222
    ...
    99999999999
    ```
    não são consideradas CPFs válidos.
8. A função deve retornar:
    * `True` para um CPF válido;
    * `False` para um CPF inválido.

### 6.2. Atividade

1. Entenda o contrato da função.
2. Analise a implementação fornecida.
3. Identifique situações relevantes que deveriam ser testadas.
4. Implemente os testes utilizando `pytest`.
5. Organize seus arquivos, por exemplo:
    ```text
    cpf.py
    test_cpf.py
    ```
6. Execute:
    ```bash
    python -m pytest
    ```
7. Verifique:
   * quais testes passaram;
   * quais testes falharam;
   * se algum comportamento observado é diferente do especificado.
8. Caso encontre um problema:
   * indique o teste que revelou o problema;
   * indique o comportamento esperado;
   * indique o comportamento observado.
9. Execute novamente os testes utilizando:
    ```bash
    coverage run -m pytest
    ```
10. Analise o relatório:
    ```bash
    coverage report -m
    ```
11. Verifique se existem partes da implementação que não foram executadas pelos testes.
12. Caso identifique comportamentos relevantes ainda não testados, acrescente novos testes.
13. Não altere a implementação antes de avaliar se uma falha encontrada está no teste ou no código fornecido.
