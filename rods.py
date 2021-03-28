""" March 27, 2021 """

import pygame
from settings import Settings
pygame.init()


class Rods:
    def __init__(self, win):
        self.win = win
        self.set = Settings()

        ## Rod width and height
        self.w = 20
        self.h = self.set.rod_h

        self.gap = self.set.gap_between_rods

        ## Start coordinates for first rod
        self.rod_x_coords = self.set.rod_x_coords
        self.y = self.set.anchor_ring_y - self.h

        self.colour = (150, 150, 150) #self.set.light_grey_object_538
        self.de_colour = self.set.light_red #light_grey_object_538
        self.vers_colour = self.set.object2_538

        self.names = list("ABC")

    def draw(self, de, vers):
        """
        is passed int for de and vers to colour those
        """

        ## Draw horizontal bar at bottom
        x = self.set.left_edge
        y = self.y + self.h - self.w - 1 # -1 for width of rod border
        w = 3 * self.gap + self.w
        pygame.draw.rect(self.win, self.colour, pygame.Rect(x, y, w, self.w))


        ## Draw rods and their labels
        for i in range(3):
            state_name, c = self.get_rod_state(de, vers, i)
            x = self.rod_x_coords[i]

            pygame.draw.rect(self.win, c, pygame.Rect(x, self.y, self.w, self.h))
            pygame.draw.rect(self.win, self.set.white, pygame.Rect(x, self.y, self.w, self.h), 1)

            self.draw_rod_labels(x, i, state_name, c)



    def draw_rod_labels(self, master_x, i, state_name, c):
        """
        Rods are permanently named 'A', 'B', and 'C'.
        Rods temporarily take on states and state names: 'de', 'vers' 'aux'
        """

        ## Draw state name
        x = master_x - 5
        y = self.y - 40
        draw_state_name = self.set.med_font.render(state_name, True, c)
        self.win.blit( draw_state_name, (x, y))

        ## Draw permanent name
        x = master_x + 6 ## Centre on rod
        y = self.y + self.h + 6
        draw_name = self.set.rod_name_font.render(self.names[i], True, self.colour)
        self.win.blit( draw_name, (x, y))



    ## Helper func
    def get_rod_state(self, de, vers, i):

        if i == de:
            state_name = "  de"
            c = self.de_colour

        elif i == vers:
            state_name = "vers"
            c = self.vers_colour

        else:
            state_name = " aux"
            c = self.colour

        return state_name, c
