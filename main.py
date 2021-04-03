""" APRIL 1, 2021 """

"""
NEXT:
    - Reverse the numbers of the rings -- high number should be wider
    - ALSO NEED TO GO THROUGH EVERYTHING AND LOOK FOR REDUNDANT CODE
        - PROBABLY A FEW THINGS LEFT OVER THAT I NO LONGER USE
"""

import pygame
from collections import namedtuple
from setup.settings import Settings
from setup.background import Background
from setup.setup import Setup

class Main:
    def __init__(self):
        pygame.init()
        self.set = Settings()
        self.win = pygame.display.set_mode((self.set.win_w, self.set.win_h))
        self.background = Background(self.win)

        self.num_rings = 9 ## To be replaced by user input
        self.setup = Setup(self.num_rings)
        self.rod_attributes = self.setup.init_rod_attributes()  ## Not sure if I need this
        self.rods = self.setup.init_rods_with_rings()

        self.de = 0
        self.vers = 2


    """ EVENTS """

    def get_events(self):
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                for rod in self.rods:
                    rod.check_moving()

            elif event.type == pygame.MOUSEBUTTONUP:
                for rod in self.rods:
                    rod.cancel_moving()

            ### Quitting ###
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit(), quit()

            elif event.type == pygame.QUIT:
                pygame.quit(), quit()


    """ UPDATES """

    def update(self):

        snap_ring = None

        for rod in self.rods:
            rod.update_rings()

            ### Stop looking if you find the snap ring
            if not snap_ring:
                snap_ring = rod.check_snap_ring()

        self.update_snap(snap_ring)

        self.update_screen()


    def update_snap(self, snap_ring):
        """ After moving, snaps a ring to a new rod, or back to its origin """
        if not snap_ring:
            return

        old, new = snap_ring.get_old_new_rods()
        old_rod, new_rod = self.rods[old], self.rods[new]

        if old_rod == new_rod:
            snap_ring.snap_back()

        ## Check if ring fits on the new rod's stack of rings
        if snap_ring.get_size() < new_rod.get_top_size():
            snap_ring.snap_back()

        else:
            old_rod.remove_ring()
            new_rod.add_ring(snap_ring)


    def update_screen(self):

        ### Draw Background -- 'de', 'vers' are dynamic states of rods
        self.background.draw(self.de, self.vers)

        ### Draw rings
        for rod in self.rods:
            rod.draw_rings()

        pygame.display.update()


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
