# -*- coding: Utf-8 -*
'''Maze game
The goal is to get Mac Gyver out of the maze
To win he must pick up 3 items that will allow him to create a syringe
to lull the guard that protects the exit.

files : constantes.py , classes.py , n1 , /Ressources'''

import pygame
from pygame.locals import (QUIT, K_DOWN,
                           K_ESCAPE, K_RIGHT,
                           K_LEFT, K_UP,
                           K_RETURN, KEYDOWN)

from classes import *
from constantes import *

pygame.init()

#Open Pygame WINDOW
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Window Icon
ICON = pygame.image.load(ICON_IMAGE)
pygame.display.set_icon(ICON)

#Window titile
pygame.display.set_caption(WINDOW_TITLE)

#Load game images
HOME = pygame.image.load(HOME_IMAGE).convert()
BACKGROUND = pygame.image.load(BACKGROUND_IMAGE).convert()
AVATAR = pygame.image.load(AVATAR_IMAGE).convert_alpha()
ETHER = pygame.image.load(ETHER_IMAGE).convert_alpha()
NEEDLE = pygame.image.load(NEEDLE_IMAGE).convert_alpha()
TUBE = pygame.image.load(TUBE_IMAGE).convert_alpha()
SYRINGE = pygame.image.load(SYRINGE_IMAGE).convert_alpha()
BANDEAU = pygame.image.load(BANDEAU_IMAGE).convert()

pygame.key.set_repeat(100, 30)
MAIN_LOOP = 1

#Booleens used to define which object is caught or not
TUBE_CATCH = False
ETHER_CATCH = False
NEEDLE_CATCH = False

