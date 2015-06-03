import hashlib

desired = "bbb8b499a0eef99b52c7f13f4e78c24b"

broken = open("mybroken.zip", "rb")
data = broken.read()
broken.close()

current = ""

for diff in range(255):
    print ("Trying diff:", diff)
    for i in range(len(data)):
        #print ("Byte:", i)
        fix = bytearray(data)
        fix[i] = int((fix[i] + diff) % 256)
        h = hashlib.md5()
        h.update(fix)
        current = h.hexdigest()
        #print(len(data))
        if desired == current:
            print("FOUND!!!! offset = ", i)
            print("Broken = " + str(data[i]) + " Fixed = " + str(fix[i]))
            print(current)
            open("myfixed.zip", "wb").write(fix)
            break
    if desired == current:
        break        
