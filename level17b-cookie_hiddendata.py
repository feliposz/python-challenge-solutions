import urllib.request
import urllib.parse
import bz2
import re

#first run
num = "12345"
#second part
#num = str(int(92118/2))

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="

data=""

for x in range(500):
    page = urllib.request.urlopen(url + str(num))
    mystr = page.read().decode()
    num = ''.join(re.findall(r"busynothing is (\d+)",mystr))

    headers = page.getheaders()
    for h in headers:
        if h[0] == "Set-Cookie":
            byte = h[1].split(";")[0].split('=')[1]
            print("byte(" + x + ") = " + byte)
            data += byte

    if not num.isdigit():
        break

print("Data: " + data)
print("Final: " + mystr)

#can't understand why this isn't working
info = bz2.decompress(urllib.parse.unquote_plus(data).encode("latin_1"))
print("Info = " + info)



import xmlrpc.client
url = "http://www.pythonchallenge.com/pc/phonebook.php"
proxy = xmlrpc.client.ServerProxy(url)
#from call his (Mozart's) father
print(proxy.phone("Leopold"))
#555-VIOLIN
        
#need to pass a cookie
#http://www.pythonchallenge.com/pc/stuff/violin.php
