# Manipulação de Arquivos em Python

## 1. Conceitos Básicos

### Tipos de Arquivos

Arquivos podem ser classificados em diferentes tipos com base no seu conteúdo e na forma como são armazenados:

- **Arquivos de Texto**: São arquivos que contêm dados legíveis por humanos, como `.txt`, `.csv`, `.json`, `.xml`.
- **Arquivos Binários**: São arquivos que contêm dados em formato binário, que não são legíveis por humanos diretamente, como imagens (`.jpg`, `.png`), vídeos, arquivos executáveis (`.exe`), etc.

#### Texto x Binário

Arquivos de texto podem ser ineficientes em termos de espaço e performance, especialmente para grandes volumes de dados numéricos ou binários, e podem apresentar problemas de encoding.
Por exemplo, para armazenar a string `"123456789"`, seriam necessários `9 bytes`, considerando `1 byte` por caractere.
Em contrapartida, ao armazenar o mesmo número em formato binário, ele poderia ser representado como um inteiro que ocupa apenas `4 bytes`.
Dessa forma, arquivos binários tendem a ser mais eficientes em termos de armazenamento e velocidade de leitura/escrita.
No entanto, a desvantagem dos arquivos binários é que você precisa conhecer exatamente a estrutura do arquivo para interpretá-lo corretamente.
Sem essa informação, é impossível determinar como os dados estão organizados e como decodificá-los adequadamente.

### Modos de Abertura de Arquivos

Os arquivos podem ser abertos em diferentes modos, dependendo do que você deseja fazer com eles:

- **Leitura (`r`)**: Abre um arquivo para leitura. O arquivo deve existir.
- **Escrita (`w`)**: Abre um arquivo para escrita. Cria um novo arquivo se não existir ou trunca o arquivo existente.
- **Anexação (`a`)**: Abre um arquivo para adicionar dados ao final. Cria um novo arquivo se não existir.
- **Leitura e Escrita (`r+`)**: Abre um arquivo para leitura e escrita. O arquivo deve existir.
- **Modos Binários**: Adicionando `b` aos modos acima (`rb`, `wb`, `ab`, `r+b`) permite a manipulação de arquivos binários.


### Opções de Encoding

O encoding é crucial ao trabalhar com arquivos de texto, pois define como os caracteres são armazenados em bytes. Python suporta vários encodings, sendo o UTF-8 o mais comum.

- **UTF-8**: Encoding padrão para arquivos de texto em Python. Suporta todos os caracteres Unicode e é compatível com ASCII.
- **ASCII**: Limita-se a caracteres de 7 bits, adequado para textos em inglês.
- **ISO-8859-1**: Suporta caracteres acentuados das línguas ocidentais.
- **UTF-16**: Usa 2 bytes por caractere, suportando todos os caracteres Unicode, mas ocupa mais espaço que UTF-8 para textos majoritariamente em inglês.

Por exemplo, o caractere "`ñ`" (U+00F1) é `0xF1` em ISO-8859-1, mas é representado como dois bytes (`0xC3 0xB1`) em UTF-8.

### Exemplo

Abertura de arquivo com especificação de encoding:

```python
# Exemplo de abertura de arquivo com encoding
arquivo_texto = open('exemplo.txt', 'r', encoding='utf-8')  # Modo leitura com encoding UTF-8
arquivo_binario = open('imagem.png', 'rb')  # Modo leitura binária
```

## 2. Operações com Arquivos

### Abertura

Para manipular um arquivo, você primeiro precisa abri-lo usando a função `open()`, que retorna um objeto de arquivo.

```python
arquivo = open('dados.txt', 'r', encoding='utf-8')
```

### Leitura

Você pode ler o conteúdo de um arquivo de várias maneiras:

* Leitura de todo o conteúdo: Usa o método read().
    ```python
    conteudo = arquivo.read()
    print(conteudo)
    ```
* Leitura linha a linha: Usa um loop para iterar sobre o arquivo.
    ```python
    for linha in open('dados.txt', 'r', encoding='utf-8'):
        print(linha, end='')
    # ou
    arquivo = open('dados.txt', 'r', encoding='utf-8')
    for linha in arquivo.readlines():
        print(linha, end='')
    ```
* Fechamento do arquivo: É importante fechar o arquivo após terminar a leitura para liberar os recursos.
    ```python
    arquivo.close()
    ```

### Escrita

Para escrever em um arquivo, você pode usar os métodos `write()` ou `writelines()`.

* Escrever em arquivo: Usa o modo `"w"`.
    ```python
    arquivo = open('saida.txt', 'w', encoding='utf-8')
    arquivo.write('Escrevendo em arquivo\n')
    arquivo.write('Mais uma linha')
    ```
* Adicionar em arquivo: Usa o modo `"a"`.
    ```python
    arquivo = open('saida.txt', 'a', encoding='utf-8')
    arquivo.write('\nAdicionando uma linha ao arquivo')
    ```

### Uso de Context Managers

Usar um gerenciador de contexto (`with`) é uma prática recomendada,
pois ele garante que o arquivo será fechado corretamente, mesmo se ocorrer uma exceção durante a manipulação do arquivo.

```python
with open('dados.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
```

## 3. Manipulação Avançada

### Posicionamento no Arquivo
Você pode controlar a posição de leitura/escrita dentro de um arquivo usando os métodos `seek()` e `tell()`.
* `seek(offset)`: Move para uma posição específica no arquivo.
* `tell()`: Retorna a posição atual no arquivo.
```python
with open('dados.txt', 'r', encoding='utf-8') as arquivo:
    arquivo.seek(5)  # Mover para a posição 5
    print(arquivo.read(10))  # Ler 10 caracteres a partir da posição 5
    posicao = arquivo.tell()  # Obter a posição atual
    print(f'Posição atual: {posicao}')
```

