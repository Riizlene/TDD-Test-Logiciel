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
        # La structure de données sera une liste vide au début
        self.queue = []

    def enqueue(self, valeur):
        # Ajoute un élément à la fin de la file
        self.queue.append(valeur)

    def dequeue(self):
        # Retire et renvoie l'élément en tête de file
        if not self.is_empty():
            return self.queue.pop(0)  # Retirer et renvoyer l'élément en tête
        return None  # Si la file est vide

    def is_empty(self):
        # Vérifie si la file est vide
        return len(self.queue) == 0


# 2.2 : Classe LIFO

class LIFO:
    def __init__(self):
        # La structure de données sera une liste vide au début
        self.stack = []

    def is_empty(self):
        # Vérifie si la pile est vide
        return len(self.stack) == 0

    def push(self, valeur):
        # Ajoute un élément au sommet de la pile
        self.stack.append(valeur)

    def pop(self):
        # Retire et renvoie l'élément au sommet de la pile
        if not self.is_empty():
            return self.stack.pop() # Retirer et renvoyer l'élément du sommet
        return None # Si la pile est vide