from email import message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import getpass

alamat_email = []                              
i = 1                                        

def sent_email ():
    fromaddr = pengirim
    toaddr = open ('receive_list.txt', 'r')
    print(toaddr.read())
    msg = MIMEMultipart()
    msg['FROM'] = fromaddr                       
    msg['TO'] = toaddr                      
    msg['SUBJECT'] = subject_email  
    msg.attach(MIMEText(body_email, 'plain'))             
 
pengirim = input('Masukkan E-mail Anda = ')     
penerima = open("D:\Dokumen\AI For Everyone, AI For Indonesia/receiver_list.txt", "r")
print(penerima.read())                 
password_email = getpass.getpass('Masukkan Password Anda = ')     
subject_email = input('Masukkan Subject = ')                         
body_email = open("D:\Dokumen\AI For Everyone, AI For Indonesia/message.txt", "r")
print(body_email.read()) 

server = smtplib.SMTP('smtp.gmail.com', 587) 
server.starttls()                              
server.login(pengirim, password_email)                           
server.sendmail(pengirim, [penerima], body_email)     
server.quit()                                       
        

'''https://rifqifai.com/program-python-untuk-mengirim-email/
https://code.tutsplus.com/id/tutorials/sending-emails-in-python-with-smtp--cms-29975'''
''' https://www.pythonindo.com/cara-mengirim-email-menggunakan-python'''
