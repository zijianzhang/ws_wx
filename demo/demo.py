from flask import Flask,request,jsonify
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify(data='hello world!')


@app.route("/play/<string:playerId>/",defaults={'level': 0},methods=['GET','POST'])
@app.route("/play/<string:playerId>/<int:level>",methods=['GET','POST'])
def main(playerId,level):
    if request.method == 'GET':
        print("nb")
        return jsonify(level=level,) 

    if request.method == 'POST':
        import os,base64 
        if not os.path.isdir('file'):
            os.makedirs('file')
        files = os.listdir('file/')
        if playerId not in files:
            os.makedirs('file/'+playerId)
        filePath = 'file/'+playerId+'/'
        data = request.get_json()
        img = data.get('img','')
        if img:
            imgdata = base64.b64decode(img)
            with open(filePath+playerId+'-'+str(level)+'.jpg','wb') as p:
                p.write(imgdata)
            from random import randint
            score = {'level'+str(level)+'score':randint(1,100)}
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