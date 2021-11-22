import pygame
from random import randint
from time import sleep
from pygame.locals import *
from copy import deepcopy


plateau = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # chaque element de cette liste représente une ligne du plateau


def gagnant(plateau_de_jeu):
    """
    :param plateau_de_jeu: le plateau en cours
    :return: un booléen rapportant si il y a un vainqueur et le nom du vainqueur (1, 4)
    """
    s1 = [sum(plateau_de_jeu[i]) for i in range(3)]
    s2 = [sum([plateau_de_jeu[i][j] for i in range(3)]) for j in range(3)]
    s3 = [sum([plateau_de_jeu[i][i-2*j*(i - 1)] for i in range(3)]) for j in range(2)]
    if 12 in s1 + s2 + s3:
        return True, 4
    elif 3 in s1 + s2 + s3:
        return True, 1
    else:
        return False, 0


def match_nul(plateau_de_jeu):
    """
    :param plateau_de_jeu: plateau a verifier
    :return: True si il y a match nul et False dans le cas contraire
    """
    liste_plateau = [plateau_de_jeu[i][j] for i in range(3) for j in range(3)]
    if 0 in liste_plateau:
        return False
    else:
        return True


def partie_alea(joueur, plateau_jeu):
    """
    :param joueur: le nom du joueur a qui c'est a de jouer
    :param plateau_jeu: le plateau en cours
    :return: dans le cas de la victoire du joueur : le gagnant, le plateau et donc le cout qui va mener a la victoire
    et le nombre de cout
             dans le cas de la defaite du joueur : le gagnant, la plateau qui va permettre de parer la defaite
    et le nombre de cout de la potentiel defaite
    """
    joueut_debut = joueur
    plateau_debut = deepcopy(plateau_jeu)
    plateau_suivant = []
    coup = 0
    while not match_nul(plateau_jeu) and not gagnant(plateau_jeu)[0]:
        continuer = True
        while continuer:
            x = randint(0, 2)
            y = randint(0, 2)
            if plateau_jeu[x][y] == 0:
                continuer = False
                plateau_jeu[x][y] = joueur
                coup += 1
                if coup == 1:
                    for i in range(3):  # permet de creer une copie independante des sous-listes
                        plateau_suivant.append(plateau_jeu[i].copy())

        joueur = 5 - joueur
    if gagnant(plateau_jeu)[1] == joueur:
        return gagnant(plateau_jeu)[1], plateau_suivant, coup
    else:
        plateau_debut[x][y] = joueut_debut

        return gagnant(plateau_jeu)[1], plateau_debut, coup


def coup_suivant(joueur_suivant, plateau_de_jeu):
    """
    :param joueur_suivant: joueur qui doit jouer
    :param plateau_de_jeu: plateau en cours
    :return: le plateau avec le nouveau coup gagnant
    """
    gagnant = (20, deepcopy(plateau_de_jeu))
    perdant = (20, deepcopy(plateau_de_jeu))
    for _ in range(1000):
        g, p, c = partie_alea(joueur_suivant, deepcopy(plateau_de_jeu))
        if g == joueur_suivant and c < gagnant[0]:
            gagnant = (c, p)

        elif g == 5 - joueur_suivant and c < perdant[0]:
            perdant = (c, p)

    if (gagnant[0], gagnant[0]) == (20, 20):
        return partie_alea(joueur_suivant, deepcopy(plateau_de_jeu))[1]
    elif gagnant[0] <= perdant[0]:

        return gagnant[1]
    else:
        return perdant[1]


def fin_partie(plateau_jeu):
    """

    :param plateau_jeu: plateau en cours
    en cas de victoire de defaite de victoire ou de match nul, arrete la partie et l'affiche
    """
    if gagnant(plateau_jeu)[1] != 0:
        if gagnant(plateau_jeu)[1] == machine:
            texte = police.render("perdu !", 1, (255, 0, 0))
        else:
            texte = police.render("Gagné !", 1, (255, 0, 0))
        sleep(1.5)
        screen.blit(poudlard, (0, 0))
        screen.blit(texte, (int(width/4), int(height/4)))
        pygame.display.update()
        sleep(4)
        pygame.quit()
    if match_nul(plateau):
        texte = police.render("matche nul", 1, (255, 0, 0))
        screen.blit(poudlard, (0, 0))
        screen.blit(texte, (0, int(height/4)))
        pygame.display.update()
        sleep(4)
        pygame.quit()


