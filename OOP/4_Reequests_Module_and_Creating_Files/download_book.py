import requests
import sys

base_url = "http://subeenn.com/download/"
info = {"name": "Subeen", "email": "book@subeen.com", "country": "Bangladesh"}
url = base_url + "process.php"
res = requests.post(url, data=info)
# print(res.text)
# print(res.content)
if res.ok is False:
    sys.exit("Error downloading the file")
with open("cpbook.pdf", "wb")as fp:
    fp.write(res.content)
print("Book download complete!")
