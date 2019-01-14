'''Classes module'''
import random
import pygame

from constantes import (NB_SPRITE_SIDE, SPRITE_SIZE,
                        BANNER_SIZE, ARRIVAL_IMAGE,
                        WALL_IMAGE, ETHER_IMAGE,
                        NEEDLE_IMAGE, TUBE_IMAGE,
                        NEEDLE_LETTER, TUBE_LETTER,
                        ETHER_LETTER)

class Maze:
    '''Define the maze strcture. Two methods

    to create and display.

    '''
    def __init__(self):

        self.inventory = 0
        self.structure_map = self.generate()

    def generate(self):
        '''create the maze structure from a external file. And

        places 3 objects randomly in the maze.
        '''
        with open("n1", "r") as file:
            structure_maze = []
            for ligne in file:
                ligne_maze = []
                for letter in ligne:
                    if letter != "\n":
                        ligne_maze.append(letter)
                structure_maze.append(ligne_maze)

        while self.inventory < 3:

            x_item = random.randint(0, 14)
            y_item = random.randint(0, 14)
            if structure_maze[y_item][x_item] == "0":
                if self.inventory == 0:
                    structure_maze[y_item][x_item] = NEEDLE_LETTER
                elif self.inventory == 1:
                    structure_maze[y_item][x_item] = TUBE_LETTER
                elif self.inventory == 2:
                    structure_maze[y_item][x_item] = ETHER_LETTER

                self.inventory += 1
                self.structure_map = structure_maze

        return structure_maze



    def display(self, window):
        '''Display the maze structure

        by displaying walls and the arrival of the maze'''
        tube = pygame.image.load(TUBE_IMAGE).convert_alpha()
        needle = pygame.image.load(NEEDLE_IMAGE).convert_alpha()
        ether = pygame.image.load(ETHER_IMAGE).convert_alpha()
        wall = pygame.image.load(WALL_IMAGE).convert()
        arrival = pygame.image.load(ARRIVAL_IMAGE).convert_alpha()
        num_ligne = 0
        for ligne in self.structure_map:
            num_case = 0
            for sprite in ligne:
                x_sprite = num_case * SPRITE_SIZE
                y_sprite = num_ligne * SPRITE_SIZE + BANNER_SIZE
                if sprite == "m":
                    window.blit(wall, (x_sprite, y_sprite))
                elif sprite == "a":
                    window.blit(arrival, (x_sprite, y_sprite))
                elif sprite == NEEDLE_LETTER:
                    window.blit(needle, (x_sprite, y_sprite))
                elif sprite == TUBE_LETTER:
                    window.blit(tube, (x_sprite, y_sprite))
                elif sprite == ETHER_LETTER:
                    window.blit(ether, (x_sprite, y_sprite))

                num_case += 1
            num_ligne += 1


class Character:
    '''Define movement of the character

    and the inventory of obects picked up

    '''

    def __init__(self, avatar, maze):
        self.avatar = avatar
        self.x_item = 0
        self.y_item = 30
        self.case_x = 0
        self.case_y = 0
        self.maze = maze
        self.inventory = 0

    def move(self, direction):
        '''verified that character can move on the desired case'''

        if direction == "right":
            if self.case_x < (NB_SPRITE_SIDE - 1):
                if self.maze.structure_map[self.case_y][self.case_x + 1] != "m":
                    self.case_x += 1
                    self.x_item = self.case_x * SPRITE_SIZE

        elif direction == "left":
            if self.case_x > 0:
                if self.maze.structure_map[self.case_y][self.case_x - 1] != "m":
                    self.case_x -= 1
                    self.x_item = self.case_x * SPRITE_SIZE

        elif direction == "up":
            if self.case_y > 0\
            and self.maze.structure_map[self.case_y - 1][self.case_x] != "m":
                self.case_y -= 1
                self.y_item = self.case_y * SPRITE_SIZE + BANNER_SIZE

        elif direction == "down":
            if self.case_y < (NB_SPRITE_SIDE - 1):
                if self.maze.structure_map[self.case_y + 1][self.case_x] != "m":
                    self.case_y += 1
                    self.y_item = self.case_y * SPRITE_SIZE + BANNER_SIZE

    def erase(self):
        '''Erase image of the maze when MG passes over it'''

        self.maze.structure_map[self.case_y][self.case_x] = "0"

    def add_inventory(self):
        '''Add the object found in the inventory'''
        self.inventory += 1

    def display_inventory(self):
        '''Display the number of object to find'''
        text = "Objets restant à trouver: {}".format(3 - self.inventory)
        return text
