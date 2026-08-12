# Aula 5: Entrada e Saída de Arquivos

## 1. Motivação

Até agora, os dados dos nossos programas existiam apenas enquanto o programa estava executando.

```python
nome = input("Nome: ")
idade = int(input("Idade: "))

print(nome, idade)
```

O que acontece com essas informações quando o programa termina?

Para manter informações entre diferentes execuções, precisamos armazená-las em algum lugar.

Exemplos:

* Configurações de um programa
* Lista de usuários
* Notas de alunos
* Logs
* Dados coletados por um programa
* Resultados de uma análise

## 2. Arquivos

Um arquivo é uma sequência de dados armazenada persistentemente.

Podemos trabalhar principalmente com dois tipos:

* Arquivos de texto
* Arquivos binários

Exemplos de arquivos de texto:

```text
.txt
.csv
.json
.xml
```

Exemplos de arquivos binários:

```text
.jpg
.png
.pdf
.exe
```

Nesta aula, vamos trabalhar principalmente com arquivos de texto.

### 2.1. Abrindo um Arquivo

Em Python usamos a função `open()`:

```python
arquivo = open("dados.txt", "r")
```

`open()` retorna um objeto que representa o arquivo.

Podemos então realizar operações sobre esse objeto:

```python
arquivo.read()
arquivo.write(...)
arquivo.close()
```

Comparação com C:

```c
FILE *arquivo = fopen("dados.txt", "r");

/* ... */

fclose(arquivo);
```

Em Python:

```python
arquivo = open("dados.txt", "r")

# ...

arquivo.close()
```

### 2.2. Modos de Abertura

O segundo argumento de `open()` indica o que queremos fazer com o arquivo.

```python
open("dados.txt", "r")
open("dados.txt", "w")
open("dados.txt", "a")
```

Principais modos:

* `r` → leitura
* `w` → escrita
* `a` → adiciona conteúdo ao final

#### 2.2.1. Leitura (`r`)

```python
arquivo = open("dados.txt", "r")
```

O arquivo precisa existir.

#### 2.2.2. Escrita (`w`)

```python
arquivo = open("dados.txt", "w")
```

Se o arquivo não existir, ele é criado.

Se já existir, seu conteúdo anterior é apagado.

#### 2.2.3. Anexação (`a`)

```python
arquivo = open("dados.txt", "a")
```

Se o arquivo não existir, ele é criado.

Se já existir, novos dados são adicionados ao final.

### 2.3. Encoding

Arquivos armazenam bytes, mas normalmente queremos trabalhar com caracteres:

```text
A
ç
ã
é
日
```

O encoding define como caracteres são convertidos em bytes e vice-versa.

Vamos utilizar principalmente UTF-8:

```python
arquivo = open("dados.txt", "r", encoding="utf-8")
```

## 3. Leitura de Arquivos

Suponha que temos o seguinte arquivo:

```text
dados.txt

Alice
Bob
Carlos
```

### 3.1. Lendo Todo o Arquivo

Podemos utilizar `read()`:

```python
arquivo = open("dados.txt", "r", encoding="utf-8")

conteudo = arquivo.read()

print(conteudo)

arquivo.close()
```

`read()` retorna uma string:

```python
print(type(conteudo))
```

### 3.2. Lendo Linha por Linha

Um arquivo também pode ser percorrido utilizando um `for`:

```python
arquivo = open("dados.txt", "r", encoding="utf-8")

for linha in arquivo:
    print(linha)

arquivo.close()
```

Por que aparecem linhas em branco?

Cada linha normalmente termina com o caractere:

```python
"\n"
```

Podemos removê-lo utilizando `strip()`:

```python
arquivo = open("dados.txt", "r", encoding="utf-8")

for linha in arquivo:
    print(linha.strip())

arquivo.close()
```

### 3.3. `read()` ou Linha por Linha?

Podemos carregar todo o conteúdo do arquivo:

```python
conteudo = arquivo.read()
```

Ou podemos processá-lo progressivamente:

```python
for linha in arquivo:
    # processar linha
```

Ao utilizar `read()`, todo o conteúdo é carregado para a memória.

Ao percorrer o arquivo linha por linha, não precisamos carregar todo o arquivo de uma vez.

Para arquivos muito grandes, processar linha por linha pode ser mais adequado.

## 4. Escrita de Arquivos

Para escrever em um arquivo, podemos utilizar `write()`:

```python
arquivo = open("saida.txt", "w", encoding="utf-8")

arquivo.write("Alice\n")
arquivo.write("Bob\n")
arquivo.write("Carlos\n")

arquivo.close()
```

`write()` não adiciona uma quebra de linha automaticamente.

Por isso:

```python
arquivo.write("Alice\n")
```

### 4.1. Adicionando Conteúdo

Se quisermos adicionar conteúdo sem apagar o que já existe, podemos utilizar o modo `a`:

```python
arquivo = open("saida.txt", "a", encoding="utf-8")

arquivo.write("Daniel\n")

arquivo.close()
```

O novo conteúdo será adicionado ao final do arquivo.

## 5. Gerenciadores de Contexto

Até agora fizemos:

```python
arquivo = open("dados.txt", "r", encoding="utf-8")

# ...

arquivo.close()
```

Por que precisamos de `close()`?

O sistema operacional mantém recursos associados ao arquivo aberto.

Além disso, dados escritos podem ainda não ter sido efetivamente enviados ao arquivo.

Existe também outro problema:

```python
arquivo = open("dados.txt", "r", encoding="utf-8")

# ocorre um erro

arquivo.close()
```

