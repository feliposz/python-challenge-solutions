import urllib.request
import sys
#import http.cookiejar

#abrindo pagina com autenticação
url = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()
passman.add_password(None, url, "butter", "fly")
auth = urllib.request.HTTPBasicAuthHandler(passman)
opener = urllib.request.build_opener(auth)
urllib.request.install_opener(opener)

#for the first part Range -> bytes 0-30202/2123456789

#offset = 30203
#offset = 2123456789
#offset = 2123456712
offset = 1152983631

while True:
    req = urllib.request.Request(url, headers={'Range': "bytes=" + str(offset) + "-"})

    try:
        page = urllib.request.urlopen(req)
    except:
        print("Error!", sys.exc_info()[0])
        break

    rangestr = page.getheader("Content-Range")
    print("Range =", rangestr)

    result = page.read()
    open("beyond.jpg", "wb").write(result)
    #print("Result =", result)


    endbyte = rangestr.split()[1].split("/")[0].split("-")[1]

    break #for the sceond part

    if endbyte.isdigit():
        offset = int(endbyte) + 1
    else:
        break
    

