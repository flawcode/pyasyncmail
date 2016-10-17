# -*- coding: utf-8 -*-
import csv
import asyncio
import smtplib
from email.mime.text import MIMEText


def _open_file():
    with open('reciepients_file.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        return [', '.join(x) for x in spamreader]


async def mail_funcs(each_person):
    with open("mailfile.txt") as fp:
        # Create a text/plain message
        msg = MIMEText(fp.read())

    me = "joydeepubuntu@gmail.com"    
    you = each_person.split(",")[1]
    msg['Subject'] = 'The contents of mailfile.txt'
    msg['From'] = me
    msg['To'] = you
    # Send the message via our own SMTP server.

    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()


async def main_mail():
    fs = []
    for each_person in _open_file():
        fs.append(mail_funcs(each_person))

    await asyncio.wait(fs)
