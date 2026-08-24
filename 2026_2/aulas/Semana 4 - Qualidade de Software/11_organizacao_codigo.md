# Aula 10: Organização de Código e Estruturação de Projetos

Na aula anterior, diferentes grupos desenvolveram uma aplicação de finanças pessoais com os mesmos dados e as mesmas funcionalidades.

Apesar de resolverem o mesmo problema, diferentes decisões podem ser tomadas durante a implementação:

* Quais funções criar?
* O que cada função deve fazer?
* Como representar os dados?
* Quando reutilizar código?
* Quando criar uma nova abstração?
* Como organizar funções relacionadas?
* Quando separar o programa em diferentes módulos?

Nesta aula, vamos comparar diferentes formas de organizar a mesma aplicação e analisar como essas decisões afetam sua compreensão e evolução.

## 1. Um Mesmo Problema, Diferentes Soluções

Considere novamente a aplicação desenvolvida na aula anterior:

```text
0 - Sair
1 - Listar transações
2 - Buscar por descrição
3 - Buscar por categoria
4 - Resumo mensal
````

Todas as soluções apresentadas a seguir implementam essas mesmas funcionalidades.

Entretanto, a organização do código é diferente.

Vamos analisar quatro possibilidades:

* Solução A
* Solução B
* Solução C
* Solução D

Antes de compará-las, considere:

* Uma solução que funciona necessariamente está bem organizada?
* Existe uma única forma correta de organizar um programa?
* Como podemos avaliar se uma determinada organização é adequada?
* O que acontece quando o programa precisa ser modificado?

## 2. Solução A: Implementação Direta

Na primeira solução, todo o comportamento da aplicação está diretamente dentro do fluxo principal:

```python
while True:
    opcao = input("Opção: ")

    if opcao == "0":
        break

    elif opcao == "1":
        arquivo = open(ARQUIVO, "r", encoding="utf-8")
        ...

    elif opcao == "2":
        busca = input("Buscar por descrição: ")

        arquivo = open(ARQUIVO, "r", encoding="utf-8")
        ...

    elif opcao == "3":
        ...

    elif opcao == "4":
        ...
```

### 2.1 A Solução Está Errada?

Não necessariamente.

O programa pode executar corretamente todas as funcionalidades solicitadas.

Entretanto, considere:

* É fácil identificar as principais operações realizadas pelo programa?
* Existem trechos de código repetidos?
* Quantas vezes o arquivo é aberto?
* Se alterarmos a forma como uma transação é exibida, quantos trechos precisam ser modificados?
* O que acontece com o `while` quando adicionamos novas funcionalidades?

Conforme o programa cresce, compreender e modificar esse código pode se tornar mais difícil.

### 2.2 Dando Nome às Operações

Uma primeira possibilidade é identificar operações com responsabilidades próprias:

```python
listar_transacoes(...)
buscar_por_descricao(...)
buscar_por_categoria(...)
resumo_mensal(...)
```

Funções não servem apenas para reduzir a duplicação.

Elas também permitem dar **nome e significado** às diferentes operações realizadas pelo programa.

## 3. Solução B: Separando Operações em Funções

Uma segunda implementação organiza as principais funcionalidades em funções:

```python
def listar_transacoes(arquivo: str) -> None:
    ...


def buscar_por_descricao(arquivo: str) -> None:
    ...


def buscar_por_categoria(arquivo: str) -> None:
    ...


def resumo_mensal(arquivo: str) -> None:
    ...
```

O fluxo principal passa a ser mais simples:

```python
if opcao == "1":
    listar_transacoes(ARQUIVO)

elif opcao == "2":
    buscar_por_descricao(ARQUIVO)

elif opcao == "3":
    buscar_por_categoria(ARQUIVO)

elif opcao == "4":
    resumo_mensal(ARQUIVO)
```

Agora podemos identificar rapidamente as principais operações da aplicação.

Mas criar funções resolve todos os problemas de organização?

## 4. Responsabilidades

Considere uma possível implementação:

```python
def buscar_por_descricao(arquivo: str) -> None:
    busca = input("Buscar por descrição: ")

    with open(arquivo, "r", encoding="utf-8") as f:
        f.readline()

        for linha in f:
            data, categoria, descricao, valor = linha.strip().split(",")

            if busca.lower() in descricao.lower():
                print(data, categoria, descricao, valor)
