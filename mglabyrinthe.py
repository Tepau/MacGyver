
import pygame
from pygame.locals import *
from classes import *
from constantes import *

pygame.init()

fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))

icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)

pygame.display.set_caption(titre_fenetre)
Char_img = pygame.image.load(image_avatar).convert_alpha()
image_tube = pygame.image.load(image_tube).convert_alpha()
image_aiguille = pygame.image.load(image_aiguille).convert_alpha()
image_ether = pygame.image.load(image_ether).convert_alpha()
pygame.display.flip()


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
				

	tube_non_attrape = True
	ether_non_attrape = True
	aiguille_non_attrape = True

	gagne = False
	perdu = False


	
	niveau = Niveau("n1")
	niveau.generer()
	niveau.afficher(fenetre)
	macgyver = Perso(image_avatar, niveau)
	tube = Objet_aleatoire(image_tube, niveau)
	tube.afficher(image_tube, fenetre)
	aiguille = Objet_aleatoire(image_aiguille, niveau)
	aiguille.afficher(image_aiguille, fenetre)
	ether = Objet_aleatoire(image_ether, niveau)
	ether.afficher(image_ether, fenetre)


	

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
		fenetre = pygame.display.set_mode((cote_fenetre, 480))
		fenetre.blit(fond, (0,30))
		niveau.afficher(fenetre)
		fenetre.blit(macgyver.avatar, (macgyver.x, macgyver.y))

		if tube_non_attrape:
			fenetre.blit(tube.image_objet, (tube.x, tube.y))
		if (macgyver.x, macgyver.y) == (tube.x, tube.y):
			tube_non_attrape = False
			fenetre.blit(tube.image_objet, (0,0))

		if ether_non_attrape:
			fenetre.blit(ether.image_objet, (ether.x, ether.y))
		if (macgyver.x, macgyver.y) == (ether.x, ether.y):
			ether_non_attrape = False
			fenetre.blit(ether.image_objet, (10,0))

		if aiguille_non_attrape:
			fenetre.blit(aiguille.image_objet, (aiguille.x, aiguille.y))
		if (macgyver.x, macgyver.y) == (aiguille.x, aiguille.y):
			aiguille_non_attrape = False
			fenetre.blit(aiguille.image_objet, (40,0))

		
		
		
		pygame.display.flip()

		if niveau.structure[macgyver.case_y][macgyver.case_x] == "a":
			if tube_non_attrape == False and ether_non_attrape == False and aiguille_non_attrape == False:
				gagne = True
			else:
				perdu = True


		if gagne == True:
			fenetre.blit(fond, (0,0))
			font = pygame.font.Font(None, 30)
			texte = font.render("Bravo! Tu as gagné!!!", 1, (255,255,255))
			texte_rect= texte.get_rect()
			texte_rect.centerx = cote_fenetre / 2
			texte_rect.centery = cote_fenetre / 2
			fenetre.blit(texte, texte_rect)


		if perdu == True:
			fenetre.blit(fond, (0,0))
			font = pygame.font.Font(None, 30)
			texte = font.render("PERDU", 1, (255,255,255))
			texte_rect= texte.get_rect()
			texte_rect.centerx, texte_rect.centery = cote_fenetre / 2, cote_fenetre / 2
			fenetre.blit(texte, texte_rect)


		pygame.display.flip()







		
		