def trace_plateau(plateau_de_jeu):
    """

    :param plateau_de_jeu:  le plateau en cours
    permet d'actualiser l'affichage en affichant le plateau en cours
    """
    screen_plateau = pygame.Surface((width, height))
    screen_plateau.blit(poudlard, (0, 0))
    screen_plateau.blit(grille, (pos_grillex, 0))
    screen_plateau.blit(croix, (2, 2))
    screen_plateau.blit(cercle, (2, height/2 + 2))
    for ligne in range(3):
        for colonne in range(3):
            if plateau_de_jeu[ligne][colonne] == 1:
                screen_plateau.blit(cercle, pos_case[ligne][colonne])
            elif plateau_de_jeu[ligne][colonne] == 4:
                screen_plateau.blit(croix, pos_case[ligne][colonne])
    return screen_plateau


x = None
# creation de la fenetre
pygame.init()


infoObject = pygame.display.Info()
(width, height) = (infoObject.current_w, infoObject.current_h - 50)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('fenetre de jeu')
poudlard = pygame.image.load('poudlard.jpg')
poudlard = pygame.transform.scale(poudlard, (width - 10, height - 10))
screen.blit(poudlard, (0, 0))


# traitement des images et de la police
police = pygame.font.SysFont("monospace", int(height/3))
cercle = pygame.image.load('griffondor.PNG').convert_alpha()
cercle = pygame.transform.scale(cercle, (int(height/3.2), int(height/3.2)))
croix = pygame.image.load('serpentard.PNG').convert_alpha()
croix = pygame.transform.scale(croix, (int(height/3.2), int(height/3.2)))
grille = pygame.image.load('grille.PNG').convert_alpha()
grille = pygame.transform.scale(grille, (height, height))
croix.set_colorkey((255, 255, 255))
cercle.set_colorkey((255, 255, 255))

# mise en place des rectangles de detection
rect_detection = pygame.Surface((int(height/3.2), int(height/3.2)))
detection_croix = screen.blit(rect_detection, (2, 2))
detection_cercle = screen.blit(rect_detection, ((2, height/2 + 2)))

# definission des positions des diférents piece en fonction des dimenssions de l'écran
pos_grillex = (width - height)/2

pos_case = [[(pos_grillex, 0), (pos_grillex + height/3, 0), (pos_grillex + height*(2/3), 0)],
            [(pos_grillex, height/3), (pos_grillex + height/3, height/3), (pos_grillex + height*(2/3), height/3)],
            [(pos_grillex, height/1.5), (pos_grillex + height/3, height/1.5), (pos_grillex + height*(2/3), height/1.5)]]

detection_plateau = [[screen.blit(rect_detection, pos_case[ligne][colonne]) for colonne in range(3)] for ligne in range(3)]


# affichage des diférent éléments
screen.blit(grille, (pos_grillex, 0))
screen.blit(croix, (2, 2))
screen.blit(cercle, ((2, height/2 + 2)))

pygame.display.update()


screen.blit(trace_plateau(plateau), (0, 0))
pygame.display.update()

# initialisation variable
machine = 4
joueur = 1

click, premier = False, False

# boucle de jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:  # reconnait sur quelle piece on clique
            if detection_croix.collidepoint(event.pos) and ((machine, joueur) == (1, 4) or not premier):
                if not premier:
                    joueur = 4
                    machine = 1
                click = True
                premier = True
                piece_clicker = croix

            if detection_cercle.collidepoint(event.pos) and (machine, joueur) == (4, 1):
                click = True
                premier = True
                piece_clicker = cercle

        if event.type == pygame.MOUSEBUTTONUP and click:  # si le cout est légale, l'incrémente au plateau
            click = False
            for ligne in range(3):
                for colonne in range(3):
                    if detection_plateau[ligne][colonne].collidepoint(event.pos):
                        if plateau[ligne][colonne] == 0:
                            plateau[ligne][colonne] = joueur
                            joueur = 5 - joueur
                            screen.blit(trace_plateau(plateau), (0, 0))
                            pygame.display.update()
                            fin_partie(plateau)


        if click:   # permet de deplacer en temps réel la piéce
            if premier:
                plateau_temporaire = trace_plateau(plateau)
                screen.blit(plateau_temporaire, (0, 0))
            else:
                screen.blit(plateau_temporaire)
            try:
                position_souris = event.pos
                px, py = position_souris
                screen.blit(piece_clicker, (px - int(height/6.4), py - int(height/6.4)))
            except:
                screen.blit(piece_clicker, (px - int(height/6.4), py - int(height/6.4)))
            pygame.display.update()

        if joueur == machine:  # fait jouer l'ordianteur a son tour
            plateau = coup_suivant(machine, plateau)
            screen.blit(trace_plateau(plateau), (0, 0))
            pygame.display.update()
            fin_partie(plateau)
            joueur = 5 - joueur
