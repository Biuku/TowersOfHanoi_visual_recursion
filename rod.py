""" March 29, 2021 """

import pygame
pygame.init()
from settings import Settings


class Rod:
    def __init__(self, id):
        self.set = Settings()
        self.stack = []
        self.id = id # rod_ids = [0, 1, 2]


    def get_id(self):
        """ Helps Main know where to snap rings """
        return self.id


    def add_ring(self, ring):
        self.stack.insert(0, ring)
        ring_pos = len(self.stack) - 1
        ring.update_rod(self.id, ring_pos)


    def update_rings(self):
        mx, my = pygame.mouse.get_pos()

        for ring in self.stack:
            ring.check_hovering(mx, my)
            ring.move(mx, my)


    """ SNAPPING """

    def remove_ring(self):
        self.stack.pop(0)


    def check_snapper(self):
        """ Pass a ready-to-snap ring back to Main """

        for ring in self.stack:
            if ring.check_snapping():
                return ring




    """ Foundation stuff -- don't need to change it """

    ### DRAW ###
    def draw_rings(self):
        for ring in self.stack:
            ring.draw()

    ### MOVING ###
    def check_moving(self):
        if self.stack:
            self.stack[0].check_moving()
            print(self.stack[0].id)

    def cancel_moving(self):
        for ring in self.stack:
            ring.cancel_moving()
