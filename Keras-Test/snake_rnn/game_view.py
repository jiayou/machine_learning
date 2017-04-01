# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 10:09:46 2017

@author: L-wxia1
"""

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QBrush 
from PyQt5.QtCore import Qt, QBasicTimer, QRectF, QRect, QPoint

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication

from game import GreedySnakeGame

import sys
import logging

#%%
class GreedySnakeGameView(QWidget):
    
    ZOOM_FACTOR = 10

    def __init__(self, game):
        self.logger = logging.getLogger(__name__)
        self.game = game
        super().__init__()

        self.logger.debug('GreedySnakeGameView Call initUI()')
        self.initUI()

        self.logger.debug('GreedySnakeGameView set up timer...')
        time_step = 2000/game.BOARDER + 10
        self.timer = QBasicTimer()
        self.timer.start(time_step , self)
        
        self.logger.debug('GreedySnakeGameView init complete.')

    def timerEvent(self, event):
#        self.logger.debug('TimerEvent Triggered.')
        self.game.update()
        if self.game.is_running():
            self.update()
        
    def paintEvent(self, event):
#        self.logger.debug('paintEvent Triggered.')
        painter = QPainter()
        painter.begin(self)
        
        B = self.game.BOARDER
        zf = self.ZOOM_FACTOR
        
        ####  Draw Field
        painter.setBrush(QBrush(QColor(255, 255, 255)))
        box = QRectF(0, 0, B*zf, B*zf)
        painter.drawRect(box)

        ####  Draw Snake
        painter.setBrush(QBrush(QColor(0, 0, 0)))
        for pt in self.game.snake.position:
            self.draw_block(painter, pt[0], pt[1])

        ####  Draw Egg
        painter.setBrush(QBrush(QColor(255, 0, 0)))
        self.draw_block(painter, self.game.egg.x, self.game.egg.y)
        
        painter.end()
        
    def draw_block(self, painter, xx, yy, shape='rect'):
        zf = self.ZOOM_FACTOR
        c = QPoint( xx*zf,   yy*zf)
        d = QPoint( (1+xx)*zf,   (1+yy)*zf)
        obj = QRect(c, d)
        painter.drawRect(obj)
        
    # http://stackoverflow.com/questions/17968267/how-to-make-click-through-windows-pyqt

    def keyPressEvent(self, e):
#        self.logger.debug('Key Pressed ' + str(e.key()))
        if e.key() == Qt.Key_Escape:
            self.close()
            return
            
        if e.key() == Qt.Key_Up:
            self.game.key_up()
            return
            
        if e.key() == Qt.Key_Down:
            self.game.key_down()
            return
            
        if e.key() == Qt.Key_Left:
            self.game.key_left()
            return
            
        if e.key() == Qt.Key_Right:
            self.game.key_right()
            return
            
        if e.key() == Qt.Key_Space:
            self.game.restart()
#            self.update()
            return
            
    def initUI(self):
        width = self.game.BOARDER*self.ZOOM_FACTOR
        height = self.game.BOARDER*self.ZOOM_FACTOR
        
        self.resize(width, height)
        self.move(300, 300)
        self.setWindowTitle('GreedySnakeGame')
        self.show()
            

def GreedySnakeGameGUI(new_game, args):
    logger = logging.getLogger(__name__)
#   app = QApplication(sys.argv)
    app = QCoreApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    logger.debug('Application Created '+str(app))

    view = GreedySnakeGameView(new_game)
    logger.debug('View Created '+ str(view))
    
    code = app.exec_()
    logger.debug('Exit Code: ' +str( code))
    
if __name__ == '__main__':
    
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    new_game = GreedySnakeGame()
    
    GreedySnakeGameGUI(new_game, sys.argv)

