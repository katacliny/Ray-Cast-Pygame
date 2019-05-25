import pygame as py
import math

class Boundary():

    def __init__(self, x1, y1, x2, y2):
        self.a = py.math.Vector2(x1, y1)
        self.b = py.math.Vector2(x2, y2)
        self.shoulByVisible = False

    def show(self, Surface, color):
        if self.shoulByVisible:
            py.draw.aaline(Surface, color, [self.a.x, self.a.y], [self.b.x, self.b.y], True)
