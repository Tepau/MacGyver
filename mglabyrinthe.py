
import pygame
from pygame.locals import *
from classes import *
from constantes import *

pygame.init()

fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))

icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)

pygame.display.set_caption(titre_fenetre)

continuer = 1

while continuer :
	accueil = pygame.image.load(image_accueil).convert()
	fenetre.blit(accueil, (0,0))

	pygame.display.flip()

	continuer_jeu = 1
	continuer_accueil = 1

	while continuer_accueil:
		for event in pygame.event.get():
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				continuer = 0
				continuer_accueil = 0
				continuer_jeu = 0

				
			elif event.type == KEYDOWN and event.key == K_SPACE:
				continuer_accueil = 0
				


	
	niveau = Niveau("n1")
	niveau.generer()
	niveau.afficher(fenetre)

	macgyver = Perso(image_avatar, niveau)

	while continuer_jeu :
		for event in pygame.event.get():
			if event.type == QUIT:
				continuer = 0
				continuer_jeu = 0
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					continuer_jeu = 0
				elif event.key == K_RIGHT:
					macgyver.deplacer("droite")
				elif event.key == K_LEFT:
					macgyver.deplacer("gauche")
				elif event.key == K_DOWN:
					macgyver.deplacer("bas")
				elif event.key == K_UP:
					macgyver.deplacer("haut")


		fond = pygame.image.load(image_fond).convert()
		fenetre.blit(fond, (0,0))
		niveau.afficher(fenetre)
		fenetre.blit(macgyver.avatar, (macgyver.x, macgyver.y))
		pygame.display.flip()

		if niveau.structure[macgyver.case_y][macgyver.case_x] == 'a':
			continuer = 0
			continuer_jeu = 0
			continuer_accueil = 0



