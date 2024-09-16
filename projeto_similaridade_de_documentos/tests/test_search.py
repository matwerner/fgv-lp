import unittest

from search import search_by_keyword, search_by_similarity

class TestSearch(unittest.TestCase):

    def test_search_by_keyword(self):
        texts = [
            'A document is a written, drawn, presented, ...',
            'A documentary is a non-fictional motion picture ...',
            'Documentation is a set of documents provided ...'
        ]
        keywords = 'document'
        expected = [(0, 1), (1, 0), (2, 0)]
        result = search_by_keyword(texts, keywords)
        self.assertListEqual(result, expected)

    def test_search_by_similarity(self):
        texts = [
            'A document is a written, drawn, presented, ...',
            'A documentary is a non-fictional motion picture ...',
            'Documentation is a set of documents provided ...'
        ]
        query = texts[0]
        result = search_by_similarity(texts, query)
        expected = [(0, 1), (1, 2/11), (2, 2/11)]
        self.assertListEqual(result, expected)