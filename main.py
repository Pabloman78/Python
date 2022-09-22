f = open("text.txt", "w")
f.write("dwadwad\n")
f.write("kdjfsldkf")
f.close()

r = open("text.txt", 'r')
print(r.read())
r.close()
r.close()