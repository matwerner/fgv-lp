'''
This module contains functions to preprocess text and compute the bag of words representation of a text.
'''

from typing import List, Set, Dict

def preprocess_text(text: str) -> str:
    """
    Preprocess the text by converting it to lowercase and removing punctuation.

    Parameters
    ----------
    text : str
        The text to be preprocessed

    Returns
    -------
    str
        The preprocessed text

    Examples
    --------
    >>> text = 'A document is a written, drawn, presented, ...'
    >>> print(preprocess_text(text))
    'a document is a written drawn presented'
    """
    text = text.lower().strip()
    chars = []
    for c in text:
        if c.isalnum() or c.isspace():
            chars.append(c)
        else:
            chars.append(' ')
    text = ''.join(chars)
    text = ' '.join(text.split())
    return text

def compute_vocab(texts: List[str], top_n: int = 10000) -> Set[str]:
    """
    Compute the vocabulary of the documents by selecting the top_n most frequent words.

    Parameters
    ----------
    texts : List[str]
        The list of documents to compute the vocabulary
    top_n : int, optional
        The number of most frequent words to select, by default 10000

    Returns
    -------
    Set[str]
        The set of most frequent words in the documents

    Examples
    --------
    >>> texts = ['a document is a written drawn presented', 'another document is a written drawn presented']
    >>> print(compute_vocab(texts))
    {'a', 'document', 'is', 'written', 'drawn', 'presented', 'another'}
    """
    vocab = {}
    for text in texts:
        for word in text.split():
            vocab[word] = vocab.get(word, 0) + 1
    vocab = [(k, v) for k, v in vocab.items()]
    vocab = sorted(vocab, key=lambda x: x[1], reverse=True)
    vocab = vocab[:top_n]
    vocab = {k for k, _ in vocab}
    return vocab

def compute_bow(text: str, vocab: Set[str]) -> Dict[str, int]:
    """
    Compute the bag of words representation of a text using a given vocabulary.

    Parameters
    ----------
    text : str
        The text to compute the bag of words
    vocab : Set[str]
        The vocabulary to use for the bag of words

    Returns
    -------
    Dict[str, int]
        The bag of words representation of the text

    Examples
    --------
    >>> vocab = {'a', 'document', 'is', 'written', 'drawn', 'presented', 'another'}
    >>> text = 'a document is a written drawn presented'
    >>> print(compute_bow(text, vocab))
    {'a': 2, 'document': 1, 'is': 1, 'written': 1, 'drawn': 1, 'presented': 1, 'another': 0}
    """
    bow = {k: 0 for k in vocab}
    for word in text.split():
        if word in vocab:
            bow[word] += 1
    return bow