```

Essa função:

1. solicita uma entrada ao usuário;
2. abre um arquivo;
3. interpreta o formato CSV;
4. percorre as transações;
5. realiza a busca;
6. apresenta os resultados.

Qual é, afinal, a responsabilidade de `buscar_por_descricao()`?

### 4.1 Responsabilidade Única

Uma função deve possuir um propósito que possa ser explicado claramente.

Isso não significa que uma função deva possuir apenas uma linha ou realizar apenas uma operação.

Considere as seguintes perguntas:

* Uma função de busca precisa saber que os dados vieram de um arquivo CSV?
* Ela precisa perguntar ao usuário o que pesquisar?
* Ela precisa decidir como os resultados serão apresentados?
* O que significa, de fato, "buscar por descrição"?

Separar responsabilidades ajuda a limitar quais partes do programa precisam mudar quando um requisito é alterado.

## 5. Solução C: Separando a Leitura dos Dados

Nas soluções anteriores, diferentes operações precisam interpretar diretamente o arquivo:

```text
listar transações
        ↓
      CSV

buscar descrição
        ↓
      CSV

buscar categoria
        ↓
      CSV

resumo mensal
        ↓
      CSV
```

Uma alternativa é carregar os dados uma única vez:

```python
transacoes = carregar_transacoes(ARQUIVO)
```

A função responsável pela leitura transforma cada linha do arquivo em uma representação utilizada pelo restante da aplicação:

```python
def carregar_transacoes(caminho: str) -> list[dict]:
    transacoes = []

    with open(caminho, "r", encoding="utf-8") as arquivo:
        arquivo.readline()

        for linha in arquivo:
            data, categoria, descricao, valor = linha.strip().split(",")

            transacao = {
                "data": data,
                "categoria": categoria,
                "descricao": descricao,
                "valor": float(valor)
            }

            transacoes.append(transacao)

    return transacoes
```

O restante do programa passa a trabalhar com:

```python
transacoes: list[dict]
```

em vez de trabalhar diretamente com linhas de um CSV.

### 5.1 Formato Externo e Representação Interna

Podemos pensar em:

```text
transacoes.csv
      ↓
carregar_transacoes()
      ↓
  list[dict]
      ↓
restante da aplicação
```

Considere:

* Uma função de busca ainda precisa saber como funciona um arquivo CSV?
* Se o arquivo mudar de CSV para JSON, quais partes da aplicação precisam mudar?
* Faz sentido converter `valor` para `float` durante a leitura ou apenas quando for utilizado?

Separar o formato externo da representação utilizada pelo programa reduz a quantidade de código que depende diretamente da fonte dos dados.

### 5.2 Como Representar uma Transação?

Uma possibilidade seria utilizar uma lista:

```python
transacao[0]
transacao[1]
transacao[2]
transacao[3]
```

Outra possibilidade é utilizar um dicionário:

```python
transacao["data"]
transacao["categoria"]
transacao["descricao"]
transacao["valor"]
```

Considere:

* Qual representação é mais compacta?
* Qual comunica melhor o significado de cada informação?
* Existe uma representação sempre melhor que a outra?

A escolha de uma estrutura de dados também influencia a legibilidade do programa.

## 6. Evitando Repetição

Considere diferentes partes do código:

```python
busca = busca.strip().lower()
```

```python
descricao = descricao.strip().lower()
```

```python
categoria = categoria.strip().lower()
```

Existe uma operação comum sendo realizada nesses casos: **normalizar um texto para comparação**.

Podemos dar um nome para essa operação:

```python
def normalizar_texto(texto: str) -> str:
    return texto.strip().lower()
