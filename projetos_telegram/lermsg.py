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

while True:
    obter_mensagens(apenas_ultima_mensagem=True)
