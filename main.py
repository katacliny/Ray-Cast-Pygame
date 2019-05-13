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

def initialitation(caption):
    py.init()
    py.display.set_caption(caption)
        
def updateActionsThread(hilo):
    while 1:
        break

def main():
    initialitation("RayCast")
    conn = DataBaseHandle.__conn__()
    display = py.display.set_mode([400, 400])
    time = py.time.Clock()
    running = 1
    wall = Boundary(300, 100, 300, 300)
    ray = Ray(100, 200)
    hilo = MainThread([
        [display.fill, [colors.BLACK]],
        [wall.show, [display, colors.WITHE]],
        [ray.show, [display, colors.WITHE]],
        [py.display.flip, []],
        [time.tick, [5]]
    ], py)
    

    t1 = Thread(name="non-block", target=updateActionsThread, args=(hilo,))
    t1.start()
    hilo.mainThread()
 