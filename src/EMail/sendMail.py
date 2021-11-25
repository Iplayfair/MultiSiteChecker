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


def sendEMail(text, address):
    # Configure Office365 SMTP Server
    smtp = smtplib.SMTP(host='smtp.office365.com', port='587')
    smtp.starttls()
    smtp.login(config.login, config.password)  # Login Credantials

    message = text.substitute(IP_ADRESS=address)

    msg = MIMEMultipart()
    msg['FROM'] = config.From
    msg['TO'] = config.To
    msg['Subject'] = "Warning!"

    msg.attach(MIMEText(message, 'plain'))

    smtp.send_message(msg)
