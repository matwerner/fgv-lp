import unittest

from data_loader import is_valid_wikipage, parse_line

class TestDataLoader(unittest.TestCase):

    def test_is_valid_wikipage_valid(self):
        doc = {
            'id': 12,
            'url': 'https://en.wikipedia.org/wiki/Document',
            'title': 'Document',
            'text': 'A document is a written, drawn, presented, ...'
        }
        self.assertTrue(is_valid_wikipage(doc))

    def test_is_valid_wikipage_invalid(self):
        doc = {
            'id': 12,
            'url': 'https://en.wikipedia.org/wiki/Document',
            'title': 'Document'
        }
        self.assertFalse(is_valid_wikipage(doc))

    def test_parse_line_valid(self):
        line = '{"id": 12, "url": "https://en.wikipedia.org/wiki/Document", "title": "Document", "text": "A document is a written, drawn, presented, ..."}'
        doc = {
            'id': 12,
            'url': 'https://en.wikipedia.org/wiki/Document',
            'title': 'Document',
            'text': 'A document is a written, drawn, presented, ...'
        }
        self.assertEqual(parse_line(line), doc)

    def test_parse_line_invalid(self):
        line = '{"id": 12, "url": "https://en.wikipedia.org/wiki/Document", "title": "Document"}'
        with self.assertRaises(ValueError):
            parse_line(line)
