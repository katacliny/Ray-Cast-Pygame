import pygame as py
from boundary import Boundary

class Block():
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
        self.resta = 22
        self.bondary1 = Boundary(self.posx - self.resta, self.posy - self.resta, self.posx + self.resta, self.posy - self.resta,)
        self.bondary2 = Boundary(self.posx - self.resta, self.posy - self.resta, self.posx - self.resta, self.posy + self.resta,)
        self.bondary3 = Boundary(self.posx + self.resta, self.posy - self.resta, self.posx + self.resta, self.posy + self.resta,)
        self.bondary4 = Boundary(self.posx - self.resta, self.posy + self.resta, self.posx + self.resta, self.posy + self.resta,)
        self.walls = [self.bondary1, self.bondary2, self.bondary3, self.bondary4]

    def show(self, surface, color):
        for wall in self.walls:
                wall.show(surface, color)
        
