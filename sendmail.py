#-*-coding:utf-8-*-

import smtplib
from email.mime.text import MIMEText
from config import *

def sendmail(filename):
    f = open(filename,'rb')
    msg = MIMEText(f.read(),'html','utf8')
    msg.set_charset('utf8')
    f.close
    #sender
    sender = EMAIL
    username = USERNAME
    password = PASSWORD
    #receiver
    receiver = TARGET_EMAIL
    #msg
    msg['Subject'] = 'result of Statistics'
    msg['From'] = sender
    msg['To'] = TARGET_EMAIL
    #smtp
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(username,password)
    s.sendmail(sender, receiver, msg.as_string())
    s.quit()
