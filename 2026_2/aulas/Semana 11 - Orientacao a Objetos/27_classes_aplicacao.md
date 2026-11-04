# Aula 28: Prática - Busca de jogos

## 1. O problema

Uma loja de jogos digitais quer um sistema de **busca**: o usuário escolhe quais jogos quer ver (os filtros) e em que ordem (a ordenação), e o sistema mostra o resultado.

Exemplos de buscas que o sistema deve conseguir fazer:

```text
- jogos de RPG, do mais bem avaliado para o menos avaliado

- jogos de RPG com nota de pelo menos 80 e preço de até R$ 100,
  do mais barato para o mais caro

- jogos com pelo menos 1000 avaliações, dos lançamentos mais recentes
  para os mais antigos
```

Perceba que as buscas **combinam** coisas: um ou mais filtros, e uma forma de ordenar. A loja ainda não sabe todos os filtros e todas as ordenações que vai querer no futuro.

Dessa forma, o sistema deve permitir:

- **(i)** carregar e armazenar os jogos;
- **(ii)** aplicar um ou mais filtros aos jogos;
- **(iii)** ordenar o resultado e mostrá-lo.



## 2. Base de dados

O arquivo `games.jsonl` contém um jogo por linha, no formato JSON.

Exemplo ilustrativo de uma linha:

```json
{"Title": "Jogo Exemplo", "Original Price": 59.9, "Release Date": "2021-03-15", "Popular Tags": ["RPG", "Indie"], "All Reviews Summary": "Very Positive", "All Reviews Score": 92, "All Reviews Count": 4300}
```

Os campos que vamos usar são:

```text
Title                  →  nome do jogo

Original Price         →  preço

Release Date           →  data de lançamento

Popular Tags           →  lista de tags (ex.: "RPG", "Indie")

All Reviews Summary    →  resumo das avaliações (ex.: "Very Positive")

All Reviews Score      →  nota das avaliações

All Reviews Count      →  número de avaliações
```

O arquivo possui outros campos, que podem ser ignorados.

Para carregar os dados, use a função abaixo. Ela devolve uma **lista de dicionários**, um por jogo:

```python
import json


def carregar_jogos(caminho):
    with open(caminho, encoding="utf-8") as arquivo:
        return [json.loads(linha) for linha in arquivo]


jogos = carregar_jogos("games.jsonl")

print(len(jogos))
print(jogos[0]["Title"])
```

O que fazer **a partir dessa lista** é com vocês.



## 3. Tarefa

Em **duplas**, projetem e implementem uma solução orientada a objetos para o sistema de busca.

### 3.1 Parte 1: o projeto (antes de programar)

Antes de escrever código, decidam e registrem (em papel ou em comentários num arquivo):

- **Quais classes** fazem sentido criar?
- Para cada classe: quais **atributos** e quais **métodos**?
- Como as classes **se conhecem**? Quem usa quem?

Não existe uma única resposta correta. Esta parte não precisa ser perfeita, ela pode mudar enquanto vocês programam.



### 3.2 Parte 2: a implementação

Requisitos:

- Deve ser possível aplicar **um ou mais filtros** ao mesmo tempo (um jogo só aparece no resultado se passar por todos).
- Deve ser possível escolher **uma forma de ordenação** para o resultado.
- Pelo menos **2 filtros** diferentes.
- Pelo menos **2 ordenações** diferentes.
- Qualquer combinação de filtros com qualquer ordenação deve funcionar.
- **Novos filtros e novas ordenações devem poder ser criados sem alterar o código que já existe.**
- O resultado deve ser mostrado em ordem, com a **posição** de cada jogo. Mostre apenas os 10 primeiros.

Exemplo de saída:

```text
#1: Jogo A | nota 95 | 5000 avaliações | R$ 50.00
#2: Jogo E | nota 85 | 2000 avaliações | R$ 80.00
```



### 3.3 Parte 3: exemplo de uso

Escrevam um programa principal (`main`) que simule **pelo menos duas buscas diferentes**, com filtros e ordenações diferentes, mostrando o resultado de cada uma no console.



## 4. Como vamos trabalhar

```text
- Duplas, com um computador por dupla

- Podem consultar as notas das aulas anteriores

- Sem ferramentas de IA: na prova elas não estarão disponíveis,
  e hoje o objetivo é treinar

- O objetivo não é terminar perfeito, e sim ter algo funcionando
  e pensar no projeto: errar faz parte

- Ao final, cada dupla envia o seu código
```

Uma sugestão de ordem para a implementação:

```text
1. Faça funcionar para UM filtro e UMA ordenação

2. Depois, acrescente o segundo filtro e a segunda ordenação

3. Por fim, permita combinar vários filtros
```



## 5. Para entregar

No **topo do arquivo**, em comentários, respondam:

1. **Relações entre as classes.** Para cada classe, indique em uma linha quais outras classes ela usa, conhece ou cria. E se uma das outras deixasse de existir, o que aconteceria com ela?

2. Para acrescentar um **filtro novo**, em quantos lugares do código vocês precisaram mexer? Liste-os.

3. Quem **cria** os filtros e as ordenações? Dois buscadores diferentes poderiam usar o mesmo filtro? O que mudaria no código?

4. Alguma das suas classes faz **mais de uma coisa**? Qual?

5. Se tivessem mais 30 minutos, o que vocês mudariam na solução?



## 6. Desafios opcionais

Para quem terminar antes:

1. **Busca ao seu gosto.** Criem uma busca customizada com filtros e ordenações novos, ou um programa de linha de comando (CLI) que pergunta ao usuário quais filtros e qual ordenação ele quer.

2. **Objetos protegidos.** Façam com que alguns dos objetos não possam mais ser alterados depois de criados (por exemplo, os jogos), ou que seus atributos fiquem escondidos, com acesso controlado.



## 7. Critério de sucesso

A solução está pronta quando:

- uma busca com **dois filtros** e uma ordenação, à sua escolha, mostra o resultado correto;
- trocar a ordenação não exige mexer nos filtros, e trocar os filtros não exige mexer na ordenação;
- é possível acrescentar um novo filtro **sem editar** nenhuma classe ou função que já existe.