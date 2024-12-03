# Alertar e pedir informação no PyAutoGui
import pyautogui
# Alerta de iniciação de automação
# pyautogui.alert(text='Iniciando sua automação', title='Automação do Login', button='ok')

# Pedir informações
email = pyautogui.prompt(text='Digite seu e-mail', title='informações obrigatórias')
print(f'Você digitou {email}')

# Confirmar se algo deve ou não acontecer
resposta = pyautogui.confirm(text='Continuar rodando nossa automação?', title='confirmação', buttons=['sim','não','cancelar'])
if resposta == 'sim':
    print('continuando automação')
elif resposta == 'não':
    print('encerrando automação')
else:
    print('operação cancelada')

# Mascarar senha
senha = pyautogui.password(text='Digite sua senha:', title='Dados de login', mask='*')
print(senha)