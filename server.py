from flask import Flask, request, Response
import numpy as np 
import json
import os
import cv2

app= Flask(__name__)
run_path='./'
upload_folder='upload'

@app.route('/upload',methods=['POST'])

def upload():
    r=request.json
    r_json=json.loads(r)
    data = r_json['data']
    numpy_data=np.array(data)
    file_dir = run_path+upload_folder
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    imgname='temp.jpg'
    cv2.imwrite(os.path.join(file_dir,imgname), numpy_data)

    #response ={'message':'shape:{}'.format(numpy_data.shape)}
    response ={'image':data}
    response_pickled = json.dumps(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")

@app.route('/download',methods=['GET'])
def download():
    #fullfilename=request.json['fileName']
    fullfilename='temp.jpg'
    filepath=os.path.join(run_path+upload_folder, fullfilename)
    if not os.path.isfile(filepath):
        print("nononofile!")
        return
    print(filepath)
    Img=cv2.imread(filepath)
    #cv2.imshow('IMG',Img)
    #cv2.waitKey(1)
    data=Img.tolist()
    json_img = json.dumps({'data': data})
    response = Response(json_img,mimetype='application/json')
    return response
 

if __name__ == '__main__':
    app.run()
