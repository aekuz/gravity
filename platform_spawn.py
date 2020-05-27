from pygame import *
from random import *
from platforms_def import *
from run_set import *

class obstacles():
    place = 1100

    '''global wall_up
    global trap_pl1
    global wall_down
    global trap_pl2
    global trap_pl3
    global trap_pl4
    global trap_pl5'''

    wall_up = wall('platform.png', place, 70, 150, 150)
    trap_pl1 = trap('trap.png', place + 25, 420, 100, 160)
    trap_pl11 = trap('trap.png', place, 70, 5, 140)
    trap_pl12 = trap('trap.png', place, 790, 5, 140)
    trap_pl2 = trap('trap.png', place + 25, 70, 100, 260)
    trap_pl3 = trap('trap.png', place + 25, 670, 100, 260)
    trap_pl4 = trap('trap.png', place + 25, 220, 100, 260)
    trap_pl5 = trap('trap.png', place + 25, 560, 100, 260)
    wall_down = wall('platform.png', place, 780, 150, 150)

    def place_choose(self,):
        self.place += runobject.speed

    def spawn_obstacle1(self,win):
        self.wall_up.place(win)
        self.trap_pl1.place(win)
        self.wall_down.place(win)
        self.trap_pl11.place(win)
        self.trap_pl12.place(win)
        self.wall_up.rect.x = self.place
        self.trap_pl1.rect.x = self.place+25
        self.wall_down.rect.x = self.place
        self.trap_pl11.rect.x = self.place
        self.trap_pl12.rect.x = self.place

    def spawn_obstacle2(self,win):
        self.trap_pl2.place(win)
        self.trap_pl3.place(win)
        self.trap_pl2.rect.x = self.place+25
        self.trap_pl3.rect.x = self.place+25

    def spawn_obstacle3(self,win):
        self.wall_up.place(win)
        self.trap_pl4.place(win)
        self.trap_pl11.place(win)
        self.wall_up.rect.x = self.place
        self.trap_pl4.rect.x = self.place+25
        self.trap_pl11.rect.x = self.place

    def spawn_obstacle4(self,win):
        self.trap_pl5.place(win)
        self.wall_down.place(win)
        self.trap_pl12.place(win)
        self.trap_pl5.rect.x = self.place+25
        self.wall_down.rect.x = self.place
        self.trap_pl12.rect.x = self.place

class barrier1():
    time = 0
    def place_config(self):
        if self.time ==30:
            self.time = 0
            obs_type = randint(1,4)
            if obs_type == 1:
                runobject.obs1 = True
            if obs_type == 2:
                runobject.obs2 = True
            if obs_type == 3:
                runobject.obs3 = True
            if obs_type == 4:
                runobject.obs4 = True
        else:
            self.time+=1

barrier = barrier1()
