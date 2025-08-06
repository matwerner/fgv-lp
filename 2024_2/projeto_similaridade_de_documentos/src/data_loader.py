'''
This module is responsible for loading the wikipedia documents from a file.
'''

import json
import os

from typing import List, Dict, Any, Optional

def read_documents(file_path: str) -> List[Dict[str, Any]]:
    """
    Read the wikipedia documents from a file.
    The file should contain one document per line in json format.

    Parameters
    ----------
    file_path : str
        The path to the file containing the documents

    Returns
    -------
    List[Dict[str, Any]]
        The list of documents read. 
        Each document is a dictionary with the keys:
        - id : int
            Wikipage identifier
        - url : str
            Wikipage url
        - title : str
            Wikipage title
        - text : str
            Wikipage content

    Raises
    ------
    FileNotFoundError
        If the file does not exist
    
    Examples
    --------
    >>> documents = read_documents('data/wikipedia_documents.json')
    >>> print(documents[0])
    {
        'id': 12,
        'url': 'https://en.wikipedia.org/wiki/Document',
        'title': 'Document',
        'text': 'A document is a written, drawn, presented, ...'
    }
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'File not found: {file_path}')
    index = 0
    documents = []
    with open(file_path, 'r') as file:
        for line in file:
            index += 1
            try:
                document = parse_line(line, index)
            except (json.JSONDecodeError, ValueError) as e:
                print(e)
                continue
            # Only add valid documents
            documents.append(document)
    return documents

def parse_line(line: str, line_idx: int = 0) -> Dict[str, Any]:
    """
    Parse a line containing a wikipedia document in json format.

    Parameters
    ----------
    line : str
        The line to parse
    line_idx : int
        The line index (default is 0)

    Returns
    -------
    Dict[str, Any]
        The parsed document. 
        The document is a dictionary with the keys:
        - id : int
            Wikipage identifier
        - url : str
            Wikipage url
        - title : str
            Wikipage title
        - text : str
            Wikipage content

    Raises
    ------
    json.JSONDecodeError
        If the line is not a valid json
    ValueError
        If the document is not a valid wikipedia page

    Examples
    --------
    >>> line = '{"id": 12, "url": "https://en.wikipedia.org/wiki/Document", "title": "Document", "text": "A document is a written, drawn, presented, ..."}'
    >>> print(parse_line(line))
    {
        'id': 12,
        'url': 'https://en.wikipedia.org/wiki/Document',
        'title': 'Document',
        'text': 'A document is a written, drawn, presented, ...'
    }
    """
    try:
        data = json.loads(line)
    except json.JSONDecodeError:
        raise json.JSONDecodeError(f'Invalid json at line {line_idx}', line, line_idx)
    if not is_valid_wikipage(data):
        raise ValueError('Invalid wikipedia document')
    return data

def is_valid_wikipage(doc: dict):
    """
    Check if a document is a valid wikipedia page.
    A valid wikipedia page should contain the keys:
    - id : int
        Wikipage identifier
    - url : str
        Wikipage url
    - title : str
        Wikipage title
    - text : str
        Wikipage content

    Parameters
    ----------
    doc : dict
        The document to check

    Returns
    -------
    bool
        True if the document is a valid wikipedia page, False otherwise

    Examples
    --------
    >>> doc = {
    ...     'id': 12,
    ...     'url': 'https://en.wikipedia.org/wiki/Document',
    ...     'title': 'Document',
    ...     'text': 'A document is a written, drawn, presented, ...'
    ... }
    >>> is_valid_wikipage(doc)
    True
    >>> doc = {
    ...     'id': 12,
    ...     'title': 'Document',
    ...     'text': 'A document is a written, drawn, presented, ...'
    ... }
    >>> is_valid_wikipage(doc)
    False
    """
    required_keys = ['id', 'url', 'title', 'text']
    for key in required_keys:
        if key not in doc:
            return False
    return True