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


    def test_est_premier(self):
        # Nombre premier
        self.assertTrue(funcs.est_premier(2))
        self.assertTrue(funcs.est_premier(3))
        self.assertTrue(funcs.est_premier(17))
        # Nombre non premier
        self.assertFalse(funcs.est_premier(1))
        self.assertFalse(funcs.est_premier(0))
        self.assertFalse(funcs.est_premier(9))
        # Nombre négatif 
        self.assertFalse(funcs.est_premier(-5)) # Pas de nombre premier négatif

    
    def test_est_arithmetique(self):
        # Suite arithmétique avec différence 2
        self.assertTrue(funcs.est_arithmetique([2,4,6,8]))

        # Suite arithmétique avec différence -3
        self.assertTrue(funcs.est_arithmetique([10,7,4,1]))

        # Liste non arithmétique
        self.assertFalse(funcs.est_arithmetique([1,2,4,5]))

        # Liste vide ou avec un seul élément : considérée comme arithmétique
        self.assertTrue(funcs.est_arithmetique([]))
        self.assertTrue(funcs.est_arithmetique([1]))


    # Exercice 2

    # 2.1 : Classe FIFO

    def test_fifo(self):
        # Cration d'une instance de FIFO
        fifo = funcs.FIFO()

        # Vérification de l'état initial : la file est vide
        self.assertTrue(fifo.is_empty())

        # Ajout d'un élément dans la file
        fifo.enqueue(10)
        self.assertFalse(fifo.is_empty()) # La file n'est plus vide
        self.assertEqual(fifo.dequeue(), 10) # On peut récupérer l'élément 10

        # Vérification si la file est vide après dequeue
        self.assertTrue(fifo.is_empty())

        # Test avec plusieurs éléments
        fifo.enqueue(20)
        fifo.enqueue(30)
        self.assertEqual(fifo.dequeue(), 20) # Le 1er ajouté est le 1er retiré
        self.assertEqual(fifo.dequeue(), 30) # Le 2ème ajouté est le 2ème retiré

        # Vérification si la file est vide après avoir retiré tous les éléments
        self.assertTrue(fifo.is_empty())


    # 2.2 : Classe LIFO

    def test_lifo(self):
        # Création d'une instance de LIFO
        lifo = funcs.LIFO()

        # Vérification de l'état initial : la pile est vide
        self.assertTrue(lifo.is_empty())

        # Ajout d'un élément dans la pile
        lifo.push(10)
        self.assertFalse(lifo.is_empty()) # La pile n'est plus vide
        self.assertEqual(lifo.pop(), 10) # Le dernier élément ajouté doit être retiré

        # Vérification si la pile est vide après pop
        self.assertTrue(lifo.is_empty())

        # Test avec plusieurs éléments
        lifo.push(20)
        lifo.push(30)
        self.assertEqual(lifo.pop(), 30) # Le dernier ajouté (30) doit être retiré en premier
        self.assertEqual(lifo.pop(), 20) # Le 2ème ajouté (20) doit être retiré après 30

        # Vérification si la pile est vide après avoir retiré tous les éléments
        self.assertTrue(lifo.is_empty())