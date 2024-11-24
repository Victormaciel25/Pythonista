# Como digitar com PyAutoGui
import pyautogui
# Biblioteca para escrever caracteres especiais
import pyperclip

# Função do pyperclip para copiar e colar caracteres especiais
def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

pyautogui.moveTo(2139,475, duration=1)
pyautogui.click()
escrever_frase('Automação é Incrivel')