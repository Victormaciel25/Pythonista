import webbrowser
import pyautogui
from time import sleep

telefones = []

with open('fones.txt', 'r') as arquivo:
    for linha in arquivo:
        telefones.append(linha.split('\n')[0])
    print(telefones)

for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(3)
    pyautogui.click(2762, 418, duration=1)
    sleep(5)
    pyautogui.click(548,1007, duration=1)
    sleep(1)
    pyautogui.typewrite('Olá')
    sleep(1)
    pyautogui.press('enter')