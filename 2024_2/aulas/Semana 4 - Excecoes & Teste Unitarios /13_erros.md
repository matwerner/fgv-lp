# Erros

Por mais que desejemos que nossas aplicações funcionem perfeitamente na primeira tentativa, é comum que desenvolvedores encontrem erros ao tentar executar um programa. 

## Tipos de erro

Esses erros são uma parte natural do processo de desenvolvimento e, na maioria das vezes, podem ser classificados em três categorias principais:

1. Erro de Sintaxe
2. Erro Lógico
3. Erro em Tempo de Execução

### Erro de Sintaxe

Erros de sintaxe ocorrem quando o código viola as regras gramaticais da linguagem de programação.
Esses erros são detectados pelo interpretador ou compilador antes mesmo do código ser executado, e resultam em mensagens de erro que indicam onde a violação ocorreu.
Exemplos comuns incluem a falta de ponto e vírgula, colchetes, ou a indentação incorreta do código.

```python
arr = [1, 2, 3, 4]
for v in arr
    print(v)
```

Neste exemplo, podemos ver claramente que falta um dois-pontos (`:`) no final da linha do `for`.
Esse pequeno erro de sintaxe impede que o código seja executado.

### Erro Lógico

Erros lógicos ocorrem quando a lógica implementada no código não corresponde ao comportamento desejado.
Mesmo que o código esteja sintaticamente correto e execute sem problemas, ele pode produzir resultados inesperados devido a uma falha na lógica.

```python
def find_min_value(arr):
    min_value = 0
    for v in arr:
        if v < min_value:
            min_value = v
    return min_value

arr = [1, 2, 3, 4]
print(find_min_value(arr))
```

Esperamos que o menor valor retornado ao executar esse código seja `1`.
No entanto, o resultado será `0`.
Isso acontece porque o valor inicial `min_value` foi definido como `0`.
Como a lista contém apenas valores positivos, nenhum deles será menor que `0`, levando a um resultado incorreto.

### Erro em Tempo de Execução

Erros em tempo de execução são causados por condições inesperadas que ocorrem enquanto o código está sendo executado.
Esses erros não são detectados pelo interpretador até que o código seja efetivamente executado e podem interromper o funcionamento do programa.
Exemplos incluem tentativas de acessar uma posição inexistente em uma lista, divisões por zero, ou manipulação inadequada de variáveis nulas.

Continuando com o exemplo anterior, podemos ajustar o valor inicial de `min_value` para `arr[0]`, esperando que o código funcione corretamente:

```python
def find_min_value(arr):
    min_value = arr[0]
    for v in arr:
        if v < min_value:
            min_value = v
    return min_value

arr = [1, 2, 3, 4]
print(find_min_value(arr))
```

Embora essa função funcione corretamente para listas não vazias, ela falhará se a lista for vazia, resultando em um erro em tempo de execução.
Nesse caso, o Python retornará um erro indicando que não é possível acessar a posição `0` de uma lista vazia.

Esse tipo de erro é comum ao lidar com entrada e saída de dados, onde é possível que o usuário forneça dados em um formato inesperado ou inválido, para o qual o código não foi preparado.

## Como Solucionar Erros?

Tudo bem, então, como podemos minimizar a ocorrência desses erros?

Para **erros de sintaxe**, não há muito com o que se preocupar. Quando tentamos executar (ou compilar) um código, o interpretador (ou compilador) identifica imediatamente esses erros, indicando sua existência e localização exata.

A verdadeira dificuldade surge ao tentarmos evitar erros lógicos e erros em tempo de execução.

### Evitando Erros Lógicos

Como podemos garantir que nossa implementação está, de fato, funcionando corretamente?
A resposta está nos testes. Ao testarmos diferentes exemplos, podemos verificar se o comportamento do código corresponde ao esperado.
Essa prática foi formalizada na área de engenharia de software como `testes unitários`.
Testes unitários são fundamentais para validar a lógica do código, ajudando a identificar e corrigir erros antes que o programa seja executado em um ambiente de produção.

### Lidando com Erros em Tempo de Execução

Para erros em tempo de execução, os testes unitários também podem ser úteis até certo ponto.
Podemos incluir exemplos de entradas inválidas para observar como nossa aplicação se comporta.
No entanto, não é viável nem desejável prever e tratar todos os possíveis erros em tempo de execução que podem ocorrer em cada função ou prever todo comportamento inesperado que um usuário pode desencadear.

Se tentássemos cobrir todos esses casos, acabaríamos com funções extremamente complexas, cheias de verificações redundantes.
Em vez disso, o que fazemos é tratar os casos mais comuns e críticos, conscientes de que outros erros podem ocorrer.
Para esses cenários, lançamos `exceções`.

#### Tratamento de Exceções

A maioria das linguagens modernas, incluindo Python, inclui mecanismos de `tratamento de exceções` como parte da linguagem.
Esses mecanismos permitem capturar erros em tempo de execução e reagir de maneira controlada, evitando que o programa simplesmente falhe.

## Próximos Passos

Nas próximas aulas, exploraremos em maior profundidade como utilizar `testes unitários` para garantir a robustez do código e como implementar `tratamentos de exceção` em Python para lidar com situações inesperadas, mantendo o controle sobre o fluxo de execução do programa.