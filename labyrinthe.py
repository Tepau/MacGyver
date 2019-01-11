# -*- coding: Utf-8 -*

import pygame
from pygame.locals import *

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

tube_catch = False
ether_catch = False
needle_catch = False

#Main loop of the game
while MAIN_LOOP:

    #Display home screen
    WINDOW.blit(HOME, (0, 30))
    WINDOW.blit(BANDEAU, (0, 0))

    #Print text on home screen
    FONT = pygame.font.Font(None, 30)
    TEXT_HOME = FONT.render\
                ("Press ENTER to continue or ECHAP to quit", 1, (0, 0, 0))
    TEXT_RECT = TEXT_HOME.get_rect()
    TEXT_RECT.centerx = SCREEN_WIDTH / 2
    TEXT_RECT.centery = SCREEN_HEIGHT / 9
    WINDOW.blit(TEXT_HOME, TEXT_RECT)

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
        #Loading background and a text zone for inventory
        FONT = pygame.font.Font(None, 25)
        INVENTORY = FONT.render(MACGYVER.display_inventory(), 1, (255, 255, 255)) # Display the text
        INVENTORY.fill((0, 0, 0))
        WINDOW.blit(INVENTORY, (0, 5))
        INVENTORY = FONT.render(MACGYVER.display_inventory(), 1, (255, 255, 255))
        WINDOW.blit(INVENTORY, (0, 5))

        WINDOW.blit(BACKGROUND, (0, 30))
        MAZE.display(WINDOW)
        WINDOW.blit(MACGYVER.avatar, (MACGYVER.x_item, MACGYVER.y_item))




        #If user quit the program stops
        for event in pygame.event.get():
            if event.type == QUIT\
            or event.type == KEYDOWN and event.key == K_ESCAPE:
                CONTINUE_GAME = 0


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


        if MAZE.structure_map[MACGYVER.case_y][MACGYVER.case_x] == TUBE_LETTER:
            MACGYVER.erase()
            MACGYVER.add_inventory()
            tube_catch = True
            WINDOW.blit(TUBE, (360, 0))

        if MAZE.structure_map[MACGYVER.case_y][MACGYVER.case_x] == NEEDLE_LETTER:
            MACGYVER.erase()
            MACGYVER.add_inventory()
            needle_catch = True
            WINDOW.blit(NEEDLE, (330, 0))

        if MAZE.structure_map[MACGYVER.case_y][MACGYVER.case_x] == ETHER_LETTER:
            MACGYVER.erase()
            MACGYVER.add_inventory()
            ether_catch = True
            WINDOW.blit(ETHER, (300, 0))

        if MACGYVER.inventory == 3:
            WINDOW.blit(BANDEAU, (300, 0))
            WINDOW.blit(SYRINGE, (310, 0))


        #If the users move to the guard position, the game is over
        if MAZE.structure_map[MACGYVER.case_y][MACGYVER.case_x] == "a":
            CONTINUE_GAME = 0
            CONTINUE_HOME = 0
            MAIN_LOOP = 0

            #If user has found all the objects we print the victory screen
            if MACGYVER.inventory == 3:
                WINDOW.blit(BACKGROUND, (0, 30))
                FONT = pygame.font.Font(None, 30)
                TEXT_VICTORY = FONT.render\
                               ("Bravo! Tu as gagné!!!", 1, (255, 255, 255))
                TEXT_RECT = TEXT_VICTORY.get_rect()
                TEXT_RECT.centerx = SCREEN_WIDTH / 2
                TEXT_RECT.centery = SCREEN_HEIGHT / 2
                WINDOW.blit(TEXT_VICTORY, TEXT_RECT)




            #Contrary the game is loose
            else:
                if tube_catch == False\
                and ether_catch == True\
                and needle_catch == True :
                    WINDOW.blit(BACKGROUND, (0, 30))
                    FONT = pygame.font.Font(None, 30)
                    TEXT_DEFEAT = FONT.render\
                                  ("Perdu tu n'as pas trouvé le tube",\
                                  1, (255, 255, 255))
                    
                elif ether_catch == False\
                and tube_catch == True\
                and needle_catch == True:
                    WINDOW.blit(BACKGROUND, (0, 30))
                    FONT = pygame.font.Font(None, 30)
                    TEXT_DEFEAT = FONT.render\
                                  ("Perdu tu n'as pas trouvé l'ether",\
                                  1, (255, 255, 255))
                    
                elif needle_catch == False\
                and ether_catch == True\
                and tube_catch == True:
                    WINDOW.blit(BACKGROUND, (0, 30))
                    FONT = pygame.font.Font(None, 30)
                    TEXT_DEFEAT = FONT.render\
                                  ("Perdu tu n'as pas trouvé l'aiguille",\
                                  1, (255, 255, 255))
                
                elif tube_catch == False\
                and ether_catch == False\
                and needle_catch == True:
                    WINDOW.blit(BACKGROUND, (0, 30))
                    FONT = pygame.font.Font(None, 30)
                    TEXT_DEFEAT = FONT.render\
                                  ("Perdu tu n'as pas trouvé le tube et l'ether",\
                                  1, (255, 255, 255))
                    
                elif tube_catch == False\
                and needle_catch == False\
                and ether_catch == True:
                    WINDOW.blit(BACKGROUND, (0, 30))
                    FONT = pygame.font.Font(None, 30)
                    TEXT_DEFEAT = FONT.render\
                                  ("Perdu tu n'as pas trouvé le tube et l'aiguille",\
                                  1, (255, 255, 255))
                    
                elif ether_catch == False\
                and needle_catch == False\
                and tube_catch == True:
                    WINDOW.blit(BACKGROUND, (0, 30))
                    FONT = pygame.font.Font(None, 30)
                    TEXT_DEFEAT = FONT.render\
                                  ("Perdu tu n'as pas trouvé l'ether et l'aiguille",\
                                  1, (255, 255, 255))
                    
                elif ether_catch == False\
                and needle_catch == False\
                and tube_catch == False:
                    WINDOW.blit(BACKGROUND, (0, 30))
                    FONT = pygame.font.Font(None, 30)
                    TEXT_DEFEAT = FONT.render\
                                  ("Perdu tu n'as trouvé aucun objet",\
                                  1, (255, 255, 255))
                
                TEXT_RECT = TEXT_DEFEAT.get_rect()
                TEXT_RECT.centerx = SCREEN_WIDTH / 2
                TEXT_RECT.centery = SCREEN_HEIGHT / 2
                WINDOW.blit(TEXT_DEFEAT, TEXT_RECT) 
                

        pygame.display.flip()
