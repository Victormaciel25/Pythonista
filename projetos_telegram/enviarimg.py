# Token - 7813985225:AAFH7Amjy_yPeO2DCHZTRzIEJJ-KxllTJas
# URL do API - https://api.telegram.org/bot7813985225:AAFH7Amjy_yPeO2DCHZTRzIEJJ-KxllTJas/getUpdates
# Qual tipo de requisiçao?
import requests
from rich import print
from time import sleep

def obter_mensagens(apenas_ultima_mensagem=False):
    update_id = None
    token = '7813985225:AAFH7Amjy_yPeO2DCHZTRzIEJJ-KxllTJas'
    data = requests.get(f'https://api.telegram.org/bot{token}/getUpdates')
    if len(data.json()['result']) > 0:
        if apenas_ultima_mensagem == True:
            update_id = data.json()['result'][-1]['update_id']
            data = requests.get(f'https://api.telegram.org/bot{token}/getUpdates?offset={update_id}')
            print(data.json())
            print('#'*10)
        else:
            print(data.json())
            print('#'*10)

def enviar_mensagem(chat_id, text, disable_notification=False):
    token = '7813985225:AAFH7Amjy_yPeO2DCHZTRzIEJJ-KxllTJas'
    data = requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}&disable_notification={disable_notification}')
    print(data.json())

def enviar_imagem(links_imagens, chat_id, caption):
    token = '7813985225:AAFH7Amjy_yPeO2DCHZTRzIEJJ-KxllTJas'
    for link in links_imagens:
        data = requests.get(f'https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id}&photo={link}&caption={caption}')
        sleep(2)
# while True:
#     obter_mensagens(apenas_ultima_mensagem=True)
# enviar_mensagem(chat_id='-4686426252', text='Conseguimos', disable_notification=True)

imagens = ['https://i.ibb.co/j6HCjKd/foto1.jpg','https://i.ibb.co/YP34cBY/foto2.jpg']
enviar_imagem(links_imagens=imagens, chat_id='-4686426252', caption='Programador!')