### Leitura e Escrita de Grandes Arquivos
Para manipular arquivos grandes que não cabem na memória, você pode ler e processar o arquivo em pedaços ou linha a linha.
```python
with open('grande_arquivo.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        processar_linha(linha)  # Função fictícia para processar a linha
```

## 4. Manipulação de Arquivos em Diferentes Sistemas Operacionais

### Paths e Diretórios

Caminhos de arquivos podem variar entre sistemas operacionais.
Em Windows, usa-se barras invertidas (`\`),
enquanto em Unix/Linux usa-se barras normais (`/`).
A biblioteca os ajuda a lidar com essa diferença.

```python
import os

# Diferentes sistemas operacionais
caminho_windows = 'C:\\Users\\User\\Documents\\arquivo.txt'
caminho_unix = '/home/user/documentos/arquivo.txt'

# Uso do os.path para compatibilidade
caminho = os.path.join('home', 'user', 'documentos', 'arquivo.txt')
print(caminho)
```

### Bibliotecas Específicas

* os: Para operações de sistema.
* shutil: Para operações de arquivos de alto nível, como cópia e movimentação.
* pathlib: Para manipulação de caminhos de arquivos de forma mais intuitiva.

```python
import os
import shutil
from pathlib import Path

# Criando um diretório
os.makedirs('novo_diretorio', exist_ok=True)

# Movendo um arquivo
shutil.move('dados.txt', 'novo_diretorio/dados.txt')

# Usando pathlib
path = Path('novo_diretorio/dados.txt')
print(path.exists())
```

## 5. Trabalhando com Arquivos Específicos

Ao lidar com arquivos, você frequentemente encontrará diferentes tipos de arquivos, como:
* arquivos de texto simples;
* arquivos CSV (Comma-Separated Values);
* arquivos JSON (JavaScript Object Notation);
* E arquivos binários.

Cada tipo de arquivo tem suas próprias características e métodos específicos para leitura e escrita.

### CSV

Os arquivos CSV são comumente usados para armazenar dados tabulares, onde cada linha representa um registro e os valores são separados por vírgulas ou outro delimitador.
Em Python, você pode usar o módulo `csv` para trabalha com arquivos CSV de forma fácil e eficiente.

* Leitura: Use `csv.reader()` para ler linhas do arquivo CSV.
    ```python
    import csv

    with open('dados.csv', 'r', newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            print(linha)
    ```
* Escrita: Use `csv.writer()` para escrever linhas em um arquivo CSV.
    ```python
    import csv

    dados = [
        ['Nome', 'Idade'],
        ['Alice', 30],
        ['Bob', 35],
        ['Charlie', 25]
    ]

    with open('saida.csv', 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        for linha in dados:
            escritor_csv.writerow(linha)
    ```

### JSON

Os arquivos JSON são usados para armazenar dados no formato JSON, que é amplamente utilizado para troca de dados na web e em muitas aplicações.
Em Python, você pode usar o módulo `json` para trabalhar com arquivos JSON de forma simples e direta.

* Leitura: Use `json.load()` para carregar dados de um JSON.
    ```python
    import json

    with open('dados.json', 'r') as arquivo_json:
        dados_json = json.load(arquivo_json)
        print(dados_json)
    ```
* Escrita: Use `json.dump()` para escrever dados em um JSON.
    ```python
    import json

    dados = {'nome': 'Alice', 'idade': 30, 'cidade': 'São Paulo'}

    with open('saida.json', 'w') as arquivo_json:
        json.dump(dados, arquivo_json)
    ```

### Outros Formatos de Arquivo

Além dos formatos mencionados acima, existem muitos outros tipos de arquivos comuns que você pode encontrar.
Alguns exemplos incluem:

* Arquivos XML: Usados para armazenar e transportar dados de forma hierárquica. Você pode usar bibliotecas como `xml.etree.ElementTree` para trabalhar com arquivos XML.
* Arquivos de Texto Estruturado: Podem ter uma estrutura específica de dados, como arquivos de configuração ou arquivos de log com formatos personalizados. Eles podem ser lidos e escritos usando manipulação de arquivos de texto simples.
* Arquivos Excel (XLSX, XLS): Usados para armazenar dados em planilhas. Você pode usar bibliotecas como `openpyxl` ou `pandas` para trabalhar com arquivos Excel.

Ao lidar com esses diferentes tipos de arquivos, é importante entender os formatos específicos e usar as bibliotecas apropriadas para manipulá-los de forma eficiente e precisa em Python. Cada formato de arquivo pode ter suas próprias considerações e desafios únicos, então familiarize-se com as práticas recomendadas ao trabalhar com eles.

## Exercícios

### Texto simples

* Escreva um programa que abra um arquivo de texto chamado `"texto.txt"`, leia o conteúdo e exiba na tela.
* Escreva uma função que receba uma lista de strings e salve essas strings em um arquivo de texto chamado `"saida.txt"`, cada string em uma linha separada.

### CSV

* Escreva um programa que leia um arquivo CSV chamado `"dados.csv"` e calcule a média de uma coluna numérica específica.
* Escreva uma função que receba uma lista de dicionários representando dados tabulares e salve esses dados em um arquivo CSV chamado `"saida.csv"`.

### JSON

* Escreva um programa que leia um arquivo JSON chamado `"dados.json"` e exiba na tela o valor de uma chave específica.
* Escreva uma função que receba um dicionário e salve esse dicionário em um arquivo JSON chamado `"saida.json"`.
