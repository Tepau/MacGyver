import pygame
from pygame.locals import *
from constantes import *
import random

class Labyrinthe: 

#Classe permettant de définir le lab
#Cette classe possède deux méthodes. Une qui ouvre le fichier, le lit et enregistre son contenu dans une liste, 
#copiée dans l'attribut structure. 
#L'autre lit cette liste et affiche son contenu à l'écran, elle doit donc être appelée à chaque fois qu'on rafraîchit l'écran !
	
	def __init__(self):
		
		self.structure = 0


	def generer(self):
		with open("n1", "r") as fichier:     #Ouverture du fichier contenant la structure du labyrinthe
			structure_niveau = []				
			for ligne in fichier:			#On parcourt les lignes du fichier
				ligne_niveau = []
				for sprite in ligne:		#On parcourt les lettre contenues dans les lignes du fichier
					if sprite != "\n":		#On ignore les \n contenus dans le fichier	
						ligne_niveau.append(sprite)		#On ajoute les lettres à la liste de la ligne
				structure_niveau.append(ligne_niveau)   # On ajoute les liste de la ligne a la structure du labyrinthe
			self.structure = structure_niveau			# On sauvegarde la structure


	def afficher(self, fenetre):
		mur = pygame.image.load(image_mur).convert()		#Chargement de images symbolisant les murs et la fin du labyrinthe
		arrivee = pygame.image.load(image_arrivee).convert_alpha()
		

		num_ligne = 0
		for ligne in self.structure:				#On parcourt les listes du niveau
			num_case = 0
			for sprite in ligne:					#On parcourt  les listes des lignes
				x = num_case * taille_sprite		#Calcul de la position réelle en pixels
				y = num_ligne * taille_sprite
				if sprite == "m":                   #m = mur
					fenetre.blit(mur, (x,y))
				if sprite == "a":
					fenetre.blit(arrivee, (x,y))    #a = arrivée = garde
				
				num_case += 1
			num_ligne += 1


class Perso:
#Classe Perso. Elle prend en paramètre l'image du personnage et la liste de structure du labyrinthe.
#Cette classe possède une seule méthode, qui s'occupe du déplacement de MG, qu'on appelle à chaque déplacement, 
#avec en paramètre la direction de celui-ci. ('droite', 'gauche', 'haut', 'bas')
#Elle vérifie qu'on ne sort pas de l'écran.
#On enlève 1 à la constante nombre_sprite_cote car la case de MG est elle comptée à partir de 0  
#Elle vérifie que la case de destination est libre en lisant la liste de structure.
#Elle déplace MG d'une case et change sa position réelle en pixel. L'attribut de direction prend la valeur de la direction du déplacement.'''

	def __init__(self, avatar, labyrinthe):
		self.avatar = avatar
		self.x = 0
		self.y = 30					#position du personnages en pixel et en case
		self.case_x = 0
		self.case_y = 1
		self.labyrinthe = labyrinthe #labyrinthe dans lequel se trouve le perso
		

	def deplacer(self, direction):
		if direction == "droite":
			if self.case_x < (nombre_sprite_cote - 1):  #Pour ne pas dépasser l'écran
				if self.labyrinthe.structure[self.case_y][self.case_x + 1] != "m": #on Vérifie que la case de destination n'est pas un mur 
					self.case_x += 1  #déplacement d'une case
					self.x = self.case_x * taille_sprite # Calcul de la nouvelle position en pixel
				


		if direction == "gauche":
			if self.case_x > 0:
				if self.labyrinthe.structure[self.case_y][self.case_x - 1] != "m":
					self.case_x -= 1
					self.x = self.case_x * taille_sprite
				

		if direction == "haut":
			if self.case_y > 0:
				if self.labyrinthe.structure[self.case_y - 1][self.case_x ] != "m":
					if self.labyrinthe.structure[self.case_y - 1][self.case_x] != "x":
						self.case_y -= 1
						self.y = self.case_y * taille_sprite
				

		if direction == "bas":
			if self.case_y < (nombre_sprite_cote):
				if self.labyrinthe.structure[self.case_y + 1][self.case_x] != "m":
					self.case_y += 1
					self.y = self.case_y * taille_sprite
				



class Objet_aleatoire: 


#Classe qui prend en paramètre l'image de l'objet et la liste de structure du labyrinthe
#Elle possède 1 méthode  qui permet de placer l'objet de façon aléatoire dans le labyrinthe
    def __init__(self, image_objet, labyrinthe):
        self.case_y = 0
        self.case_x = 0
        self.x = 0
        self.y = 0
        self.labyrinthe = labyrinthe
        self.loaded = True
        self.image_objet = image_objet

    def afficher(self, image_objet, fenetre):
        while self.loaded:
            self.case_x = random.randint(0, 14) 
            self.case_y = random.randint(0, 14)  
            if self.labyrinthe.structure[self.case_y][self.case_x] == "0": 
                self.y = self.case_y * taille_sprite  
                self.x = self.case_x * taille_sprite
                self.loaded = False  







