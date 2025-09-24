# Exercícios de Revisão

## EX1 – Algoritmo de Luhn com Documentação
Implemente uma função para validar números de cartão de crédito com **16 dígitos**, utilizando o **algoritmo de Luhn**.  

1. A função deve receber uma string representando o número do cartão.  
2. Retornar `True` se o número for válido, `False` caso contrário.  
3. Adicione **docstring**, **type hints** e pelo menos **2 doctests** e **2 testes unitários**.  

**Exemplo:**
```python
>>> validar_cartao("4532015112830366")
True
>>> validar_cartao("1234567890123456")
False
```

**Regras do Algoritmo de Luhn:**

1. **Verificar o tamanho:**
O número deve ter exatamente 16 dígitos.

2. **Começar pela direita:**
Pegue os dígitos do cartão da direita para a esquerda (o último dígito é o dígito verificador).

3. **Dobrar os dígitos alternados:**
A cada segundo dígito (contando a partir do penúltimo), dobre o valor.
    * Se o resultado da multiplicação for maior que 9, subtraia 9 (ou some os dois dígitos).

4. **Somar todos os dígitos:**
Some todos os números obtidos (os dobrados + ajustados e os que não foram alterados).

5. **Checar divisibilidade por 10:**
Se a soma total for divisível por 10, o número do cartão é válido.
Caso contrário, é inválido.

**Exemplo Passo a Passo**

Número de cartão: 4532015112830366

1. Dígitos originais:\
```4  5  3  2  0  1  5  1  1  2  8  3  0  3  6  6```
2. Começando da direita, dobramos a cada segundo dígito:\
```8  5  6  2  0  1  1  1  2  2  7  3  0  3  3  6```
3. Soma dos valores:\
```8 + 5 + 6 + 2 + 0 + 1 + 1 + 1 + 2 + 2 + 7 + 3 + 0 + 3 + 3 + 6 = 50```
4. Verificação:\
```50 % 10 = 0  ✅```

## EX2 – Funções como Objetos
A) Crie uma função que receba `*args` e `**kwargs` e exiba os valores recebidos.  

**Exemplo:**
```python
mostrar_parametros(1, 2, nome="Ana", idade=25)
# Saída: args=(1, 2), kwargs={'nome': 'Ana', 'idade': 25}
```

B) Implemente uma função que receba **outra função matemática simples** (ex: `quadrado(x)`, `dobro(x)`) e aplique a todos os elementos de uma lista.  

**Exemplo:**
```python
aplicar([1, 2, 3], quadrado)
# Saída: [1, 4, 9]
```

C) Implemente uma função que retorne **outra função**. Essa nova função deve multiplicar qualquer número por um fator definido pelo usuário.  

**Exemplo:**
```python
multiplicar_por_3 = criar_multiplicador(3)
multiplicar_por_3(10)
# Saída: 30
```



## EX3 – Exceções: Estados Brasileiros
Implemente uma função que receba uma string no formato "Cidade, Estado" ou "Cidade - Estado" e converta o nome do estado brasileiro para sua sigla oficial.

1. A função deve usar um dicionário de mapeamento contendo os estados do Brasil:
```python
estados = {
    "Acre": "AC", 
    "Alagoas": "AL",
    "Amapá": "AP",
    "Amazonas": "AM",
    "Bahia": "BA",
    "Ceará": "CE",
    "Distrito Federal": "DF",
    "Espírito Santo": "ES",
    "Goiás": "GO",
    "Maranhão": "MA",
    "Mato Grosso": "MT",
    "Mato Grosso do Sul": "MS",
    "Minas Gerais": "MG",
    "Pará": "PA",
    "Paraíba": "PB",
    "Paraná": "PR",
    "Pernambuco": "PE",
    "Piauí": "PI",
    "Rio de Janeiro": "RJ",
    "Rio Grande do Norte": "RN",
    "Rio Grande do Sul": "RS",
    "Rondônia": "RO",
    "Roraima": "RR",
    "Santa Catarina": "SC",
    "São Paulo": "SP",
    "Sergipe": "SE", "Tocantins": "TO"
}
```
2. Caso o estado não seja reconhecido, a função deve lançar uma exceção (ValueError).
3. O código que chama a função deve tratar a exceção, exibindo uma mensagem clara ao usuário.

