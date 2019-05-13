import pygame as py

class Boundary():

    def __init__(self, x1, y1, x2, y2):
        self.a = py.math.Vector2(x1, y1)
        self.b = py.math.Vector2(x2, y2)

    def show(self, Surface, color):
        py.draw.aaline(Surface, color, [self.a.x, self.a.y], [self.b.x, self.b.y], True)
        