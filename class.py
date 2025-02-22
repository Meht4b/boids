import pygame
import random
import math

CONST_RAD = 40
CONST_WIDTH = 600
CONST_HEIGHT = 400

class vector:
    
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    def __add__(self,other):
        return vector(self.x+other.x,self.y+other.y)
    
    def __sub__(self,other):
        return vector(self.x-other.x,self.y-other.y)
    
    def __mul__(self,other):
        if isinstance(other,float) or isinstance(other,int):
            return vector(self.x*other,self.y*other)
    
    def __truediv__(self,other):
        if isinstance(other,float) or isinstance(other,int):
            return vector(self.x*1/other,self.y*1/other)
    
    def __repr__(self):
        return f'{self.x},{self.y}'

    def magnitudeSquare(self):
        return self.x ** 2 + self.y ** 2

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
        
    def unitVector(self):
        return vector(self.x/self.magnitude(),self.y/self.magnitude())

    def tup(self):
        return (self.x,self.y)
    
    def tupAdj(self):
        
        return (self.x,coord(self.y))
    

class bird:
    def __init__(self,pos:vector,awareness_rad):
        self.pos=pos
        self.vel = vector()
        self.acc = vector()

        self.awareness_rad = awareness_rad

    def update(self,neighbors):

        self.update_phy(neighbors)

        #keeps velocity near 30 units/s
        if self.vel.magnitudeSquare>30:
            self.acc += self.vel *-0.5

        elif self.vel.magnitudeSquare<30:
            self.acc += self.vel *0.5

        self.pos+=self.vel
        self.vel += self.acc
        self.acc = 0

    def update_phy(self,neighbors):
        
        res = vector()
        for i in neighbors:
            res = res+neighbors.vel

        res = res/len(neighbors)

        self.acc = res


    def draw(self,win):
        


class flock:
    def __init__(self,win_h:int,win_w:int,bird_awareness_rad:int,flock_count:int):
        self.birds_grid = []
        self.win_h = win_h
        self.win_w = win_w
        
        
        for i in range(math.ceil(win_h/bird_awareness_rad)):
            self.birds_grid.append([])
            for j in range(math.ceil(win_w/bird_awareness_rad)):
                self.birds_grid[-1].append([])

        self.bird_awareness_rad = bird_awareness_rad
        self.flock_count = flock_count
        self.birds = []

        for i in range(flock_count):
            self.birds.append(bird(vector(random.randint(0,win_w-1),random.randint(0,win_h-1)),self.bird_awareness_rad))
            self.birds_grid[self.birds[-1].pos.x//bird_awareness_rad][self.birds[-1].pos.y//bird_awareness_rad].append(self.birds[-1])
    
    def grid_reset(self):
        for i in range(math.ceil(self.win_h/self.bird_awareness_rad)):
            self.birds_grid.append([])
            for j in range(math.ceil(self.win_w/self.bird_awareness_rad)):
                self.birds_grid[-1].append([])

    def update(self):
        self.grid_reset
        #puts each bird into their respective grids
        for i in self.birds:
            self.birds_grid[i.pos.x//self.bird_awareness_rad][i.pos.y//self.bird_awareness_rad].append(i)
       

       #checks the 
        for i in range(len(self.birds_grid)):
            for j in range(len(self.birds_grid[0])):
                res = self.birds_grid[i][j] #temp list of birds in nearby grids 
                if i>0:
                    res.extend[i-1][j]                       
                    if j<len(self.birds_grid[0])-1:
                        res.extend[i-1][j+1]
                    if j>0:
                        res.extend[i-1][j+1]
                if i<len(self.birds_grid)-1:
                    res.extend[i+1][j]
                    
                    if j<len(self.birds_grid[0])-1:
                        res.extend[i+1][j+1]
                    if j>0:
                        res.extend[i+1][j+1]
                if j<len(self.birds_grid[0])-1:
                    res.extend[i][j+1]
                if j>0:
                    res.extend[i][j+1]
                
                for k in range(len(self.birds_grid[i][j])):
                    k.update(res)



    def draw(self,win):
        for i in self.birds:
            i.draw()