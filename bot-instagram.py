import webbrowser
import pyautogui
from time import sleep
from loginesenha import login,senha

# 1 - Navegar até o site https://instagram.com
webbrowser.open_new_tab('https://www.instagram.com/accounts/login/')
sleep(2)
# 2 - Entrar com meu usuário
pyautogui.click(2605,447,duration=1)
pyautogui.write(login)
sleep(1)
# 3 - Entrar com a minha senha
pyautogui.click(2606,490,duration=1)
pyautogui.write(senha)
sleep(1)
# 4 - Clicar em "login"
pyautogui.click(2715,539,duration=1)
sleep(6)
# 5 - Clicar em "Not now" para não salvar no navegador
pyautogui.click(2829,716,duration=1)
sleep(4)
# 6 - Fechar janela de "salvar senha"
# 7 - Pesquisar pela pagina
pyautogui.click(1987,447,duration=1)
sleep(2)
pyautogui.write('nike')
sleep(2)
# 8 - Entrar na pagina
pyautogui.click(2085,432,duration=1)
sleep(2)
# 9 - Clicar na postagem mais recente
pyautogui.click(2512,903,duration=1)
sleep(3)
# 10 - Verificar se já curti ou não aquela postagem
like = pyautogui.locateCenterOnScreen('like.png')
sleep(1)
# 11 - Se já tiver curtido, fazer nada, e pausar o bot por 24 horas
if like is not None:
    sleep(86400)
# 12 - Se não tiver curtido, curti a foto
elif like == None:
    pyautogui.click(2797,919,duration=1)
    sleep(5)
# 13 - Se não tiver curtido, comentar na foto
    pyautogui.click(2836,921,duration=1)
    sleep(3)
    pyautogui.typewrite('Legal')

# 14 - Pausar por 24 horas
# 15 - Após as 24 horas rodar tudo de novo

