import urllib.request
#import http.cookiejar

#abrindo pagina com autenticação
#url = "http://www.pythonchallenge.com/pc/return/play.html"
url = "http://www.pythonchallenge.com/pc/hex/decent.html"
passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()
passman.add_password(None, url, "huge", "file")
auth = urllib.request.HTTPBasicAuthHandler(passman)
opener = urllib.request.build_opener(auth)
urllib.request.install_opener(opener)

page = urllib.request.urlopen(url)
result = page.read()
print(result)
