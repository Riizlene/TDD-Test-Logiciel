// Auteure : Rizlène Belabdelli

#include "inventaire.h"

int main() {
    Inventaire inventaire = { .taille = 0 };

    ajouter_article(&inventaire, "Pomme", 10, 0.5);
    ajouter_article(&inventaire, "Banane", 5, 0.3);
    afficher_inventaire(&inventaire);

    retirer_article(&inventaire, "Pomme", 3);
    afficher_inventaire(&inventaire);

    retirer_article(&inventaire, "Banane", 5);
    afficher_inventaire(&inventaire);

    return 0;
}