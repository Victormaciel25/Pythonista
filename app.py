# Como usar a função click
import pyautogui

# Click personalizado
pyautogui.click(x=1611, y=507, clicks=5, interval=0.5, button='left', duration=2)

# Click na posição atual
pyautogui.click()
pyautogui.click(button='left')
pyautogui.click(button='right')
pyautogui.click(button='middle')