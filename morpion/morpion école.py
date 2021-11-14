import pygame
from random import randint
import numpy as np
from pygame.locals import *


continuer = True

pygame.init()   # ne pas se préocuper de cette ligne

pygame.display.set_caption( 'fenetre de jeu' )  # créer une fentre et lui attribut un nom
infoObject = pygame.display.Info()  # récupére les valeur de l'écran de l'utilisateur
(width , height) = (infoObject.current_w , infoObject.current_h - 50 )  #calcule la taille de la fenetre
screen = pygame.display.set_mode((width , height))   # paramétre la taille de la fenetre en fonction de la taille de l'écran
screen.fill(( 255 , 255 , 255 ))  #Pour le moment, rempli le fond d'écran en blanc

pygame.display.update()

cercle = pygame.image.load('cercle.PNG').convert_alpha() #charge l'image du cercle
croix = pygame.image.load('croix.PNG').convert_alpha() #charge l'image d'une croix
grille = pygame.image.load('grille.PNG').convert_alpha() #charge l'image de la grille
grille = pygame.transform.scale(grille, (height, height)) # change les dimenssions de la grille pour quelle coresponde a la fenetre
croix = pygame.transform.scale(croix, (int(height/3.2), int(height/3.2)))
cercle = pygame.transform.scale(cercle, (int(height/3.2), int(height/3.2)))
croix.set_colorkey((255,255,255)) #permet de rendre transparent le blanc
'''
L'interet de la ligne qui suit est difficile a comprendre:
pygame a une méthode: collidepoint qui renvoie True si la position qu'on lui donne est sur l'objet placer avant cette methode
cepandant, ca ne marche simplement qu'avec des rectangles et non des images on créer donc des rectangles de la tailles des images
que l'on placera au niveau des croix puis on verifiera si l'on clique sur ces rectangles et donc sur la croix.
'''
rect_detection = pygame.Surface((int(height/3.2), int(height/3.2)))



screen.blit(grille, ((width - height)/2 , 0))  #colle la surface grille sue l'écran
pos_croix = [(2, 2)]
pos_cercle = [(2, height/2 + 2)]

pygame.display.update()   # cette ligne est essentiel, elle permet d'actualiser l'écran: envoyer l'ordre a l'écran d'afficher
detection_croix = screen.blit(rect_detection, (2, 2))

def actu():  # cette fonction permettra d' afficher tous les objets sur l'écran a leur nouvelle place
    detection_croix = [screen.blit(rect_detection, position) for position in pos_croix]
    detection_cercle = [screen.blit(rect_detection, position) for position in pos_cercle]
    screen.fill((255, 255, 255))
    screen.blit(grille, ((width - height) / 2, 0))  # colle la surface grille sue l'écran
    for position in pos_croix:
        screen.blit(croix, position)
    for position in pos_cercle:
        screen. blit(cercle, position)
    pygame.display.update()
actu()

click = False # cette variable va donner True tant que l'on a la souris enfoncé
liste_clicker = []      #cette variable contiendra la piece clicker et son type

while continuer : #début de la boucle des événements
    for event in pygame.event.get() : # va chercher les événements dans la liste des événements (clavier, souris...)

        if event.type == pygame.QUIT : #si l'on clique si la croix pas défauts au niveau de la fenetre
            quit() # on éteint la fenetre

        if event.type == pygame.MOUSEBUTTONDOWN: # si l'on clique avec la souris
            position_souris = event.pos # on capte dans une variable la position de la souris
            for piece in range((len(pos_croix))): #on cherche quelle potentiel piece a été cliquer
                if detection_croix.collidepoint(position_souris):
                    click = True
                    liste_clicker = pos_croix
            if click:
                pos_croix.append(position_souris)

        if event.type == pygame.MOUSEBUTTONUP:
            click = False

        if click:
            pos_croix[-1] = event.pos
            actu()