```

E utilizá-la em diferentes lugares:

```python
busca = normalizar_texto(busca)
descricao = normalizar_texto(descricao)
```

### 6.1 DRY: Don't Repeat Yourself

O princípio DRY sugere evitar a repetição desnecessária de conhecimento ou lógica dentro do programa.

Código duplicado pode causar problemas quando uma regra precisa ser modificada.

Por exemplo, se decidirmos posteriormente remover acentos antes de realizar uma busca, seria melhor alterar:

```python
normalizar_texto(...)
```

em um único lugar.

Entretanto:

> Toda repetição deve necessariamente virar uma função?

Não.

## 7. Simplicidade e o Custo das Abstrações

Considere:

```python
def ler_entrada(mensagem: str) -> str:
    return input(mensagem)
```

Em seguida:

```python
descricao = ler_entrada("Descrição: ")
```

Essa função realmente tornou o programa mais simples?

Ela possui algum comportamento ou significado adicional em relação a utilizar diretamente:

```python
descricao = input("Descrição: ")
```

Agora considere:

```python
def ler_opcao() -> str:
    while True:
        opcao = input("Opção: ")

        if opcao in ("0", "1", "2", "3", "4"):
            return opcao

        print("Opção inválida.")
```

Nesse caso, a função representa uma operação própria:

> Ler uma opção válida do menu.

Uma abstração deve ajudar a compreender ou modificar o programa.

Criar mais funções não significa automaticamente produzir um código melhor.

### 7.1 Uma Única Função de Busca?

Considere:

```python
buscar_por_descricao(transacoes, descricao)
buscar_por_categoria(transacoes, categoria)
```

As duas operações são semelhantes:

* percorrem transações;
* verificam determinado campo;
* retornam os elementos correspondentes.

Poderíamos criar:

```python
def buscar(transacoes, campo, termo):
    ...
```

E utilizar:

```python
buscar(transacoes, "descricao", "uber")
buscar(transacoes, "categoria", "alimentação")
```

Essa solução é melhor?

Considere agora que:

```text
descrição → verifica se contém o termo
categoria → verifica igualdade
```

Seria necessário adicionar outro parâmetro?

```python
buscar(transacoes, campo, termo, busca_exata)
```

A função está ficando mais simples ou mais complexa?

### 7.2 Generalização Nem Sempre É Simplificação

Evitar repetição é importante.

Entretanto, criar uma função excessivamente genérica pode:

* aumentar a quantidade de parâmetros;
* adicionar condições internas;
* esconder o propósito da operação;
* dificultar a leitura.

Duas funções parecidas não precisam necessariamente se transformar em uma única função.

O objetivo não é minimizar a quantidade de linhas, mas tornar o programa mais compreensível e fácil de modificar.

## 8. Solução D: Separando Entrada, Processamento e Saída

Considere novamente uma função da Solução C:

```python
def buscar_por_descricao(transacoes: list[dict]) -> None:
    busca = input("Buscar por descrição: ").lower()

    for transacao in transacoes:
        if busca in transacao["descricao"].lower():
            exibir_transacao(transacao)
```

Essa função:

```text
recebe entrada
     ↓
realiza processamento
     ↓
apresenta saída
```

Uma alternativa seria:

```python
def buscar_por_descricao(
    transacoes: list[dict],
    descricao: str
) -> list[dict]:

    resultado = []
    descricao = normalizar_texto(descricao)

    for transacao in transacoes:
        descricao_transacao = normalizar_texto(
            transacao["descricao"]
        )

        if descricao in descricao_transacao:
            resultado.append(transacao)

    return resultado
```

Agora a interação com o usuário ocorre fora da função:

```python
descricao = input("Buscar por descrição: ")

resultado = buscar_por_descricao(
    transacoes,
    descricao
)

exibir_transacoes(resultado)
```

### 8.1 Processar ou Apresentar?

Considere:

```python
def calcular_resumo_mensal(...):
    ...
    print(f"Receitas: {receitas}")
    print(f"Despesas: {despesas}")
    print(f"Saldo: {saldo}")
```

Uma alternativa:

```python
def calcular_resumo_mensal(...) -> dict[str, float]:
    ...
    return {
        "receitas": receitas,
        "despesas": despesas,
        "saldo": receitas - despesas
    }
```

E:

```python
def exibir_resumo(resumo: dict[str, float]) -> None:
    print(f"Receitas: R$ {resumo['receitas']:.2f}")
    print(f"Despesas: R$ {resumo['despesas']:.2f}")
    print(f"Saldo: R$ {resumo['saldo']:.2f}")
