""" March 27, 2021 """

import pygame
from settings import Settings
pygame.init()


class Main:
    def __init__(self, win, w, name):
        self.win = win
        self.set = Settings()
        self.colour = None

        # Flag
        self.active = False
        self.final_pos = False

        self.get_rod_x_coords = self.set.get_rod_x_coords

        self.w = self.set.ring_max_w * w ## W is a percent
        self.h = 20

        self.colour = self.set.blue

        self.name = name ## Integer name


    def draw(self, y):
        x = self.s
