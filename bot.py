import time
import pyautogui
from PIL import ImageGrab, ImageOps
from numpy import *


class Coordinates():
    replayBtn = (341, 419)
    dinasaur = (176, 359)
    # 216 383

def restartGame():
    pyautogui.click(Coordinates.replayBtn)
    pyautogui.keyDown("down")


def pressSpace():
    pyautogui.keyUp("down")
    pyautogui.keyDown("space")
    time.sleep(0.2)
    pyautogui.keyUp("space")
    pyautogui.keyDown("down")


def imageGrab():
    box = (238, 440, 285, 450)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print (a.sum())
    return (a.sum())


def main():
    restartGame()
    while True:
        if (imageGrab() != 717):
            pressSpace()
            time.sleep(0.1)


main()
