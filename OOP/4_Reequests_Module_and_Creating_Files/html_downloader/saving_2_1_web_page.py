# The "requests module" allows you to send HTTP requests using Python.
import requests
# "os module" in Python provides functions for interacting with the operating system.
# This module provides a portable way of using operating system dependent functionality.
# os.path module is sub module of OS module in Python used for common path name manipulation.
import os
# In Python, "webbrowser module" provides a high-level interface which allows displaying Web-based documents to users.
# The "webbrowser module" can be used to launch a browser in a platform-independent manner.
import webbrowser as wb


class Web:
    # this __init__ method is a constructor
    # if we make a object of "Web" class this __init__ method also will be called automatically
    def __init__(self, url, file_name):
        # Instance attributes
        self.url = url
        self.file_name = file_name
        # Here "self.url & self.file_name" this are instance attribute of "w_obj" object
        # Now for this type of attribute(instance) we can not use class.attribute(ex: print(Web.url))
        # this will cause "AttributeError"

    def get_url(self):
        # Making a GET request to pul web page information
        # Now "response" is object of requests class & we are saving all data in it :).
        response = requests.get(self.url)
        # print(response.text)
        """We use open () function in Python to open a file in read or write mode.
        Open ( ) will return a file object. To return a file object we use open() function along with two arguments,
        that accepts file name and the mode, whether to read or write. So, the syntax being: open(filename, mode). 
        There are three kinds of mode, that Python provides and how files can be opened:
            “ r “, for reading.
            “ w “, for writing.
            “ a “, for appending.
            “ r+ “, for both reading and writing of string data ;)"""
        with open(self.file_name, "w", encoding=response.encoding) as dc:
            dc.write(response.text)

        """os.path.realpath() method in Python is used to get the canonical path of 
        the specified filename by eliminating any symbolic links encountered in the path."""
        file_path = os.path.realpath(self.file_name)
        print("File Path:", file_path)
        wb.open("file://" + file_path)


if __name__ == "__main__":
    print("Attention User!!!\nYou need to put a space after inputting URL\nIf you don't you will face error"
          "\nDemo:[Input your URL:http://example.com ]")
    url = input("Input your URL:")
    url = url.strip()
    file_name = input("Give a name to your file:")
    file_name = file_name + ".html"
    # Creating Object of Web class
    w_obj = Web(url, file_name)
    w_obj.get_url()
    print("Url:", url)
