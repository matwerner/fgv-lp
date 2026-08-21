# Aula 9: Projeto Prático - Finanças Pessoais

Nas últimas aulas, discutimos diferentes formas de tornar um programa mais fácil de compreender e manter.

Entre elas:
* utilização de funções com responsabilidades bem definidas;
* escolha de nomes descritivos;
* comentários para explicar decisões não óbvias;
* docstrings para documentar funções;
* Type Hints para explicitar os tipos esperados;
* convenções de escrita e legibilidade.

Nesta aula, vamos aplicar esses conceitos no desenvolvimento de uma aplicação nova.

## 1. Aplicação de Finanças Pessoais

Considere um arquivo contendo as transações financeiras realizadas por uma pessoa ao longo de um ano.

Cada transação possui quatro informações:

| Campo        | Descrição                        |
| ------------ | -------------------------------- |
| `Data`       | Data em que a transação ocorreu  |
| `Categoria`  | Categoria associada à transação  |
| `Descrição`  | Descrição apresentada no extrato |
| `Valor (R$)` | Valor da transação               |

Por exemplo:

```csv
Data,Categoria,Descrição,Valor (R$)
2025-01-01,Alimentação,CHOCOLATESLUGANO,-8.90
2025-01-01,Alimentação,MENDONCA FOODS RESTAUR,-133.50
2025-01-01,Educação,EBN *CAMBLY,-69.00
```

Os valores possuem o seguinte significado:

* valores **positivos** representam receitas;
* valores **negativos** representam despesas.

As transações no arquivo fornecido já estão ordenadas pela data, em ordem crescente.

## 2. Objetivo

Desenvolva uma aplicação de linha de comando que permita consultar as transações presentes no arquivo fornecido.

Ao iniciar o programa, o usuário deve encontrar um menu semelhante a:

```text
0 - Sair
1 - Listar transações
2 - Buscar por descrição
3 - Buscar por categoria
4 - Resumo mensal
```

Após executar uma operação, o programa deve voltar ao menu principal, permitindo que uma nova operação seja realizada.

O programa termina apenas quando o usuário selecionar a opção `0`.

## 3. Funcionalidades

### 3.1 Listar Transações

A opção `1` deve apresentar todas as transações existentes no arquivo.

Por exemplo:

```text
2025-01-01 | Alimentação | CHOCOLATESLUGANO       | R$ -8,90
2025-01-01 | Alimentação | MENDONCA FOODS RESTAUR | R$ -133,50
2025-01-01 | Educação    | EBN *CAMBLY             | R$ -69,00
...
```

Não é necessário ordenar as transações: considere que o arquivo de entrada já está em ordem crescente de data.

### 3.2 Buscar por Descrição

A opção `2` deve solicitar ao usuário uma descrição, ou parte dela, e apresentar as transações correspondentes.

Por exemplo:

```text
Buscar por descrição: UBER
```

O programa deve apresentar todas as transações cuja descrição contenha o texto informado.

A busca não deve depender da utilização de letras maiúsculas ou minúsculas.

Por exemplo:

```text
uber
UBER
Uber
```

devem produzir o mesmo resultado.

### 3.3 Buscar por Categoria

A opção `3` deve solicitar uma categoria e apresentar todas as transações pertencentes a ela.

Por exemplo:

```text
Categoria: Alimentação
```

Resultado:

```text
2025-01-01 | Alimentação | CHOCOLATESLUGANO       | R$ -8,90
2025-01-01 | Alimentação | MENDONCA FOODS RESTAUR | R$ -133,50
...
```

### 3.4 Resumo Mensal

A opção `4` deve solicitar um mês e um ano e apresentar um resumo das transações realizadas naquele período.

O resumo deve apresentar:

* total de receitas;
* total de despesas;
* saldo do mês.

Por exemplo:

```text
Mês: 01
Ano: 2025

Resumo - 01/2025

Receitas: R$ 8.742,63
Despesas: R$ 8.320,25
Saldo:    R$   422,38
```

Considere:

```text
Receitas = soma dos valores positivos
Despesas = soma, em valor absoluto, dos valores negativos
Saldo    = Receitas - Despesas
```

## 4. Requisitos

A implementação deve:

* utilizar funções para organizar as diferentes operações;
* utilizar Type Hints nas funções desenvolvidas;
* documentar as principais funções utilizando docstrings;
* utilizar nomes de funções e variáveis que expressem claramente seu propósito;
* evitar duplicação desnecessária de código;
* utilizar apenas os recursos do Python vistos até o momento e sua biblioteca padrão;
* não utilizar Pandas.

A forma de organizar internamente o programa fica a critério de cada dupla.

Vocês podem utilizar um ou mais arquivos Python, conforme julgarem adequado.

Não existe uma estrutura de arquivos previamente definida para o exercício.

## 5. Simplificações

Neste momento, considere que:

* o arquivo fornecido existe;
* seu conteúdo está no formato esperado;
* todas as transações possuem os campos necessários;
* os valores numéricos são válidos;
* as datas estão corretamente formatadas.

Não é necessário tratar arquivos inválidos ou outras situações de erro nesta versão da aplicação.

## 6. Desenvolvimento

O exercício deve ser realizado em **duplas**.

Antes de começar a implementação, pensem em algumas questões:

* Como uma transação será representada dentro do programa?
* Quais funções serão necessárias?
* O que cada função deverá receber?
* O que cada função deverá retornar?
* Existem operações que podem reutilizar outras partes do código?
* Como tornar o programa fácil de compreender para alguém que não participou de sua implementação?

A organização e as decisões de implementação fazem parte do exercício.

Durante a aula, o professor poderá discutir dúvidas e decisões de implementação com cada dupla, mas não existe uma única estrutura obrigatória para a solução.

## 7. Entrega

Ao final da aula, cada dupla deverá enviar os arquivos Python desenvolvidos.

A entrega deve representar **o estado da aplicação ao final da aula**, mesmo que alguma funcionalidade não tenha sido completamente finalizada.
Não é necessário que todas as funcionalidades estejam implementadas para realizar a entrega.

Inclua também o nome dos integrantes da dupla.

Essa versão da aplicação será utilizada posteriormente para continuar o desenvolvimento do projeto.

## 8. Próximos Passos

Na próxima aula, continuaremos trabalhando sobre esta aplicação.

A partir das soluções desenvolvidas, discutiremos como diferentes decisões de implementação podem facilitar ou dificultar a compreensão, manutenção e evolução de um programa.
