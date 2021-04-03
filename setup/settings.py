""" March 27, 2021 """

import pygame
from collections import namedtuple
import numpy as np

class Settings:

    def __init__(self):

        self.win_w = 1500
        self.win_h = 800

        self.FPS = 60

        self.white, self.black = (255, 255, 255), (0, 0, 0)
        self.light_grey, self.grey, self.dark_grey = (150, 150, 150), (100,100,100), (45, 45, 45)
        self.blue, self.light_blue = (190, 170, 255), (164, 150, 255),
        self.red, self.light_red = (235, 52, 52), (255, 175, 175)
        self.green = (35, 130, 60)

        ### COLOUR STYLES ###
        self.object1_538 = (217, 240, 222)
        self.object2_538 = (255, 234, 217)
        self.light_grey_object_538 = (221, 221, 221)

        ### Fonts ###
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

        ### Rods
        """
        Two anchor positions -- all else is relative to these:
            - left_edge: an x coordinate for the start of the base_plate of the rods
            - bottom_ring_y: a y coordinate for the top of the bottom ring.
        """
        self.left_edge = 100 # x coordinate
        self.anchor_ring_y = 600
        self.gap_between_rods = 300

        ### Rod ID's
        self.rod_attributes = self.get_rod_attributes()

        ## Other settings
        self.rod_h = 400
        self.rod_w = 20

        ### Rings
        self.ring_max_w = self.gap_between_rods - 50
        self.ring_widths = self.get_ring_widths()
        self.ring_y_coords = self.get_ring_y_coords()

        ## Lookups
        self.rod_x_coords = self.get_rod_x_coords() ## lookup of left edges of rods
        self.rod_x_spans = self.get_rod_x_spans() ## For snapping rings to new rods


    def get_rod_attributes(self):
        """ Returns named tuple for easy lookups of static rod attributes """
        rods_nt = namedtuple("rod_ids", ["labels", "ids", "states"])

        labels = ['a', 'b', 'c']
        ids = [0, 1, 2]
        states = ['de', 'aux', 'vers']

        return rods_nt(labels, ids, states)


    def get_rod_x_coords(self):

        x1 = self.left_edge + (self.gap_between_rods // 2) + (self.rod_w // 2)
        gap = self.gap_between_rods

        x_coords = [x1 + (gap*x) for x in range(3)]

        return tuple(x_coords)


    def get_ring_y_coords(self):
        """ Lookup: lets rings get their y coord based on their order on the rod """

        ring_y = [self.anchor_ring_y - (self.rod_w * x) for x in range(10)]
        return tuple(ring_y)


    def get_ring_widths(self):
        """ Lookup: provides pixel-width of rings when initialized """

        ring_w = [self.ring_max_w * x for x in np.arange(1, 0, -0.1)]
        return tuple(ring_w)


    def get_rod_x_spans(self):
        """ Lookup: for a moving ring, which rod is it close to """

        left_span =  (self.rod_w // 2) - (self.ring_max_w // 2)
        right_span = (self.rod_w // 2) + (self.ring_max_w // 2)

        spans = [(x + left_span, x + right_span) for x in self.rod_x_coords]

        return tuple(spans)
