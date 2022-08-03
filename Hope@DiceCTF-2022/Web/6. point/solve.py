import requests

URL="https://point.mc.ax/"

s = requests.Session()
payload = {"What_point":"that_point"}
res = s.post(URL, json=payload)
print(res.text)
