import sys
sys.path.append('../utils')
from utils import *
import numpy as np
import cv2

class Robot:

    def __init__(self, pos, vel):
        self.x = pos[1]
        self.y = pos[0]
        self.velx = vel[1]
        self.vely = vel[0]
    
    def move(self, mapp):
        self.x = (self.x + self.velx) % mapp.a
        self.y = (self.y + self.vely) % mapp.b
        

class Map:

    def __init__(self, a, b):
        self.map = np.zeros((a, b)).astype(int)
        self.a = a
        self.b = b
        self.robots = set()

    def __str__(self):
        strmap = self.map.copy()
        for r in self.robots:
            strmap[r.x, r.y] += 1
        return strmap.__str__()

    def addRobot(self, pos, vel):
        r = Robot(pos, vel)
        self.robots.add(r)

    def moveRobots(self):
        for r in self.robots:
            r.move(self)

    def produceFrame(self):
        smap = np.zeros((self.a, self.b), dtype='uint8') 
        for r in self.robots:
            if smap[r.x, r.y] == 0:
                smap[r.x, r.y] = 255
        return smap

    def safetyFactor(self):
        aq = self.a // 2
        bq = self.b // 2
        smap = self.map.copy()
        for r in self.robots:
            smap[r.x, r.y] += 1
        return np.sum(smap[:aq,:bq]) * np.sum(smap[aq+1:, :bq]) * np.sum(smap[aq+1:,bq+1:]) * np.sum(smap[:aq, bq+1:])

lines = read_data()
mapp = Map(103, 101)
for line in lines:
    line = line.strip()
    pos, vel = line.split(' ')
    pos = pos.split('=')[1]
    pos = *map(int, pos.split(',')),
    vel = vel.split('=')[1]
    vel = *map(int, vel.split(',')),
    mapp.addRobot(pos, vel)

out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M','P','E','G'), 1, (101, 103), False)
for i in range(10000):
    mapp.moveRobots()
    if i in range(7200, 8100):
        out.write(mapp.produceFrame())
out.release()
