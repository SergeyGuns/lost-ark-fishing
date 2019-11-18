import pyautogui
import time
import math, operator
from functools import reduce 
from PIL import Image
from PIL import ImageChops
from PIL import Image
import sys
import tkinter as tk
from overlay import Window

win = Window()
label = tk.Label(win.root, text="Window_0")
label.pack()
Window.launch()


def my_print(text):
    sys.stdout.write(str(text))
    sys.stdout.write(str('\n'))
    sys.stdout.flush()

sourceRect =  Image.open("source.png")
def compare(image1, image2):

    h1 = image1.histogram()
    h2 = image2.histogram()
    rms = math.sqrt(reduce(operator.add,
        map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
    return rms

def average(lst): 
    return sum(lst) / len(lst) 

diffArr = [2,2,2,2,2,2,2,2,2,2]


def startFishing(red):
    global fishingStatus,diffArr
    if fishingStatus == 'stop':
        fishingStatus = 'started'
        pyautogui.press('w')
        time.sleep(5)
    elif fishingStatus == 'started' and red < 65:
        fishingStatus = 'ending'
        pyautogui.press('w')
        time.sleep(7)
    if fishingStatus == 'ending':
        fishingStatus = 'stop'


time.sleep(3)


x1 = 413
y1 = 666
x2 = 576
y2 = 675

while True:
   
    imgRect = pyautogui.screenshot(region=(x1,y1,x2 - x1, y2 - y1))
    pixels = imgRect.load()
    avg = [0, 0, 0]
    for x in range(imgRect.size[0]):
        for y in range(imgRect.size[1]):
            for i in range(3):
                avg[i] += pixels[x, y][i]
    red,g,b = tuple(c // (imgRect.size[0] * imgRect.size[1]) for c in avg) 
    my_print(red)
    time.sleep(.5)

