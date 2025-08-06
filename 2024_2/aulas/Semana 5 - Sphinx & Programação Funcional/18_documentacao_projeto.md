# Documentação com Sphinx

Sphinx é uma ferramenta de documentação automatizada, inicialmente desenvolvida para documentar projetos em Python.
Ela simplifica o processo de criação de documentação ao extrair automaticamente as docstrings do código, formatá-las e exportá-las para vários formatos, como HTML, PDF e ePub.
Usando o Sphinx, podemos manter a documentação sempre alinhada com o código, garantindo consistência e facilidade de manutenção.

O Sphinx utiliza o reStructuredText (reST), uma linguagem de marcação de texto simples e poderosa, semelhante ao Markdown.
Essa linguagem permite que você escreva a documentação de forma clara e estruturada, o que facilita a leitura e a navegação.
Com o Sphinx, você pode gerar documentação de alta qualidade que é fácil de manter e distribuir, seja para desenvolvedores, usuários finais ou outros interessados no projeto.

## Por que usar?

* **Facilidade de Uso**:
Sphinx usa reStructuredText, uma linguagem de marcação fácil de aprender e usar.
* **Gerenciamento de Documentação**:
Sphinx permite criar uma estrutura organizada de documentação, o que é essencial para projetos maiores.
* **Geração Automática de Documentação**:
Ele pode gerar documentação automaticamente a partir de docstrings no código Python, o que ajuda a manter a documentação sincronizada com o código.
* **Flexibilidade**:
Sphinx suporta extensões que permitem personalizar o comportamento e a aparência da documentação.

##  Como Configurar o Sphinx?

Para começar a usar o Sphinx, você precisará instalá-lo usando pip:
```bash
pip install sphinx
```

Depois, você pode inicializar um novo projeto de documentação com:
```bash
sphinx-quickstart
```

Esse comando cria uma estrutura básica de diretórios e arquivos para a documentação do seu projeto.
A estrutura típica criada pelo `sphinx-quickstart` inclui:
* `conf.py`:
O arquivo de configuração principal onde se define a maioria das opções de configuração do Sphinx, incluindo o tema, extensões, informações do projeto, e mais.

* `index.rst`:
O arquivo de índice principal, escrito em reStructuredText, que serve como o ponto de entrada para a documentação.
A partir deste arquivo, outros documentos são referenciados e vinculados.

* `_static/`:
Um diretório para armazenar arquivos estáticos, como CSS ou JavaScript personalizados, que você deseja incluir na sua documentação.

* `_templates/`:
Um diretório para armazenar templates personalizados para substituir os templates padrão do Sphinx.
Isso permite que você personalize a aparência e o layout da sua documentação.

* `make.bat`:
Um script de construção para ambientes Windows.
Ele facilita a geração de diferentes formatos de documentação, como HTML e PDF, a partir da linha de comando.

* `Makefile`:
Similar ao make.bat, mas para ambientes Unix/Linux.
Ele permite que você execute comandos como make html para construir a documentação em diferentes formatos.

Esses arquivos e diretórios fornecem uma base organizada e funcional para começar a criar e gerenciar a documentação do seu projeto.
A partir dessa estrutura, você pode adicionar novos arquivos de documentação, configurar extensões adicionais, e personalizar o layout e estilo da sua documentação.

## O Arquivo conf.py

O arquivo `conf.py` é a principal configuração do Sphinx para o seu projeto de documentação.
Ele é gerado automaticamente pelo sphinx-quickstart e está localizado no diretório docs do seu projeto.

### Principais Configurações no conf.py

#### extensions
Lista das extensões do Sphinx que você deseja usar. Extensões adicionam funcionalidades adicionais à sua documentação.
```python
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']
```

#### source_suffix
Define as extensões dos arquivos de entrada, geralmente .rst para reStructuredText.
```python
source_suffix = '.rst'
```

#### master_doc
O nome do arquivo que serve como ponto de entrada principal para a documentação, geralmente index.

```python
master_doc = 'index'
```

#### project
O nome do projeto que aparecerá no cabeçalho da documentação.
```python
project = 'Meu Projeto'
```

#### html_theme
Define o tema para a documentação em HTML.
O Sphinx fornece vários temas, e você pode escolher o que melhor se adequa ao seu projeto.
```python
html_theme = 'alabaster'
```

