""" March 29, 2021 """


""" THINK I'LL CALL IT A DAY SOON, BUT AN ISSUE THAT EMERGED...
- I CAN NOW MOVE RINGS, BUT WITHOUT RULES. I NEED TO ADD IN:
    - WHEN ARE YOU NOT ALLOWED TO MOVE A RUN (CAN ONLY MOVE THE TOP RING)
    - HOW DOES MAIN CONTROL HOW A RING SNAPS TO ANOTHER ROD? IF THE MOVEMENT IS WITHIN THE RING OBJECT?

- ALSO, I THINK I NEED TO DROP MY NAMED TUPLE.
    - IF I USED A DICT INSTEAD
"""


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

        self.num_rings = 7 ## To be replaced by user input
        self.rods = self.make_rods_and_rings()


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
                rod.check_moving()


    def mouse_button_up_events(self):
        for rod in self.rods:
            rod.cancel_moving()


    def keydown_events(self, event):
        if event.key == pygame.K_q:
            pygame.quit(), quit()


    """ UPDATES """

    def update(self):
        self.draw_page_border()

        for rod in self.rods:
            rod.check_hovering()

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
        for rod in self.rods:
            rod.draw_rings()

        pygame.display.update()



    """ Initialization things """

    def make_rods_and_rings(self):

        rods_structure = namedtuple('rods', ['a', 'b', 'c'])
        rods = rods_structure(Stack(0), Stack(1), Stack(2))

        rings = self.make_rings(self.num_rings)

        for ring in rings:
            rods.a.add_ring(ring)

        return rods


    def make_rings(self, num_rings):
        rings = []
        width_factor = 1 ### Start with a ring 100% the with of max

        for ring_name in range(num_rings):
            rings.append(Ring(self.win, width_factor, ring_name))
            width_factor -= 0.1 ## Decrease width 10% per ring

        return rings


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
