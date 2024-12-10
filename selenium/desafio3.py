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
driver.maximize_window()
sleep(1)
driver.execute_script("window.scrollTo(0, 600);")
sleep(2)
conversivel = driver.find_element(By.ID, 'conversivelcheckbox')
offroad = driver.find_element(By.ID, 'offroadcheckbox')

conversivel.click()
sleep(1)
offroad.click()
sleep(1)

input('')
driver.close()
    