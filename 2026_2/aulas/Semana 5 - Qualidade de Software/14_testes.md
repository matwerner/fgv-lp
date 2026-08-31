# Aula 13: Testes Automatizados I

## 1. Por que Testar?

Nas aulas anteriores, vimos diferentes tipos de erros.

Alguns erros são identificados diretamente pelo Python:

```python
int("abc")
```

produz:

```text
ValueError
```

Entretanto, outros programas podem executar normalmente e ainda produzir resultados incorretos.

Considere:

```python
def find_min_value(arr):
    min_value = 0

    for value in arr:
        if value < min_value:
            min_value = value

    return min_value
```

Ao executar:

```python
find_min_value([1, 2, 3, 4])
```

obtemos:

```text
0
```

quando esperamos:

```text
1
```

Não existe erro de sintaxe.

Nenhuma exceção é levantada.

O problema está na lógica utilizada pela implementação.

Para descobrir esse tipo de problema, precisamos comparar o comportamento obtido com o comportamento esperado.

```text
Entrada
   ↓
Programa
   ↓
Resultado obtido
   ↕
Resultado esperado
```

Essa é a ideia fundamental de um teste:

> Executar uma operação para uma determinada situação e verificar se seu comportamento corresponde ao esperado.

### 1.1. Testar Apenas uma Vez é Suficiente?

Considere uma função:

```python
def dobro(x):
    return x * 2
```

Podemos verificar:

```python
dobro(5)
```

e obter:

```text
10
```

Isso aumenta nossa confiança na implementação.

Entretanto, em funções mais complexas, uma entrada pode funcionar corretamente enquanto outras revelam erros.

Portanto, além de testar, precisamos decidir:

> Quais situações devemos testar?

## 2. Diferentes Tipos de Teste

Existem diferentes formas de testar um software.

Alguns exemplos incluem:

| Tipo de teste                | Objetivo                                                                            |
| ---------------------------- | ----------------------------------------------------------------------------------- |
| Teste unitário               | Verificar uma pequena unidade do programa isoladamente                              |
| Teste de integração          | Verificar se diferentes partes do sistema funcionam corretamente em conjunto        |
| Teste de sistema / E2E       | Verificar o comportamento do sistema completo                                       |
| Teste de aceitação           | Verificar se o sistema atende aos requisitos esperados pelo usuário ou pelo negócio |
| Teste de performance / carga | Verificar desempenho e comportamento do sistema sob diferentes níveis de utilização |
| Teste A/B                    | Comparar diferentes versões de uma funcionalidade utilizando alguma métrica         |

Por exemplo, em uma aplicação de compras:

```text
Teste unitário
    ↓
A função calcular_desconto() retorna o valor correto?


Teste de integração
    ↓
O serviço de compras consegue consultar corretamente o serviço de estoque?


Teste de sistema
    ↓
O usuário consegue adicionar um produto, pagar e finalizar uma compra?


Teste de performance
    ↓
O sistema continua respondendo adequadamente com milhares de usuários?


Teste A/B
    ↓
Qual das duas versões da página resulta em mais compras?
```

Testes A/B possuem um objetivo um pouco diferente dos demais.

Normalmente, eles não procuram verificar se uma implementação está correta, mas comparar alternativas e descobrir qual apresenta melhores resultados segundo determinada métrica.

Nesta disciplina, vamos nos concentrar principalmente em **testes unitários**.

## 3. Testes Unitários e Código Testável

Um teste unitário verifica uma pequena unidade do programa de forma isolada.

Em programas procedurais, essa unidade normalmente é uma função.

Por exemplo:

```python
def converter_data(data):
    ...


def calcular_dias(data_inicio, data_fim):
    ...
```

Podemos verificar separadamente se:

```python
converter_data(...)
```

interpreta corretamente uma data e se:

```python
calcular_dias(...)
```

calcula corretamente um intervalo.

### 3.1. Responsabilidade e Testabilidade

Considere um programa que:

