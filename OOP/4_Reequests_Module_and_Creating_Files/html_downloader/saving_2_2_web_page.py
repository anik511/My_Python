import saving_2_1_web_page as swp

print("Attention User!!!\nYou need to put a space after inputting URL\nIf you don't you will face error"
      "\nDemo:[Input your URL:http://example.com ]")
user_url = input("Input your URL:")
user_url = user_url.strip()
file_name = input("Give a name to your file:")
file_name = file_name + ".html"
print(type(file_name), type(user_url))
print(file_name, user_url)
obj = swp.Web(user_url, file_name)
obj.get_url()
print("Url:", obj.url)
