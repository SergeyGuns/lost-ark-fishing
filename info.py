import pyautogui
import time
import math, operator
from functools import reduce 
from PIL import Image
from PIL import ImageChops
from PIL import Image
import sys

def my_print(text):
    sys.stdout.write(str(text))
    sys.stdout.write(str('\n'))
    sys.stdout.flush()

while True: 
    my_print(pyautogui.position())
    time.sleep(.1)