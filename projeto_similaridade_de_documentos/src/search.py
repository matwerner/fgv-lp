'''
This module is responsible for searching documents by title and by text.
'''

from typing import List, Dict, Tuple, Any

from text import preprocess_text, compute_vocab, compute_bow
from metrics import jaccard_similarity

def search_by_keyword(
        texts: List[str],
        keywords: str,
        top_n: int=5,
        already_preprocessed: bool=False
    ) -> List[Tuple[int, int]]:
    """
    Search texts using the given keywords.

    Parameters
    ----------
    texts : List[str]
        The list of texts to search
    keywords : str
        The keywords to search in the texts
    top_n : int, optional
        The number of texts to return, by default 5
    already_preprocessed : bool, optional
        If the texts are already preprocessed, by default False

    Returns
    -------
    List[Tuple[int, int]]
        The list of texts with the number of keywords found
        The texts are sorted by the number of keywords found
    
    Examples
    --------
    >>> texts = [
    ...     'A document is a written, drawn, presented, ...',
    ...     'A documentary is a non-fictional motion picture ...',
    ...     'Documentation is a set of documents provided ...'
    ... ]
    >>> keywords = 'document'
    >>> print(search_by_keyword(texts, keywords))
    [(0, 1), (1, 0), (2, 0)]
    """
    if not already_preprocessed:
        for i in range(len(texts)):
            texts[i] = preprocess_text(texts[i])
        keywords = preprocess_text(keywords)
    keywords = keywords.split()

    index = 0
    scores = []
    for text in texts:
        words = set(text.split())
        keyword_score = 0
        for keyword in keywords:
            if keyword in words:
                keyword_score += 1
        scores.append((index, keyword_score))
        index += 1
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    return scores[:top_n]

def search_by_similarity(
        texts: List[str],
        query: str,
        top_n: int=5,
        already_preprocessed: bool=False
    ) -> List[Tuple[int, float]]:
    """
    Search texts using the given query.

    Parameters
    ----------
    texts : List[str]
        The list of texts to search
    query : str
        The query to search in the texts
    top_n : int, optional
        The number of texts to return, by default 5
    already_preprocessed : bool, optional
        If the texts are already preprocessed, by default False

    Returns
    -------
    List[Tuple[int, float]]
        The list of texts with the similarity to the query
        The texts are sorted by the similarity to the query

    Examples
    --------
    >>> texts = [
    ...     'A document is a written, drawn, presented, ...',
    ...     'A documentary is a non-fictional motion picture ...',
    ...     'Documentation is a set of documents provided ...'
    ... ]
    >>> query = 'document'
    >>> print(search_by_similarity(texts, query))
    [(0, 1), (1, 2/11), (2, 2/11)]
    """
    if not already_preprocessed:
        for i in range(len(texts)):
            texts[i] = preprocess_text(texts[i])
        query = preprocess_text(query)

    vocab = compute_vocab(texts, top_n=10000)

    query_bow = compute_bow(query, vocab)
    index = 0
    similarities = []
    for text in texts:
        doc_bow = compute_bow(text, vocab)
        similarity = jaccard_similarity(query_bow, doc_bow)
        similarities.append((index, similarity))
        index += 1
    similarities = sorted(similarities, key=lambda x: x[1], reverse=True)
    return similarities[:top_n]
