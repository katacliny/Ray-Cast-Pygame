import pygame as py

class Ray():

    def __init__(self, x, y):
        self.pos = py.math.Vector2(x, y)
        self.dir = py.math.Vector2(1, 0)

    def show(self, Surface, color):
        py.draw.aaline(Surface, color, [self.pos.x, self.pos.y], [self.pos.x + 10, self.pos.y], True)
        