**Exemplo:**
```python
>>> estado_para_sigla("Campinas, São Paulo")
'Campinas, SP'
>>> estado_para_sigla("Belo Horizonte - Minas Gerais")
'Belo Horizonte - MG'
>>> estado_para_sigla("Cidade Inexistente - Neverland")
ValueError: Estado 'Neverland' não reconhecido.
```

## EX4 – Decoradores de Nível de Acesso
A) Implemente um **decorador** que só permita executar uma função se o usuário for `"admin"`. Caso contrário, deve levantar uma exceção `PermissionError`.  

B) Generalize para um **decorador parametrizado** que permita definir quais papéis têm acesso (ex: `"admin"`, `"editor"`, `"viewer"`).  

**Exemplo:**
```python
@somente_admin
def deletar_usuario():
    return "Usuário deletado!"

deletar_usuario("admin")  # OK
deletar_usuario("editor") # PermissionError

@somente_roles(["admin", "editor"])
def editar_artigo():
    return "Artigo editado!"

editar_artigo("editor") # OK
editar_artigo("viewer") # PermissionError
```



## EX5 – Estruturas de Dados e Frequência
Dada uma lista de palavras extraídas de um texto:  

A) Crie um conjunto com as palavras **únicas**.  
B) Calcule a **frequência** de cada palavra.  
C) Retorne as palavras mais frequentes em ordem decrescente.  
D) Generalize para **bigramas** (sequências de duas palavras).  

**Exemplo:**
```python
texto = "o gato preto viu o outro gato preto"
# Únicos: {"o", "gato", "preto", "viu", "outro"}
# Frequência: {"o": 2, "gato": 2, "preto": 2, "viu": 1, "outro": 1}
# Mais frequentes: ["o", "gato", "preto"]

# Bigramas: ["o gato", "gato preto", "preto viu", "viu o", "o outro", "outro gato", "gato preto"]
```



## EX6 – Distâncias com NumPy
A) Implemente a **distância de Manhattan** entre dois vetores NumPy.  
Fórmula: `∑ |xi - yi|`  

B) Implemente a **distância de Hamming** entre dois vetores NumPy de mesmo tamanho.  
Fórmula: número de posições diferentes.  

**Exemplo:**
```python
a = np.array([1, 2, 3])
b = np.array([2, 4, 3])

# Manhattan: |1-2| + |2-4| + |3-3| = 1 + 2 + 0 = 3
# Hamming: posições diferentes = 2
```



## EX7 – Estatísticas com NumPy
Dado:  
```python
idades = np.array([22, 25, 29, 35, 42, 55])
salarios = np.array([2500, 3000, 3200, 4500, 5200, 6100])
```

Calcule a **média salarial** para as seguintes faixas etárias:  
- `[20,30)`  
- `[30,40)`  
- `[40,50)`  
- `[50,60)`  

**Saída esperada (valores aproximados):**
```python
Faixa [20,30): 2900
Faixa [30,40): 4500
Faixa [40,50): 5200
Faixa [50,60): 6100
```



## EX8 – Processamento de Logs
Dada a lista de acessos:  
```python
acessos = [
 (1111, "2025-01-01T09:00:00"),
 (2222, "2025-02-02T05:00:00"),
 (3333, "2025-02-07T10:00:00"),
 (4444, "2025-01-10T10:00:00"),
]
```

A) Identifique o número de usuários que acessaram a plataforma no **mês 02**.
B) Retorne a lista de **IDs únicos** desses usuários.  

**Saída esperada:**
```python
Quantidade de usuários: 1
IDs: [2222, 3333]
```

## EX9 – Filtragem de Texto com Palavras Proibidas
Implemente uma função que, dado um texto e um conjunto de **palavras proibidas**, substitua cada palavra proibida por `"x"` repetido com o mesmo número de caracteres.  

**Exemplo:**
```python
texto = "Eu gosto de futebol e política"
proibidas = {"futebol", "política"}

# Saída: "Eu gosto de xxxxxxx e xxxxxxxx"
```

A função deve ter **docstring**, **type hint**, pelo menos 2 doctests e 2 testes unitários. 
