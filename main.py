import pygame as py
import math 
import sys
import os
from boundary import Boundary 
from ray import Ray 
from dataLayer import DataBaseHandle
import colors
from mainThread import MainThread
from threading import Thread
from particle import Particle
import random
from block import Block


map =   [[0,0,0,0,0,0,0,0,0,0],
         [0,1,0,1,0,0,1,0,1,0],
         [0,1,0,1,1,1,1,0,1,0],
         [0,1,0,1,0,0,0,0,1,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,1,0,1,0,0,0,0,1,0],
         [0,1,0,1,1,1,1,0,1,0],
         [0,1,0,1,0,0,1,0,1,0],
         [0,0,0,0,0,0,0,0,0,0],
         ]
        
      

def initialitation(caption):
    py.init()
    py.display.set_caption(caption)
        
def updateActionsThread(hilo):
    while 1:
        break

def intersection(wall, ray, display):
        pt = ray.cast(wall)
        if(pt):
            py.draw.circle(display, colors.WITHE, (int(pt.x), int(pt.y)), 5)

def drawWall(surface, color, walls):
        for wall in walls:
                wall.show(surface, color)
        
def makeMap():
        contx = 0
        conty = 0
        for y in map:
                for x in y:
                        if x is 1:
                                map[conty][contx] = Block(45 * contx, 45 * conty)
                        
                        contx += 1
                contx = 0
                conty += 1
        return map

def recorrer():
        ground = []
        for x in map:
                for y in x:
                        if y is not 0:
                                for m in y.walls:
                                        ground.append(m)

        return ground

def main():
    initialitation("RayCast")
    conn = DataBaseHandle.__conn__()
    display = py.display.set_mode([400, 400])
    time = py.time.Clock()
    running = 1
    makeMap()
    particle = Particle(600, 450, display, colors.GRAY, recorrer())
    
    hilo = MainThread([
        [display.fill, [colors.BLACK]],
        [particle.show, []],
        [drawWall, [display, colors.WITHE, recorrer()]],
        
        #[recorrer, [display, colors.WITHE, mapat]],
        [py.display.flip, []],
        [time.tick, [64]],
    ], py)
    

    t1 = Thread(name="non-block", target=updateActionsThread, args=(hilo,))
    t1.start()
    hilo.mainThread()
 