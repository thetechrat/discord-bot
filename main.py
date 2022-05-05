import requests
import random
from time import sleep
import discum
from discum.gateway.session import guild
channel_id='966149952747237426'

count = 0

token='ODI2Nzk1NjI4NDE1NTQ5NDUx.YYnzaw.Mh-xmcsukXtVwCym3Ok2-FX77xo'


bot = discum.Client(token=token)


def sendMessage(token, channel_id, message):
    try:
        url = 'https://discord.com/api/v9/channels/{}/messages'.format(channel_id)
        data = {"content": message}
        header = {"authorization": token}

        r = requests.post(url, data=data, headers=header)
        if r.status_code == 200:
            print(f'quote sent: {message} \n')
        else:
            print(r.raise_for_status())
    except Exception as e:
        print(e)

    
    sleep(random.randint(15,20))



LIST=[]

while True:
    try:    

        with open('read.txt') as f:
         lines = f.readlines()
    
        print (lines[count])
        message =  lines[count]
      
        taguser=message
        
        with open('readme.txt', 'w') as f:
            f.write(lines[count])
        
        sendMessage(token,channel_id,taguser)
        count = count + 1
      #  sendMessage(token2,channel_id,taguser2)
    except Exception as e:
        sleep(360)
        print(e)