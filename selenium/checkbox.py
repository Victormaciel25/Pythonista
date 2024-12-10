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
driver.get('https://cursoautomacao.netlify.app')

checkbox_1 = driver.find_element(By.ID, 'acessoNivel1CheckBox')
checkbox_2 = driver.find_element(By.ID, 'acessoNivel2CheckBox')
checkbox_3 = driver.find_element(By.ID, 'acessoNivel3CheckBox')

checkbox_1.click()
checkbox_2.click()
if checkbox_1.is_selected() == True:
    print('checkbox 2 está selecionado')

input('')
driver.close()
    