'''
This module contains the implementation of metrics to compare documents.
'''

from typing import Dict

def jaccard_similarity(bow1: Dict[str, int], bow2: Dict[str, int]) -> float:
    """
    Compute the Jaccard similarity between two bag of words representations.

    Parameters
    ----------
    bow1 : Dict[str, int]
        The first bag of words representation
    bow2 : Dict[str, int]
        The second bag of words representation

    Returns
    -------
    float
        The Jaccard similarity between the two bag of words representations

    Examples
    --------
    >>> bow1 = {'a': 2, 'document': 1, 'is': 1, 'written': 1, 'drawn': 1, 'presented': 1, 'another': 0}
    >>> bow2 = {'a': 1, 'document': 1, 'is': 1, 'written': 1, 'drawn': 1, 'presented': 1, 'another': 0}
    >>> print(compute_jaccard_similarity(bow1, bow2))
    1.0
    """
    intersection = 0
    union = 0
    for k in bow1:
        if bow1[k] > 0 or bow2[k] > 0:
            union += 1
        if bow1[k] > 0 and bow2[k] > 0:
            intersection += 1
    return intersection / union