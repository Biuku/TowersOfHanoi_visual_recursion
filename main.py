""" March 27, 2021 """

import pygame
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

    def update_rings_in_rods():
        """ Push rings to the lowest possible level in each rod """
        pass


    def update_screen(self):
        """ DRAW RODS """

        de = 0
        vers = 2
        self.drawRods.draw(de, vers)


        """ DRAW RINGS """
        rods = [0, 1, 2, 0]
        y = self.set.anchor_ring_y

        for i, ring in enumerate(self.rings):
            ring.draw(y, rods[0])
            y -= self.set.rod_w

        pygame.display.update()


    def make_rings(self):
        rings = []
        num_rings = self.num_rings  ### To be replaced with user input

        width_factor = 1 ### Start with a ring 100% the with of max

        for ring_name in range(num_rings):
            rings.append(Ring(self.win, width_factor, ring_name))
            width_factor -= 0.1

        return rings


    def main(self):
        clock = pygame.time.Clock()





        while True:
            clock.tick(self.set.FPS)
            self.win.fill(self.set.white)

            ### Do pygame things here ###

            self.get_events()
            self.update()

x = Settings()
print(x.rod_x_coords)

if __name__ == "__main__":
    x = Main()
    x.main()