1. solicita duas datas;
2. separa seus componentes;
3. converte os componentes para inteiros;
4. valida as datas;
5. calcula a quantidade de dias;
6. apresenta o resultado.

Podemos colocar tudo em uma única função:

```python
def programa():
    data_inicio = input("Data inicial: ")
    data_fim = input("Data final: ")

    # conversão
    # validação
    # cálculo
    # apresentação
```

Entretanto, como podemos testar apenas:

> A conversão de uma data funciona corretamente?

Ou:

> O cálculo entre duas datas já válidas está correto?

Quando várias responsabilidades estão misturadas, precisamos lidar simultaneamente com diferentes combinações de situações.

Por exemplo:

```text
Conversão da primeira data
×
Conversão da segunda data
×
Validade da primeira data
×
Validade da segunda data
×
Ordem das datas
```

O número de combinações cresce rapidamente.

Ao separar responsabilidades:

```python
def converter_data(data):
    ...


def calcular_dias(data_inicio, data_fim):
    ...
```

podemos testar cada problema isoladamente.

Isso recupera princípios vistos anteriormente:

```text
Responsabilidade
      ↓
Funções menores e mais coesas
      ↓
Menos comportamentos misturados
      ↓
Funções mais fáceis de testar
```

Portanto:

> Código bem modularizado não é apenas mais fácil de entender e modificar. Ele também tende a ser mais fácil de testar.

### 3.2. Separando Lógica de Entrada e Saída

Considere:

```python
def calcular_media():
    entrada = input("Valores: ")

    # processamento

    print(media)
```

Essa função mistura:

* entrada;
* processamento;
* apresentação.

Compare com:

```python
def calcular_media(valores):
    return sum(valores) / len(valores)
```

Agora conseguimos fornecer diretamente diferentes valores e observar o resultado retornado.

Separar a lógica do programa de operações de entrada e saída normalmente facilita a criação de testes unitários.

## 4. Como Escolher Casos de Teste?

Não é possível, na maioria dos programas, testar todas as entradas possíveis.

Precisamos escolher exemplos que representem situações relevantes e diferentes entre si.

Existem algumas estratégias que podem nos ajudar.

### 4.1. Casos Típicos

São situações comuns para as quais esperamos que a função funcione normalmente.

Considere:

```python
def merge(a, b):
    ...
```

que combina duas listas previamente ordenadas.

Um caso típico poderia ser:

```python
merge([1, 3], [2, 4])
```

com resultado esperado:

```python
[1, 2, 3, 4]
```

### 4.2. Casos de Borda

Casos de borda aparecem próximos aos limites do problema.

Para `merge()`, podemos considerar:

```python
merge([], [])
```

```python
merge([], [1, 2])
```

```python
merge([1, 2], [])
```

```python
merge([1], [2])
```

Listas vazias ou com poucos elementos frequentemente revelam problemas que não aparecem em entradas maiores.

Outros exemplos de casos de borda incluem:

* primeiro elemento;
* último elemento;
* valor mínimo;
* valor máximo;
* zero;
* transições entre diferentes comportamentos.

### 4.3. Entradas Inválidas

Também devemos considerar situações que violam as condições esperadas pela função.

Se `merge()` exige listas ordenadas:

```python
merge([3, 1, 5], [2, 4])
```

viola uma pré-condição.

O comportamento esperado depende do contrato definido para a função.

Ela poderia:

* lançar uma exceção;
* ordenar automaticamente;
* assumir que o usuário sempre fornecerá entradas válidas.

O teste deve verificar o comportamento que foi definido.

### 4.4. Diferentes Regras e Caminhos

Também podemos olhar para as decisões realizadas pelo algoritmo.

Considere uma implementação de `merge()`:

```python
def merge(a, b):
    i = 0
    j = 0
    resultado = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            resultado.append(a[i])
            i += 1
        else:
            resultado.append(b[j])
            j += 1

    return resultado
```

Existem diferentes situações relevantes:

```text
a[i] < b[j]
```

ou:

```text
a[i] >= b[j]
```

