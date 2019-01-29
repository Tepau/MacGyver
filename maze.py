#!/usr/bin/env python
# coding: utf-8

'''Class for generate and display the maze'''
import random
import pygame

from constantes import (SPRITE_SIZE, ETHER_LETTER,
                        BANNER_SIZE, ARRIVAL_IMAGE,
                        WALL_IMAGE, ETHER_IMAGE,
                        NEEDLE_IMAGE, TUBE_IMAGE,
                        NEEDLE_LETTER, TUBE_LETTER,
                        )


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
