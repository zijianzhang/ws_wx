import json
import api
import random
import os
import base64
from PIL import Image
from flask import Flask,request,jsonify
from utils import resize_by_size,getEmoji,initialEmoji

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify(data='hello world!')

@app.route("/play/<string:playerId>/",defaults={'level': 0},methods=['GET','POST'])
@app.route("/play/<string:playerId>/<int:level>",methods=['GET','POST'])
def main(playerId,level):
    if request.method == 'GET':
        print("nb")
        emoji = initialEmoji()
        return jsonify(level=level,emoji=emoji) 

    if request.method == 'POST':
        if not os.path.isdir('file'):
            os.makedirs('file')
        files = os.listdir('file/')
        if playerId not in files:
            os.makedirs('file/'+playerId)
        filePath = 'file/'+playerId+'/'
        data = request.get_json()
        imgdata = data.get('img','')
        if imgdata:
            imgPath = filePath+playerId+'-'+str(level)+'.jpg'
            imgdata = resize_by_size(imgdata, imgPath)
            score = api.emotion(imgdata)
            score = getEmoji(score)
            with open(filePath+playerId+'-'+str(level)+'.json','wb') as s:
                s.write(str(score).encode())
        else:
            score = {'score':-1}
        return jsonify(score=score)

class player(object):
    def __init__(self):
        self.name = None
        self.id = None
        self.level = 0
        self.score = []

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000)
    print('nb')

