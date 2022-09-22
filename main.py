# f = open("text.txt", "w")
# f.write("dwadwad\n")
# f.write("kdjfsldkf")
# f.close()

# r = open("text.txt", 'r')
# print(r.read())
# r.close()
# r.close()

# name = open('names.txt', 'w', encoding='utf-8')
# name.write("Mamatkadyrov Artur")
# name.write("Маматкадыров Артур")
# name.close()

# read_name = open('names.txt', 'r', encoding='utf-8')
# print(read_name.read())
# read_name.close()

password = open('passwords.txt', 'a+')
password.write('2021itrun\n')
password.close()