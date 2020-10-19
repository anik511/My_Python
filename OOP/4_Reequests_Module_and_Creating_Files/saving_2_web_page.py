import requests
import os
import webbrowser as wb

url = "http://example.com/"
response = requests.get(url)
with open("example.html", "w", encoding=response.encoding) as web:
    web.write(response.text)
file_path = os.path.realpath("example.html")
print(file_path)
wb.open("file://" + file_path)
