import requests

URL="http://maas.chal.imaginaryctf.org"
res = requests.get(URL+"/users")
print(res.text)

ADMIN_UUID="015d8174-10ca-11ed-8b52-eaba7a1d8dc7"
