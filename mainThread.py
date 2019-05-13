import pygame as py
import asyncio

class MainThread():

    def __init__(self, actions, py):
        self.actions = actions
        self.running = 1
        self.py = py
    
    def startStopRunning(self):
        self.running = not self.running

    def addActions(self, action):
        self.actions.append(action)

    def deleteAction(self, action):
        self.actions.pop(self.actions.index(action))

    def mainThread(self):
        while self.running: 
            for evento in self.py.event.get():
                if evento.type == self.py.QUIT:
                    self.startStopRunning
                    self.py.quit()

            for x in self.actions:
                x[0](*x[1])
                  