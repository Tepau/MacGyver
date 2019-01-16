import sys

from cx_Freeze import setup, Executable

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# options for the build
build_exe_options = dict(
    include_files = ["Ressources", "n1"]
)

setup(
    name = "Maze_Mac_Gyver",
    version = "0.1",
    description = "Projet 3 OC",
    author = "Malau",
    executables = [Executable("labyrinthe.py", base = base)],
    options = dict(build_exe = build_exe_options)
)