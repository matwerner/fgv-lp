## 1. Implementação de Operações Básicas de Álgebra Linear

Implemente três funções em Python que realizam operações básicas de álgebra linear:

### A. Produto Interno: 
Implemente uma função chamada produto_interno(vetor1, vetor2) que recebe dois vetores (listas de números) como entrada e retorna o produto interno (dot product) desses vetores.
* Entrada: Dois vetores representados como listas de números [a1, a2, ..., an] e [b1, b2, ..., bn].
* Saída: O valor do produto interno entre os vetores.

Exemplo:

```python
vetor1 = [1, 2, 3]
vetor2 = [4, 5, 6]
resultado = produto_interno(vetor1, vetor2) 
# resultado deve ser 32
```

### B. Multiplicação de Matriz por Vetor:
Implemente uma função chamada matriz_por_vetor(matriz, vetor) que recebe uma matriz (lista de listas de números) e um vetor como entrada, e retorna o produto da matriz pelo vetor.

* Entrada: Uma matriz representada como uma lista de listas de números, onde cada sublista é uma linha da matriz, e um vetor representado como uma lista de números.
* Saída: O resultado da multiplicação da matriz pelo vetor, representado como uma lista de números.

Exemplo:

```python

matriz = [
    [1, 2],
    [3, 4],
    [5, 6]
]
vetor = [7, 8]
resultado = matriz_por_vetor(matriz, vetor)
# resultado deve ser [23, 53, 83]
```

### C. Multiplicação de Matriz por Matriz
Implemente uma função chamada matriz_por_matriz(matriz1, matriz2) que recebe duas matrizes como entrada e retorna o produto dessas duas matrizes.

* Entrada: Duas matrizes representadas como listas de listas de números.
* Saída: O resultado da multiplicação das duas matrizes, representado como uma nova matriz (lista de listas).

Exemplo:

```python
matriz1 = [
    [1, 2],
    [3, 4]
]
matriz2 = [
    [5, 6],
    [7, 8]
]
resultado = matriz_por_matriz(matriz1, matriz2)
# resultado deve ser [[19, 22], [43, 50]]
```

Restrições e Considerações:
* Os vetores e as matrizes fornecidos como entrada estarão sempre corretamente dimensionados para as operações (ou seja, terão tamanhos compatíveis).
* Não é permitido utilizar bibliotecas externas como NumPy para realizar as operações. Implemente as operações manualmente.

Dica: Para a multiplicação de matriz por matriz, lembre-se de que o elemento na posição (i, j) da matriz resultante é o produto interno da linha i da primeira matriz com a coluna j da segunda matriz.

## 2. Similaridade de Jaccard entre Textos

A similaridade de Jaccard é uma medida de similaridade entre dois conjuntos, muito utilizada para comparar textos, 
definida como:

$$ S_{Jaccard}(A, B) = \frac{|A \cap B|}{|A \cup B|} $$

onde:
- $|A \cap B|$ é o número de elementos na interseção dos conjuntos $A$ e $B$,
- $|A \cup B|$ é o número de elementos na união dos conjuntos $A$ e $B$.

Considere os seguintes textos:

**Texto 1:** "O gato está no telhado."

**Texto 2:** "O gato dorme no telhado."

### Perguntas:

A. Quais são os conjuntos de palavras únicos para cada texto após a padronização (remover pontuações e transformar todas as palavras para letras minúsculas)?

B. Quantos elementos estão na interseção dos dois conjuntos?

C. Quantos elementos estão na união dos dois conjuntos?

D. Qual é a similaridade de Jaccard entre os dois textos?

## 3. Encontrar termos no texto 

Dado o texto abaixo, escreva um programa em Python que receba uma lista de termos e reporte em quais linhas cada termo apareceu.

Texto:

```
Este é o primeiro exemplo de linha.
Esta linha é a segunda linha do exemplo.
O terceiro exemplo está aqui.
Aqui temos a quarta linha de exemplo.
E finalmente, esta é a quinta linha de exemplo.
```

Lista de Termos:

```
linha
exemplo
segunda
quinta

```

Requisitos do Programa:
* O programa deve ler o texto e a lista de termos.
* Para cada termo da lista, o programa deve identificar e imprimir em quais linhas (números das linhas) o termo aparece.
* A numeração das linhas deve começar de 1.

### Saída esperada
```
Termo 'linha' aparece nas linhas: 1, 2, 4, 5
Termo 'exemplo' aparece nas linhas: 1, 2, 3, 4, 5
Termo 'segunda' aparece na linha: 2
Termo 'quinta' aparece na linha: 5
```

## 4. Contar palavras em arquivo

Você deve desenvolver um programa em Python que leia o arquivo de texto `nintendo.txt` e realize as seguintes tarefas:

* Contar o número total de palavras contidas no arquivo.
* Listar as 5 palavras mais frequentes no arquivo.
* Listar as 5 sequências de duas palavras mais frequentes no arquivo.

Para a contagem das palavras e sequências:
* Desconsidere diferenças entre maiúsculas e minúsculas (ou seja, trate todas as palavras como se fossem minúsculas) -> `str.lower()`.
* Descartar todos os caracteres que não sejam letras e números para garantir a precisão das contagens -> `str.isalnum()`.

### Exemplo

```python
texto = "A programação em Python é divertida. A programação é poderosa e simples. Python é uma linguagem versátil."
obter_estatisticas(texto)
# Número total de palavras: 15

# Top 5 palavras mais frequentes:
# 1. é: 3
# 2. a: 2
# 3. programação: 2
# 4. python: 2
# 5. em: 1

# Top 5 sequências de duas palavras mais frequentes:
# 1. a programação: 2
# 2. python é: 2
# 3. programação em: 1
# 4. em python: 1
# 5. é divertida: 1
```


## 5. Validar CPF

Um CPF (Cadastro de Pessoas Físicas) é composto por 11 dígitos numéricos,
geralmente apresentados no formato "XXX.XXX.XXX-YY".
Para ser considerado válido, um CPF deve atender aos seguintes critérios:

1. Deve conter 11 dígitos numéricos.
2. Não deve consistir de todos os dígitos iguais (por exemplo, "111.111.111-11" não é um CPF válido).
3. Deve obedecer ao algoritmo de validação do CPF, descrito a seguir:
    * Os primeiros 9 dígitos são os números base.
    * O 10º dígito (primeiro dígito verificador) é calculado da seguinte forma:
        * Multiplique os 9 primeiros dígitos pela sequência decrescente de 10 a 2.
        * Some os resultados dessas multiplicações.
        * Calcule o resto da divisão dessa soma por 11.
        * Se o resto for menor que 2, o dígito verificador é 0. Se for maior ou igual a 2, o dígito verificador é 11 menos o resto.
    * O 11º dígito (segundo dígito verificador) é calculado da mesma forma, mas agora com a sequência decrescente de 11 a 2 (considerando os 9 dígitos base mais o primeiro dígito verificador).

Implemente a função `valida_cpf(cpf)` que recebe uma string representando o CPF no formato "XXX.XXX.XXX-YY"
e retorna um valor booleano indicando se o CPF é válido ou não.

### Exemplos

```python
print(valida_cpf("123.456.789-14"))  # Deve retornar False
print(valida_cpf("111.444.777-35"))  # Deve retornar True
```
