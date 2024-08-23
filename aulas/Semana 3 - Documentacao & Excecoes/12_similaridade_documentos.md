# Similaridade entre Documentos

Até agora, ao falar sobre qualidade de software, discutimos tópicos como documentação e uso de *type hints*.
Para consolidar esses conceitos, vamos criar uma aplicação simples para encontrar documentos similares.
Esta aplicação também servirá como base para as próximas aulas, nas quais abordaremos conceitos de testes unitários e tratamento de exceções.

Nesta aula, vamos introduzir alguns conceitos básicos de Processamento de Linguagem Natural (NLP, em inglês).
Vamos focar em três conceitos principais:
1. Representação de Documentos
2. Vocabulário
3. Similaridade entre Documentos

É importante notar que a ideia aqui é apenas apresentar esses tópicos de forma superficial, para que a aplicação faça mais sentido.
Para um estudo mais aprofundado, recomendo a disciplina de Processamento de Linguagem Natural oferecida pela FGV.

## 1. Representação Computacional de Texto

### Por que Representar Textos Computacionalmente?

Em aplicações envolvendo processamento de texto, é essencial que o computador seja capaz de compreender e manipular texto de maneira significativa.
Para isso, precisamos transformar o texto, que originalmente é uma sequência de caracteres, em uma representação numérica que o computador possa processar e analisar.

### Diferentes Formas de Representar Texto

Não existe uma única maneira correta de representar texto;
a escolha da representação depende da aplicação específica.
Aqui estão algumas formas comuns de representação:

1. **Representação como Cadeia de Caracteres**:
    - A forma mais básica, onde cada documento é simplesmente uma sequência de caracteres.
    - **Caso de uso**: Exibição para o usuário.
    - **Limitação**: Não permite operações matemáticas ou comparações eficientes entre diferentes textos.

2. **Representação como Lista de Palavras**:
    - Nesta abordagem, introduzimos o conceito de "palavra".
    - Para computação, uma palavra é normalmente qualquer sequência de caracteres delimitada por espaços em branco.
    - Chamamos o processo de converter uma sequência de caracteres em uma sequência de palavras de **tokenização**.
    - **Exemplo**: A frase "o gato preto" é dividida em ["o", "gato", "preto"].
    - **Caso de uso**: Permite operações como contagem de palavras e construção de vocabulário.
    - **Limitação**: Não permite a aplicação de operações matemáticas de forma eficiente.

3. **Vocabulário**:
    - Consiste em um conjunto de todas as palavras únicas (tokens) validas presentes em um ou mais documentos.
    - **Exemplo**: Dado os documentos ["o gato", "o cachorro"], o vocabulário seria {"o", "gato", "cachorro"}.
    - Ter um vocabulário é essencial para converter texto em uma representação numérica.

### Exemplo Prático de Tokenização e Criação de Vocabulário

```python
docs = [
    "o gato preto",
    "o cachorro marrom",
    "o gato e o cachorro"
]

# Criação de vocabulário
vocab = set()
for doc in docs:
    words = doc.split()
    vocab.update(words)

print(vocab)
# Saída: {'o', 'gato', 'preto', 'cachorro', 'marrom', 'e'}
```

## 2. Modelo Bag-of-Words (BoW)

### O que é o Modelo Bag-of-Words?

Bag-of-Words é uma técnica simples e amplamente utilizada para representar texto em forma de vetor.
Nessa abordagem:

* Cada documento é representado por um vetor.
* O vetor contém a contagem de cada palavra do vocabulário no documento.
* Ignora a ordem das palavras, a estrutura gramatical e a semântica das palavras.

Por que Usar Bag-of-Words?
* É uma forma direta e eficiente de transformar texto em dados numéricos que podem ser usados por algoritmos de aprendizado de máquina.
* É fácil de implementar e funciona bem para tarefas básicas de classificação de texto.

### Implementação de Bag-of-Words

```python
def bag_of_words(doc, vocab):
    words = doc.split()

    bow = [0] * len(vocab)
    for i in range(len(vocab)):
        word = vocab[i]
        bow[i] = words.count(word)
    return bow

# Ordenar o vocabulário para consistência
# Ou seja, saberemos que:
# vocab[0] = "cachorro"
# vocab[1] = "e"
# ...
vocab = sorted(list(vocab))
bows = []
for doc in docs:
    bow = bag_of_words(doc, vocab)
    bows.append(bow)

# Exibindo as representações
for i in range(len(docs)):
    doc = docs[i]
    bow = bows[i]
    print(f"Documento: {doc}\nRepresentação: {bow}")
```

### Vantagens e Limitações do Bag-of-Words

Vantagens:
* Simplicidade: Fácil de entender e implementar.
* Escalabilidade: Funciona bem para grandes coleções de documentos.

Limitações:
* Ignora a ordem das palavras: Perde o contexto que a ordem das palavras pode fornecer.
* Dimensionalidade: O vetor pode se tornar muito grande se o vocabulário for extenso, o que pode levar a problemas de armazenamento e processamento.

## 3. Cálculo de Distância entre Documentos

Uma vez que temos nossos documentos representados como vetores, podemos comparar sua similaridade usando medidas de distância.

### Distância de Jaccard

A distância de Jaccard mede a similaridade entre dois conjuntos, calculando a razão entre a interseção e a união dos conjuntos de palavras.

```python
def jaccard_distance(s1, s2):
    num = len(s1.intersection(s2))
    den = len(s1.union(s2))
    return 1 - num / den

# Exemplo de uso
doc1 = set(docs[0].split())
doc2 = set(docs[1].split())
print(f"Distância de Jaccard: {jaccard_distance(doc1, doc2)}")
```
 
Útil quando queremos comparar documentos com base no conjunto de palavras únicas, desconsiderando a frequência.

### Distância Euclidiana

```python
import math

def euclidean_distance(v1, v2):
    dist = 0
    for i in range(len(v1)):
        dist += (v1[i] - v2[i]) ** 2
    return math.sqrt(dist)

# Exemplo de uso
print(f"Distância Euclidiana: {euclidean_distance(bows[0], bows[1])}")
```

Considera a frequência das palavras, sendo mais sensível a mudanças nas contagens de palavras entre os documentos.

## Exercicio

Adaptar os códigos de exemplo acima para podermos lidar com as páginas da wikipedia vistos na ultima aula.
Para comparar as paginas, utilizar a distancia euclidiana.