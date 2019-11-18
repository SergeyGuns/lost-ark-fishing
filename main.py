import pyautogui
import time
import math
import operator
from functools import reduce
from PIL import Image
from PIL import ImageChops
from PIL import Image
import sys
import datetime

fishingStatus = 'stop'  # started | ending
fishingVershiStatus = 'empty' # 'load' 
fishingVershiLoadingTime = datetime.datetime.now()

def my_print(text):
    sys.stdout.write(str(text))
    sys.stdout.write(str('\n'))
    sys.stdout.flush()

lastBuff = datetime.datetime.now()

def startFishing(red):
    global lastBuff, fishingStatus, diffArr, fishingVershiStatus, fishingVershiLoadingTime
    now = datetime.datetime.now()
    buffDelta = now - lastBuff
    vershiDelda = now - fishingVershiLoadingTime
    my_print(
        str('{vershiDelda: ' + 
            str(vershiDelda.seconds) +', red: ' + 
            str(red)
            # ', vershiDelta: ' + 
            # str(vershiDelda.seconds) + 'fishingStatus:' + 
            # str(fishingStatus) + 'vershiStatus:' + 
            # str(fishingVershiStatus) 
            +'}'
        )
    )

    
    if vershiDelda.seconds > 320 and fishingStatus == 'stop':
        fishingVershiLoadingTime = datetime.datetime.now()
        pyautogui.press('g')
        time.sleep(11)
        pyautogui.press('g')
        time.sleep(5)

    if fishingStatus == 'stop':
        my_print('start')
        # time to buff
        if buffDelta.seconds > 240:
            lastBuff = datetime.datetime.now()
            pyautogui.press('s')
            time.sleep(4)
        fishingStatus = 'started'
        pyautogui.press('w')
        time.sleep(5)
    elif fishingStatus == 'started' and red < 85:
        my_print('ending')
        fishingStatus = 'ending'
        pyautogui.press('w')
        time.sleep(7)
    if fishingStatus == 'ending':
        my_print('stop')
        fishingStatus = 'stop'

time.sleep(5)
pyautogui.press('g')
time.sleep(5)

while True:
    imgRect = pyautogui.screenshot(region=(635, 367, 651 - 635, 387 - 367))
    pixels = imgRect.load()
    avg = [0, 0, 0]
    for x in range(imgRect.size[0]):
        for y in range(imgRect.size[1]):
            for i in range(3):
                avg[i] += pixels[x, y][i]
    red, g, b = tuple(c // (imgRect.size[0] * imgRect.size[1]) for c in avg)
    startFishing(red)
    time.sleep(.2)