Além disso:

```text
primeira lista termina antes
```

ou:

```text
segunda lista termina antes
```

Podemos então escolher casos como:

```python
merge([1, 3], [2, 4])
```

listas intercaladas.

```python
merge([1, 2], [3, 4])
```

primeira lista termina antes.

```python
merge([3, 4], [1, 2])
```

segunda lista termina antes.

```python
merge([1, 2], [1, 2])
```

valores repetidos.

A ideia não é testar cada linha do código individualmente.

O objetivo é pensar em situações que exercitem comportamentos diferentes da implementação.

### 4.5. O Comportamento Esperado Nem Sempre é um Retorno

Considere:

```python
converter_data("10/08/2026")
```

O comportamento esperado pode ser retornar:

```python
(10, 8, 2026)
```

Entretanto:

```python
converter_data("35/08/2026")
```

pode ter como comportamento esperado:

```text
ValueError
```

Portanto, um caso de teste possui:

```text
Entrada
   ↓
Comportamento esperado
```

Esse comportamento pode significar:

* retornar determinado valor;
* modificar determinado estado;
* lançar determinada exceção.

Uma exceção não significa necessariamente que o teste falhou.

Se a função deveria rejeitar aquela entrada, a exceção pode ser exatamente o comportamento correto.

## 5. Exemplo: Projetando Testes para um Validador de CPF

Considere:

```python
def cpf_valido(cpf):
    ...
```

A função deve retornar:

```python
True
```

quando o CPF for válido e:

```python
False
```

quando for inválido.

Uma primeira tentativa poderia utilizar apenas:

```text
um CPF válido
um CPF inválido
```

Esses casos são suficientes?

### 5.1. Formato da Entrada

Podemos considerar:

* quantidade correta de dígitos;
* menos dígitos;
* mais dígitos;
* caracteres não numéricos.

Também precisamos definir o contrato da função.

Ela aceita:

```text
12345678909
```

ou também:

```text
123.456.789-09
```

?

Essa decisão influencia os testes que precisamos escrever.

### 5.2. Regras de Validação

Também podemos considerar situações nas quais:

* o CPF é válido;
* o primeiro dígito verificador está incorreto;
* o segundo dígito verificador está incorreto;
* os dois dígitos verificadores estão incorretos.

Cada uma dessas situações pode exercitar uma parte diferente da lógica implementada.

### 5.3. Casos Especiais

Também existem entradas como:

```text
00000000000
11111111111
22222222222
...
99999999999
```

Dependendo da implementação, sequências repetidas podem satisfazer parte do cálculo matemático dos dígitos verificadores e ainda assim não representar CPFs válidos.

Esse tipo de situação mostra que escolher bons testes exige conhecer as regras do problema.

Não basta gerar entradas aleatórias.

Precisamos perguntar:

> Quais situações podem fazer uma implementação aparentemente correta falhar?

## 6. O que Bons Testes nos Fornecem?

Testes não demonstram necessariamente que um programa está correto para todas as entradas possíveis.

Mesmo que:

```python
cpf_valido(cpf1)
cpf_valido(cpf2)
cpf_valido(cpf3)
```

produzam os resultados esperados, ainda podem existir outros casos que revelem problemas.

Entretanto, bons testes nos ajudam a:

* encontrar erros lógicos;
* verificar comportamentos conhecidos;
* aumentar nossa confiança na implementação;
* documentar como uma função deve se comportar;
* verificar casos de borda;
* garantir que entradas inválidas sejam tratadas corretamente;
* detectar erros reintroduzidos após modificações futuras.

Considere que corrigimos um erro específico no tratamento de CPFs repetidos.

Podemos manter um teste para:

```text
11111111111
```

Se uma alteração futura fizer a função voltar a aceitar esse valor, o teste poderá revelar imediatamente que um comportamento já corrigido foi quebrado novamente.

Esse tipo de problema é chamado de **regressão**.

### 6.1. Escolhendo Bons Casos

Ao pensar em testes, podemos perguntar:

