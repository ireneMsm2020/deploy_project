import requests
import numpy as np
import json
import cv2

addr = 'http://127.0.0.1:5000'
upload_url= addr + '/upload'
down_url = addr+ '/download'
content_type = 'application/json'
headers = {'content-type': content_type}

img_path='/home/Pictures/index.jpeg'
Img=cv2.imread(img_path)
#temp = np.zeros((2,4))+0.1

temp=Img.tolist()
json_f1=json.dumps({'data':temp})

response = requests.post(upload_url, json=json_f1, headers=headers)
#print(response.text)
#data = {"fileName": "test.jpg"}
re_json=response.json()
Imgdata=np.array(re_json['image'])
print('success')
print(Imgdata.shape)


