import requests
import json

response = requests.get('https://i.pinimg.com/736x/f3/e0/d9/f3e0d974fdc0639446596718fd649abf.jpg')
if 200 <= response.status_code < 300:
    with open('cbum.jpg', 'wb') as f:
        f.write(response.content)

url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
params = {
    'path': 'image.jpg'
}

headers = {
    # тут добавить токен:
    'Authorization': 'OAuth '
}
response = requests.get(url, params=params, headers=headers)

url_for_upload = response.json().get('href', '')

with open('cbum.jpg', 'rb') as f:
    response = requests.put(url_for_upload, files={"file": f})
    print(response.status_code)

assert 200 <= response.status_code < 300