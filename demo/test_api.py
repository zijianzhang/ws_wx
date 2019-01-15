import requests
import base64
import csv
import uuid
import json
import time
import binascii
import os
from Crypto.Cipher import AES        
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256

def padding(s):
    BS = 16
    return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

def mkRequest(aesKey, data):
    SERVER_PUBLIC_KEY, CLIENT_PRIVATE_KEY, orgCode, channelId = get_setting()
    format = "json"
    version = "1.0"
    encodeKey = base64.b64encode(SERVER_PUBLIC_KEY.encrypt(aesKey.encode(),0)[0]).decode("utf-8")
    IV = os.urandom(16)
    aes = AES.new(aesKey, AES.MODE_CBC, IV)
    requestData = base64.b64encode(aes.encrypt(padding(json.dumps(data)))).decode("utf-8")
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    requestId = str(uuid.uuid1()).replace('-','')[0:16]
    signMethod = "SHA256withRSA"
    post_data = {
        "channelId":channelId,
        "encodeKey":encodeKey,
        "format":format,
        "orgCode":orgCode,
        "requestData":requestData,
        "requestId":requestId,
        "signMethod":signMethod,
        "timestamp":timestamp,
        "version":version,
    }
    signer = PKCS1_v1_5.new(CLIENT_PRIVATE_KEY) 
    digest = SHA256.new(json.dumps(post_data,separators=(',',':')).encode()) 
    # digest = SHA256.new(json.dumps({"channelId":"C"},separators=(',',':')).encode()) 
    sign = base64.b64encode(signer.sign(digest)).decode("utf-8")
    print(sign)
    post_data = json.dumps({
        "encodeKey": encodeKey,
        "format": format,
        "orgCode": orgCode,
        "requestData": requestData,
        "requestId": requestId,
        "version": version,
        "signMethod": signMethod,
        "timestamp": timestamp,
        "channelId": channelId,
        "sign": sign
    })
    return post_data

def emotion():
    requestDataJson = {}
    with open('demo.jpg','rb') as p:
        fileBase64 = base64.b64encode(p.read()).decode("utf-8")
        requestDataJson["data"] = fileBase64
        requestDataJson["type"] = 0
    requestDataStr = json.dumps(requestDataJson)
    aesKey = str(uuid.uuid1()).replace('-','')[0:16]
    requestJson = mkRequest(aesKey, requestDataStr)
    print(requestJson)
    responseJson = requests.post("https://ipms.pingan.com/openapi/ai/emotion", data=json.loads(requestJson))
    return responseJson

def get_setting():
    with open('secret.csv','r') as s:
        test_secret = dict(filter(None,csv.reader(s)))
        SERVER_PUBLIC_KEY = RSA.importKey(base64.b64decode(test_secret['serverPublic']))
        CLIENT_PRIVATE_KEY = RSA.importKey(base64.b64decode(test_secret['cilentPrivate'])) 
        orgCode = test_secret['orgCode']
        channelId = test_secret['channelId']
    return SERVER_PUBLIC_KEY, CLIENT_PRIVATE_KEY, orgCode, channelId

if __name__ == '__main__':

    print(emotion().json())
  

