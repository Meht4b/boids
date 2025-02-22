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

class rect_obstacles:
    def __init__(self,pos,size,color,win):
        self.size = size
        self.pos = pos
        self.color = color
        self.win = win

    def draw(self):
        pygame.draw.rect(self.win,self.color,(self.pos.x,self.pos.y,(self.pos+self.size).x,(self.pos+self.size).y))

class bird:
    def __init__(self,pos:vector,awareness_rad,win):
        self.pos=pos
        self.vel = vector()
        self.acc = vector(0,0)
        self.win = win

        self.awareness_rad = awareness_rad

    def update(self,neighbors):

        self.update_phy(neighbors)

        #keeps velocity near 30 units/s
        
        if self.vel.magnitudeSquare()>4:
            self.acc += self.vel *-1

        self.pos+=self.vel
        self.vel += self.acc
        self.acc = vector()

    def update_phy(self,neighbors):
        

        pos_center = vector()
        close_center = vector()
        average_vel = vector()
        c = 0 
        d = 0
        


        for i in neighbors:
            dis = (i.pos-self.pos).magnitudeSquare()
            if dis<self.awareness_rad:
                c+=1
                pos_center = pos_center + i.pos
                average_vel = average_vel + i.vel

            if dis<self.awareness_rad/4:
                d+=1
                close_center = close_center + i.pos
            
        


        pos_center = pos_center/c
        vel_center = pos_center-self.pos
        average_vel = average_vel/c

        if d:
            close_center = close_center/d
        vel_close = self.pos - close_center

        self.acc = vel_center*0.01 + vel_close*0.03 +average_vel
        pygame.draw.circle(self.win,(255,0,0),(pos_center.x,pos_center.y),1)


    def draw(self):
        
        pygame.draw.circle(self.win,(255,255,255),(self.pos.x,self.pos.y),2)
        
class flock:
    def __init__(self,win_h:vector,win_w:vector,bird_awareness_rad:int,flock_count:int,win):

        self.win_h = win_h
        self.win_w = win_w
        
        self.bird_awareness_rad = bird_awareness_rad
        self.flock_count = flock_count
        self.birds = []

        for i in range(flock_count):
            self.birds.append(bird(vector(random.randint(win_w.x,win_w.y-1),random.randint(win_h.x,win_h.y-1)),self.bird_awareness_rad,win))
            
    
    def grid_reset(self):
        for i in range(math.ceil(self.win_h/self.bird_awareness_rad)):
            self.birds_grid.append([])
            for j in range(math.ceil(self.win_w/self.bird_awareness_rad)):
                self.birds_grid[-1].append([])

    def update(self):
        self.grid_reset
        #puts each bird into their respective grids
        
        for i in self.birds:
            i.update(self.birds)
        self.draw()

        


    def draw(self):
        for i in self.birds:
            i.draw()


