#!/usr/bin/env python
# coding: utf-8

# ### Tugas-1/Soal-1

# In[ ]:


nama = input("Nama: ")
umur = int(input("Umur: "))
tinggi = float(input("Tinggi: "))

text = "Nama saya {}, umur saya {} tahun dan tinggi saya {} cm".format(nama, umur, tinggi)

print(text) 


# ### Tugas-1/Soal-2

# In[ ]:


r = float(input("Masukkan jari-jari lingkaran: "))
pi = 22/7


# In[ ]:


def hitung_luas_lingkaran(r):
    luas = pi * r * r
    return luas


# In[ ]:


luas = hitung_luas_lingkaran(r)

print("Luas lingkaran: {:.2f}".format(luas))


# ### Tugas-1/Soal-3

# In[ ]:


nilai_minimum = float(input("Nilai minimun: "))

nilai_teori = float(input("Nilai teori: "))
nilai_praktek = float(input("Nilai prakrek: "))


# In[ ]:


if nilai_teori >= nilai_minimum and nilai_praktek >= nilai_minimum:
    print("Lulus")
elif nilai_teori >= nilai_minimum and nilai_praktek < nilai_minimum:
    print("Anda mengulang ujian praktek")
elif nilai_teori < nilai_minimum and nilai_praktek >= nilai_minimum:
    print("Anda mengulang ujian teori")
else:
    print("Anda mengulang ujian teori dan praktek")


# ## Dictionary

# In[ ]:


pelanggan = {
    "nama": "farhan",
    "umur": 21
}

pelanggan_2 = {
    "nama": "andi",
    "umur": 18
}

print("Nama: {}".format(pelanggan["nama"]))
print("Umur: {}".format(pelanggan["umur"]))


# In[ ]:


# change value of dictionary
pelanggan["umur"] = 22

print("Nama: {}".format(pelanggan["nama"]))
print("Umur: {}".format(pelanggan["umur"]))


# In[ ]:


# loop through dictionary
for x in pelanggan:
    print(x)
    print(pelanggan[x])   
    print(pelanggan_2[x])   


# In[ ]:


# list of dictionary
daftar_pelanggan = []
daftar_pelanggan.append(pelanggan)
daftar_pelanggan.append(pelanggan_2)


# In[ ]:


for pelanggan in daftar_pelanggan:
    print("Nama: {}".format(pelanggan["nama"]))
    print("Umur: {}".format(pelanggan["umur"]))


# ## Function

# In[ ]:


def my_function(first_name, last_name=""):
    print("Hello {} - {}".format(first_name, last_name))


# In[ ]:


my_function("Farhan", "Mardadi")
my_function("Andi", "Wijaya")
my_function("Yusuf")


# In[ ]:


# function keywords
def my_function2(child3, child2, child1):
  print("The youngest child is " + child3)


# In[ ]:


my_function2(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
my_function2("Emil", "Tobias", "Linus")


# ## Function_example

# In[ ]:


nama_buah = []

def tambah_nama_buah(nama):
    nama_buah.append(nama)
    print_nama_buah()

def print_nama_buah():
    for buah in nama_buah:
        print(buah)
    print("-----")


# In[ ]:


tambah_nama_buah("jeruk")
tambah_nama_buah("apel")
tambah_nama_buah("melon")
tambah_nama_buah("pisang")

def total(x,y):
    total = x + y
    return total

def total_buah_sisa():
    return 20


# In[ ]:


jumlah = total(3,2)
print(jumlah)

total_buah = len(nama_buah) + total_buah_sisa()
print(total_buah)

