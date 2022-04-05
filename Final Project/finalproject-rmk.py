"""
Rifqi Mulya Kiswanto - Indonesia AI Batch 14
"""

import smtplib
import getpass
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def penerima():
    i = 0
    with open('receiver_list.txt', 'r') as file:
        list_penerima = file.read()
        print("\tEmail Penerima: ")
        print(list_penerima)


def tambah_penerima():
    print("\tTambah Email")
    tambah_email = input("Masukkan tambahan email: ")
    with open('receiver_list.txt', 'a') as file:
        file.write('\n')
        file.write(tambah_email)


def kirim_email():
    print("\tKirim Email")
    fromaddr = input("Masukkan Email\t: ")
    password = getpass.getpass()
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['Subject'] = input("Masukkan Subject: ")
    body = input("Masukkan Body\t: ")

    lampiran = input("Ada Lampiran (Y/N): ")

    if lampiran == "Y" or lampiran == 'y':
        filename = input("Nama Lampiran: ")
        path = input("Path: ")
        attachment = open(path, "rb")

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        "attachment; filename= %s" % filename)

        msg.attach(part)

    with open('receiver_list.txt', 'r') as file:
        penerima = file.readlines()

    msg['To'] = f"{penerima}"
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, penerima, text)
    server.quit()
    print("Kirim Email Sukses!!!")


while True:
    print("\tEMAIL YUK!")
    print("*"*25)
    print("\tMENU")
    print("*"*25)
    print("1. Penerima\n2. Tambah Penerima\n3. Kirim Email\n4. Keluar")
    pilih = int(input("Pilih: "))
    os.system("cls")
    if pilih == 1:
        penerima()
        tanya = input("Kembali Ke Menu? (Y/N): ")
        if tanya == "N" or tanya == "n":
            print("Terima Kasih")
            break
        os.system("cls")
    elif pilih == 2:
        tambah_penerima()
        tanya = input("Kembali Ke Menu? (Y/N): ")
        if tanya == "N" or tanya == "n":
            print("Terima Kasih")
            break
        os.system("cls")
    elif pilih == 3:
        kirim_email()
        tanya = input("Kembali Ke Menu? (Y/N): ")
        if tanya == "N" or tanya == "n":
            print("Terima Kasih")
            break
        os.system("cls")
    elif pilih == 4:
        print("Terima Kasih")
        break
    else:
        print("Salah memasukkan angka")

"""
Sumber : https://www.pythonindo.com/cara-mengirim-email-menggunakan-python/
         https://github.com/FarisNadhila/AI10/tree/main/Final%20Project
"""
