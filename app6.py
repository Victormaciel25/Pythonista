# Como usar botões e atalhos do teclado
import pyautogui
# Nome das teclas do teclado
# print(pyautogui.KEYBOARD_KEYS)

# como usar combinações de teclas
pyautogui.click(1503,234, duration=2)
# simular "segurar uma tecla"
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('ctrl','c')
pyautogui.click(1468,516, duration=2)
pyautogui.hotkey('ctrl','v')

