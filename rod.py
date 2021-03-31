""" March 29, 2021 """

import pygame ## Can I delete??
pygame.init() ## Can I delete??
from settings import Settings


class Rod:
    def __init__(self, id):
        self.set = Settings()

        self.stack = [] ### to be deleted
        self.id = id

    ### HOVERING ###
    def check_hovering(self):
        mx, my = pygame.mouse.get_pos()

        for ring in self.stack:
            ring.check_hovering(mx, my)

    ### MOVING ###
    def check_moving(self):
        for ring in self.stack:
            ring.check_moving()

    def cancel_moving(self):
        for ring in self.stack:
            ring.cancel_moving()


    ### ADD RING ###
    def check_fit(self, ring):
        if ring.get_size() < self.get_top_ring_size():
            return True

        return False

    def get_top_ring_size(self):
        if self.stack:
            return self.stack[0].getsize()

        return self.set.ring_max_w

    def add_ring(self, ring):
        self.stack.insert(0, ring)

    ### DRAW ###
    def draw_rings(self):
        y = self.set.anchor_ring_y

        reversed_stack = self.stack[::-1]

        for ring in reversed_stack:
            ring.draw(y, self.id)
            y -= self.set.rod_w


    def pop_ring(self):
        ring = self.stack.pop(0)
        return ring

    def get_num_rings(self):
        return len(self.stack)
