import zipfile

path = "channel\\"
zip = "channel.zip"
num = "90052"

zf = zipfile.ZipFile(zip)
final = ""

for x in range(1000):
    file = zf.open(num + ".txt", "r")
    firstline = file.readline().decode()
    file.close()
    info = zf.getinfo(num + ".txt")
    #print(info.comment)
    final += (info.comment.decode())
    if firstline[0:15] == "Next nothing is":
        parts = firstline.split()
        num = parts[3]
    else:
        break

print(final)
