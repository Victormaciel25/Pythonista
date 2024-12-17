from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
# Tem que importar o WebDriverWait para poder usar e fazer alterações no def iniciar_driver
from selenium.common.exceptions import *
# Essa importação vai te ajudar na hora que ocorrer um erro dentro da automação, que vai ser inserido dentro do iniciar_driver em ignored_exceptions
from selenium.webdriver.support import expected_conditions as CondicaoEsperada
# São as condições esperadas que pode ocorrer dentro da automação, o "as CondicaoEsperada" é como um apelido para chamar essa importação
from loginesenha import login,senha


def iniciar_driver():
    chrome_options = Options()
    # Fonte de opções de switches https://peter.sh/experiments/chromium-command-line-switches/

    arguments = ['--lang=pt-BR', '--start-maximized',
                 '--incognito']
    ''' Common arguments
    --start-maximized # Inicia maximizado
    --lang=pt-BR # Define o idioma de inicialização, # en-us , pt-BR
    --incognito # Usar o modo anônimo
    --window-size=800,800 # Define a resolução da janela em largura e altura
    --headless # Roda em segundo plano(com a janela fechada)
    --disable-notifications # Desabilita notificações
    --disable-gpu # Desabilita renderização com GPU
    '''
    for argument in arguments:
        chrome_options.add_argument(argument)

    # Colocar sempre duas barras para o caminho \\
    caminho_padrao_para_download = 'C:\\Users\\anton\\Downloads'

    # Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/32352ad08ee673a4d43e8593ce988b224f6482d3/chrome/common/pref_names.cc
    chrome_options.add_experimental_option("prefs", {
        'download.default_directory': caminho_padrao_para_download,
        # Atualiza diretório para diretório passado acima
        'download.directory_upgrade': True,
        # Setar se o navegar deve pedir ou não para fazer download
        'download.prompt_for_download': False,
        # Desabilita notificações (pode atrapalhar na automatização )
        "profile.default_content_setting_values.notifications": 2,
        # Permite realizar múltiplos downlaods multiple downloads
        "profile.default_content_setting_values.automatic_downloads": 1,
    })

    driver = webdriver.Chrome(options=chrome_options)

    # Aqui fica a alteração para poder usar o wait
    wait = WebDriverWait(
        driver,
        10,  # tempo que vai usar para carregar a página
        poll_frequency=1,  # ele vai tentar fazer uma ação de 1 em 1 seg
        # dentro do ignored_exceptions vamos colocar os erros que pode acontecer dentro da automação caso a página não tenha carregado, assim não vai aparecer o erro dentro do programa e ele vai continuar até que ele consiga executar
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException
        ]
        # LEMBRANDO ele vai carregar a página por 10seg, vai tentar fazer a primeira ação no intervalo de 1seg e os erros que mais acontece estão sendo ignorados de aparecer. Tem a documentação salva no arquivo "wait ou sleep"
    )
    return driver, wait


# assim ele vai retornar as duas variável dentro de uma vez
driver, wait = iniciar_driver()

# Entrar no site do instagram
driver.get('https://www.instagram.com/')

# Clicar e digitar meu usuário
campo_usuario = wait.until(CondicaoEsperada.element_to_be_clickable((By.XPATH,'//input[@name="username"]')))
campo_usuario.send_keys(login)
sleep(1)

# Clicar e digitar minha senha 
campo_senha = wait.until(CondicaoEsperada.element_to_be_clickable((By.XPATH,'//input[@name="password"]')))
campo_senha.send_keys(senha)
sleep(1)

# Clicar no campo entrar
botao_entrar = wait.until(CondicaoEsperada.element_to_be_clickable((By.XPATH,'//div[text()="Entrar"]')))
sleep(2)
botao_entrar.click()
sleep(3)
# Navegar até a página alvo
driver.get('https://www.instagram.com/disciplinados_ofc')
sleep(3)

while True: 
    # Clicar na última  postagem
    postagens = wait.until(CondicaoEsperada.visibility_of_any_elements_located((By.XPATH, '//div[@class="_aagw"]')))
    sleep(3)
    postagens[0].click()
    sleep(3)
    # Verificar se postagem foi curtida, caso não tenha sido, clicar curtir, caso já tenha sido, aguardar 24hrs
    try:
        verifica_curtida = driver.find_element(By.XPATH,'//section//div[@role="button"]//*[@aria-label="Curtir"]')
    except:
        print('A imagem já havia sido curtida.')
        sleep(86400)
    else:
        botao_curtir = driver.find_elements(By.XPATH,'//article[@role="presentation"]//section//div[@role="button"]')
        sleep(5)
        driver.execute_script('arguments[0].click()', botao_curtir[0])
        print('Deu certo! A imagem acabou de ser curtida.')
        sleep(86400)