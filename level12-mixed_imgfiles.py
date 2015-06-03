file = open("evil2.gfx", "rb")
gfxbin = file.read()
file.close()
for i in range(5):
	newfile = open("evil2gfx_" + str(i) + ".jpg", "wb")
	newfile.write(gfxbin[i::5])
	newfile.close()
	
