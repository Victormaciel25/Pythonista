import pyautogui
import keyboard
from time import sleep

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(1291,760,(12,152,33)):
        pyautogui.press('a')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(1378,761,(254,15,23)):
        pyautogui.press('s')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(1378,761,(254,15,23)):
        pyautogui.press('j')
        sleep(0.05)