## Escrevendo Documentação com reStructuredText

O Sphinx usa o reStructuredText (reST), uma linguagem de marcação leve e fácil de usar, semelhante ao Markdown, para escrever e organizar a documentação.
O arquivo de entrada principal que o Sphinx considera é o `index.rst`, que funciona como o ponto de partida da documentação.
A partir desse arquivo, outros documentos são referenciados e vinculados, formando a estrutura completa da documentação.

Abaixo estão algumas estruturas básicas e recursos do reStructuredText que você usará frequentemente ao criar documentação com Sphinx.

### Cabeçalhos
Use sinais de igual, hífens, ou outros caracteres para criar diferentes níveis de cabeçalhos.
```
Título Principal
================

Subtítulo
----------

Sub-subtítulo
^^^^^^^^^^^^^
```

### Paragráfos
Parágrafos são criados simplesmente escrevendo o texto. Um parágrafo é definido por uma linha de texto seguida por uma linha em branco.
```
Este é um parágrafo. Parágrafos são blocos de texto que são separados por uma linha em branco.
```

### Listas
O reST suporta diferentes tipos de listas:
* Listas não ordenadas usam asteriscos, mais ou hífens:
    ```
    * Item 1
    * Item 2
    * Subitem 2.1
    ```
* Listas ordenadas usam números seguidos por pontos:
    ```
    1. Primeiro item
    2. Segundo item
    ```
* Listas definidas usam dois-pontos para separar termos e definições:
    ```
    Termo 1:
        Definição do termo 1.
    ```

### Links
Links podem ser criados de várias formas:
* Links externos: Incluindo o texto do link seguido por um URL:
    ```
    `Sphinx documentation <https://www.sphinx-doc.org>`_
    ```
* Links internos: Usados para criar âncoras dentro do mesmo documento ou entre diferentes documentos:
    ```
    Veja a seção `Subtítulo <nome do arquivo>`_ para mais detalhes.
    ```

### Código
Blocos de código podem ser incluídos usando duplas crases para código em linha ou usando dois-pontos e recuo para blocos de código:
* Código em linha:
    ```
    Utilize a função ``print()`` para exibir mensagens.
    ```
* Bloco de código:
    ```
    .. code-block:: python
        def hello_world():
            print("Hello, World!")
    ```

### Tabelas
Tabelas podem ser criadas usando a notação de barra vertical e hífens, que é mais simples para tabelas pequenas:
```
========  ========
Coluna 1  Coluna 2
========  ========
Dado 1    Dado 2
Dado 3    Dado 4
========  ========
```

### Imagens
Para inserir uma imagem, você utiliza a diretiva .. image:: seguida pelo caminho da imagem.
Aqui estão alguns exemplos de como fazer isso:
* Imagem com Caminho Relativo
```
.. image:: my_image.png
.. image:: images/my_image.png
```
* Imagem com URL Externo
```
.. image:: https://www.exemplo.com/images/my_image.png
```
* Configurando Atributos da Imagem
```
.. image:: images/my_image.png
   :width: 400px
   :height: 200px
   :align: center
   :alt: Imagem de exemplo
```

### Referenciando Outros Arquivos

No  Sphinx, o arquivo `index.rst` serve como o ponto de entrada principal para a documentação e frequentemente atua como um "índice" para outros arquivos de documentação.
Para organizar e navegar entre diferentes seções ou capítulos da documentação, você pode usar a diretiva `toctree`.

A diretiva `toctree` permite criar uma árvore de conteúdos (table of contents tree) que define a hierarquia dos documentos.
Cada linha dentro da diretiva `toctree` representa o nome de um arquivo `.rst` que será incluído na estrutura de navegação.
Esses nomes são especificados sem a extensão `.rst`, pois o Sphinx automaticamente assume que eles têm essa extensão.
Por exemplo:

```
.. toctree::
   :maxdepth: 2
   :caption: Conteúdos:

   introducao
   capitulo1
   capitulo2
