from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as condicao_esperada

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
    
    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )

    return driver, wait


driver, wait = iniciar_driver()
driver.implicitly_wait(10)

driver.get('https://google.com/flights')
sleep(1)
driver.maximize_window()
sleep(1)
driver.execute_script("window.scrollTo(0, 500);")
sleep(1)
sugestoes_de_voo = wait.until(condicao_esperada.visibility_of_all_elements_located((By.XPATH, "//div[@class='OJsCSd']")))
sleep(1)
sugestoes_de_voo = wait.until(condicao_esperada.visibility_of_any_elements_located((By.XPATH, "//div[@class='OJsCSd']")))
sleep(1)
sugestoes_de_voo[0].click()
# ---------------- outro exemplo, para login -----------------
driver.get('https://cursoautomacao.netlify.app/login')

campo_email = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//input[@id='email']")))

campo_email.send_keys('jhonatan@hotmail.com')

input('')
driver.close()
    