import pyautogui
import time
import math, operator
from functools import reduce 
from PIL import Image
from PIL import ImageChops
from PIL import Image
import sys

fishingStatus = 'stop' # started | ending
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


time.sleep(2)



while True:
    imgRect = pyautogui.screenshot(region=(500,250,750 - 500, 450 - 250))
# imgRect.save("source.png")
    pixels = imgRect.load()
    avg = [0, 0, 0]
    for x in range(imgRect.size[0]):
        for y in range(imgRect.size[1]):
            for i in range(3):
                avg[i] += pixels[x, y][i]
    red,g,b = tuple(c // (imgRect.size[0] * imgRect.size[1]) for c in avg) 
    my_print(red)
    # image_one = sourceRect
    # image_two = imgRect
    # if  len(diffArr) > 5:
    #   diffArr = diffArr[1:5];
    # diff = compare(image_one, image_two)
    # diffArr.append(diff)
    # my_print(average(diffArr))
    # startFishing()
    # if diff.getbbox():
    #     print("images are different")
    # else:
    #     print("images are the same")
    time.sleep(.5)

