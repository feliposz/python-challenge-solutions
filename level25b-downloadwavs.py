import urllib.request
import pygame

def downloadfile(url):
#abrindo pagina com autenticação
    filename = url.split("/")[-1]
    passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, url, "butter", "fly")
    auth = urllib.request.HTTPBasicAuthHandler(passman)
    opener = urllib.request.build_opener(auth)
    urllib.request.install_opener(opener)

    page = urllib.request.urlopen(url)
    result = page.read()
    open("download\\" + filename, "wb").write(result)

for i in range(25):
    downloadfile("http://www.pythonchallenge.com/pc/hex/lake" + str(i+1) + ".wav")


