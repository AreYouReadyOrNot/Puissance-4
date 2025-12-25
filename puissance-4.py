"""
Puissance 4 - Jeu classique en Python
Auteur: Walid Bouknia
Date: 2025

Mode de jeu:
- Humain vs IA
- IA vs IA
"""

from random import randint


def grille_vide():
    """Retourne une grille vide (6 lignes x 7 colonnes)."""
    return [[0] * 7 for _ in range(6)]


def affiche(grille):
    """Affiche la grille de jeu.
    
    Args:
        grille (list): La grille de jeu
    """
    # Affiche les numéros des colonnes
    print("0 1 2 3 4 5 6")
    
    # Affiche la grille de haut en bas
    for i in range(6):
        ligne = 5 - i
        for element in grille[ligne]:
            if element == 0:
                print(".", end=" ")
            elif element == 1:
                print("X", end=" ")
            else:
                print("O", end=" ")
        print()
    print()


def coup_possible(grille, colonne):
    """Vérifie si on peut jouer dans la colonne.
    
    Args:
        grille (list): La grille de jeu
        colonne (int): La colonne où jouer
        
    Returns:
        bool: True si le coup est possible, False sinon
    """
    return grille[5][colonne] == 0


def jouer(grille, joueur, colonne):
    """Joue un coup pour le joueur dans la colonne.
    
    Args:
        grille (list): La grille de jeu
        joueur (int): Le joueur (1 ou 2)
        colonne (int): La colonne où jouer
    """
    ligne = 0
    while grille[ligne][colonne] != 0:
        ligne += 1
    grille[ligne][colonne] = joueur


def horiz(grille, joueur, ligne, colonne):
    """Vérifie un alignement horizontal.
    
    Args:
        grille (list): La grille de jeu
        joueur (int): Le joueur à vérifier
        ligne (int): La ligne
        colonne (int): La colonne de départ
        
    Returns:
        bool: True s'il y a un alignement de 4
    """
    for i in range(4):
        if grille[ligne][colonne + i] != joueur:
            return False
    return True


def verti(grille, joueur, ligne, colonne):
    """Vérifie un alignement vertical.
    
    Args:
        grille (list): La grille de jeu
        joueur (int): Le joueur à vérifier
        ligne (int): La ligne de départ
        colonne (int): La colonne
        
    Returns:
        bool: True s'il y a un alignement de 4
    """
    for i in range(4):
        if grille[ligne - i][colonne] != joueur:
            return False
    return True


def diag_ascendante(grille, joueur, ligne, colonne):
    """Vérifie un alignement diagonal ascendant (bas-gauche vers haut-droit).
    
    Args:
        grille (list): La grille de jeu
        joueur (int): Le joueur à vérifier
        ligne (int): La ligne de départ
        colonne (int): La colonne de départ
        
    Returns:
        bool: True s'il y a un alignement de 4
    """
    for i in range(4):
        if grille[ligne - i][colonne + i] != joueur:
            return False
    return True


def diag_descendante(grille, joueur, ligne, colonne):
    """Vérifie un alignement diagonal descendant (haut-gauche vers bas-droit).
    
    Args:
        grille (list): La grille de jeu
        joueur (int): Le joueur à vérifier
        ligne (int): La ligne de départ
        colonne (int): La colonne de départ
        
    Returns:
        bool: True s'il y a un alignement de 4
    """
    for i in range(4):
        if grille[ligne + i][colonne + i] != joueur:
            return False
    return True


def victoire(grille, joueur):
    """Vérifie si le joueur a gagné.
    
    Args:
        grille (list): La grille de jeu
        joueur (int): Le joueur à vérifier
        
    Returns:
        bool: True si le joueur a gagné, False sinon
    """
    for ligne in range(6):
        for colonne in range(7):
            # Vérifier horizontal
            if colonne < 4 and horiz(grille, joueur, ligne, colonne):
                return True
            # Vérifier vertical
            if ligne > 2 and verti(grille, joueur, ligne, colonne):
                return True
            # Vérifier diagonal ascendant
            if colonne < 4 and ligne > 2 and diag_ascendante(grille, joueur, ligne, colonne):
                return True
            # Vérifier diagonal descendant
            if colonne < 4 and ligne < 3 and diag_descendante(grille, joueur, ligne, colonne):
                return True
    return False


def match_nul(grille):
    """Vérifie s'il y a match nul (grille pleine).
    
    Args:
        grille (list): La grille de jeu
        
    Returns:
        bool: True s'il y a match nul, False sinon
    """
    for colonne in range(7):
        if grille[5][colonne] == 0:
            return False
    return True


def coup_aleatoire(grille, joueur):
    """Joue un coup aléatoire pour l'IA.
    
    Args:
        grille (list): La grille de jeu
        joueur (int): Le joueur (IA)
    """
    while True:
        colonne = randint(0, 6)
        if coup_possible(grille, colonne):
            break
    jouer(grille, joueur, colonne)
    print(f"L'IA joue dans la colonne {colonne}")


def coup_human(grille, joueur):
    """Demande au joueur humain de jouer un coup.
    
    Args:
        grille (list): La grille de jeu
        joueur (int): Le joueur humain
    """
    while True:
        try:
            colonne = int(input("Quelle colonne ? (0-6): "))
            if 0 <= colonne <= 6 and coup_possible(grille, colonne):
                break
            print("❌ Coup impossible ! Essayez une autre colonne.")
        except ValueError:
            print("❌ Veuillez entrer un nombre valide.")
    jouer(grille, joueur, colonne)


def match_human_vs_ia():
    """Lance une partie Humain vs IA."""
    grille = grille_vide()
    joueur = 1
    
    print("\n=== PUISSANCE 4 - Humain vs IA ===")
    print("Vous êtes X, l'IA est O")
    affiche(grille)
    
    while True:
        if joueur == 1:
            print("À votre tour !")
            coup_human(grille, joueur)
        else:
            coup_aleatoire(grille, joueur)
        
        affiche(grille)
        
        if victoire(grille, joueur):
            if joueur == 1:
                print("🎉 Vous avez gagné !")
            else:
                print("😔 L'IA a gagné !")
            break
        elif match_nul(grille):
            print("🤝 Match nul !")
            break
        
        joueur = 3 - joueur


def match_ia_vs_ia():
    """Lance une partie IA vs IA."""
    grille = grille_vide()
    joueur = 1
    
    print("\n=== PUISSANCE 4 - IA vs IA ===")
    affiche(grille)
    
    while True:
        coup_aleatoire(grille, joueur)
        affiche(grille)
        
        if victoire(grille, joueur):
            print(f"🎉 Le joueur {joueur} (IA) a gagné !")
            break
        elif match_nul(grille):
            print("🤝 Match nul !")
            break
        
        joueur = 3 - joueur


def menu_principal():
    """Affiche le menu principal et lance la partie."""
    print("\n" + "="*40)
    print("   BIENVENUE AU PUISSANCE 4")
    print("="*40)
    print("\n1️⃣  Humain vs IA")
    print("2️⃣  IA vs IA")
    print("3️⃣  Quitter")
    
    while True:
        choix = input("\nVotre choix (1, 2 ou 3): ").strip()
        
        if choix == "1":
            match_human_vs_ia()
            break
        elif choix == "2":
            match_ia_vs_ia()
            break
        elif choix == "3":
            print("Au revoir ! 👋")
            break
        else:
            print("❌ Choix invalide. Veuillez entrer 1, 2 ou 3.")


if __name__ == "__main__":
    menu_principal()
