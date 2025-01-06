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

def enviar_audio(links_audios, chat_id, caption):
    token = '7813985225:AAFH7Amjy_yPeO2DCHZTRzIEJJ-KxllTJas'
    for link in links_audios:
        data = requests.get(f'https://api.telegram.org/bot{token}/sendAudio?chat_id={chat_id}&audio={link}&caption={caption}')
        print(data.json())
        sleep(1)


# while True:
#     obter_mensagens(apenas_ultima_mensagem=True)
# enviar_mensagem(chat_id='-4686426252', text='Conseguimos', disable_notification=True)

# imagens = ['https://i.ibb.co/j6HCjKd/foto1.jpg','https://i.ibb.co/YP34cBY/foto2.jpg']
# enviar_imagem(links_imagens=imagens, chat_id='-4686426252', caption='Programador!')

audios = ['https://download1589.mediafire.com/ldzeagdongcgUJZ2Z4UyWFYV15pop8DUUZSIPVP0Uoco-duW1IkxD4_iz5OlUUHNtH14HoLJm4fPf-wTLYZHvAW7bs1TSSSdmZxcIjUqxZ6oQ1qqNvVmXZ8cIv-Ux8dlSxz8zJQYgzOrrzNTx9SkGeysoSq_Lr5u0BlmkYFGIq5TIaME/bj39g1bjtfep6ax/Melhor+Dia+7+-+Sossego+%28Marcos+Baroni%2C+Teto%2C+Wiu%2C+Edi+Rock%2C+Alee%2C+Brand%C3%A3o%29.mp3', 'https://download1322.mediafire.com/32k4lkajcdrgkIeP4RifbGI5Ltd-93tUG_7smPNFEWgS02LAYu2gFv7-bjwrD2gM9fLKBPv0p9PurJMFlWp30-_QHsnFUQjQy6EEen3wCD5VSCJxYb8AwRaNM-qXOtzzLQknxHCto6UgWGhG2BzXzj3LuMghc_hC5GItGZMxZBqmdYW2/0jnl3yhyook2joy/Nattan+e+L%C3%A9o+Foguete+-+%C3%9Altima+Noite.mp3']

enviar_audio(links_audios=audios, chat_id='-4686426252', caption='Audio')
