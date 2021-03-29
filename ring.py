""" March 27, 2021 """

import pygame
from settings import Settings
pygame.init()


class Ring:
    def __init__(self, win, w, name):
        self.win = win
        self.set = Settings()

        self.colour = self.set.blue
        self.name = name ## Integer name

        ## Coordinates and size
        self.rod_x_coords = self.set.rod_x_coords

        self.size = self.set.ring_max_w * w ## W is a percent
        self.w = self.size ## Same things, but used for different purposes
        self.h = self.set.rod_w ## -1 so I can draw a border on it

        ## To centre ring on any rod
        self.half_ring = self.w // 2
        self.half_rod = self.set.rod_w // 2

        # Flags
        self.active = False
        self.final_pos = False

        self.hovering = False
        self.moving = False


    def get_size(self):
        return self.size


    def draw(self, y, rod):
        x = self.get_ring_x(rod)

        pygame.draw.rect(self.win, self.colour, pygame.Rect(x, y, self.w, self.h))
        pygame.draw.rect(self.win, self.set.white, pygame.Rect(x, y, self.w, self.h), 1)

        self.draw_ring_name(rod, y)


    def draw_ring_name(self, rod, y):
        x = self.rod_x_coords[rod] + 5
        #y += 2
        ring_name = str(self.name)

        draw_name = self.set.med_font.render(ring_name, True, self.set.white)
        self.win.blit( draw_name, (x, y))



    def get_ring_x(self, rod):
        """
        To centre ring on rod, get left side of rod and adjust two ways:
            - Right by half the rod's width
            - Left by half the ring's width
        """
        x = self.rod_x_coords[rod]
        return x + self.half_rod - self.half_ring