```

Considere:

* Qual versão pode ser utilizada sem um usuário utilizando o terminal?
* E se quisermos apresentar o resultado em uma interface gráfica?
* E se quisermos salvar o resultado em um arquivo?
* E se quisermos utilizar o resultado em outro cálculo?

Separar processamento de entrada e saída tende a tornar as funções mais reutilizáveis.

## 9. Princípios de Organização de Código

As diferenças observadas entre as soluções permitem identificar alguns princípios úteis.

### 9.1 Legibilidade

Código deve comunicar sua intenção.

Algumas práticas incluem:

* utilizar nomes descritivos;
* dividir operações complexas em funções;
* utilizar Type Hints;
* documentar interfaces importantes;
* evitar comentários que apenas repetem o código.

### 9.2 Simplicidade

Uma solução deve evitar complexidade que não seja necessária para resolver o problema.

Mais funções, parâmetros, módulos ou abstrações não significam necessariamente uma solução melhor.

### 9.3 Não-redundância

Evite manter a mesma regra ou conhecimento espalhado por diferentes partes do programa.

Entretanto, não elimine repetição criando abstrações mais complexas que o próprio problema.

### 9.4 Responsabilidade

Funções e módulos devem possuir propósitos que possam ser descritos claramente.

Pergunte:

> Qual é a responsabilidade desta função?

Se a resposta envolver muitas atividades não relacionadas, talvez existam responsabilidades que podem ser separadas.

### 9.5 Proximidade e Coesão

Elementos relacionados devem permanecer próximos.

Considere as funções:

```text
carregar_transacoes()

normalizar_texto()
buscar_por_descricao()
buscar_por_categoria()
calcular_resumo_mensal()

mostrar_menu()
ler_opcao()
exibir_transacao()
exibir_transacoes()
exibir_resumo()

main()
```

Quais delas parecem estar relacionadas entre si?

Podemos identificar alguns grupos:

```text
carregamento de dados

consultas e cálculos

interação com o usuário

coordenação da aplicação
```

Quando um conjunto de funções possui responsabilidades relacionadas, pode fazer sentido mantê-las próximas.

## 10. Organizando o Código em Módulos

Até agora, todas as funções podem existir dentro de um único arquivo.

Entretanto, conforme o programa cresce, podemos separar responsabilidades relacionadas em diferentes módulos.

Uma possível organização seria:

```text
financas/
├── main.py
├── data.py
├── analysis.py
└── interface.py
```

### 10.1 `data.py`

Responsável pela obtenção dos dados utilizados pela aplicação.

```python
carregar_transacoes(...)
```

### 10.2 `analysis.py`

Responsável pelas operações realizadas sobre as transações.

```python
normalizar_texto(...)
buscar_por_descricao(...)
buscar_por_categoria(...)
calcular_resumo_mensal(...)
```

### 10.3 `interface.py`

Responsável pela interação com o usuário.

```python
mostrar_menu(...)
ler_opcao(...)
exibir_transacao(...)
exibir_transacoes(...)
exibir_resumo(...)
```

### 10.4 `main.py`

Responsável por coordenar o funcionamento da aplicação.

```python
def main():
    transacoes = carregar_transacoes(...)

    while True:
        mostrar_menu()
        opcao = ler_opcao()

        ...
