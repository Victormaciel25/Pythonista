# Como tirar print(foto) da tela inteira ou parte dela
import pyautogui
# Tirar print da tela inteira
pyautogui.screenshot('tela.jpg')
# Tirar um print de parte da tela
pyautogui.screenshot('calculado.jpg',region=(1426,159,327,506))