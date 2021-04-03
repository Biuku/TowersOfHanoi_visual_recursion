
import pygame
from collections import namedtuple
from setup.settings import Settings
from ring import Ring
from rod import Rod


class Setup:
    def __init__(self, num_rings):
        pygame.init()
        self.set = Settings()
        self.attributes = self.set.rod_attributes
        self.win = pygame.display.set_mode((self.set.win_w, self.set.win_h))
        self.num_rings = num_rings


    def init_rods_with_rings(self):
        """ Build 3 rods and n rings, with all rings on the first rod """
        rods = [Rod(i) for i in range(3)]

        for ring in self.init_rings():
            rods[2].add_ring(ring)

        return rods


    def init_rings(self):
        """ Initialize n rings -- called while initializing rods """

        IDs = [x for x in range(0, 10)]
        rings = [Ring(self.win, IDs[i]) for i in range(self.num_rings)]

        return tuple(rings)


    def init_rod_attributes(self):
        """ Not sure I'll even need this, but keeping in for now """

        rods_outer = namedtuple('o', self.attributes.labels)
        rods_inner = namedtuple('i', ['state', 'num'])

        r = [rods_inner(self.attributes.states[i], self.attributes.ids[i]) for i in range(3)]

        return rods_outer(r[0], r[1], r[2])
