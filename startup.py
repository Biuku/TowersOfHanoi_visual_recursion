
import pygame
from collections import namedtuple
from settings import Settings
from ring import Ring
from rod import Rod


pygame.init()

"""
Care and feeding (in main) of the 2d namedtuple data structure:
    - First layer:
        - self.rods.a, self.rods.b, self.rods.c
        - Not useful without second layer
    - Second layer:
        - Get the state -- is the rod set as 'de', 'aux' or 'vers'
            - self.rods.x.state
        - Access the rod object -- encapsulates most functionality and all rings
            - self.rods.a.rod, self.rods.b.rod, self.rods.c.rod
            - E.g., self.rods.a.rod.get_num_rings()
"""


class Startup:
    def __init__(self, num_rings):
        self.set = Settings()
        self.win = pygame.display.set_mode((self.set.win_w, self.set.win_h))
        self.num_rings = num_rings


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
