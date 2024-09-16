import unittest

from text import preprocess_text, compute_vocab, compute_bow

class TestText(unittest.TestCase):

    def test_preprocess_text(self):
        text = 'A document is a written, drawn, presented, ...'
        result = preprocess_text(text)
        expected = 'a document is a written drawn presented'
        self.assertEqual(result, expected)

    def test_compute_vocab(self):
        texts = ['a document is a written drawn presented', 'another document is a written drawn presented']
        result = compute_vocab(texts)
        expected = {'a', 'document', 'is', 'written', 'drawn', 'presented', 'another'}
        self.assertSetEqual(result, expected)

    def test_compute_bow(self):
        text = 'a document is a written drawn presented'
        vocab = {'a', 'document', 'is', 'written', 'drawn', 'presented', 'another'}
        result = compute_bow(text, vocab)
        expected = {'a': 2, 'document': 1, 'is': 1, 'written': 1, 'drawn': 1, 'presented': 1, 'another': 0}
        self.assertDictEqual(result, expected)
