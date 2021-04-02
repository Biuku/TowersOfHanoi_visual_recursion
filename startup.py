
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
        self.attributes = self.set.rod_attributes
        self.win = pygame.display.set_mode((self.set.win_w, self.set.win_h))
        self.num_rings = num_rings


    def init_rod_attributes(self):

        rods_outer = namedtuple('o', self.attributes.ids)
        rods_inner = namedtuple('i', ['state', 'num'])

        r = [rods_inner(self.attributes.states[i], self.attributes.nums[i]) for i in range(3)]

        return rods_outer(r[0], r[1], r[2])


    def init_rods_with_rings(self):
        rods = []

        for i in range(3):
            rods.append(Rod(i))

        for ring in self.make_rings():
            rods[2].add_ring(ring)

        return rods

    def make_rings(self):
        IDs = [x for x in range(0, 10)]
        r = self.num_rings

        rings = [Ring(self.win, IDs[i]) for i in range(r)]

        return rings
