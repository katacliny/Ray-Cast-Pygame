import pygame as py
import math

class Ray():

    def __init__(self, pos, angle):
        self.pos = pos
        self.dir = py.math.Vector2(math.cos(angle), math.sin(angle))
        self.draw = py.math.Vector2(self.pos.x + 10, self.pos.y)
        self.colision = False

    def show(self, Surface, color):
        
        py.draw.aaline(Surface, color, [self.pos.x, self.pos.y], [self.pos.x + (self.dir.x * 1000), self.pos.y + (self.dir.y * 1000)], True)

    def lookAt(self, py):
      pass

    def cast(self, wall):
        x1 = wall.a.x
        y1 = wall.a.y
        x2 = wall.b.x
        y2 = wall.b.y

        x3 = self.pos.x
        y3 = self.pos.y
        x4 = self.pos.x + self.dir.x
        y4 = self.pos.y + self.dir.y

        den = (x1 - x2) * (y3- y4) - (y1 - y2) * (x3 - x4)

        if den == 0:
            return False

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 -x4)) / den

        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 -x3)) / den

        if t > 0 and t < 1 and u > 0:
            pt = py.math.Vector2()
            pt.x = x1 + t * (x2 - x1)
            pt.y = y1 + t * (y2 - y1)
            self.colision = True
            
            return pt
        else:
            self.colision = False
            return False
        