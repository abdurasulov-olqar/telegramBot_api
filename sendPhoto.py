import os 
import requests


TOKEN ="5591155154:AAHn0llNadmGCykPsdpkfc5OXcv54S0MQyc"
def sendPhoto(chat_id:str,photo:str):
    URL = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    
    payload = {
                "chat_id": chat_id,
                "photo": photo
                }
    return requests.get(url=URL, params=payload)

        




photo_url='https://random.dog/2bff25d0-c721-4078-8cc9-f3ce6b464428.jpg'
# photo_id = 'AgACAgIAAxkDAAMgY7evYvSyDJQ8DS-1S5Irjcd9cIgAAoa_MRvjDsFJ4H7lvD-PEXwBAAMCAAN4AAMtBA'
# img = open('logo.jpg','rb').read()

sendPhoto("1503632278", photo_url)

# send photo with three ways: url, id, file
