# LABYRINTHE MAC GYVER

Exercice du Projet n°3 du parcours développeur Python Openclassrooms


Mac Gyver est enfermé dans un labyrinthe. Pour s'échapper il doit ramasser 3 objets qui lui permettront de confectionner une seringue afin d'endormir le garde qui protège la sortie.

## Fonctionnalités 

Un seul niveau : la structure est enregistrée dans un fichier à part pour la modifier facilement

La fenêtre du jeu est un carré affichant 15 sprites sur la longueur

Mac Gyver se déplace de case en case à l'aide des touches directionnelles du clavier 

Les objets sont placés de façon aléatoire et changent de place à chaque fois que l'utilisateur relance le jeu

Mac Gyver ramasse un objet en se déplaçant dessus

La sortie du labyrinthe est protégée par un garde

Si Mac Gyver ramasse les 3 objets et se présente devant le garde l’utilisateur gagne

Si il n'a pas ramassé les 3 objets et qu'il se présente devant le garde, la sortie lui est 
refusée et le jeu est perdu.

## Language utilisé 

Python

## Construit avec

Pygame 

## Descriptioon des fichiers

maze.py ==> Fichier de classe
character.py ==> Fichier de classe
constantes.py ==> Fichier contenant ls constantes
n1 ==> Structure du labyrinthe
labyrinthe.py ==> Fichier du jeu, à lancer pour jouer

## Récupération des codes du jeu 

    git clone https://github.com/Tepau/MacGyver

## Installation nécessaire
Se placer dans le répertoire du projet et lancer les commmandes suivantes

    python install.py
    
## Lancement du jeu

    python labyrinthe.py

