# coding: utf-8

'''Class for create a character'''
from constantes import (NB_SPRITE_SIDE, SPRITE_SIZE,
                        BANNER_SIZE)


class Character:
    '''Define movement of the character

    and the inventory of obects picked up

    '''

    def __init__(self, avatar, lab):
        self.avatar = avatar
        self.x_item = 0
        self.y_item = 30
        self.case_x = 0
        self.case_y = 0
        self.lab = lab
        self.inventory = 0

    def move(self, direction):
        '''verified that character can move on the desired case'''

        if direction == "right":
            if self.case_x < (NB_SPRITE_SIDE - 1):
                if self.lab.structure_map[self.case_y][self.case_x + 1] != "m":
                    self.case_x += 1
                    self.x_item = self.case_x * SPRITE_SIZE

        elif direction == "left":
            if self.case_x > 0:
                if self.lab.structure_map[self.case_y][self.case_x - 1] != "m":
                    self.case_x -= 1
                    self.x_item = self.case_x * SPRITE_SIZE

        elif direction == "up":
            if self.case_y > 0:
                if self.lab.structure_map[self.case_y - 1][self.case_x] != "m":
                    self.case_y -= 1
                    self.y_item = self.case_y * SPRITE_SIZE + BANNER_SIZE

        elif direction == "down":
            if self.case_y < (NB_SPRITE_SIDE - 1):
                if self.lab.structure_map[self.case_y + 1][self.case_x] != "m":
                    self.case_y += 1
                    self.y_item = self.case_y * SPRITE_SIZE + BANNER_SIZE

    def erase(self):
        '''Erase image of the lab when MG passes over it and

        increase inventory'''
        self.lab.structure_map[self.case_y][self.case_x] = "0"
        self.inventory += 1

    def display_inventory(self):
        '''Display the number of object to find'''
        text = "Remaining items to find: {}".format(3 - self.inventory)
        return text
