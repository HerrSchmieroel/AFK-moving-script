import pyautogui
from pyautogui import keyDown , keyUp
from time import sleep

print("You have 5 seconds to go in your game")
sleep(5)
pyautogui.FAILSAFE = False

while True:
    keyDown('w')
    sleep(1)
    keyUp('w')
    keyDown('a')
    sleep(1)
    keyUp('a')
    keyDown('s')
    sleep(1)
    keyUp('s')
    sleep(1)
    keyDown('d')
    sleep(1)
    keyUp('d')