Se ocorrer uma exceção antes de `close()`, o arquivo pode não ser fechado corretamente.

### 5.1. `with`

Python possui gerenciadores de contexto, representados nesse caso pela instrução `with`:

```python
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
```

Ao sair do bloco `with`, o arquivo é fechado automaticamente.

Por isso, normalmente preferimos:

```python
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())
```

em vez de:

```python
arquivo = open("dados.txt", "r", encoding="utf-8")

for linha in arquivo:
    print(linha.strip())

arquivo.close()
```

Também podemos utilizar `with` para escrita:

```python
with open("saida.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Alice\n")
    arquivo.write("Bob\n")
```

## 6. Arquivos Estruturados

Até agora nosso arquivo poderia conter qualquer texto:

```text
Alice
Bob
Carlos
```

Mas frequentemente queremos armazenar dados com alguma estrutura.

Por exemplo:

```text
Alice,20,8.5
Bob,21,7.0
Carlos,19,9.0
```

Existem diversos formatos utilizados para representar dados estruturados.

Dois formatos muito comuns são:

* CSV
* JSON

### 7. CSV

CSV significa *Comma-Separated Values*.

É um formato muito utilizado para representar dados tabulares.

Por exemplo:

```csv
nome,idade,nota
Alice,20,8.5
Bob,21,7.0
Carlos,19,9.0
```

Cada linha representa um registro e os valores são separados por um delimitador.

### 7.1. Processando Manualmente

Poderíamos processar um arquivo desse tipo utilizando apenas as operações que já conhecemos:

```python
with open("alunos.csv", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        valores = linha.strip().split(",")
        print(valores)
```

Por exemplo:

```python
nome, idade, nota = linha.strip().split(",")
```

Entretanto, o formato CSV possui algumas regras e casos especiais.

Por isso, Python fornece o módulo `csv`.

### 7.2. Lendo CSV

```python
import csv

with open("alunos.csv", "r", encoding="utf-8", newline="") as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        print(linha)
```

Cada linha é retornada como uma lista:

```python
["Alice", "20", "8.5"]
```

Também podemos utilizar unpacking:

```python
import csv

with open("alunos.csv", "r", encoding="utf-8", newline="") as arquivo:
    leitor = csv.reader(arquivo)

    for nome, idade, nota in leitor:
        print(nome, idade, nota)
```

### 7.3. Escrevendo CSV

```python
import csv

dados = [
    ["Nome", "Idade"],
    ["Alice", 30],
    ["Bob", 35],
    ["Charlie", 25]
]

with open("saida.csv", "w", encoding="utf-8", newline="") as arquivo:
    escritor = csv.writer(arquivo)

    for linha in dados:
        escritor.writerow(linha)
```

Também podemos escrever todas as linhas de uma vez:

```python
escritor.writerows(dados)
```

## 8. JSON

JSON significa *JavaScript Object Notation*.

É um formato bastante utilizado para armazenar e trocar dados estruturados.

Por exemplo:

```json
{
    "nome": "Alice",
    "idade": 20,
    "nota": 8.5
}
```

Compare com um dicionário Python:

```python
aluno = {
    "nome": "Alice",
    "idade": 20,
    "nota": 8.5
}
```

JSON também permite representar estruturas mais complexas:

```json
{
    "turma": "A",
    "alunos": [
        {
            "nome": "Alice",
            "nota": 8.5
        },
        {
            "nome": "Bob",
            "nota": 7.0
        }
    ]
}
```

### 8.1. Lendo JSON

Python fornece o módulo `json`:

```python
import json

with open("dados.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

print(dados)
```

O conteúdo JSON é convertido para objetos Python.

Podemos então trabalhar normalmente com essas estruturas:

```python
print(dados["turma"])

for aluno in dados["alunos"]:
    print(aluno["nome"])
```

### 8.2. Escrevendo JSON

```python
import json

dados = {
    "nome": "Alice",
    "idade": 20,
    "nota": 8.5
}

with open("saida.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo)
```

Podemos utilizar `indent` para tornar o arquivo mais legível:

```python
with open("saida.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4)
```

### 8.3. CSV x JSON

CSV é particularmente adequado para dados tabulares:

```text
nome,idade,nota
Alice,20,8.5
Bob,21,7.0
```

JSON permite representar estruturas hierárquicas:

```json
{
    "turma": "A",
    "professor": "João",
    "alunos": [
        {
            "nome": "Alice",
            "notas": [8.0, 9.0]
        }
    ]
}
```

A escolha depende principalmente da estrutura dos dados e de como eles serão utilizados.

## 9. Exercícios

### 9.1. Texto Simples

1. Escreva um programa que abra um arquivo de texto chamado `"texto.txt"`, leia o conteúdo e exiba na tela.

2. Escreva uma função que receba uma lista de strings e salve essas strings em um arquivo de texto chamado `"saida.txt"`, cada string em uma linha separada.

### 9.2. CSV

1. Escreva um programa que leia um arquivo CSV chamado `"dados.csv"` e calcule a média de uma coluna numérica específica.

2. Escreva uma função que receba uma lista de dicionários representando dados tabulares e salve esses dados em um arquivo CSV chamado `"saida.csv"`.

### 9.3. JSON

1. Escreva um programa que leia um arquivo JSON chamado `"dados.json"` e exiba na tela o valor de uma chave específica.

2. Escreva uma função que receba um dicionário e salve esse dicionário em um arquivo JSON chamado `"saida.json"`.
