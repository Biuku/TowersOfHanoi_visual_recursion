""" APRIL 1, 2021 """


"""
NEXT:
    - ADD THE LOGIC FOR HOW A RING IS MOVED FROM ONE STACK TO ANOTHER
        - SEE RODS MODULE FOR NOTES
    - ALSO NEED TO GO THROUGH EVERYTHING AND LOOK FOR REDUNDANT CODE
        - PROBABLY A FEW THINGS LEFT OVER THAT I NO LONGER USE
    - I COULD MOVE THE INITIALIZATION CODE TO A MODULE
        - **DONE**
"""

import pygame
from collections import namedtuple
from settings import Settings
from drawRods import DrawRods
from startup import Startup


pygame.init()


class Main:
    def __init__(self):
        self.set = Settings()
        self.win = pygame.display.set_mode((self.set.win_w, self.set.win_h))
        self.drawRods = DrawRods(self.win)

        self.num_rings = 6 ## To be replaced by user input
        self.startup = Startup(self.num_rings)
        self.rod_attributes = self.startup.init_rod_attributes()
        self.rods = self.startup.init_rods_with_rings()
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
                rod.check_moving()


    def mouse_button_up_events(self):
        """ Cancel moving: all rings, all rods """
        for rod in self.rods:
            rod.cancel_moving()


    def keydown_events(self, event):
        if event.key == pygame.K_q:
            pygame.quit(), quit()


    """ UPDATES """

    def update(self):
        self.draw_page_border()

        ## Look for any ring that's ready to snap to a new rod
        for rod in self.rods:
            ring = rod.check_snapper()
            if ring:
                self.update_snap(ring)
                break

        for rod in self.rods:
            rod.update_rings()

        self.update_screen()



    def update_snap(self, ring):

        old_rod = self.rods[ring.get_rod()]
        new_rod = self.rods[ring.get_new_rod()]

        if old_rod == new_rod:
            ring.snap_back()

        if ring.get_size() < new_rod.get_top_size():
            ring.snap_back()

        else:
            old_rod.remove_ring()
            new_rod.add_ring(ring)



    def update_screen(self):
        ### Draw rods
        de, vers = 2, 0
        self.drawRods.draw(de, vers)

        ### Draw rings
        for rod in self.rods:
            rod.draw_rings()

        pygame.display.update()


    def draw_page_border(self):
        x, y = self.set.left_border, self.set.top_border
        w, h = self.set.border_w, self.set.border_h
        c, thick = self.set.border_colour, self.set.border_thickness

        pygame.draw.rect(self.win, c, pygame.Rect(x, y, w, h), thick)


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
