// Auteure : Rizlène Belabdelli

#include "inventaire.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Affiche tous les articles disponibles dans l'inventaire
void afficher_inventaire(const Inventaire* inventaire) {
    printf("Inventaire:\n");
    for (int i = 0; i < inventaire->taille; i++) {
        printf("%s: %d (%.2f€)\n", inventaire->articles[i].nom,
               inventaire->articles[i].quantite, inventaire->articles[i].prix);
    }
}

// Ajoute un article à l'inventaire ou on met à jour la quantité si l'article existe déjà
void ajouter_article(Inventaire* inventaire, const char* nom, int quantite, float prix) {
    for (int i = 0; i < inventaire->taille; i++) {
        if (strcmp(inventaire->articles[i].nom, nom) == 0) {
            inventaire->articles[i].quantite += quantite;
            return;
        }
    }

    if (inventaire->taille < 100) { // Limite de stockage
        strcpy(inventaire->articles[inventaire->taille].nom, nom);
        inventaire->articles[inventaire->taille].quantite = quantite;
        inventaire->articles[inventaire->taille].prix = prix;
        inventaire->taille++;
    }
    else {
        printf("L'inventaire est plein.\n");
    }
}

// Retire une quantité d'un article de l'inventaire ou le supprime completement si la quantité est nulle
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