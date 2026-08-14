# Exercícios de Python

## 1. Decomposição de Valor em Notas

Dado um valor inteiro, implemente uma função chamada `decomposicao_notas` que calcula a menor quantidade de notas de R$ $100$, $50$, $20$, $10$, $5$ e $1$ necessárias para representá-lo, e liste quais são essas notas.

**Exemplo:**
```python
valor = 287
decomposicao_notas(valor)
# Saída esperada:
# 2 notas de 100
# 1 nota de 50
# 1 nota de 20
# 1 nota de 10
# 1 nota de 5
# 2 notas de 1
```

## 2. Implementar Busca Binária

Escreva uma função que receba uma lista ordenada e um valor alvo, e retorne o índice desse valor usando o algoritmo de busca binária.

**Exemplo:**
```python
lista = [1, 3, 5, 7, 9]
print(busca_binaria(lista, 7))  # Saída: 3
```

## 3. Cadastro e Estatísticas de Alunos

Implemente uma função `estatisticas_alunos` que receba uma lista de dicionários, onde cada dicionário representa um aluno com `nome` e `nota`, e retorne:
* Maior nota e nome do aluno
* Menor nota e nome do aluno
* Média das notas

**Exemplo:**
```python
alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Bruno", "nota": 6.0},
    {"nome": "Carla", "nota": 9.2},
    {"nome": "Daniel", "nota": 7.3}
]

resultado = estatisticas_alunos(alunos)
print(resultado)
# Saída esperada:
# {
#   'maior': ('Carla', 9.2),
#   'menor': ('Bruno', 6.0),
#   'media': 7.75
# }
```

## 4. Processamento de Arquivo de Vendas

Dado o arquivo `vendas.txt` contendo uma lista de produtos vendidos (cada linha: categoria, valor), calcule o total de vendas por categoria e escreva o resultado no arquivo `compilado.txt`.

Exemplo de entrada (vendas.txt):
```txt
Alimentos e Bebidas,10
Vestuário e Acessórios,200
Eletroeletrônicos,500
Móveis e Decoração,1000
Vestuário e Acessórios,75
Produtos de Higiene e Limpeza,5
Alimentos e Bebidas,45
Eletroeletrônicos,320
Móveis e Decoração,880
Produtos de Higiene e Limpeza,25
```

Exemplo de saída (compilado.txt):
```txt
Alimentos e Bebidas,55
Vestuário e Acessórios,275
Eletroeletrônicos,820
Móveis e Decoração,1880
Produtos de Higiene e Limpeza,30
```

## 5. [Desafio] Jogo da Forca

Implemente o clássico Jogo da Forca no terminal:
* A palavra é escolhida pelo programa ou inserida pelo jogador 1
* O jogador 2 tenta adivinhar letra por letra
* Contabilizar tentativas erradas e encerrar quando o limite for atingido ou a palavra for descoberta

Dicas de implementação:
1. Crie uma variável para armazenar as letras já tentadas.
2. Use uma lista para representar o estado atual da palavra, preenchendo com `_` as letras ainda não descobertas.
3. A cada tentativa, atualize a lista caso a letra esteja na palavra.
4. Limite o número de erros (ex.: 6 tentativas).
5. Mostre ao jogador:
    - Letras já usadas
    - Quantidade de erros restantes
    - Estado atual da palavra (ex.: `_ _ a _ a`)
6. Use `while` para manter o jogo ativo até vitória ou derrota.
