import os
import json
import requests
import base64
from PIL import Image
from IPython.display import display
from IPython.display import Image as Show
from sys import exit
from time import sleep
apiKey = 'xxx'
def get_payload(imgData):
    # Establish the payload, which includes our image data as a long string of text
    payload = {
        'requests':[
            {
                'image':{
                    'content': imgData
                },
                'features':[
                    {
                        'type':'LABEL_DETECTION'
                    },
                ]
            }
        ]
    }
    return payload

# Here we open our boat file and convert it into image data text (called base-64-encoded text)
res = []
for file in os.listdir('data/images/'):
    with open('data/images/'+file, "rb") as img:
        print ('data/images/'+file)
        imgData = str(base64.b64encode(img.read()).decode("utf-8"))
        payload = get_payload(imgData)
        googleUrl = 'https://vision.googleapis.com/v1/images:annotate?key=' + apiKey
        r = requests.post(googleUrl, json=payload)
        response = json.loads(r.text)
        response['root'] = 'data/images/'+file
        
        res.append(response)
        with open('data/json/data.json', 'w') as file:
            json.dump(res, file, indent=4)
        sleep(3)
        
        