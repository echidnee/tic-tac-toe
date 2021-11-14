import numpy as np
from random import randint

'''
house_list = []
with open("Houses.csv", mode='r', encoding='utf-8') as f:
    house_list = f.readlines()

for i, chaine in enumerate(house_list):
    house_list[i] = chaine.strip()
print(house_list)
'''


plateau = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#print(plateau)


def gagnant(plateau_de_jeu):
    s1 = [sum(plateau_de_jeu[i]) for i in range(3)]     # somme des lignes
    s2 = [sum([plateau_de_jeu[i][j] for i in range(3)]) for j in range(3)]  # somme des colonnes
    s3 = [sum([plateau_de_jeu[i][i-2*j*(i - 1)] for i in range(3)]) for j in range(2)]
    #print(s1, s2, s3)
    if 12 in s1 + s2 + s3:
        print('4 a gagné')
        #gagnant += 1
        return True
    elif 3 in s1 + s2 + s3:
        print('1 a gagné')
        #gagnant += 1
        return True
    else :
        return False


def match_nul(plateau_de_jeu):
    l = [plateau_de_jeu[i][j] for i in range(3) for j in range(3)]
    if 0 in l:
        return False
    else:
        return True

joueur = 1


while not match_nul(plateau) and not gagnant(plateau):
    continuer = True
    while continuer:
        x = randint(0, 2)
        y = randint(0, 2)
        if plateau[x][y] == 0:
            continuer = False
            plateau[x][y] = joueur
            print(plateau)
    joueur = 5 - joueur
print(plateau)




