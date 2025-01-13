// Auteure : Rizlène Belabdelli

#ifndef INVENTAIRE_H
#define INVENTAIRE_H

typedef struct {
    char nom[50];
    int quantite;
    float prix;
} Article;

typedef struct {
    Article articles[100];
    int taille;
} Inventaire;

void afficher_inventaire(const Inventaire* inventaire);
void ajouter_article(Inventaire* inventaire, const char* nom, int quantite, float prix);
void retirer_article(Inventaire* inventaire, const char* nom, int quantite);

#endif
