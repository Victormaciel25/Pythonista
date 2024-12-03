import pyautogui

pyautogui.moveTo(x=1776, y=515, duration=1)
pyautogui.click(button='right')
pyautogui.move(-150, 150, duration=1)
pyautogui.click(button='left')
pyautogui.move(-220, -480, duration=2)
pyautogui.click(button='left')
pyautogui.write('Victor')