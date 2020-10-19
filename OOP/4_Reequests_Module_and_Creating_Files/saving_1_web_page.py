import requests

url = "http://example.com/"
response = requests.get(url)
with open("example.html", "w") as web:
    web.write(response.text)
