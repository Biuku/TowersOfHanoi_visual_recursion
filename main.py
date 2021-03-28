""" March 27, 2021 """

import pygame
from settings import Settings
from rods import Rods
pygame.init()


class Main:
    def __init__(self):
        self.set = Settings()
        self.win = pygame.display.set_mode((self.set.win_w, self.set.win_h))
        self.rods = Rods(self.win)


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


    def update_screen(self):
        de = 0
        vers = 2
        self.rods.draw(de, vers)

        pygame.display.update()


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
