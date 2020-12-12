import re
import numpy as np
from collections import deque
from pathlib import Path

def parse_input(inp):
    return [(x,int(y)) for (x,y) in [re.match(r'(\w)(\d+)',line).groups() for line in inp.splitlines()]]

class Ship():
    def __init__(self):
        self.current_direction = deque('ENWS') #current direction at [0]

        self.pos = np.array([0,0])
        self.waypoint = np.array([-1, 10])
        self.move_map = {
            'E' : lambda num :np.array([0,1])*num,
            'W' : lambda num :np.array([0,-1])*num,
            'N' : lambda num :np.array([-1,0])*num,
            'S' : lambda num :np.array([1,0])*num,
            'F' : self.forward,
            'R' : self.rot_ship_R,
            'L' : self.rot_ship_L,
        }
        self.waypoint_map = {
            'E' : lambda num :np.array([0,1])*num,
            'W' : lambda num :np.array([0,-1])*num,
            'N' : lambda num :np.array([-1,0])*num,
            'S' : lambda num :np.array([1,0])*num,
            'R' : self.rot_waypointR,
            'L' : self.rot_waypointL,
        }

    def forward(self, num):
        return self.move_map[self.current_direction[0]](num)

    def rot_ship_R(self, num):
        self.current_direction.rotate(num // 90)
        return np.array([0,0]) #position unchanged

    def rot_ship_L(self, num):
        return self.rot_ship_R(-num)

    #Part1 parser, nice and clean
    def move(self, movements):
        for direction, num in movements:
            self.pos += self.move_map[direction](num)


    def rot_waypointR(self,num):
        for i in range(num // 90):
            y,x = self.waypoint
            self.waypoint = np.array([x,-y])

    def rot_waypointL(self,num):
        self.rot_waypointR(360-num)

    #Part2 parser, less nice, less clean
    def move_wayp(self, movements):
        for direction, num in movements:
            if direction == 'F':
                #Move no use of map
                self.pos += self.waypoint * num
            elif direction == 'R' or direction == 'L':
                #rotate
                self.waypoint_map[direction](num)
            else:
                self.waypoint += self.waypoint_map[direction](num)

def manhattan(arr):
    return sum(abs(x) for x in arr)


def run_test():
    inp = 'F10\nN3\nF7\nR90\nF11'
    dirs = parse_input(inp)
    s = Ship()
    s.move(dirs)
    assert 25 == manhattan(s.pos)
    s2 = Ship()
    s2.move_wayp(dirs)
    assert 286 == manhattan(s2.pos)

run_test()
with open(Path("2020") / "day12" / "day12_input.txt") as f:
    directions = parse_input(f.read())
    s = Ship()
    s.move(directions)
    print(f'Manhattan distance part 1: {manhattan(s.pos)}')
    s2 = Ship()
    s2.move_wayp(directions)
    print(f'Manhattan distance part 2: {manhattan(s2.pos)}')
