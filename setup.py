from cx_Freeze import setup, Executable

setup(
	name = "Maze Mac Gyver" ,
	version = "0.1" ,
	description = "Projet 3 OC" ,
	executables = [Executable("labyrinthe.py")("n1")("/Ressources")]
	)