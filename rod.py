""" March 29, 2021 """

import pygame
pygame.init()
from settings import Settings


class Rod:
    def __init__(self, id):
        self.set = Settings()
        self.stack = []
        self.id = id



    def add_ring(self, ring):
        self.stack.insert(0, ring)
        ring_pos = self.get_num_rings() - 1
        ring.update_rod(self.id, ring_pos)


    def update_rings(self):
        mx, my = pygame.mouse.get_pos()

        for ring in self.stack:
            ring.check_hovering(mx, my)
            ring.move()



    def get_num_rings(self):
        return len(self.stack)


    """

    REMOVE A RING FROM A STACK
        - ONLY UPON BEING ADDED TO ANOTHER STACK

    ADD RING FROM A STACK TO A NEW STACK
        1. HAVE A MOVING RING
            - MOVING RING MUST BE TOP RING
        2. BE CLOSE TO A STACK
            - X COORD WITHIN WIDTH OF LARGEST RING, CENTRED ON ROD
            - Y COORD = WITHIN A MARGIN ABOVE / BELOW RODS
        3. MOUSE BUTTON UP
        4. CHECK IF THE MOVING RING IS SMALLER THAN THE LARGEST RING BELOW


    ### ADD RING ###
    def check_fit(self, ring):
        if ring.get_size() < self.get_top_ring_size():
            return True

        return False


    def pop_ring(self):
        ring = self.stack.pop(0)
        return ring

    def get_top_ring_size(self):
        if self.stack:
            return self.set.ring_widths[len(stack)]
            #return self.stack[0].getsize()

        return self.set.ring_max_w
    """


    """ Foundation stuff -- don't need to change it """

    ### DRAW ###
    def draw_rings(self):
        for ring in self.stack:
            ring.draw()

    ### MOVING ###
    def check_moving(self):
        top_ring = len(self.stack) -1
        for ring in self.stack:
            ring.check_moving(top_ring)

    def cancel_moving(self):
        for ring in self.stack:
            ring.cancel_moving()