```

O módulo principal não precisa implementar todas as operações.

Ele coordena os diferentes componentes da aplicação.

## 11. Existe Uma Estrutura Correta?

A estrutura anterior é apenas uma possibilidade.

Poderíamos tomar decisões diferentes dependendo:

* do tamanho do projeto;
* das funcionalidades existentes;
* das mudanças esperadas;
* da quantidade de pessoas trabalhando no programa.

Criar vários arquivos também não significa automaticamente organizar bem um projeto.

Por exemplo:

```text
projeto/
├── main.py
├── funcoes.py
├── utils.py
└── outras_coisas.py
```

Considere:

* Qual é a responsabilidade de `funcoes.py`?
* O que pertence em `utils.py`?
* Como decidir em qual arquivo procurar determinada operação?

Nomes de módulos também devem comunicar suas responsabilidades.

## 12. Estrutura do Projeto

Além dos módulos Python, um projeto pode conter arquivos com diferentes finalidades.

Para nossa aplicação, uma possível estrutura seria:

```text
financas/
├── main.py
├── data.py
├── analysis.py
├── interface.py
├── data/
│   └── transacoes.csv
└── README.md
```

### 12.1 Código-fonte

Os arquivos Python contêm as diferentes partes da aplicação:

```text
main.py
data.py
analysis.py
interface.py
```

### 12.2 Dados

Arquivos utilizados pela aplicação podem ser armazenados separadamente:

```text
data/
└── transacoes.csv
```

Isso evita misturar arquivos de dados com código-fonte.

### 12.3 Documentação do Projeto

O arquivo:

```text
README.md
```

pode apresentar:

* objetivo do programa;
* instruções para execução;
* formato esperado dos dados;
* estrutura geral do projeto.

Docstrings documentam funções, módulos e seus contratos.

O `README.md` documenta o projeto como um todo.

## 13. Evoluindo a Aplicação

Considere agora uma nova funcionalidade:

```text
5 - Exibir as três categorias com maior total de despesas no ano
````

Para cada categoria, devemos considerar a soma de todas as despesas realizadas ao longo do ano e apresentar as três categorias com os maiores totais.

Antes de implementar, considere:

* Onde essa funcionalidade seria adicionada na Solução A?
* E na Solução D?
* A leitura do arquivo precisa mudar?
* A representação das transações precisa mudar?
* Como podemos acumular as despesas de cada categoria?
* Depois de calcular os totais, como identificar as três maiores categorias?
* O cálculo deve imprimir diretamente o resultado ou retornar alguma informação?
* Alguma função existente pode ser reutilizada?
* Quais módulos precisariam ser modificados?
* Quais módulos não deveriam precisar ser modificados?

Observe que adicionar uma nova funcionalidade não significa necessariamente alterar todas as partes da aplicação.

Se as diferentes responsabilidades estiverem bem separadas, mudanças relacionadas à análise das transações podem permanecer concentradas nas partes responsáveis por esse tipo de operação.

Uma boa organização não é importante apenas porque o código "parece melhor".

Ela ajuda principalmente quando o software precisa ser:

* compreendido;
* corrigido;
* reutilizado;
* expandido;
* modificado.

## 14. Exercício

Utilizando a aplicação desenvolvida na aula anterior:
1. Identifique possíveis responsabilidades presentes no programa.
2. Procure trechos de código repetidos.
3. Verifique se existem funções que realizam entrada, processamento e saída simultaneamente.
4. Analise se alguma abstração existente é desnecessária.
5. Reorganize o código quando julgar necessário.
6. Separe funções relacionadas em módulos, caso essa divisão torne a organização mais clara.
7. Implemente a seguinte funcionalidade:
```text
5 - Exibir as três categorias com maior total de despesas no ano
```

Para cada categoria, considere a soma de todas as despesas realizadas ao longo do ano.

Por exemplo:

```text
Categorias com maiores despesas em 2025:

1. Moradia       - R$ 32.400,00
2. Alimentação   - R$ 18.750,30
3. Transporte    - R$  9.830,40
```

Considere apenas transações com valores negativos no cálculo das despesas.

As categorias devem ser apresentadas em ordem decrescente de total de despesas.

Ao final, compare a nova versão com a implementação original.

Considere:
* Foi fácil identificar onde implementar a nova funcionalidade?
* Foi necessário modificar a leitura dos dados?
* Foi necessário modificar alguma funcionalidade que não estava relacionada ao novo requisito?
* Alguma função existente pôde ser reutilizada?
* Foi necessário criar alguma nova abstração?
* Essa abstração tornou o código mais simples ou apenas mais genérico?
* A separação em módulos ajudou a identificar onde cada alteração deveria ser realizada?
* A quantidade de arquivos aumentou. O programa ficou necessariamente mais complexo?

Boas práticas não são regras que devem ser aplicadas mecanicamente.

São princípios que ajudam a decidir como organizar um programa para que ele permaneça compreensível à medida que cresce e muda.