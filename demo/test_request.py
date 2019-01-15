import requests,json,base64


url = "http://127.0.0.1:5000/play/nb/2"
with open('owater.jpg','rb') as p:
    fileBase64 = base64.b64encode(p.read()).decode("utf-8")
r = requests.post(url,json={'img':fileBase64})

print(r.json())