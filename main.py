""" APRIL 1, 2021 """


"""
APRIL 1:
    - MINOR FEATURE IMPROVEMENTS
        - RING NAMES ARE DRAWN WITH MOVING RING
        - ONLY TOP RING CAN MOVE
    - MAJOR BACK-END IMPROVEMENTS
        - CONTINUED TO REORGANIZE THE DATA HIERARCHY TO ENABLE MAIN TO PERFORM LOGIC ON RODS/RINGS

NEXT:
    - ADD THE LOGIC FOR HOW A RING IS MOVED FROM ONE STACK TO ANOTHER
        - SEE RODS MODULE FOR NOTES
    - ALSO NEED TO GO THROUGH EVERYTHING AND LOOK FOR REDUNDANT CODE
        - PROBABLY A FEW THINGS LEFT OVER THAT I NO LONGER USE
    - I COULD MOVE THE INITIALIZATION CODE TO A MODULE
        - NOT INIT, BUT THE CODE THAT MAKES THE RINGS AND RODS AT THE START.
        - IT ONLY RUNS ONCE

REFLECTION
    - SO CLEAR NOW HOW IMPORTANT IT IS TO HAVE A VERY ORDERLY DATA HIERARCHY FROM THE START
        - YOU DON'T ALWAYS KNOW WHERE YOU'RE GOING, BUT IF YOU DO... BETTER TO BUILD IN FROM START
    -
"""

import pygame
from collections import namedtuple
import numpy as np ## to make the ring widths
from settings import Settings
from drawRods import DrawRods
from ring import Ring
from rod import Rod


pygame.init()


class Main:
    def __init__(self):
        self.set = Settings()
        self.win = pygame.display.set_mode((self.set.win_w, self.set.win_h))
        self.drawRods = DrawRods(self.win)

        self.num_rings = 6 ## To be replaced by user input
        self.rods = self.init_rods_and_rings()
        self.moving_ring = None


    """ EVENTS """

    def get_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit(), quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_button_down_events()

            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse_button_up_events()

            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event)


    def mouse_button_down_events(self):
        """ Set moving flag = True on hovering ring -- check all rings, all rods """
        if pygame.mouse.get_pressed()[0]:
            for rod in self.rods:
                rod.rod.check_moving()


    def mouse_button_up_events(self):
        """ Cancel moving: all rings, all rods """
        for rod in self.rods:
            rod.rod.cancel_moving()


    def keydown_events(self, event):
        if event.key == pygame.K_q:
            pygame.quit(), quit()


    """ UPDATES """

    def update(self):
        self.draw_page_border()

        for rod in self.rods:
            rod.rod.update_rings()

        self.update_screen()


    def update_screen(self):
        ### Draw rods
        de, vers = 2, 0
        self.drawRods.draw(de, vers)

        ### Draw rings
        for r in self.rods:
            r.rod.draw_rings()

        pygame.display.update()


    def draw_page_border(self):
        x, y = self.set.left_border, self.set.top_border
        w, h = self.set.border_w, self.set.border_h
        c, thick = self.set.border_colour, self.set.border_thickness

        pygame.draw.rect(self.win, c, pygame.Rect(x, y, w, h), thick)


    """ Initialization things """

    def init_rods_and_rings(self):
        rods_outer = namedtuple('o', ['a', 'b', 'c'])
        rods_inner = namedtuple('i', ['state', 'rod'])

        states = ['de', 'aux', 'vers']
        rod_ids = [0, 1, 2]

        ### Make rods data structure
        r = [rods_inner(states[i], Rod(rod_ids[i])) for i in range(3)]
        rods = rods_outer(r[0], r[1], r[2])

        for ring in self.make_rings():
            rods.c.rod.add_ring(ring)

        return rods


    def make_rings(self):
        IDs = [x for x in range(0, 10)]
        r = self.num_rings

        rings = [Ring(self.win, IDs[i]) for i in range(r)]

        return rings


    """ MAIN """
    def main(self):
        clock = pygame.time.Clock()
        print(self.set.ring_y_coords)

        while True:
            clock.tick(self.set.FPS)
            self.win.fill(self.set.white)

            self.get_events()
            self.update()

if __name__ == "__main__":
    x = Main()
    x.main()
