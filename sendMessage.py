import os
import time
import requests



TOKEN = '5591155154:AAHn0llNadmGCykPsdpkfc5OXcv54S0MQyc'
URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

BASE_URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

update_id = -1

while True:
    response = requests.get(url=BASE_URL)
    updates=response.json()['result']

    last_update = updates[-1]

    last_update_id = last_update['update_id']
    if update_id != last_update_id:

        last_msg = last_update['message']
        if "text" in last_msg.keys():
            # print(last_msg.keys())
            chat_id = last_msg['chat']['id']
            text = last_msg['text']
        
        
            # print(chat_id)
            payload = {
                "chat_id": chat_id,
                "text": text
                }
            requests.get(url=URL, params=payload)

            update_id = last_update_id
    time.sleep(1)

