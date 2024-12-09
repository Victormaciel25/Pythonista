from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1000,900', '--incognito']
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
# navegar até o site
driver.get('https://cursoautomacao.netlify.app')
driver.maximize_window()
# encontrar e clicar no link de login
botao_desafios = driver.find_element(By.LINK_TEXT, 'Desafios')
botao_desafios.click()
sleep(1)
# encontrar e clicar no campo de email
campo_nome = driver.find_element(By.CLASS_NAME, 'form-control')
sleep(1)
# digitar meu email
campo_nome.send_keys('Victor de Oliveira Maciel Rodrigues')
sleep(1)
# encontrar e clicar no campo senha
botao_cliqueaqui = driver.find_element(By.LINK_TEXT, 'Clique aqui')
botao_cliqueaqui.click()

input('')
driver.close()
    