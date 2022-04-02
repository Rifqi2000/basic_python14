with open("text.txt","w") as f:
    f.write("WELCOME!!\n")
    f.write("Ini baris kedua\nIni baris ketiga\n")

with open("text.txt","a") as files:
    files.write("Ini baris keempat")

with open("text.txt","r") as file:
    print(file.read())