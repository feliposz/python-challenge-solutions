import urllib.request

#first run
#num = "12345"

#second part
num = str(int(92118/2))

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

for x in range(400):
    page = urllib.request.urlopen(url + str(num))
    mystr = page.read().decode()
    parts = mystr.split()
    num = parts[len(parts)-1]
    print(num)
    if not num.isdigit():
        break

print("Final: " + mystr)
        

