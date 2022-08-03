import requests

URL="https://oeps.mc.ax"

s = requests.Session()
# res = s.post(URL+"/search")

res = s.post(URL+"/submit")
print(res.text)
print(s.cookies.get_dict())
