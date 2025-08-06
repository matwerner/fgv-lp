from collections import Counter
import math
import json

def preprocessamento_texto(texto: str) -> str:
    """
    Realiza o preprocessamento de um texto.

    Parameters
    ----------
    texto: str
        Texto a ser preprocessado

    Returns
    -------
    str
        Texto preprocessado

    Examples
    --------
    >>> preprocessamento_texto("Hello, World!")
    'hello world'
    >>> preprocessamento_texto("Hello, World! 123")
    'hello world 123'
    >>> preprocessamento_texto("Hello, World! 123 @#")
    'hello world 123'
    >>> preprocessamento_texto(123)
    Traceback (most recent call last):
        File "main.py", line 34, in preprocessamento_texto
            texto = texto.lower()
    AttributeError: 'int' object has no attribute 'lower'
    """
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
    """
    Carrega os textos da aplicação

    Returns
    -------
    List[Dict[str, Any]]
        Lista de dicionarios representando paginas da wikipedia.
        Cada dicionario ira conter as seguintes chaves:
            - id: int
                Identificador da pagina
            - title: str
                Titulo da pagina
            - text: str
                O conteudo da pagina
    """
    wiki_pages = []
    with open(caminho, mode='r', encoding='utf-8') as fp:
        for line in fp:
            wiki_page = json.loads(line)
            wiki_pages.append(wiki_page)
    return wiki_pages

def criar_vocabulario(textos: list[str], vocab_size: int=10000) -> dict[str, int]:
    """
    Cria um vocabulário baseado numa lista de documentos

    Parameters
    ----------
    textos: List[str]
        Documentos utilizados para gerar o vocabulario
    vocab_size: int
        Tamanho maximo do vocabulario
    """
    contador = Counter()
    for texto in textos:
        palavras = texto.split()
        contador.update(palavras)

    vocab = dict()
    index = 0
    for palavra, freq in contador.most_common(vocab_size):
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

def selecionar_titulo(titulos: list[str]) -> int:
    """
    Pede para o usuário selecionar um titulo da lista disponivel

    parameters
    ----------
    titulos: list[str]
        Lista de titulos disponiveis

    returns
    -------
        Indice do titulo escolhido
    """
    for i in range(len(titulos)):
        print(f'#{i}: {titulos[i]}')
    
    idx = input('Selecione um dos titulos acima: ')
    return int(idx)

def main():
    # Descompactar o zip presente em:
    # ./aulas/Semana 3 - Documentacao & Type Hint/wikipedia_good_articles_video_games.zip
    # e jogar no diretório do presente script (ou atualizar o caminho abaixo para o local adequado)
    # caminho = 'wikipedia_good_articles_video_games.txt'
    caminho = './aulas/Semana 3 - Documentacao & Type Hint/wikipedia_good_articles_video_games.txt'
    wiki_pages = carregar_dados(caminho)

    docs = []
    titulos = []
    for wiki_page in wiki_pages:
        texto = wiki_page["text"]
        texto = preprocessamento_texto(texto)
        docs.append(texto)

        titulo = wiki_page["title"]
        titulos.append(titulo)

    vocab = criar_vocabulario(docs)
    print(f'Tamanho do vocabulario: {len(vocab)}')
            
    bows = []
    for doc in docs:
        bow = bag_of_words(doc, vocab)
        bows.append(bow)

    # Ranking
    bow_busca_idx = selecionar_titulo(titulos)
    bow_busca = bows[bow_busca_idx]
    ranking = ranquear_documentos(bows, bow_busca)

    rank_index = 0
    print(f'Documento selecionado: {titulos[bow_busca_idx]}')
    for idx, dist in ranking[:5]:
        print(f'#{rank_index}: {titulos[idx]}')
        rank_index+=1

if __name__ == "__main__":
    # main()
    import doctest
    doctest.testmod()