#Main loop of the game
while MAIN_LOOP:

    #Display home screen
    WINDOW.blit(HOME, (0, 30))
    #Print text on home screen
    FONT = pygame.font.Font(None, 30)
    TEXT_HOME = FONT.render\
                ("Press ENTER to continue or ECHAP to quit", 1, (0, 0, 0))
    WINDOW.blit(TEXT_HOME, (20, 40))

    #Refresh the screen
    pygame.display.flip()

    CONTINUE_HOME = 1
    CONTINUE_GAME = 1

    #Home loop
    while CONTINUE_HOME:

        #Speeed limitation for the loop
        pygame.time.Clock().tick(30)

        #If user quit the program stops
        for event in pygame.event.get():
            if event.type == QUIT\
            or event.type == KEYDOWN and event.key == K_ESCAPE:
                MAIN_LOOP = 0
                CONTINUE_HOME = 0
                CONTINUE_GAME = 0

            #If user presses "Enter", the maze starts
            elif event.type == KEYDOWN and event.key == K_RETURN:
                CONTINUE_HOME = 0

        pygame.display.flip()


    MAZE = Maze()
    MAZE.display(WINDOW)
    MACGYVER = Character(AVATAR, MAZE)

    #Game loop
    while CONTINUE_GAME:

        pygame.time.Clock().tick(30)
        #Loading background and a text zone for inventory
        FONT = pygame.font.Font(None, 25)
        INVENTORY = FONT.render\
        (MACGYVER.display_inventory(), 1, (255, 255, 255)) # Display the text
        INVENTORY.fill((0, 0, 0))
        WINDOW.blit(INVENTORY, (0, 5))
        INVENTORY = FONT.render\
        (MACGYVER.display_inventory(), 1, (255, 255, 255))
        WINDOW.blit(INVENTORY, (0, 5))


        #If user quit we come-back at home
        for event in pygame.event.get():
            if event.type == QUIT\
            or event.type == KEYDOWN and event.key == K_ESCAPE:
                CONTINUE_GAME = 0
                CONTINUE_HOME = 0
                MAIN_LOOP = 0

            #Directional keys are used to move Mac Gyver
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    MACGYVER.move("right")
                elif event.key == K_LEFT:
                    MACGYVER.move("left")
                elif event.key == K_DOWN:
                    MACGYVER.move("down")
                elif event.key == K_UP:
                    MACGYVER.move("up")

        WINDOW.blit(BACKGROUND, (0, 30))
        MAZE.display(WINDOW)
        WINDOW.blit(MACGYVER.avatar, (MACGYVER.x_item, MACGYVER.y_item))

        if MAZE.structure_map[MACGYVER.case_y][MACGYVER.case_x] == TUBE_LETTER:
            MACGYVER.erase()
            MACGYVER.add_inventory()
            TUBE_CATCH = True
            WINDOW.blit(TUBE, (360, 0))

        if MAZE.structure_map[MACGYVER.case_y][MACGYVER.case_x] == NEEDLE_LETTER:
            MACGYVER.erase()
            MACGYVER.add_inventory()
            NEEDLE_CATCH = True
            WINDOW.blit(NEEDLE, (330, 0))

        if MAZE.structure_map[MACGYVER.case_y][MACGYVER.case_x] == ETHER_LETTER:
            MACGYVER.erase()
            MACGYVER.add_inventory()
            ETHER_CATCH = True
            WINDOW.blit(ETHER, (300, 0))

        if MACGYVER.inventory == 3:
            WINDOW.blit(BANDEAU, (300, 0))
            WINDOW.blit(SYRINGE, (310, 0))

        #If the users move to the guard position, the game is over
        if MAZE.structure_map[MACGYVER.case_y][MACGYVER.case_x] == "a":

            #If user has found all the objects we print the victory screen
            if MACGYVER.inventory == 3:

                WINDOW.blit(BACKGROUND, (0, 30))
                FONT = pygame.font.Font(None, 30)
                TEXT_VICTORY = FONT.render\
                               (" Well done! Mac Gyver is safe!!",\
                               1, (255, 255, 255))
                TEXT_EXIT = FONT.render(TEXT_END, 1, (0, 0, 0))
                WINDOW.blit(TEXT_VICTORY, (65, 225))
                WINDOW.blit(TEXT_EXIT, (65, 430))
                for event in pygame.event.get():
                    if event.type == QUIT\
                    or event.type == KEYDOWN and event.key == K_ESCAPE:
                        CONTINUE_GAME = 0
                        CONTINUE_HOME = 0
                        MAIN_LOOP = 0

            else:
                #If user didn't find the tube
                if TUBE_CATCH is False\
                and ETHER_CATCH is True\
                and NEEDLE_CATCH is True:
                    FONT = pygame.font.Font(None, 30)
                    TEXT_DEFEAT = FONT.render\
                                  ("Game over! You didn't find the tube!",\
                                  1, (255, 255, 255))
                    TEXT_EXIT = FONT.render\
                                (TEXT_END,\
                                1, (0, 0, 0))

                #If user didn't find the ether
                elif ETHER_CATCH is False\
                and TUBE_CATCH is True\
                and NEEDLE_CATCH is True:
                    FONT = pygame.font.Font(None, 25)
                    TEXT_DEFEAT = FONT.render\
                                  ("Game Over! You didn't find the bottle of ether!",\
                                  1, (255, 255, 255))
                    TEXT_EXIT = FONT.render\
                                (TEXT_END,\
                                1, (0, 0, 0))

                #If user didn't find the needle
                elif NEEDLE_CATCH is False\
                and ETHER_CATCH is True\
                and TUBE_CATCH is True:
                    FONT = pygame.font.Font(None, 30)
                    TEXT_DEFEAT = FONT.render\
                                  ("Game Over! You didn't find the needle!",\
                                  1, (255, 255, 255))
                    TEXT_EXIT = FONT.render\
                                (TEXT_END,\
                                1, (0, 0, 0))

                #If user didn't find the tube and the ether
                elif TUBE_CATCH is False\
                and ETHER_CATCH is False\
                and NEEDLE_CATCH is True:
                    FONT = pygame.font.Font(None, 25)
                    TEXT_DEFEAT = FONT.render\
                                  ("Game Over! You didn't find the tube and the ether!",\
                                  1, (255, 255, 255))
                    TEXT_EXIT = FONT.render\
                                (TEXT_END,\
                                1, (0, 0, 0))

                #If user didn't find the tube and the needle
                elif TUBE_CATCH is False\
                and NEEDLE_CATCH is False\
                and ETHER_CATCH is True:
                    FONT = pygame.font.Font(None, 25)
                    TEXT_DEFEAT = FONT.render\
                                  ("Game Over! You didn't find the tube and the needle!",\
                                  1, (255, 255, 255))
                    TEXT_EXIT = FONT.render\
                                (TEXT_END,\
                                1, (0, 0, 0))

                #If user didn't find the ether and the needle
                elif ETHER_CATCH is False\
                and NEEDLE_CATCH is False\
                and TUBE_CATCH is True:
                    FONT = pygame.font.Font(None, 25)
                    TEXT_DEFEAT = FONT.render\
                                  ("Game Over! You didn't find the ether and the needle!",\
                                  1, (255, 255, 255))
                    TEXT_EXIT = FONT.render\
                                (TEXT_END,\
                                1, (0, 0, 0))

                #If user didn't find anything
                elif ETHER_CATCH is False\
                and NEEDLE_CATCH is False\
                and TUBE_CATCH is False:
                    FONT = pygame.font.Font(None, 30)
                    TEXT_DEFEAT = FONT.render\
                                  ("Game Over! You have not found anything!",\
                                  1, (255, 255, 255))
                    TEXT_EXIT = FONT.render\
                                (TEXT_END,\
                                1, (0, 0, 0))

                WINDOW.blit(BACKGROUND, (0, 30))
                WINDOW.blit(TEXT_DEFEAT, (10, 225))
                WINDOW.blit(TEXT_EXIT, (65, 430))
                for event in pygame.event.get():
                    if event.type == QUIT\
                    or event.type == KEYDOWN and event.key == K_ESCAPE:
                        CONTINUE_GAME = 0
                        CONTINUE_HOME = 0
                        MAIN_LOOP = 0

        pygame.display.flip()
