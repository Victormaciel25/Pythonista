from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver


driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app/')
# Situação 1 - Fechar alerta
# Descer a página até elementos estarem visíveis
driver.execute_script('window.scrollTo(0, 350);')
# Digitar meu nome
campo_nome = driver.find_element(By.ID, "nome")
sleep(1)
campo_nome.send_keys('Victor')
sleep(1)
botao_alerta = driver.find_element(By.ID,"buttonalerta")
sleep(2)
# Clicar em alerta
botao_alerta.click()
sleep(2)
# Clicar em OK para fehcar alerta
alerta1 = driver.switch_to.alert
alerta1.accept()
sleep(5)

# Situação 2 - Confirmar ou cancelar alerta
# Encontrar o campo continuar
botao_confirmar = driver.find_element(By.ID,"buttonconfirmar")
sleep(2)
# Clicar no campo de confirmar
botao_confirmar.click()
# Clicar em OK para fehcar alerta
alerta2 = driver.switch_to.alert
sleep(2)
# Confirmar
alerta2.accept()
# Cancelar
#alerta2.dismiss()

# Situação 3 - Inserir dados em alerta e depois confirmar ou cancelar esses dados, além de fechar a alerta posterior
# Encontrar o campo fazer pergunta
botao_pergunta = driver.find_element(By.ID, "botaoPrompt")
sleep(1)
botao_pergunta.click()
# Digitar algo dentro da alerta
alerta3 = driver.switch_to.alert
sleep(1)
alerta3.send_keys('Victor')
sleep(2)
# Clicar em confirmar (ou cancelar)
alerta3.accept()
sleep(1)
# Fechar a janela posterior
alerta3.dismiss()
sleep(1)

input('')
driver.close()