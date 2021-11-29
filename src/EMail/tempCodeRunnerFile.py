from email import message
from icmplib import ping
from icmplib.exceptions import NameLookupError
import shutil
import socket
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Password import endecryption
from database import networkcheckStorageDB
from string import Template
import time


def sendEMail(text, address):
    # Configure Office365 SMTP Server
    smtp = smtplib.SMTP(host='smtp.office365.com', port='587')
    smtp.starttls()
    smtp.login(networkcheckStorageDB.readLogin(),
               endecryption.decryptPW())  # Login Credantials

    message = text.substitute(IP_ADRESS=address)

    msg = MIMEMultipart()
    msg['FROM'] = networkcheckStorageDB.readLogin
    msg['TO'] = networkcheckStorageDB.readLogin
    msg['Subject'] = "Warning!"

    msg.attach(MIMEText(message, 'plain'))

    smtp.send_message(msg)
