import pickle

file = open("banner.p", "rb")
obj = pickle.load(file)
file.close()

print(obj)
for line in obj:
    for piece in line:
        char = piece[0]
        num = piece[1]
        for x in range(num):
            print(char, end="")
    print()
