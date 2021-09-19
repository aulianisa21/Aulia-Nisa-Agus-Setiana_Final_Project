from email import message
from os import read
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

msg = MIMEMultipart()
msg['FROM'] = input('Masukkan Email Anda = ') #diisi email Anda (pengirim)
msg['TO'] = open("D:\Dokumen\AI For Everyone, AI For Indonesia/receiver_list.txt", "r") ##Diisi email tujuan (penerima)
msg['Subject'] = ('Lets introduce my self!') #Subject Email
body = open("D:\Dokumen\AI For Everyone, AI For Indonesia/message.txt", "r") #isian email yang terdapat pada file message.txt
pwd = input("Masukan Password Anda = ") #diisi password Anda (pengirim)
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(msg['FROM'], pwd)
server.sendmail(msg['FROM'], msg['TO'], msg.as_string)
server.quit()

'''https://rifqifai.com/program-python-untuk-mengirim-email/
https://code.tutsplus.com/id/tutorials/sending-emails-in-python-with-smtp--cms-29975'''