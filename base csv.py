import numpy as np
from random import randint

plateau = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
'''
Chaques éléments de la liste représente une ligne sachant que
le zéro correspond a une case non-occupée,
le 1 ,une case rempli par un cercle
et le 4 ,une case rempli par une croix
'''


def gagnant(plateau_de_jeu):
    """
    :paramètre plateau_de_jeu: le plateau de jeu
    :return: un booléen indicant si quelq'un a gagné et le nombre du vainqueur
    pour savoir si trois même pièces sont alignées on calcule la somme
    des élements des lignes, des colonnes et des diagonales:
    si cette somme est 12: il y a 3 quatre (croix) alignés
    et si cette sommme et 3: il y a 3 un (cercle) alignés
    """
    s_ligne = [sum(plateau_de_jeu[ligne]) for ligne in range(3)]
    s_colonne = [sum([plateau_de_jeu[ligne][colonne] for ligne in range(3)]) for colonne in range(3)]
    s_diagonale = [sum([plateau_de_jeu[ligne][ligne-2*j*(ligne - 1)] for ligne in range(3)]) for j in range(2)]
    if 12 in s_ligne + s_colonne + s_diagonale:
        return True, 4
    elif 3 in s_ligne + s_colonne + s_diagonale:
        return True, 1
    else:
        return False, 0


def match_nul(plateau_de_jeu):
    """
    :paramètre plateau_de_jeu: le plateau en cours
    :return: un booléen True si il y a match nul
    """
    liste_plateau = [plateau_de_jeu[ligne][colonne] for ligne in range(3) for colonne in range(3)]
    if 0 in liste_plateau:
        return False
    else:
        return True


def partie_alea(joueur=1):
    """
    :paramètre joueur: le joueur qui commence
    :return: le joueur qui gagne
    """
    plateau = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    while not match_nul(plateau) and not gagnant(plateau)[0]:
        continuer = True
        while continuer:
            x = randint(0, 2)
            y = randint(0, 2)
            if plateau[x][y] == 0:
                continuer = False
                plateau[x][y] = joueur
        joueur = 5 - joueur
    return gagnant(plateau)[1]


#  créer une liste des dictionnaires relatifs à chaques personnages
house_tab = []
with open("Characters.csv", mode='r', encoding='utf-8') as f:
    lines = f.readlines()
    key_line = lines[0].strip()
    keys = key_line.split(";")
    for line in lines[1:]:
        line = line.strip()
        values = line.split(';')
        dico = {}
        for i in range(len(keys)):
            dico[keys[i]] = values[i]
        house_tab.append(dico)


nb_partie = int(input('combien de partie devra jouer chaque joueur?  '))

for dict_perso in house_tab:  # fait jouer les parties aléatoires a chaques personnages
    victoire = 0
    for _ in range(nb_partie):
        gagnant_partie = partie_alea(1)
        if gagnant_partie == 1:
            victoire += 1
    dict_perso['point'] = victoire

house_tab = sorted(house_tab, key=lambda k: k['point'])  # trie la liste
house_tab.reverse()

for perso in range(140):   # gére l'affichage de la liste
    dict_perso = house_tab[perso]
    nb_point = dict_perso['point']
    nom = dict_perso['Name']
    maison = dict_perso['House']
    print(f"{perso + 1}. {nom} de {maison} avec {nb_point} victoires")