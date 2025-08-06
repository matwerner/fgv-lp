import unittest

from metrics import jaccard_similarity

class TestMetrics(unittest.TestCase):

    def test_jaccard_similarity_perfect(self):
        bow1 = {'a': 2, 'document': 1, 'is': 1, 'written': 1, 'drawn': 1, 'presented': 1, 'another': 0}
        bow2 = {'a': 1, 'document': 1, 'is': 1, 'written': 1, 'drawn': 1, 'presented': 1, 'another': 0}
        self.assertEqual(jaccard_similarity(bow1, bow2), 1.0)

    def test_jaccard_similarity_almost(self):
        bow1 = {'a': 2, 'document': 1, 'is': 1, 'written': 1, 'drawn': 1, 'presented': 1, 'another': 0}
        bow2 = {'a': 1, 'document': 1, 'is': 1, 'written': 1, 'drawn': 1, 'presented': 1, 'another': 1}
        self.assertAlmostEqual(jaccard_similarity(bow1, bow2), 0.857, places=3)

if __name__ == '__main__':
    unittest.main()
