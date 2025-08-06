########## Questão 1.A ##########
print('########## Questão 1.A ##########')

def inner_product(v1, v2):
    size_v1 = len(v1)
    size_v2 = len(v2)
    if size_v1 != size_v2:
        print('Os vetores devem ter o mesmo tamanho')
        return None
    
    result = 0
    for i in range(size_v1):
        result += v1[i] * v2[i]
    return result

v1 = [1, 2, 3]
v2 = [4, 5, 6]
print(inner_product(v1, v2))



########## Questão 1.B ##########
print('\n\n\n')
print('########## Questão 1.B ##########')

def mult_matrix_vector(m, v):
    rows_m = len(m)
    cols_m = len(m[0])

    size_v = len(v)
    
    if cols_m != size_v:
        print('O número de colunas da matriz deve ser igual ao tamanho do vetor')
        return None
    
    result = []
    for i in range(rows_m):
        result.append(inner_product(m[i], v))
    return result

m = [
    [1, 2],
    [3, 4],
    [5, 6]
]
v = [7, 8]
print(mult_matrix_vector(m, v))



########## Questão 1.C ##########
print('\n\n\n')
print('########## Questão 1.C ##########')

def mult_matrix_matrix(m1, m2):
    rows_m1 = len(m1)
    cols_m1 = len(m1[0])

    rows_m2 = len(m2)
    cols_m2 = len(m2[0])

    if cols_m1 != rows_m2:
        print('O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz')
        return None
    
    cols = []
    for j in range(cols_m2):
        v_col = []
        for i in range(rows_m2):
            v_col.append(m2[i][j])
        col = mult_matrix_vector(m1, v_col)
        cols.append(col)
    
    # Aplicar a transposta
    # A represetação de uma matriz é uma lista das linhas, não das colunas 
    result = []
    for i in range(rows_m1):
        row = []
        for j in range(cols_m2):
            row.append(cols[j][i])
        result.append(row)
    return result

matriz1 = [
    [1, 2],
    [3, 4]
]
matriz2 = [
    [5, 6],
    [7, 8]
]
print(mult_matrix_matrix(matriz1, matriz2))



########## Questão 2 ##########
print('\n\n\n')
print('########## Questão 2 ##########')

def computar_jaccard(a, b):
    num = a.intersection(b)
    den = a.union(b)
    return len(num) / len(den)

def process_text(t):
    t = t.lower()
    # Remover pontuação
    # Opção 1 - Só funciona para o exemplo dado
    # t = t.replace('.', '')
    # Opção 2 - Funciona para qualquer texto
    c_valid = []
    for c in t:
        if c.isalnum() or c.isspace():
            c_valid.append(c)
    t = ''.join(c_valid)
    return t

t1 = "O gato está no telhado."
t2 = "O gato dorme no telhado."

# Aplica o processamento de texto
t1 = process_text(t1)
t2 = process_text(t2)

# Convertendo para conjuntos
t1 = set(t1.split())
t2 = set(t2.split())

# Calcula a similaridade de Jaccard
print(computar_jaccard(t1, t2))



########## Questão 3 ##########
print('\n\n\n')
print('########## Questão 3 ##########')

text = """
Este é o primeiro exemplo de linha.
Esta linha é a segunda linha do exemplo.
O terceiro exemplo está aqui.
Aqui temos a quarta linha de exemplo.
E finalmente, esta é a quinta linha de exemplo.
"""

terms = """
linha
exemplo
segunda
quinta
"""

text = text.strip().split('\n')
terms = terms.strip().split('\n')

def find_lines(text, term):
    num_line = 1
    result = []
    for line in text:
        if term in line:
            result.append(num_line)
        num_line += 1
    return result

for term in terms:
    line_indices = find_lines(text, term)
    print(f"Termo '{term}' aparece nas linhas: {line_indices}")



########## Questão 4 ##########
print('\n\n\n')
print('########## Questão 4 ##########')

def count_words(words):
    count_map = {}
    for word in words:
        if word not in count_map:
            count_map[word] = 0
        count_map[word] += 1
    return count_map

def most_frequent_word(count_map):
    max_count = 0
    max_word = None
    for word, count in count_map.items():
        if count > max_count:
            max_count = count
            max_word = word
    return max_word

def most_frequent_words(count_map, top_n):
    # Copiar o dicionário para não alterar o original
    count_map = count_map.copy()

    words = []
    for i in range(top_n):
        word = most_frequent_word(count_map)
        del count_map[word]
        words.append(word)
    return words

def get_2_words(words):
    two_words_list = []
    for i in range(len(words) - 1):
        two_words_list.append((words[i], words[i+1]))
    return two_words_list

def get_stats(words):
    count_map = count_words(words)

    top_n = 5
    top_words = most_frequent_words(count_map, top_n)
    print(f"Total de palavras: {len(words)}")
    print(f"Top {top_n} palavras:")
    for word in top_words:
        print(f"{word}: {count_map[word]}")

    two_words_list = get_2_words(words)
    count_map = count_words(two_words_list)
    top_n = 5
    top_words = most_frequent_words(count_map, top_n)
    print(f"Top {top_n} pares de palavras:")
    for word in top_words:
        print(f"{word}: {count_map[word]}")
    return top_words

filepath = "nintendo.txt"
with open(filepath, 'r') as f:
    text = f.read()
# Roubando a função process_text do exercício 2
text = process_text(text)

words = text.split()
get_stats(words)
get_stats(text)



########## Questão 5 ##########
print('\n\n\n')
print('########## Questão 5 ##########')
print('Error 404: Resposta não encontrada')