from email.mime import text
from re import T
from icmplib import ping, multiping, traceroute, resolve, async_multiping
import tkinter as tk
from tkinter.constants import BOTTOM, END, LEFT, RIGHT, TOP, X
from typing import Counter, List, final
from tkinter import Button, Frame, Listbox, messagebox
from icmplib.exceptions import NameLookupError
from email import message
from icmplib import ping
from icmplib.exceptions import NameLookupError
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
import config
import smtplib

after_id = None
counter = 0
dic = {}
dic2 = {}
key = ""
v = ""

def switchButtonState():
    if (b3['state'] == tk.NORMAL):
        b3['state'] = tk.DISABLED
        b2['state'] = tk.DISABLED
        b1['state'] = tk.DISABLED
    elif(b3['state'] == tk.DISABLED):
        b3['state'] = tk.NORMAL
        b2['state'] = tk.NORMAL
        b1['state'] = tk.NORMAL
    else:
        b3['state'] = tk.NORMAL


def connections_check():
    global after_id
    hosts = []
    x = -1
    with open("asset/txtData/hosts.txt", "r") as file:
        for line in file:
            hosts.append(line.strip())

        for host in hosts:

            try:

                x = x+1

                y = ping(host, count=1)
            except NameLookupError:
                lbox.itemconfig(x, {'bg': 'yellow'})
                checkChecked(host)
                continue

            """ indx = hosts.index(host) """
            if y.is_alive:
                lbox.itemconfig(x, {'bg': 'green'})

            else:
                lbox.itemconfig(x, {'bg': 'red'})
                checkChecked(host)

    after_id = window.after(10000, connections_check)
    return hosts


def connections_add():

    hosts = []

    with open("asset/txtData/hosts.txt", "r") as file:
        for line in file:
            hosts.append(line.strip())

    with open("asset/txtData/hosts.txt", "a") as file:
        try:
            input = e1.get()
            host = ping(input)

            if host.is_alive:

                if input in hosts:
                    messagebox.showinfo(
                        title=None, message="The Adress " + input + " is already included.")
                    e1.delete(0, 'end')
                elif input == "":
                    messagebox.showinfo(
                        title=None, message="The Input is Empty please insert an Adress")
                    e1.delete(0, 'end')
                else:
                    key = "c" + input
                    v = "var"+input
                    dic2[v] = tk.IntVar()
                    dic[key] = tk.Checkbutton(
                        window, variable=dic2["var"+input], onvalue=1, offvalue=0).pack()
                    e1.delete(0, 'end')
                    lbox.insert("end", input)
                    file.write(input + "\n")
            else:
                messagebox.showinfo(
                    title=None, message="The Host is no avaible to add it")
        except NameLookupError:
            msgbox = messagebox.askquestion(
                title=None, message=input + " Cannot be resolved do you wanna still add it?")
            if msgbox == "yes":
                key = "c" + input
                v = "var"+input
                dic2[v] = tk.IntVar()
                dic[key] = tk.Checkbutton(
                    window, variable=dic2["var"+input], onvalue=1, offvalue=0).pack()
                e1.delete(0, 'end')
                lbox.insert("end", input)
                file.write(input + "\n")
            else:
                e1.delete(0, 'end')


def connections_delete():

    tuple_index = lbox.curselection()
    index = sum(tuple_index)

    lbox.delete(index)

    with open("asset/txtData/hosts.txt", "r") as f:
        lines = f.readlines()
        del lines[index]
        hosts.pop(index)

    with open("asset/txtData/hosts.txt", "w+") as f:
        for line in lines:
            f.write(line)


def connections_stop(hosts):
    global after_id
    hosts = init()
    if after_id is not None:
        window.after_cancel(after_id)
        after_id = None

    for host in hosts:
        indx = hosts.index(host)
        lbox.itemconfig(indx, {'bg': 'white'})


def checkChecked(address):
    global counter
    if dic2["var" + address].get() == 1 and counter == 0:
        with open("asset/txtData/messageNoPing.txt", "r") as tempFile:
            tempFile1 = tempFile.read()
        tempFile2 = Template(tempFile1)
        sendEMail(tempFile2, address)
        counter = counter + 1
    elif dic2["var"+address].get() == 0 and counter == 1:
        counter = counter - 1
    else:
        pass


def sendEMail(text, address):
    smtp = smtplib.SMTP(host='smtp.office365.com', port='587')
    smtp.starttls()
    smtp.login(config.login, config.password)

    message = text.substitute(IP_ADRESS=address)

    msg = MIMEMultipart()
    msg['FROM'] = config.From
    msg['TO'] = config.To
    msg['Subject'] = "Warning!"

    msg.attach(MIMEText(message, 'plain'))

    smtp.send_message(msg)

# Building GUI


def init():
    hosts = []

    with open("asset/txtData/hosts.txt", "r") as file:
        for line in file:
            hosts.append(line.strip())

    return hosts


window = tk.Tk()
top = Frame(window)
top.pack(side=TOP)
bottom = Frame(window)
bottom.pack(side=BOTTOM)

l1 = tk.Label(window,text="Address:").pack(in_=top,side=TOP)

e1 = tk.Entry(window)
e1.pack(in_=top,side = TOP)

b1 = tk.Button(window,text="Add Connection", command=connections_add)
b1.pack(in_=top,side=TOP)
b2 = tk.Button(window,text="Delete Connections", command=connections_delete)
b2.pack(in_=top,side=TOP)
b3 = tk.Button(window,text="Check Connections", command=lambda: [
               connections_check(), switchButtonState()])
b3.pack(in_=top,side=TOP)
b4 = tk.Button(window,text="Stop", command=lambda: [
               connections_stop(hosts), switchButtonState()])
b4.pack(in_=top,side=TOP)


lbox = tk.Listbox(window)
lbox.pack(in_= bottom,side=LEFT)
hosts = init()
for i in hosts:
    key = "c" + i
    v = "var"+i
    dic2[v] = tk.IntVar()
    dic[key] = tk.Checkbutton(window, variable=dic2["var"+i]).pack(in_=bottom,side=TOP)
    lbox.insert("end", i)


def main():

    window.mainloop()


if __name__ == '__main__':
    main()
