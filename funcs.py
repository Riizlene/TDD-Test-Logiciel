# Auteure : Rizlène Belabdelli

# Exercice 1 

# 1.1 : Fonction qui renvoie les 3 plus grandes valeurs d'une liste d'entiers

def top_3_valeurs(liste):
    return sorted(liste, reverse=True)[:3]

# 1.2 : Fonction qui renvoie si un nombre est premier ou non

def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# 1.3 : Fonction qui à partir d’une liste de nombre reverra si la liste représente ou pas une suite arithmétique

def est_arithmetique(liste):
    # Si la liste a moins de 2 éléments, on considère que c'est une suite arithmétique
    if len(liste) < 2:
        return True

    # On calcule la différence entre les 2 premiers éléments
    diff = liste[1] - liste[0]

    # Vérification des autres éléments
    for i in range(2, len(liste)):
        if liste[i] - liste[i-1] != diff:
            return False

    # Si toutes les différences sont égales
    return True
    

# Exercice 2

# 2.1 : Classe FIFO

class FIFO:
    def __init__(self):
        # Initialisation de la structure de données
        pass

    def enqueue(self, valeur):
        # Ajoute un élément à la fin de la file
        pass

    def dequeue(self):
        # Retire et renvoie l'élément en tête de file
        pass

    def is_empty(self):
        # Vérifie si la file est vide
        pass