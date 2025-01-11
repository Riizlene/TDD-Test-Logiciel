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
    pass
    