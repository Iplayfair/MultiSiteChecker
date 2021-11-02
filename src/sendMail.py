from email import message
from icmplib import ping
from icmplib.exceptions import NameLookupError
import shutil
import socket
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
import time
import config




def sendMail(tempFile2, free, usedInPercent, alive, hostname, localIP):
    # Configure SMTP-Server

    smtp = smtplib.SMTP(host='smtp.office365.com', port='587')
    smtp.starttls()
    smtp.login(config.login, config.password)
# Send E-Mail
    if alive == False:
        message = tempFile2.substitute(SERVER_NAME=hostname, IP_ADRESS=localIP)

    else:

        message = tempFile2.substitute(
            SERVER_NAME=hostname, LEFT=free, PERCENT=usedInPercent, IP_ADRESS=localIP)

    msg = MIMEMultipart()
    msg['FROM'] = config.From
    msg['TO'] = config.To
    msg['Subject'] = "Warning!"

    msg.attach(MIMEText(message, 'plain'))

    smtp.send_message(msg)

    del msg

