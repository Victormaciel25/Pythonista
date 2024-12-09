from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,600', '--incognito']
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
driver.get('https://cursoautomacao.netlify.app/desafios.html')

btn1 = driver.find_element(By.CSS_SELECTOR, '.btn.btn-info')
btn2 = driver.find_element(By.CSS_SELECTOR, '.btn2.btn.btn-dark')
btn3 = driver.find_element(By.CSS_SELECTOR, '.btn2.btn.btn-warning')

if btn1.is_enabled():
    print('Botão 1 está habilitato')
if btn1.is_enabled() == False:
    print('Botão 1 está desabilitado')
# ou usando "else"
if btn2.is_enabled():
    print('Botão 2 está habilitato')
else:
    print('Botão 2 está desabilitado')

if btn3.is_enabled():
    print('Botão 3 está habilitato')
else:
    print('Botão 3 está desabilitado')
    
input('')
driver.close()
    