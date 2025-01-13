// Auteure : Rizlène Belabdelli

#include <stdio.h>
#include <string.h>

#define MAX_PRODUITS 100

typedef struct {
    char nom[50];
    int quantite;
    float prix;
} Produit;

Produit inventaire[MAX_PRODUITS];
int nombreProduits = 0;

void ajouterProduit(char *nom, int quantite, float prix) {
    for (int i = 0; i < nombreProduits; i++) {
        if (strcmp(inventaire[i].nom, nom) == 0) {
            inventaire[i].quantite += quantite;
            inventaire[i].prix = prix;
            return;
        }
    }
    strcpy(inventaire[nombreProduits].nom, nom);
    inventaire[nombreProduits].quantite = quantite;
    inventaire[nombreProduits].prix = prix;
    nombreProduits++;
}

void afficherInventaire() {
    printf("Inventaire:\n");
    for (int i = 0; i < nombreProduits; i++) {
        printf("%s: %d (%.2f€)\n", inventaire[i].nom, inventaire[i].quantite, inventaire[i].prix);
    }
}

void retirerProduit(char *nom, int quantite) {
    for (int i = 0; i < nombreProduits; i++) {
        if (strcmp(inventaire[i].nom, nom) == 0) {
            if (inventaire[i].quantite >= quantite) {
                inventaire[i].quantite -= quantite;
            } else {
                printf("Quantité insuffisante pour retirer %s\n", nom);
            }
            if (inventaire[i].quantite == 0) {
                for (int j = i; j < nombreProduits - 1; j++) {
                    inventaire[j] = inventaire[j + 1];
                }
                nombreProduits--;
            }
            return;
        }
    }
    printf("Produit %s introuvable\n", nom);
}

int main() {
    ajouterProduit("Pomme", 10, 0.5);
    ajouterProduit("Banane", 5, 0.3);
    afficherInventaire();
    retirerProduit("Pomme", 3);
    afficherInventaire();
    retirerProduit("Banane", 5);
    afficherInventaire();
    return 0;
}

