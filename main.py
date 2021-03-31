""" March 29, 2021 """


""" THINK I'LL CALL IT A DAY SOON, BUT AN ISSUE THAT EMERGED...
- I CAN NOW MOVE RINGS, BUT WITHOUT RULES. I NEED TO ADD IN:
    - WHEN ARE YOU NOT ALLOWED TO MOVE A RUN (CAN ONLY MOVE THE TOP RING)
    - HOW DOES MAIN CONTROL HOW A RING SNAPS TO ANOTHER ROD? IF THE MOVEMENT IS WITHIN THE RING OBJECT?

1. Implement named tuple data class
    - Main tracks
        - Top rings in each rod
        -

- .
    - IF I USED A DICT INSTEAD
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
        if pygame.mouse.get_pressed()[0]:
            for rod in self.rods:
                rod.rod.check_moving()


    def mouse_button_up_events(self):
        for rod in self.rods:
            rod.rod.cancel_moving()


    def keydown_events(self, event):
        if event.key == pygame.K_q:
            pygame.quit(), quit()


    """ UPDATES """

    def update(self):
        self.draw_page_border()

        for rod in self.rods:
            rod.rod.check_hovering()

        self.update_screen()


    def draw_page_border(self):
        x, y = self.set.left_border, self.set.top_border
        w, h = self.set.border_w, self.set.border_h
        c, thick = self.set.border_colour, self.set.border_thickness

        pygame.draw.rect(self.win, c, pygame.Rect(x, y, w, h), thick)


    def update_rings_in_rods(self):
        """ Push rings to the lowest possible level in each rod """
        pass


    def update_screen(self):
        ### Draw rods
        de, vers = 2, 0
        self.drawRods.draw(de, vers)

        ### Draw rings
        for r in self.rods:
            r.rod.draw_rings()

        pygame.display.update()


    """ Initialization things """

    def init_rods_and_rings(self):
        rods_outer = namedtuple('o', ['a', 'b', 'c'])
        rods_inner = namedtuple('i', ['state', 'rod'])

        states = ['de', 'aux', 'vers']
        ids = [0, 1, 2]

        ### Make rods data structure
        makr = [rods_inner(states[i], Rod(ids[i])) for i in range(3)]
        rods = rods_outer(makr[0], makr[1], makr[2])

        for ring in self.make_rings(self.num_rings):
            rods.a.rod.add_ring(ring)

        return rods


    def make_rings(self, rings):
        names = [x for x in range(1, 11)]
        widths = np.arange(1, 0, -.1)

        return [Ring(self.win, names[i], widths[i]) for i in range(rings)]


    """ MAIN """
    def main(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(self.set.FPS)
            self.win.fill(self.set.white)

            self.get_events()
            self.update()

if __name__ == "__main__":
    x = Main()
    x.main()
