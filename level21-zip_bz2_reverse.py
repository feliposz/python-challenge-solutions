import cys_magic
import zlib, bz2

packFileName = "unreal\\package.pack"

print(cys_magic.file(packFileName))

pack = open(packFileName, "rb")
contents = pack.read()

zflag = False
bz2flag = False
reverse = False
log = ''
while True:
    try:
        contents = zlib.decompress(contents)
        zflag = True
        reverse = False
        print(".", end="")
    except:
        zflag = False

    try:
        contents = bz2.decompress(contents)
        bz2flag = True
        reverse = False
        print("@", end="")
    except:
        bz2flag = False

    if (zflag == False and bz2flag == False):
        if (reverse):
            break
        contents = contents[::-1]
        reverse = True

print(contents)
