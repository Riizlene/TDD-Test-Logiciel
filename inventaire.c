// Auteure : Rizlène Belabdelli

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char nom[50];
    int quantite;
    float prix;
} Article;

typedef struct {
    Article articles[100];
    int taille;
} Inventaire;

void afficher_inventaire(const Inventaire* inventaire) {
    printf("Inventaire:\n");
    for (int i = 0; i < inventaire->taille; i++) {
        printf("%s: %d (%.2f€)\n", inventaire->articles[i].nom,
               inventaire->articles[i].quantite, inventaire->articles[i].prix);
    }
}

void ajouter_article(Inventaire* inventaire, const char* nom, int quantite, float prix) {
    for (int i = 0; i < inventaire->taille; i++) {
        if (strcmp(inventaire->articles[i].nom, nom) == 0) {
            inventaire->articles[i].quantite += quantite;
            return;
        }
    }
    strcpy(inventaire->articles[inventaire->taille].nom, nom);
    inventaire->articles[inventaire->taille].quantite = quantite;
    inventaire->articles[inventaire->taille].prix = prix;
    inventaire->taille++;
}

void retirer_article(Inventaire* inventaire, const char* nom, int quantite) {
    for (int i = 0; i < inventaire->taille; i++) {
        if (strcmp(inventaire->articles[i].nom, nom) == 0) {
            if (inventaire->articles[i].quantite <= quantite) {
                // Supprimer l'article
                for (int j = i; j < inventaire->taille - 1; j++) {
                    inventaire->articles[j] = inventaire->articles[j + 1];
                }
                inventaire->taille--;
            } else {
                inventaire->articles[i].quantite -= quantite;
            }
            return;
        }
    }
    printf("Article '%s' introuvable dans l'inventaire.\n", nom);
}

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