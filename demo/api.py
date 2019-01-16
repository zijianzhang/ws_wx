import requests
import base64
import csv
import uuid
import json
import time
import binascii
import os
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_v1_5 as pk
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256

def padding(s):
    BS = 16
    PADDING = '\0'
    pad_it = lambda s: s + (BS - len(s)%BS)*PADDING
    #pad_txt = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    return pad_it(s)

def mkRequest(aesKey, data):
    SERVER_PUBLIC_KEY, CLIENT_PRIVATE_KEY, orgCode, channelId = get_setting()
    format = "json"
    version = "1.0"
    cipher = pk.new(SERVER_PUBLIC_KEY)
    encodeKey = base64.b64encode(cipher.encrypt(aesKey.encode())).decode("utf-8")
    IV = '1234567812345678'.encode()
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
    sign = base64.b64encode(signer.sign(digest)).decode("utf-8")
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

def gtResponse(aesKey, data):
    IV = '1234567812345678'.encode()
    aes = AES.new(aesKey, AES.MODE_CBC, IV)
    responseData = json.loads(aes.decrypt(base64.b64decode(data)).decode())
    return responseData

def emotion(fileBase64):
# def emotion():
    requestDataJson = {}
    # with open('demo.jpg','rb') as p:
    #     fileBase64 = base64.b64encode(p.read()).decode("utf-8")
    requestDataJson["data"] = fileBase64
    requestDataJson["type"] = 0
    aesKey = str(uuid.uuid1()).replace('-','')[0:16]
    requestJson = mkRequest(aesKey, requestDataJson)
    responseJson = requests.post("https://ipms.pingan.com/openapi/ai/emotion", data=json.loads(requestJson))
    print(responseJson.json().get("responseMessage"))
    responseDataStr = responseJson.json().get("responseData")
    responseData = gtResponse(aesKey, responseDataStr)
    return responseData

def get_setting():
    with open('secret.csv','r') as s:
        test_secret = dict(filter(None,csv.reader(s)))
        SERVER_PUBLIC_KEY = RSA.importKey(base64.b64decode(test_secret['serverPublic']))
        CLIENT_PRIVATE_KEY = RSA.importKey(base64.b64decode(test_secret['cilentPrivate'])) 
        orgCode = test_secret['orgCode']
        channelId = test_secret['channelId']
    return SERVER_PUBLIC_KEY, CLIENT_PRIVATE_KEY, orgCode, channelId


if __name__ == "__main__":
    print(emotion())