import unittest

from aula16_logica import unir_lista


class TesteUnirLista(unittest.TestCase):

    def test_sucesso_lista_iguais(self):
        # Entrada
        seq1 = [1, 3, 5, 7]
        seq2 = [2, 4, 6, 8]

        # Saida
        real = unir_lista(seq1, seq2)

        # Comparacao
        esperado = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertListEqual(real, esperado)

    def test_sucesso_l2_maior_l1(self):
        seq1 = [1, 3, 5, 7]
        seq2 = [2, 4, 6, 8, 9, 10, 11]

        real = unir_lista(seq1, seq2)

        esperado = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.assertListEqual(real, esperado)

    def test_sucesso_l1_maior_l2(self):
        seq1 = [2, 4, 6, 8, 9, 10, 11]
        seq2 = [1, 3, 5, 7]

        real = unir_lista(seq1, seq2)

        esperado = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.assertListEqual(real, esperado)

    def test_erro_lista_nao_ordenada(self):
        seq1 = [7, 5, 3, 1]
        seq2 = [2, 4, 6, 8]

        with self.assertRaises(ValueError):
            unir_lista(seq1, seq2)


if __name__ == "__main__":
    unittest.main()
