import urllib.request
import urllib.parse

info='the flowers are on their way'
url='http://www.pythonchallenge.com/pc/stuff/violin.php'
req = urllib.request.Request(url, headers={'Cookie': 'info=' + urllib.parse.quote_plus(info)})
page = urllib.request.urlopen(req)

print(page.read())
