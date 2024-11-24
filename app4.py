# Como simular "rolagem" do mouse
import pyautogui
from time import sleep

pyautogui.moveTo(2600,587, duration=2)
for i in range(3):
    pyautogui.scroll(-900)
    sleep(0.5)