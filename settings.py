""" March 27, 2021 """


import pygame

class Settings:

    def __init__(self):

        self.win_w = 1500
        self.win_h = 800

        self.FPS = 60

        self.white, self.black = (255, 255, 255), (0, 0, 0)
        self.light_grey, self.grey, self.dark_grey = (200, 200, 200), (100,100,100), (45, 45, 45)
        self.blue,  = (164, 150, 255),
        self.red, self.light_red = (235, 52, 52), (255, 175, 175)
        self.green = (35, 130, 60)

        """ COLOUR STYLES """
        ### 538 white colour style
        self.object1_538 = (217, 240, 222)
        self.object2_538 = (255, 234, 217)
        self.light_grey_object_538 = (221, 221, 221)

        """ COLOUR PALLETT """
        self.screen_background_colour = self.white
        self.instructions_font_colour = self.light_grey

        ## Font
        self.small_font_size = 10
        self.med_font_size = 12
        self.small_font = pygame.font.SysFont('lucidasans', 10)
        self.med_font = pygame.font.SysFont('lucidasans', 12)
        self.rod_name_font = pygame.font.SysFont('lucidasans', 14)

        ## Pager border
        self.border_gap = .03 ## In percent
        self.left_border = self.win_w * self.border_gap
        self.top_border = self.win_h * self.border_gap
        self.bottom_border = self.win_h * (1 - self.border_gap)

        self.border_w = self.win_w * (1 - (2 * self.border_gap))
        self.border_h = self.win_h * (1 - (2 * self.border_gap))

        self.border_colour = self.light_grey
        self.border_thickness = 4

        ## Rods
        """
        Two anchor positions that all else anchor off off:
        - left_edge: an x coordinate for the start of the base_plate of the rods
        - bottom_ring_y: a y coordinate for the top of the bottom ring.
            - All else is relative to this ring
            - Important to anchor to this because a lot of calculations for ring stacking
        """
        ### Anchor coordinatess
        self.left_edge = 100 # x coordinate
        self.anchor_ring_y = 700

        ## Other settings
        self.rod_h = 400
        self.ring_max_w = 250
        self.gap_between_rods = self.ring_max_w + 50

        self.rod_x_coords = self.get_rod_x_coords()


    def get_rod_x_coords(self):
        x = self.left_edge + (self.gap_between_rods // 2)
        x_coords = [x]

        for _ in range(2):
            x += self.gap_between_rods
            x_coords.append(x)

        return x_coords
