import pyautogui

local = pyautogui.locateCenterOnScreen('captcha.png')
pyautogui.click(local, duration=2)