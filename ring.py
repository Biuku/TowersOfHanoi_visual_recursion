""" March 27, 2021 """

import pygame
from settings import Settings
pygame.init()


class Ring:
    def __init__(self, win, w, name):
        self.win = win
        self.set = Settings()

        self.colour = self.set.blue
        self.hover_colour = self.set.light_blue
        self.name = name ## Integer name

        ## Coordinates and size
        self.rod_x_coords = self.set.rod_x_coords

        self.x = 1000 ## Temporary value
        self.y = 1000 ## Temporary value
        self.size = self.set.ring_max_w * w ## W is a percent
        self.w = self.size ## Same things, but used for different purposes
        self.h = self.set.rod_w ## -1 so I can draw a border on it

        ## To centre ring on any rod
        self.half_ring = self.w // 2
        self.half_rod = self.set.rod_w // 2

        self.hovering = False
        self.moving = False

        ## TRACER
        self.mouse_coords = (1, 1)


    def get_size(self):
        return self.size


    def check_hovering(self, mx, my):
        self.hovering = False

        x = y = False

        if mx >= self.x and mx <= self.x + self.w:
            x = True

        if my >= self.y and my <= self.y + self.h:
            y = True

        if x and y:
            self.hovering = True


    def check_moving(self):
        if self.hovering:
            self.moving = True


    def cancel_moving(self):
        self.moving = False


    def draw(self, y, rod):
        if self.moving:
            self.move()
            return

        x = self.get_ring_x(rod)
        colour = self.colour

        if self.hovering:
            colour = self.hover_colour

        pygame.draw.rect(self.win, colour, pygame.Rect(x, y, self.w, self.h))
        pygame.draw.rect(self.win, self.set.white, pygame.Rect(x, y, self.w, self.h), 1)

        self.draw_ring_name(rod, y)

        ## Update coordinates to check hovering, moving etc.
        self.x = x
        self.y = y


    def move(self):
        mx, my = pygame.mouse.get_pos()
        colour = self.hover_colour

        pygame.draw.rect(self.win, colour, pygame.Rect(mx, my, self.w, self.h))
        pygame.draw.rect(self.win, self.set.white, pygame.Rect(mx, my, self.w, self.h), 1)

        """
        DRAWING RING NAME IS HARD TO DO, WHICH REVEALS AN ISSUE IN MY CODE.
        I NEED TO ALWAYS KEEP AN X AND A Y, AND ANCHOR OFF THAT.

        """
        #ring_name = str(self.name)

        #draw_name = self.set.med_font.render(ring_name, True, self.set.white)
        #self.win.blit( draw_name, (x, y))


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