```

Neste exemplo:
* `introducao` corresponde ao arquivo `introducao.rst`.
* `capitulo1` corresponde ao arquivo `capitulo1.rst`.
* `capitulo2` corresponde ao arquivo `capitulo2.rst`.

Esses arquivos precisam estar localizados no mesmo diretório que o `index.rst`, a menos que um caminho relativo seja especificado.
O parâmetro `:maxdepth:` controla a profundidade da hierarquia exibida na árvore de conteúdo, e `:caption:` fornece um título para a seção de conteúdos.

Ao usar o `toctree`, você define claramente como os diferentes documentos se conectam, permitindo que o Sphinx gere automaticamente links de navegação entre eles, facilitando a leitura e a organização da documentação.
Isso cria uma estrutura navegável no formato final da documentação, seja ela gerada em HTML, PDF ou outro formato suportado pelo Sphinx.

### Compilando a Documentação

Depois de escrever e organizar seu texto em arquivos `.rst`, você pode compilar esses arquivos para gerar a documentação em vários formatos, como HTML e PDF.

#### Convertendo para HTML
Para gerar a documentação em formato HTML, utilize o comando make (para ambientes Unix/Linux) ou make.bat (para Windows).
Navegue até o diretório onde está localizado o Makefile ou make.bat e execute o seguinte comando: 
```bash
make html     # Em Unix/Linux
make.bat html # Em Windows
```

Esse comando irá compilar os arquivos `.rst` e gerar a documentação em HTML, que será salva no diretório `_build/html`.
Você pode visualizar a documentação abrindo o arquivo `index.html` nesse diretório com um navegador web.

## Importando Docstrings dos Módulos Python

A documentação automática de módulos Python pode ser significativamente facilitada usando o Sphinx, especialmente com a ajuda de extensões e ferramentas específicas.
Este tópico cobre como importar e documentar automaticamente as docstrings dos módulos Python.

### 1. Extensões Necessárias
Para importar e documentar docstrings dos módulos Python, você precisará configurar algumas extensões essenciais no Sphinx.
As principais extensões para isso são:

* `sphinx.ext.autodoc`:
Esta extensão é fundamental para a documentação automática.
Ela permite a extração de docstrings dos módulos Python e a geração de documentação diretamente a partir dessas docstrings.
Para configura-lo, adicione `sphinx.ext.autodoc` à lista de extensões no arquivo `conf.py`:
    ```python
    extensions = ['sphinx.ext.autodoc']
    ```
* `sphinx.ext.napoleon`:
Se você usa docstrings no estilo Google ou NumPy, essa extensão ajuda a interpretar esses formatos e a convertê-los em documentação reStructuredText.
Para configura-lo, adicione `sphinx.ext.napoleon` ao `conf.py` e habilite os estilos:
    ```python
    extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']

    napoleon_google_docstring = True
    napoleon_numpy_docstring = True
    ```

### 2. Gerando a Documentação com sphinx-apidoc
O `sphinx-apidoc` é uma ferramenta útil para gerar automaticamente os arquivos `.rst` que documentam seus módulos Python.
Esses arquivos incluem diretivas que o Sphinx usa para criar documentação.
* Comando Básico:
    ```
    sphinx-apidoc -o <output_dir> <source_dir>
    ```
    * `<output_dir>`: Diretório onde os arquivos `.rst` serão salvos.
    * `<source_dir>`: Diretório contendo o código fonte Python.
* Exemplo de Comando: Se o código está em src e você deseja gerar a documentação em docs/source:
    ```
    sphinx-apidoc -o docs/source src
    ```
    Este comando cria arquivos `.rst` no diretório `docs/source` para cada módulo encontrado no diretório `src`.

### 3. Configuração dos Arquivos .rst
Após gerar os arquivos `.rst`, você pode precisar ajustar o arquivo `index.rst` ou outros arquivos de índice para incluir a documentação dos módulos. Aqui está um exemplo de como incluir a documentação gerada em seu `index.rst`:
* Exemplo de `index.rst`:
    ```
    .. toctree::
       :maxdepth: 2
       :caption: Conteúdos:

       modulos
       outro_modulo
    ```
    Certifique-se de que cada entrada no `toctree` corresponde a um arquivo `.rst` gerado.

### 4. Executando o Sphinx
Depois de configurar os arquivos `.rst` para incluir a documentação dos módulos,
compile a documentação novamente usando os comandos de compilação do Sphinx:
```bash
make html     # Em Unix/Linux
make.bat html # Em Windows
```
