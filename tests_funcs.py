# Auteure : Rizlène Belabdelli

import unittest
import funcs

# Exercice 1 

# 1.1 : Fonction qui renvoie les 3 plus grandes valeurs d'une liste d'entiers

class TestFuncs(unittest.TestCase):
    def test_top_3_valeurs(self):
        self.assertEqual(funcs.top_3_valeurs([5,3,1,4,2]), [5,4,3])  # Cas général
        self.assertEqual(funcs.top_3_valeurs([10, 10, 10]), [10,10,10])  # Doublons
        self.assertEqual(funcs.top_3_valeurs([1,2]), [2,1]) # Moins de 3 élements
        self.assertEqual(funcs.top_3_valeurs([]), [])   # liste vide
