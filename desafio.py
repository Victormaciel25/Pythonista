import pyautogui

email = pyautogui.prompt(text='Digite seu e-mail', title='Informações obrigatórias')
senha = pyautogui.password(text='Digite sua senha', title='Informações obrigatórias', mask='*')
pyautogui.click(2178,476, duration=1)
pyautogui.write(email)
pyautogui.hotkey('enter')
pyautogui.write(senha)
