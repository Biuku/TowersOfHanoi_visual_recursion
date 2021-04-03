""" March 27, 2021 """

import pygame
from setup.settings import Settings

class Ring:
    def __init__(self, win, id):
        pygame.init()
        self.win = win
        self.set = Settings()
        self.id = id

        ## Positioning
        self.rod = None ## Which of the 3 rods
        self.pos = None ## Position in the rod stack

        ## Flags
        self.hovering = False
        self.moving = False
        self.snap = False ## Flag ring as wanting to move to new rod (unclick after moving)
        self.new_rod = None ## For Main to access the new rod

        ## Colours
        self.colour = self.set.blue
        self.hover_colour = self.set.light_blue

        ## Coordinates
        self.x = self.y = 1000 ## Temp
        self.w = self.set.ring_widths[self.id]
        self.h = self.set.rod_w ## -1 so I can draw a border on it
        self.id_x = 1000 ## Temp

        ## To centre ring on any rod
        #self.half_ring = self.w // 2
        self.half_rod = self.set.rod_w // 2

        ##Lookups
        self.rod_x_coords = self.set.rod_x_coords
        self.rod_x_spans = self.set.rod_x_spans


    ### Main body of class ###

    def update_rod(self, rod, pos):
        """Attaches ring to rod. Used to add ring to rod, and when snapping  back"""

        self.snap = False
        self.new_rod = None

        ### Centre ring on rod
        x = self.rod_x_coords[rod]
        self.x = self.centre_ring(x)

        self.y = self.set.ring_y_coords[pos]
        self.rod, self.pos = rod, pos


    """ MOVING """

    def check_moving(self):
        if self.hovering:
            self.moving = True

    def move(self, mx, my):
        if self.moving:
            self.x = self.centre_ring(mx)
            self.y = my

    def cancel_moving(self):
        """
        - Identifies which rod to snap to after moving.
        - Sets snap flag to True so Main snaps the ring to a rod.
        """

        if self.moving:
            self.new_rod = self.rod # Defaul: snap back to old rod
            mx, _ = pygame.mouse.get_pos()

            for i, rod_coords in enumerate(self.rod_x_spans):
                x1, x2 = rod_coords
                if mx > x1 and mx < x2:
                    self.new_rod = i

            self.moving = False
            self.snap = True


    def centre_ring(self, x):
        """ Used by self.update_rod() and self.move() """
        self.id_x = x + 5
        return x - (self.w // 2) + (self.set.rod_w // 2)


    """ HOVERING """

    def check_hovering(self, mx, my):
        self.hovering = False

        if mx >= self.x and mx <= (self.x + self.w):
            if my >= self.y and my <= (self.y + self.h):
                self.hovering = True


    """ DRAW RING """

    def draw(self):
        x, y = self.x, self.y
        colour = self.colour

        if self.hovering:
            colour = self.hover_colour

        pygame.draw.rect(self.win, colour, pygame.Rect(x, y, self.w, self.h))
        pygame.draw.rect(self.win, self.set.white, pygame.Rect(x, y, self.w, self.h), 1)

        self.draw_ring_id(y)

    def draw_ring_id(self, y):
        ring_id_text = self.set.med_font.render(str(self.id), True, self.set.white)
        self.win.blit( ring_id_text, (self.id_x, y))


    """ FOR SNAP RINGS """

    def get_snap(self):
        return self.snap

    def get_old_new_rods(self):
        """ While changing rods, pass origin and destination back to main"""
        return self.rod, self.new_rod

    def get_size(self):
        """ Used by Main to check whether ring can fit on new stack of rods """
        return self.id

    def snap_back(self):
        """ On failed attempt to change rods, return ring to rod it came from"""
        self.update_rod(self.rod, self.pos)
        self.new_rod = None
