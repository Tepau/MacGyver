from cx_Freeze import setup, Executable

setup(
	name = "LMaze Mac Gyver" ,
	version = "0.1" ,
	description = "Projet 3 OC" ,
	executables = [Executable("labyrinthe.py")]
	)