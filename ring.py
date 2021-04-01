""" March 27, 2021 """

import pygame
from settings import Settings
pygame.init()


class Ring:
    def __init__(self, win, id):
        self.win = win
        self.set = Settings()
        self.rod = None
        self.id = id

        ## Colours
        self.colour = self.set.blue
        self.hover_colour = self.set.light_blue

        ## Coordinates and size

        self.x = 1000 ## Temp
        self.y = 1000 ## Temp
        self.w = self.set.ring_widths[self.id]
        self.h = self.set.rod_w ## -1 so I can draw a border on it

        self.id_x = 1000 ## Temp

        ## To centre ring on any rod
        self.half_ring = self.w // 2
        self.half_rod = self.set.rod_w // 2

        ## Flags
        self.hovering = False
        self.moving = False


    ### Main body of class ###

    ### Moving ###
    def check_moving(self, top_ring):
        if self.hovering:
            if self.y == self.set.ring_y_coords[top_ring]:
                self.moving = True


    def cancel_moving(self):
        self.moving = False


    def move(self):
        if self.moving:
            mx, my = pygame.mouse.get_pos()
            self.x = self.update_rod_x(mx)
            self.y = my


    def get_size(self):
        return self.w


    def update_rod(self, rod, pos):
        ### Update X -- Centre ring on rod -- adjust for ring's w and rod's w
        self.rod = rod
        x = self.set.rod_x_coords[self.rod]
        self.x = self.update_rod_x(x)

        ### Update Y
        self.y = self.set.ring_y_coords[pos]


    def update_rod_x(self, x):
        self.id_x = x + 5
        return x - self.half_ring + self.half_rod





    """ Foundation stuff -- don't need to change it """

    def check_hovering(self, mx, my):
        self.hovering = False
        x = y = False

        if mx >= self.x and mx <= self.x + self.w:
            x = True

        if my >= self.y and my <= self.y + self.h:
            y = True

        if x and y:
            self.hovering = True


    def draw(self):

        x = self.x
        y = self.y
        colour = self.colour

        if self.hovering:
            colour = self.hover_colour

        pygame.draw.rect(self.win, colour, pygame.Rect(x, y, self.w, self.h))
        pygame.draw.rect(self.win, self.set.white, pygame.Rect(x, y, self.w, self.h), 1)

        self.draw_ring_id(y)

    def draw_ring_id(self, y):
        #ring_id = str(self.id)
        ring_id = str(self.y)
        colour = self.set.white

        draw_name = self.set.med_font.render(ring_id, True, colour)
        self.win.blit( draw_name, (self.id_x, y))
