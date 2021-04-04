""" April 3, 2021 """

"""
Background objects are like painted scenery.
They cannot be interacted with by the rest of the game.
"""

import pygame
from setup.settings import Settings
pygame.init()

class Background:
    def __init__(self, win):
        self.win = win
        self.set = Settings()

        ## Rod width and height
        self.w = self.set.rod_w
        self.h = self.set.rod_h

        ## Start y coordinates for first rod
        self.rods_bottom = self.set.anchor_ring_y + self.w
        self.y = self.rods_bottom - self.h    ## Top of rods

        ## Spans
        self.gap = self.set.gap_between_rods
        self.bottom_bar_w = (3 * self.gap) + self.w

        self.colour = self.set.light_grey_object_538
        self.font_colour = self.set.grey
        self.de_colour = self.set.light_red
        self.vers_colour = self.set.object2_538
        self.rod_border_colour = self.set.white

        self.names = list("ABC")



    # def draw(self, de, vers):
    def draw(self, rods):
        # """ Passes 'de' and 'vers' as ints -- to mark rods """
        """ Passes list containing rod objects -- to determine 'de' and 'vers' states -- to mark rods """
        self.draw_page_border()
        self.draw_rods_bottom_bar()
        self.draw_rods(rods)


    def draw_rods(self, rods):
        """ Draw 3 rods and their labels -- is passed 3 rod objects """
        for i, rod in enumerate(rods):
            state_name, c = self.get_state(rod)
            x = self.set.rod_x_coords[i]

            pygame.draw.rect(self.win, c, pygame.Rect(x, self.y, self.w, self.h)) ## Draw bar
            pygame.draw.rect(self.win, self.rod_border_colour, pygame.Rect(x, self.y, self.w, self.h), 1) # Draw bar outline

            self.draw_rod_labels(x, i, state_name)


    def get_state(self, rod):

        ### For sure I could use my named tuple here, but going to do a more proven way first
        if rod.get_state() == "de":
            return "From", self.de_colour

        if rod.get_state() == "vers":
            return "  To", self.vers_colour

        return "Extra", self.colour


    def draw_rods_bottom_bar(self):
        """ A visual base -- rods appear to be mounted on it """
        x = self.set.left_edge
        y = self.rods_bottom + 1
        w = self.bottom_bar_w
        h = self.w  ## Rotated 90° from rods, so bottom bar h = rod w

        pygame.draw.rect(self.win, self.colour, pygame.Rect(x, y, w, h))


    def draw_rod_labels(self, master_x, i, state_name):
        """ Dynamic state names 'de', 'aux', 'vers' | Fixed names: 'A', 'B', 'C' """

        ## Draw state name above rod
        x = master_x - 5
        y = self.y - 30
        state_name_text = self.set.med_font.render(state_name, True, self.font_colour)
        self.win.blit( state_name_text, (x, y))

        ## Draw fixed name below rod
        x = master_x + 7
        y = self.rods_bottom + self.w + 5
        fixed_name_text = self.set.rod_name_font.render(self.names[i], True, self.font_colour)
        self.win.blit( fixed_name_text, (x, y))


    def draw_page_border(self):
        """ Draw rectangle around the entire page to give it an edge """

        x, y = self.set.left_border, self.set.top_border
        w, h = self.set.border_w, self.set.border_h
        c, thick = self.set.border_colour, self.set.border_thickness

        pygame.draw.rect(self.win, c, pygame.Rect(x, y, w, h), thick)
