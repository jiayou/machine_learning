# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 10:56:36 2017

@author: L-wxia1
"""

from random import randint
import logging

class GreedySnakeGame():

    BOARDER = 20
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
        field  = (0,self.BOARDER,0,self.BOARDER)
        self.snake  = GreedySnake(field)
        self.egg    = Egg(field)
        self.field  = field
        self.running = False
        self.score = 0
        
    def key_up(self):
        self.move_snake('up')

    def key_down(self):
        self.move_snake('down')
        
    def key_left(self):
        self.move_snake('left')
        
    def key_right(self):
        self.move_snake('right')
    
    def restart(self):
        self.logger.info('Game Start')
        self.snake.revive()
        self.running = True

    def move_snake(self, direction):
        self.snake.move(direction)
        if self.snake.eat(self.egg):
            self.score+=10
            self.egg = Egg(self.field)
        
    def update(self):
        if self.snake.is_alive():
            self.move_snake('')
        else:
            self.running = False
            self.score = 0

    def is_running(self):
        return self.running
        
    def get_info(self):
        field = [[0]* self.BOARDER] * self.BOARDER
        
        for c in self.snake.position:
            field[c] = 1
        
        field[self.egg.x, self.egg.y] = 2
        
        return (field, self.score)

    def get_score(self):
        return self.score


#%%        
class GreedySnake:
    def __init__(self, lim):
        self.logger = logging.getLogger(__name__)
        self.lim = lim
        self.revive()
        
    def revive(self):
        center_x = int(self.lim[-1] * 0.5)

        self.position = [(center_x, 1), (center_x, 0)]
        self.direction = 'down'
        self.alive = True
        self.logger.info('Snake revived.')
        
    def die(self):
        self.alive = False
        self.logger.info('Snake died.')
    
    def is_alive(self):
        return self.alive
        
    def move(self, new_direction=''):
        if not self.is_alive():
            self.logger.info('Dead snake does not move.')
            return
            
        old_direction = self.direction
        if old_direction == new_direction:
            return
        
        if len(new_direction)==0:
            new_direction = old_direction
        else:
            self.direction = new_direction
                    
        m = (old_direction, new_direction)
#        print('Snake moving '+ new_direction)
        
#        if m==('down', 'down') or m==('up', 'up') or m==('left', 'left') or m==('right', 'right'):
#            return
#            
        if   m==('down', 'up') or m==('up', 'down') or m==('left', 'right') or m==('right', 'left'):
#            self.die();
            m==m
        elif new_direction == 'left':
            self.dx = -1
            self.dy = 0
        elif new_direction == 'right':
            self.dx = 1
            self.dy = 0
        elif new_direction == 'up':
            self.dx = 0
            self.dy = -1
        elif new_direction ==  'down':
            self.dx = 0
            self.dy = 1
        else:
            return
            
        self.position[1] = self.position[0]
        x = self.position[0][0]+ self.dx
        y = self.position[0][1]+ self.dy
        
        x0,x1,y0,y1 = self.lim
        if x<x0 or x>=x1 or y<y0 or y>=y1:
            self.die()
        
        self.dx=0
        self.dy=0
        
        self.position[0] = [x,y]
#        print(self.position)

    def eat(self, egg):
        return self.position[0] == [egg.x, egg.y]

#%%        
class Egg:
    def __init__(self, lim):
        x0,x1,y0,y1 = lim
        self.x = randint(x0, x1-1)
        self.y = randint(y0, y1-1)

