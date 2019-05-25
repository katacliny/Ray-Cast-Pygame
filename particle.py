import pygame as py
from ray import Ray
import math
import noise
from pygame import gfxdraw
import colors

class Particle():

    def __init__(self, width, height, surface, color, wall):
        self.pos = py.math.Vector2(py.mouse.get_pos()[0], py.mouse.get_pos()[1])
        self.surface = surface
        self.color = color
        self.wall = wall
        self.rays = []
        self.xoff = 0
        self.yoff = 0
        self.width = width
        self.height = height
        self.poligon = []
        for i in range(360):
            self.rays.append(Ray(self.pos, math.radians(i)))

    def look(self):
        walltoShow = []
        self.poligon = []
        for ray in self.rays:
            closest = None
            record = math.inf
            
            for wall in self.wall:
                pt = ray.cast(wall)
                if pt:
                    d = py.Vector2.distance_to(self.pos, pt)
                    if d < record:
                        record = d
                        closest = pt
                    
            if closest:
                self.poligon.append([closest.x, closest.y])
                #py.draw.aaline(self.surface, colors.WITHE, [self.pos.x, self.pos.y], [closest.x, closest.y], True)
            else:
                self.poligon.append([ray.pos.x + (ray.dir.x * 1000), ray.pos.y + (ray.dir.y * 1000)])
                #ray.show(self.surface, colors.WITHE)
        #gfxdraw.textured_polygon(self.surface, self.poligon, py.image.load("C:\\raycast\\gradient.png"), 1, 1)
        #gfxdraw.filled_polygon(self.surface, self.poligon, colors.WITHE)
        py.draw.polygon(self.surface, colors.WITHE, self.poligon, 1)

    def update(self):
        #self.pos = py.math.Vector2(noise.pnoise1(self.xoff) * self.width, noise.pnoise1(self.yoff) * self.height)
        self.pos = py.math.Vector2(py.mouse.get_pos()[0], py.mouse.get_pos()[1])
        self.rays = []
        self.xoff += 0.01
        self.yoff += 0.01
        for i in range(360):
            self.rays.append(Ray(self.pos, math.radians(i)))
    
    def show(self):
        self.update()
        self.look()
        
                
