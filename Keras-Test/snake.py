# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 10:56:36 2017

@author: L-wxia1
"""

import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QBrush, QImage 
from PyQt5.QtCore import Qt, QBasicTimer, QRectF, QCoreApplication, QRect, QPoint
import numpy as np
from PIL import Image

class GreedySnakeGame(QWidget):

    BOARDER = 20    
    ZOOM_FACTOR = 10
    
    def __init__(self):
        super().__init__()
        self.snake = GreedySnake((0,self.BOARDER,0,self.BOARDER))
        self.score = 0
        self.initUI()
        
    def print_snake(self):
        s = self.snake
        print('Snake at ', s.position, s.direction, self.score)
        
        
    def timerEvent(self, event):
#        print('Timer Triggered', event.timerId())
#        self.print_snake()
        if self.snake.is_alive():
            self.score+=1
            self.snake.move('')
        else:
            self.score = 0
            self.timer.stop()
        self.update()
            

        
    def paintEvent(self, event):
#        print('Paint Event Triggered')

        zf = self.ZOOM_FACTOR
        B  = self.BOARDER
        
        painter = QPainter()
        painter.begin(self)
        
        painter.setBrush(QBrush(QColor(255, 255, 255)))
        box = QRectF(0, 0, B*zf, B*zf)
        painter.drawRect(box)

        painter.setBrush(QBrush(QColor(0, 0, 0)))
#        if self.snake.is_alive():
        p = self.snake.position
        for pt in p:
            xx = pt[0]
            yy = pt[1]
            c = QPoint( xx*zf,   yy*zf)
            d = QPoint( (1+xx)*zf,   (1+yy)*zf)
            obj = QRect(c, d)
            painter.drawRect(obj)

        painter.end()
        
        
    # http://stackoverflow.com/questions/17968267/how-to-make-click-through-windows-pyqt
    
    def keyPressEvent(self, e):
#        print('Key Pressed', e.key())
        if e.key() == Qt.Key_Escape:
            self.close()
            return
            
        if e.key() == Qt.Key_Up:
            self.snake.move('up')
            self.update()
            return
            
        if e.key() == Qt.Key_Down:
            self.snake.move('down')
            self.update()
            return
            
        if e.key() == Qt.Key_Left:
            self.snake.move('left')
            self.update()
            return
            
        if e.key() == Qt.Key_Right:
            self.snake.move('right')
            self.update()
            return
            
        if e.key() == Qt.Key_Space:
            self.snake.revive()
            self.score = 0
            print('Game Start')
            self.timer.start(100 , self)
            self.update()
            return
            
    def initUI(self):
        width = self.BOARDER*self.ZOOM_FACTOR
        height = self.BOARDER*self.ZOOM_FACTOR
        
        self.resize(width, height)
        self.move(300, 300)
        self.setWindowTitle('GreedySnakeGame')
        self.timer = QBasicTimer()
        self.show()

    def get_pixels(self):
        field = [[0]* self.BOARDER] * self.BOARDER
        
        for c in self.snake.position:
            field[c] = 1
        
        return field

    def get_score(self):
        return self.score
        
class GreedySnake:
    def __init__(self, lim):
        self.lim = lim
        self.revive()
        
    def revive(self):
        center_x = int(self.lim[-1] * 0.5)

        self.position = [(center_x, 0), (center_x, 1)]
        self.direction = 'down'
        self.alive = True
        print('Snake revived.')
        
    def die(self):
        self.alive = False
        print('Snake died.')
    
    def is_alive(self):
        return self.alive
        
    def move(self, new_direction=''):
        if not self.is_alive():
            print('Dead snake does not move.')
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
            
        self.position[0] = self.position[1]
        x = self.position[1][0]+ self.dx
        y = self.position[1][1]+ self.dy
        
        x0,x1,y0,y1 = self.lim
        if x<x0 or x>=x1 or y<y0 or y>=y1:
            self.die()
        
        self.dx=0
        self.dy=0
        
        self.position[1] = [x,y]
#        print(self.position)
        

#%% visualization
if __name__ == '__main__':
#    app = QApplication(sys.argv)
    
    app = QCoreApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    
    game = GreedySnakeGame()
#    print (game.score)
    code = app.exec_()
    
    
    print(code)
#    quit()
#    sys.exit(code)
    
#    game = GreedySnakeGame
#    game.
#    