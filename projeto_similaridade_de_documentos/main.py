from collections import Counter
import math
import json

def preprocessamento_texto(texto: str) -> str:
    # Colocar texto em caixa-baixa.
    # Exemplo: "Hello, World!" -> "hello, world!"
    texto = texto.lower()

    # Troca todos os caracteres não alfanuméricos por espaços
    # Exemplo: "hello, world!" -> "hello  world"
    char_validos = []
    for c in texto:
        if c.isalnum() or c.isspace():
            char_validos.append(c)
        else:
            char_validos.append(' ')
    texto = ''.join(char_validos)

    # Troca todos as sequencias de espaços em brancos por um único espaço
    # Exemplo: "hello  world" -> "hello world"
    texto = ' '.join(texto.split())
    return texto

def carregar_dados(caminho: str) -> list[str]:
    """Carrega os textos da aplicação"""
    wiki_pages = []
    with open(caminho, mode='r', encoding='utf-8') as fp:
        for line in fp:
            wiki_page = json.loads(line)
            texto = wiki_page["text"]
            texto = preprocessamento_texto(texto)
            wiki_pages.append(texto)
    return wiki_pages

def criar_vocabulario(textos: list[str]) -> dict[str, int]:
    """Cria um vocabulário baseado numa lista de documentos"""
    contador = Counter()
    for texto in textos:
        palavras = texto.split()
        contador.update(palavras)
    
    vocab = dict()
    index = 0
    for palavra, freq in contador.items():
        vocab[palavra] = index
        index += 1
    
    return vocab

def bag_of_words(texto: str, vocab: dict[str, int]):
    """Converte um texto na sua representação Bag-of-Words"""
    # Divido em palavras
    palavras = texto.split()

    # Vetor ocorrencias das palvras
    vetor = [0] * len(vocab)

    # Mapear palvras no vetor
    for palavra in palavras:
        index = vocab.get(palavra, -1)
        if index < 0:
            continue
        vetor[index] += 1

    return vetor

def distancia_euclideana(v1: list[float], v2: list[float]) -> float:
    """Calcula a distância euclidiana entre dois vetores"""
    if len(v1) != len(v2):
        print("Tamanhos diferentes!")
        exit()

    tam1 = len(v1)
    dist = 0
    for i in range(tam1):
        dist += (v1[i] - v2[i]) ** 2
    return math.sqrt(dist)

def ranquear_documentos(bows: list[list[float]], bow_busca: list[float]) -> list[tuple[int, float]]:
    """Ranquear os documentos mais similares a um documento especifico"""
    dists = []
    for i in range(len(bows)):
        dist = distancia_euclideana(bows[i], bow_busca)
        dists.append((i, dist))
    dists = sorted(dists, key=lambda x: x[1])
    return dists

def main():
    # Descompactar o zip presente em:
    # ./aulas/Semana 3 - Documentacao & Type Hint/wikipedia_good_articles_video_games.zip
    # e jogar no diretório do presente script (ou atualizar o caminho abaixo para o local adequado)
    caminho = 'wikipedia_good_articles_video_games.txt'
    docs = carregar_dados(caminho)

    vocab = criar_vocabulario(docs)
    print(f'Tamanho do vocabulario: {len(vocab)}')
            
    bows = []
    for doc in docs:
        bow = bag_of_words(doc, vocab)
        bows.append(bow)

    # Ranking
    bow_busca = bows[58]
    dists = ranquear_documentos(bows, bow_busca)
    for dist in dists[:5]:
        print(dist)

if __name__ == "__main__":
    main()