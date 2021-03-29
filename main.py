""" March 27, 2021 """

import pygame
from collections import namedtuple
from settings import Settings
from drawRods import DrawRods
from ring import Ring
from stack import Stack
pygame.init()


class Main:
    def __init__(self):
        self.set = Settings()
        self.win = pygame.display.set_mode((self.set.win_w, self.set.win_h))
        self.drawRods = DrawRods(self.win)
        self.num_rings = 10 ## To be replaced by user input

        self.rings = self.make_rings()
        self.rods = self.make_rods()


    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(), quit()

            if event.type == pygame.KEYDOWN:
                self.keydown_events(event)

    def keydown_events(self, event):
        if event.key == pygame.K_q:
            pygame.quit(), quit()


    def update(self):
        self.draw_page_border()
        self.update_screen()



    def draw_page_border(self):
        x, y = self.set.left_border, self.set.top_border
        w, h = self.set.border_w, self.set.border_h
        c, thick = self.set.border_colour, self.set.border_thickness

        pygame.draw.rect(self.win, c, pygame.Rect(x, y, w, h), thick)


    def update_rings_in_rods(self):
        """ Push rings to the lowest possible level in each rod """

        for ring in self.rings:
            self.rods.b.add_ring(ring)


    def update_screen(self):
        """ DRAW RODS """
        de = 0
        vers = 2
        self.drawRods.draw(de, vers)


        """ DRAW RINGS """
        self.rods.a.draw_rings()
        self.rods.b.draw_rings()
        self.rods.c.draw_rings()

        #self.rods.c.test()

        pygame.display.update()


    def make_rings(self):
        rings = []
        num_rings = self.num_rings  ### To be replaced with user input

        width_factor = 1 ### Start with a ring 100% the with of max

        for ring_name in range(num_rings):
            rings.append(Ring(self.win, width_factor, ring_name))
            width_factor -= 0.1

        return rings


    def make_rods(self):
        """ Rod 0 = A, Rod 1 = B, Rod 2 = C """

        rods = namedtuple('rods', ['a', 'b', 'c'])
        return rods(Stack("AAA", 0), Stack("BBB", 1), Stack("CCC", 2))


    def main(self):
        clock = pygame.time.Clock()

        self.update_rings_in_rods() ### Tracer
        print(self.rods.b.test())

        while True:
            clock.tick(self.set.FPS)
            self.win.fill(self.set.white)

            ### Do pygame things here ###

            self.get_events()
            self.update()


        """ TRACER -- PROCES MY NAMED TUPLE WORKS """



if __name__ == "__main__":
    x = Main()
    x.main()
