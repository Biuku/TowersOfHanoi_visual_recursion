""" March 29, 2021 """

"""
I think the rods module will be 'dumb' -- it won't control where rings land on rods, etc.
It will just draw rods, and modify which are the 'de', 'aux' and 'vers' rods.
"""


import pygame
from settings import Settings
pygame.init()


class DrawRods:
    def __init__(self, win):
        self.win = win
        self.set = Settings()

        ## Rod width and height
        self.w = self.set.rod_w
        self.h = self.set.rod_h

        self.gap = self.set.gap_between_rods

        ## Start coordinates for first rod
        self.rod_x_coords = self.set.rod_x_coords
        self.rods_bottom = self.set.anchor_ring_y + self.w
        self.y = self.rods_bottom - self.h    ## Top of rods

        ## Bottom bar width
        self.bottom_bar_w = (3 * self.gap) + self.w

        self.colour = (150, 150, 150) #self.set.light_grey_object_538
        self.de_colour = self.set.light_red #light_grey_object_538
        self.vers_colour = self.set.object2_538

        self.names = list("ABC")



    def draw(self, de, vers):
        """
        Is passed int for de and vers to colour those
        """

        self.draw_bottom_bar()

        ## Draw rods and their labels
        for i in range(3):
            state_name, c = self.get_rod_state(de, vers, i)
            x = self.rod_x_coords[i]

            pygame.draw.rect(self.win, c, pygame.Rect(x, self.y, self.w, self.h)) ## Draw bar
            pygame.draw.rect(self.win, self.set.white, pygame.Rect(x, self.y, self.w, self.h), 1) # Draw bar outline

            self.draw_rod_labels(x, i, state_name, c)


    def draw_bottom_bar(self):
        x = self.set.left_edge
        y = self.rods_bottom + 1
        w = self.bottom_bar_w
        h = self.w  ## it's rotated 90 degrees from rods

        pygame.draw.rect(self.win, self.colour, pygame.Rect(x, y, w, h))


    def draw_rod_labels(self, master_x, i, state_name, c):
        """
        Rods are permanently named 'A', 'B', and 'C'.
        Rods temporarily take on states and state names: 'de', 'vers' 'aux'
        """

        ## Draw state name above rod
        x = master_x - 5
        y = self.y - 30
        draw_state_name = self.set.med_font.render(state_name, True, c)
        self.win.blit( draw_state_name, (x, y))

        ## Draw permanent name
        x = master_x + 6 ## Centre on rod
        y = self.rods_bottom + self.w + 6
        draw_name = self.set.rod_name_font.render(self.names[i], True, self.colour)
        self.win.blit( draw_name, (x, y))


    ## Helper func
    def get_rod_state(self, de, vers, i):

        if i == de:
            return "  de", self.de_colour

        elif i == vers:
            return "vers", self.vers_colour

        else:
            return " aux", self.colour
