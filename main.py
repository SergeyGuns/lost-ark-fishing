import pyautogui
import time
import sys
import datetime
import serial

fishingStatus = 'stop'  # started | ending
fishingVershiStatus = 'empty' # 'load' 
fishingVershiLoadingTime = datetime.datetime.now()
ser = serial.Serial('COM3', baudrate=9600, timeout=1)

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
        ser.write('R_G'.encode('utf-8'))
        time.sleep(11)
        ser.write('R_G'.encode('utf-8'))
        time.sleep(5)

    if fishingStatus == 'stop':
        my_print('start')
        # time to buff
        if buffDelta.seconds > 240:
            lastBuff = datetime.datetime.now()
            ser.write('R_S'.encode('utf-8'))
            time.sleep(4)
        fishingStatus = 'started'
        ser.write('R_W'.encode('utf-8'))
        time.sleep(5)
    elif fishingStatus == 'started' and red < 85:
        my_print('ending')
        fishingStatus = 'ending'
        ser.write('R_W'.encode('utf-8'))
        time.sleep(7)
    if fishingStatus == 'ending':
        my_print('stop')
        fishingStatus = 'stop'

time.sleep(5)
ser.write('R_G'.encode('utf-8'))
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
