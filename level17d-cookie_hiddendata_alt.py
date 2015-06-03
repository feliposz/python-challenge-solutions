import urllib.request, urllib.parse, re, bz2
url='http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
seed="12345"
info=b''
while True:
    req=urllib.request.urlopen(url+seed)
    text=req.read().decode()
    seed=''.join(re.findall(r"busynothing is (\d+)",text))
    for header in req.getheaders():
        if header[0] == 'Set-Cookie':
            cookies = header[1]        
    byte=cookies.split(';')[0].split('=')[1]
    info+=ord(urllib.parse.unquote_plus(byte))
    try :
        int(seed)
        print("   Info:",byte,"t   Next:",seed)
    except :
        print("   Info:",byte,"t   Last:",text)
        break
print("info:",bz2.decompress(info))
