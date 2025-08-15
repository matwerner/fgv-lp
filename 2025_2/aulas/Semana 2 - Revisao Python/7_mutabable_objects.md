# Objetos Mutáveis vs. Imutáveis

Qual comportamento você espera que aconteça no script abaixo?

```python
a = 2
b = a
a = 1
print(b)
```

E agora?

```python
a = [1, 2, 3]
b = a
a.append(4)
print(b)
```

Por que isso ocorre?

## Introdução

Em Python, os objetos podem ser classificados como mutáveis ou imutáveis com 
base na sua capacidade de alterarmos seu conteúdo após a criação.
Essa distinção é fundamental para entendermos como Python trata diferentes tipos de dados.

## Objetos imutáveis

Os objetos imutáveis são aqueles cujo conteúdo não pode ser alterado após a criação.
Quando tentamos modificar um objeto desse tipo, na verdade estamos criando um novo objeto. 

Exemplos de objetos imutáveis incluem:
* Inteiros (int)
* Floats (float)
* Strings (str)
* Tuplas (tuple)

Como

```python
x = 5
x += 1
print(x)
```

Neste caso, o resultado da soma $5 + 1$ é atribuido ao ```x```,
sobrescrevendo o valor anterior armazenado.

## Objetos Mutáveis

Por outro lado, os objetos mutáveis são aqueles cujo conteúdo podemos alterar após a criação sem precisar de um novo objeto.

Exemplos comuns de objetos mutáveis incluem:
* Listas (list)
* Dicionários (dict)
* Conjuntos (set)

Como 

```python
lista = [1, 2, 3]
lista.append(4)
print(lista)
```

## Importância na Prática

Na prática, compreender a diferença entre esses tipos de objetos é crucial para evitar efeitos colaterais inesperados em seu código.

Por exemplo, como vimos no começo, ao atribuir a mesma lista a mais de uma váriavel.
Mais comumente, porém, ao passar objetos mutáveis como argumentos para funções, 
é possível que esses objetos sejam alterados dentro da função, afetando o estado do objeto fora da função.