```text
Qual é o caso normal?

Quais são os limites do problema?

Quais entradas são inválidas?

Quais regras diferentes existem?

Quais caminhos diferentes o algoritmo pode seguir?

Que problemas já encontramos anteriormente?

Qual comportamento esperamos em cada situação?
```

Não precisamos testar todas as entradas possíveis.

Precisamos escolher casos que representem situações relevantes do problema.


## 7. Exercícios

### 7.1. Adicionando Dias a uma Data

Considere que:

* todos os meses possuem exatamente 30 dias;
* todos os anos possuem exatamente 360 dias;
* uma data é representada por uma tupla `(dia, mes, ano)`;
* a quantidade de dias adicionada será um inteiro não negativo.

Implemente:

```python
def adicionar_dias(data, quantidade):
    ...
```

A função deve retornar a nova data após adicionar `quantidade` dias.

Por exemplo:

```python
adicionar_dias((10, 8, 2026), 5)
```

deve retornar:

```python
(15, 8, 2026)
```

Caso `quantidade` seja negativa, a função deve lançar uma `ValueError`.

Após implementar a função, escolha pelo menos **6 casos de teste** que representem situações diferentes do problema.

Para cada caso:

1. identifique o que está sendo testado;
2. determine previamente o resultado esperado;
3. execute a função;
4. compare o resultado obtido com o esperado;
5. informe se o teste passou ou falhou.

Organize os testes em um arquivo separado, por exemplo:

```text
datas.py
teste_datas.py
```

Os testes podem inicialmente ser implementados utilizando código Python comum.

Por exemplo:

```python
resultado = adicionar_dias((10, 8, 2026), 5)
esperado = (15, 8, 2026)

if resultado == esperado:
    print("Teste: OK")
else:
    print(
        f"Teste: FALHOU - "
        f"esperado {esperado}, obtido {resultado}"
    )
```

Evite escolher apenas valores diferentes para testar exatamente a mesma situação.

Procure identificar casos que exercitem comportamentos diferentes da função.



### 7.2. Interseção entre Intervalos

Implemente:

```python
def intervalos_intersectam(inicio1, fim1, inicio2, fim2):
    ...
```

A função recebe dois intervalos fechados:

```text
[inicio1, fim1]
[inicio2, fim2]
```

e deve retornar `True` caso exista pelo menos um ponto pertencente aos dois intervalos.

Caso contrário, deve retornar `False`.

Os extremos pertencem aos intervalos.

Portanto:

```python
intervalos_intersectam(1, 5, 5, 10)
```

deve retornar:

```python id="5mbd73"
True
```

Se:

```text
inicio1 > fim1
```

ou:

```text
inicio2 > fim2
```

a função deve lançar uma `ValueError`.

Após implementar a função, escolha pelo menos **6 casos de teste** que representem situações diferentes do problema.

Para cada caso:

1. indique a entrada;
2. determine o comportamento esperado;
3. explique brevemente por que o caso é relevante;
4. implemente o teste em um arquivo separado.

Por exemplo:

```python
resultado = intervalos_intersectam(1, 3, 5, 8)
esperado = False

if resultado == esperado:
    print("Teste: OK")
else:
    print(
        f"Teste: FALHOU - "
        f"esperado {esperado}, obtido {resultado}"
    )
```

Considere também que alguns testes podem ter como comportamento esperado o lançamento de uma exceção.



### 7.3. Organizando os Testes

Para evitar repetir o mesmo código em todos os testes, considere criar uma função auxiliar:

```python
def testar(nome, resultado, esperado):
    ...
```

Ela deve informar se o resultado obtido corresponde ao esperado.

Por exemplo:

```python
testar(
    "Mesmo mês",
    adicionar_dias((10, 8, 2026), 5),
    (15, 8, 2026)
)
```

e:

```python
testar(
    "Intervalos separados",
    intervalos_intersectam(1, 3, 5, 8),
    False
)
```

Ao final, observe quanto código foi necessário apenas para executar e organizar os testes.
