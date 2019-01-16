from PIL import Image
import os
import base64
import random

def resize_by_size(imgdata, imgPath):
    """按照生成图片文件大小进行处理(单位B)"""
    size = 512*1024
    img = base64.b64decode(imgdata)
    with open(imgPath,'wb') as p:
        p.write(img)
    im = Image.open(imgPath)
    size_tmp = os.path.getsize(imgPath)
    print(size_tmp/1024)
    q = 100
    while size_tmp > size and q > 0:
        print(q)
        out = im.resize(im.size, Image.ANTIALIAS)
        out.save(imgPath, quality=q)
        size_tmp = os.path.getsize(imgPath)
        q -= 5
    with open(imgPath,'rb') as p:
        fileBase64 = base64.b64encode(p.read()).decode("utf-8")
    return fileBase64

def getEmoji(rawData):
    data = []
    for r in rawData:
        d = {}
        d['rect'] = r['rect']
        emoji = []
        for e in r['emot']:
            if e['confid'] > 0.1:
                print()
                emoji.append(e)
            else:
                break
        d['emot'] = emoji
        data.append(d)
    return data

def initialEmoji():
    emoji = [   'Joy', 'Optimism', 'Pride', 'Vitality', 'Harmony', 'Hate',
                'Surprise', 'Calm', 'Interest', 'Embarrassed', 'Grievance',
                'Conflict', 'Aggressiveness', 'Sincerity', 'Apprehension',
                'Serenity', 'Trust', 'Anticipation', 'Angry', 'Disgust', 
                'Love', 'Cowardice', 'Deceptiveness', 'Acceptance', 'Annoyance', 
                'Gratitude', 'Insincerity', 'Contempt', 'Fatigue', 'Submission', 
                'Admiration', 'Desire', 'Envy', 'Fear', 'Depression', 
                'Boredom', 'Passiveness', 'Bravery', 'Suspicion', 'Puzzlement', 
                'Awe', 'Distraction', 'Sadness', 'Neglect', 'Boastfulness', 
                'Pessimism', 'Neutral', 'Uneasiness', 'Insult', 'Tension', 
                'Disapproval', 'Defiance', 'Shame', 'Remorse']
    random.shuffle(emoji)
    return emoji[0]