import unittest

# Evitar: Apenas utilizando por uma questão de organização do código
# 
# Normalmente faríamos:
# from mymodule import unir_lista
#
# Porém, nomes de módulos que começam com números (ex.: "19_aula_logica")
# não podem ser importados diretamente.  
# Para contornar, usamos __import__
mymodule = __import__("19_aula_logica")


class TesteUnirLista(unittest.TestCase):

    def test_sucesso_lista_iguais(self):
        # Entrada
        seq1 = [1, 3, 5, 7]
        seq2 = [2, 4, 6, 8]

        # Saida
        real = mymodule.unir_lista(seq1, seq2)

        # Comparacao
        esperado = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertListEqual(real, esperado)

    def test_sucesso_l2_maior_l1(self):
        seq1 = [1, 3, 5, 7]
        seq2 = [2, 4, 6, 8, 9, 10, 11]

        real = mymodule.unir_lista(seq1, seq2)

        esperado = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.assertListEqual(real, esperado)

    def test_sucesso_l1_maior_l2(self):
        seq1 = [2, 4, 6, 8, 9, 10, 11]
        seq2 = [1, 3, 5, 7]

        real = mymodule.unir_lista(seq1, seq2)

        esperado = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.assertListEqual(real, esperado)

    def test_erro_lista_nao_ordenada(self):
        seq1 = [7, 5, 3, 1]
        seq2 = [2, 4, 6, 8]

        with self.assertRaises(ValueError):
            mymodule.unir_lista(seq1, seq2)


if __name__ == "__main__":
    unittest.main()
