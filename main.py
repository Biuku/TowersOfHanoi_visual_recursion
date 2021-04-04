""" APRIL 4, 2021 """

"""
I AM BUILDING THE ALGO
STEP 1. FUNCTIONAL ALGO:
    • Build algo in main code
    • Test with only 3 Rings
    • Spacebar advances algo 1 step
    • No colour changes or anything else – it just moves the rings
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

        self.num_rings = 4 ## To be replaced by user input
        self.setup = Setup(self.num_rings)
        self.rod_attributes = self.setup.init_rod_attributes()  ## Not sure if I need this
        self.rods = self.setup.init_rods_with_rings()

        ### ALGO STUFF ###
        self.instructions = []

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
                self.keydown_events(event)

            elif event.type == pygame.QUIT:
                pygame.quit(), quit()


    def keydown_events(self, event):
        if event.key == pygame.K_SPACE:
            """ Advance 1 step in the 'recursion' """
            self.algo_mover()

        if event.key == pygame.K_q:
            pygame.quit(), quit()


    """    *** THE ALGO ***    """

    def algo_mover(self):
        """ Moves one ring """

        de, aux, vers = self.instructions.pop(0)

        ring = de.pop_ring()
        vers.add_ring(ring)


    """ INITIATE FUNCTIONAL RECURSION ALGO """

    def make_instructions(self):
        """ Called once from Main. Pre-builds the solution steps. """
        de, aux, vers = self.rods
        n = self.num_rings

        self.recur(n, de, aux, vers)


    """ FUNCTIONAL RECURSION ALGO """
    def recur(self, n, de, aux, vers):

        if n == 1:
            self.instructions.append((de, aux, vers))
            return

        self.recur(n-1, de, vers, aux)

        self.instructions.append((de, aux, vers))


        self.recur(n-1, aux, de, vers)


    """ ************************************** """

    """ UPDATES """

    def update(self):

        snap_ring = None

        for rod in self.rods:
            rod.update_rings()

            ### Stop looking if you find the snap ring
            if not snap_ring:
                snap_ring = rod.check_snap_ring()

        self.update_snap(snap_ring)

        self.check_win()

        self.update_screen()


    def check_win(self):
        if self.rods[2].get_len() == self.num_rings:
            win_game_text = self.set.end_game_font.render("You win!!!", True, self.set.grey)
            self.win.blit( win_game_text, (400, 100))


    def update_snap(self, snap_ring):
        """ After moving, snaps a ring to a new rod, or back to its origin """
        if not snap_ring:
            return

        old, new = snap_ring.get_old_new_rods()
        old_rod, new_rod = self.rods[old], self.rods[new]

        if old_rod == new_rod:
            snap_ring.snap_back()

        ## Check new ring is smaller than top ring on the rod
        if snap_ring.get_id() > new_rod.get_top_id():
            snap_ring.snap_back()

        else:
            old_rod.remove_ring()
            new_rod.add_ring(snap_ring)


    def update_screen(self):

        ### Draw Background -- pass self.rods to unpack states
        # self.background.draw(self.de, self.vers)
        self.background.draw(self.rods)


        ### Draw rings
        for rod in self.rods:
            rod.draw_rings()

        pygame.display.update()


    """ MAIN """
    def main(self):
        clock = pygame.time.Clock()

        self.make_instructions()

        while True:
            clock.tick(self.set.FPS)
            self.win.fill(self.set.white)

            self.get_events()
            self.update()

if __name__ == "__main__":
    x = Main()
    x.main()
