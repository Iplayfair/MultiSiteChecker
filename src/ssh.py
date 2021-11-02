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

hostname = socket.gethostname()
localIP = socket.gethostbyname(hostname)




def main():
    counter = 0
    counterPing = 0
    while True:

        total, used, free = shutil.disk_usage("/")

        total = (total // (2**30))
        used = (used // (2**30))
        free = (free // (2**30))

        usedInPercent = round(used/total*100)

        y = ping(localIP, count=3)

        print(usedInPercent)
        print(y.is_alive)
        alive = y.is_alive
        time.sleep(5)

        if usedInPercent >= 59 and counter == 0:
            with open("asset/txtData/message.txt", "r") as tempFile:
                tempFile1 = tempFile.read()
            tempFile2 = Template(tempFile1)
            sendEmail(tempFile2, free, usedInPercent, alive)
            counter = counter+1

        elif usedInPercent < 59 and counter == 1:
            counter = counter - 1

        else:
            pass

        if y.is_alive and counterPing == 1:
            counterPing = counterPing - 1
        elif y.is_alive == False and counterPing == 0:
            with open("asset/txtData/messageNoPing.txt", "r") as noPing:
                noPingFile = noPing.read()
            noPingFile2 = Template(noPingFile)
            sendEmail(noPingFile2, free, usedInPercent, alive)
            counterPing = counterPing + 1


def sendEmail(tempFile2, free, usedInPercent, alive):
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


if __name__ == '__main__':
    main()
