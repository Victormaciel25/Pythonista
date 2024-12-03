# Como pegar e "arrastar" algo para outro lugar
import pyautogui

for i in range(8):
    # Mover até um coord
    pyautogui.moveTo(2277,347, duration=1)
    # Clicar arrastar até um ponto e soltar
    pyautogui.dragTo(3272,622, button='left', duration=0.5)

