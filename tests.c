// Auteure : Rizlène Belabdelli

#include "inventaire.h"
#include <assert.h>
#include <string.h>

void test_ajouter_article() {
    Inventaire inventaire = { .taille = 0 };
    ajouter_article(&inventaire, "Pomme", 10, 0.5);
    assert(inventaire.taille == 1);
    assert(strcmp(inventaire.articles[0].nom, "Pomme") == 0);
    assert(inventaire.articles[0].quantite == 10);
}

void test_retirer_article() {
    Inventaire inventaire = { .taille = 0 };
    ajouter_article(&inventaire, "Pomme", 10, 0.5);
    retirer_article(&inventaire, "Pomme", 5);
    assert(inventaire.articles[0].quantite == 5);

    retirer_article(&inventaire, "Pomme", 5);
    assert(inventaire.taille == 0);
}

int main() {
    test_ajouter_article();
    test_retirer_article();
    printf("Tous les tests ont réussi !\n");
    return 0;
}