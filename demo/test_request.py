import requests,json,base64


url = "http://127.0.0.1:8080/play/sb/"
with open('owater.jpg','rb') as p:
    fileBase64 = base64.b64encode(p.read()).decode("utf-8")
r = requests.post(url,json={'img':fileBase64})

# r = requests.post(url)
print(r.json())