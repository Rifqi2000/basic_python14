file = open("data.txt","w")
file.write("Selamat Datang!")
file.close()

file = open("data.txt","a")
file.write("\nNama saya adalah Rifqi Mulya K")
file.close()

file = open("data.txt","r")
print(file.read())


file = open("data.txt","r")
print(file.readline())
print(file.readlines())