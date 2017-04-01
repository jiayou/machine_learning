# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 15:03:25 2017

@author: L-wxia1
"""


#%%
SM_CXSCREEN = 0
SM_CYSCREEN = 1
SM_CXVSCROLL = 2
SM_CYHSCROLL = 3
SM_CYCAPTION = 4
SM_CXBORDER = 5
SM_CYBORDER = 6
SM_CXDLGFRAME = 7
SM_CYDLGFRAME = 8
SM_CYVTHUMB = 9
SM_CXHTHUMB = 10
SM_CXICON = 11
SM_CYICON = 12
SM_CXCURSOR = 13
SM_CYCURSOR = 14
SM_CYMENU = 15
SM_CXFULLSCREEN = 16
SM_CYFULLSCREEN = 17
SM_CYKANJIWINDOW = 18
SM_MOUSEPRESENT = 19
SM_CYVSCROLL = 20
SM_CXHSCROLL = 21
SM_DEBUG = 22
SM_SWAPBUTTON = 23
SM_RESERVED1 = 24
SM_RESERVED2 = 25
SM_RESERVED3 = 26
SM_RESERVED4 = 27
SM_CXMIN = 28
SM_CYMIN = 29
SM_CXSIZE = 30
SM_CYSIZE = 31
SM_CXFRAME = 32
SM_CYFRAME = 33
SM_CXMINTRACK = 34
SM_CYMINTRACK = 35
SM_CXDOUBLECLK = 36
SM_CYDOUBLECLK = 37
SM_CXICONSPACING = 38
SM_CYICONSPACING = 39
SM_MENUDROPALIGNMENT = 40
SM_PENWINDOWS = 41
SM_DBCSENABLED = 42
SM_CMOUSEBUTTONS = 43
SM_CMETRICS = 44
SM_CXPADDEDBORDER = 92

#%% get window

import win32gui
import win32con
import subprocess
import _thread

#subprocess.run('python snake.py')

_thread.start_new_thread(subprocess.run, ('python snake.py',))

w= win32gui.FindWindow(None, 'Score: 0')
win32gui.IsWindow(w)

win32gui.SendMessage(w, win32con.WM_KEYDOWN, 32, 0)

title = win32gui.GetWindowText(w)


#%% pass key

from PIL import ImageGrab
import numpy as np

bbox = win32gui.GetWindowRect(w)
img0 = ImageGrab.grab(bbox)

M,N = img0.size
wbox = [4+1, 4+19+1, M-4, N-4]
# win32api.GetSystemMetrics(SM_CYFRAME)
# win32api.GetSystemMetrics(SM_CYCAPTION)
# win32api.GetSystemMetrics(SM_CXBORDER)

BOARDER=20

img=img0.crop(wbox).resize((BOARDER, BOARDER)).convert('L')
data = np.array(img)

print(data)
img.show()


#%%
