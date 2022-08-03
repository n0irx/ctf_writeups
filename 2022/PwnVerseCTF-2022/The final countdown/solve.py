from requests import request


import requests

CHALLENGE_URL="https://challenges.hackrocks.com/launch-code/"
API_URL = "https://challenges.hackrocks.com/launch-code/get_current_code"
CHECK_CODE_URL="https://challenges.hackrocks.com/launch-code/check_code"

s = requests.session()

res = s.post(API_URL)
first_code = res.json()["current_code"]
current_code = first_code
while current_code == first_code:
    res = s.post(API_URL)
    current_code = res.json()["current_code"]
    print(current_code)

res = s.post(CHECK_CODE_URL, data={"code": current_code})
print(res.text)

