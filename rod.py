""" March 29, 2021 """

import pygame
from setup.settings import Settings


class Rod:
    def __init__(self, id):
        pygame.init()
        self.set = Settings()
        self.stack = []
        self.id = id # rod_ids = [0, 1, 2]



    """ ALWAYS PERFORMED """

    def update_rings(self):
        mx, my = pygame.mouse.get_pos()

        for ring in self.stack:
            ring.check_hovering(mx, my)
            ring.move(mx, my)

    def draw_rings(self):
        for ring in self.stack:
            ring.draw()



    """ SNAPPING """

    def check_snap_ring(self):
        """ Pass a ready-to-snap ring back to Main """

        for ring in self.stack:
            if ring.get_snap():
                return ring

    def get_top_id(self):
        """ Pass the id as proxy for size up to Main """
        if self.stack:
            return self.stack[0].get_id()
        return float('inf') ## If empty, send the largest number

    def remove_ring(self):
        self.stack.pop(0)


    """ MOVING """
    def check_moving(self):
        if self.stack:
            self.stack[0].check_moving()

    def cancel_moving(self):
        for ring in self.stack:
            ring.cancel_moving()


    """ OTHER FUNCTION(S) """
    def add_ring(self, ring):
        """ Used at initialization and when moving rings to new rods """
        self.stack.insert(0, ring)
        ring_pos = len(self.stack) - 1

        ring.update_rod(self.id, ring_pos)


    def get_len(self):
        """ Check if the game is won """
        return len(self.stack)
