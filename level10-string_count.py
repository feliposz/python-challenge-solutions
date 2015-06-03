def minhaString(mystr):
    oldchar = mystr[0]
    cont = 0
    novaStr = ""
    for char in mystr:
       if char == oldchar:
          cont += 1
       else:
          novaStr += str(cont) + oldchar
          cont = 1
          oldchar = char
    novaStr += str(cont) + oldchar
    return novaStr

mystr = "1"
x = 0
while True:
    print("minhaString( " + str(x) + ") = len(" + str(len(mystr)) + ")")
    x += 1
    if x == 31:
        break;
    mystr = minhaString(mystr)
    
