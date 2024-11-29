# Reconhecimento de imagem simples com pyautogui
import pyautogui

# Encontrar as coordenadas próximas de onde aquela imagem está
print(pyautogui.locateAllOnScreen('1.png'))
# Encontrar a coordenada do centro de uma imagem
print(pyautogui.locateCenterOnScreen('1.png'))
local = pyautogui.locateCenterOnScreen('1.png')
# Como usar na prática
pyautogui.click(local, duration=2)