# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 10:56:36 2017

@author: L-wxia1
"""

from random import randint
import logging

class GreedySnakeGame():

    BOARDER = 8
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
        rect  = (0, 0, self.BOARDER, self.BOARDER)
        self.snake  = GreedySnake(rect)
        self.egg    = Egg(rect)
        self.rect  = rect
        
    def key_arrow(self, direction):
        self.move_snake(direction)
        
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
        self.score = 0

    def move_snake(self, direction):
        self.snake.move(direction)
        if self.snake.eat(self.egg):
            self.score+=10
            self.egg = Egg(self.rect)
        
    def update(self):
        if self.snake.is_alive():
            self.move_snake('')

    def gameover(self):
        return not self.snake.is_alive()
        
    def get_info(self):
        field = [[0]* self.BOARDER for i in range(self.BOARDER) ]
        
        if not self.gameover():
            for (x,y) in self.snake.position:
                x = min(self.BOARDER-1, x)
                y = min(self.BOARDER-1, y)
                field[x][y] = 1
            
            field[self.egg.x][self.egg.y] = 2
        
        return field

    def get_score(self):
        return self.score


#%%        
class GreedySnake:
    def __init__(self, rect):
        self.logger = logging.getLogger(__name__)
        self.rect = rect
        self.alive = False
        
    def revive(self):
        center_x = int(self.rect[-1] * 0.5)

        self.position = [(center_x, 1), (center_x, 0)]
        self.direction = 'down'
        self.alive = True
        self.logger.debug('Snake revived.')
        
    def die(self):
        self.alive = False
        self.logger.debug('Snake died.')
    
    def is_alive(self):
        return self.alive
        
    def move(self, new_direction=''):
        if not self.is_alive():
            self.logger.debug('Dead snake does not move.')
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
            self.die();
            return
            
        if   new_direction == 'left':
            dx = -1
            dy = 0
        elif new_direction == 'right':
            dx = 1
            dy = 0
        elif new_direction == 'up':
            dx = 0
            dy = -1
        elif new_direction ==  'down':
            dx = 0
            dy = 1
        else:
            return
            
        self.position[1] = self.position[0]
        x = self.position[0][0]+ dx
        y = self.position[0][1]+ dy
        
        x0,y0,x1,y1 = self.rect
        if x<x0 or x>=x1 or y<y0 or y>=y1:
            self.die()
        
        self.position[0] = [x,y]
#        print(self.position)

    def eat(self, egg):
        return self.position[0] == [egg.x, egg.y]

#%%        
class Egg:
    def __init__(self, rect):
        x0,y0,x1,y1 = rect
        self.x = randint(x0, x1-1)
        self.y = randint(y0, y1-1)

