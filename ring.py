""" March 27, 2021 """

import pygame
from settings import Settings
pygame.init()


class Ring:
    def __init__(self, win, id):
        self.win = win
        self.set = Settings()
        self.id = id
        self.rod_x_coords = self.set.rod_x_coords
        self.rod = None ## Which of the 3 rods
        self.pos = None ## Position in the rod stack

        ## Colours
        self.colour = self.set.blue
        self.hover_colour = self.set.light_blue

        ## Coordinates and size
        self.x = self.y = 1000 ## Temp
        self.w = self.set.ring_widths[self.id]
        self.h = self.set.rod_w ## -1 so I can draw a border on it

        self.id_x = 1000 ## Temp

        ## To centre ring on any rod
        self.half_ring = self.w // 2
        self.half_rod = self.set.rod_w // 2

        ## To snap rings to rods
        self.rod_x_spans = self.get_rod_x_spans()

        ## Flags
        self.hovering = False
        self.moving = False
        self.snap = None ## Flag ring as wanting to move to new rod (unclick after moving)
        self.new_rod = None ## For Main to access the new rod


    ### Main body of class ###

    def get_size(self):
        return self.id

    ### Moving ###
    def check_moving(self):
        if self.hovering:
            #if self.y == self.set.ring_y_coords[top_ring]:
            self.moving = True


    ### Snapping

    def get_new_rod(self):
        return self.new_rod

    def get_rod(self):
        return self.rod


    def snap_back(self):
        """ Return ring to rod it came from after failed attempt to change rods """
        self.update_rod(self.rod, self.pos)
        self.snap = False
        self.new_rod = None

        #self.y = self.set.ring_y_coords[pos]
        #x = self.rod_x_coords[self.rod]
        #self.x = self.update_rod_x(x)


    def check_snapping(self):
        if self.snap:
            return True
        return False


    def cancel_moving(self):
        if self.moving:
            self.moving = False

            ### Check whether the ring should snap to a new rod
            new_rod = self.rod
            mx, _ = pygame.mouse.get_pos()

            for i, rod_coords in enumerate(self.rod_x_spans):
                x1, x2 = rod_coords
                if mx > x1 and mx < x2:
                    new_rod = i

            self.snap = True ## Tell Main that this ring wants to snap to a rod
            self.new_rod = new_rod



    def update_rod(self, rod, pos):
        """Attaches a ring to a rod. Used by rod/add_ring() and self.cancel_moving() """

        ## Cancel any flags from snapping after moving
        self.snap = False
        self.new_rod = None

        ### Centre ring on rod -- adjust for ring's w and rod's w

        x = self.rod_x_coords[rod]
        self.x = self.update_rod_x(x)

        ### Update Y
        self.y = self.set.ring_y_coords[pos]

        self.rod = rod
        self.pos = pos



    def update_rod_x(self, x):
        """ Used by self.update_rod() and self.move() """
        self.id_x = x + 5
        x += self.half_rod - self.half_ring

        return x





    """ Foundation stuff -- don't need to change it """

    def move(self, mx, my):
        if self.moving:
            self.x = self.update_rod_x(mx)
            self.y = my

    def get_rod_x_spans(self):
        reach = self.set.ring_max_w // 2 ## look half the largest ring either side of a rod

        spans = []
        for rod in self.rod_x_coords:
            x1 = rod + self.half_rod - reach
            x2 = rod + self.half_rod + reach
            spans.append( (x1, x2) )

        return tuple(spans)


    def check_hovering(self, mx, my):
        self.hovering = False
        x = y = False

        if mx >= self.x and mx <= self.x + self.w:
            x = True

        if my >= self.y and my <= self.y + self.h:
            y = True

        if x and y:
            self.hovering = True


    def draw(self):

        x = self.x
        y = self.y
        colour = self.colour

        if self.hovering:
            colour = self.hover_colour

        pygame.draw.rect(self.win, colour, pygame.Rect(x, y, self.w, self.h))
        pygame.draw.rect(self.win, self.set.white, pygame.Rect(x, y, self.w, self.h), 1)

        self.draw_ring_id(y)

    def draw_ring_id(self, y):
        ring_id = str(self.id)
        #ring_id = str(self.y)
        colour = self.set.white

        draw_name = self.set.med_font.render(ring_id, True, colour)
        self.win.blit( draw_name, (self.id_x, y))
