import requests

img_url = "https://goo.gl/JxktPw"
r = requests.get(img_url)
# print(r.text)
with open("pybook.jpg", "wb") as f:
    f.write(r.content)
