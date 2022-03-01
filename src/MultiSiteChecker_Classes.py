import tkinter as tk
from email.mime import text
from tkinter.font import nametofont
from icmplib import ping, multiping, traceroute, resolve, async_multiping
import tkinter as tk
from tkinter.constants import ACTIVE, ANCHOR, BOTTOM, DISABLED, END, INSIDE, LEFT, RADIOBUTTON, RIGHT, TOP, X, YES
from typing import Counter, List, final
from tkinter import Button, Entry, Frame, Image, Label, Listbox, Toplevel, messagebox
from icmplib.exceptions import NameLookupError
from email import message
from icmplib import ping
from icmplib.exceptions import NameLookupError
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
import database
from snmp import snmp
from EMail import sendMail
from Password import endecryption
from database import networkcheckStorageDB


class MainWindow:
    def __init__(self, window):

        self.after_id = None
        self.counter = 0
        self.dic = {}
        self.dic2 = {}
        self.key = ""
        self.v = ""
        self.hosts = []

        self.window = window
        self.frame = tk.Frame(self.window)
        self.top = Frame(window)
        self.top.pack(side=TOP)
        self.bottom = Frame(window)
        self.bottom.pack(side=BOTTOM)

        # Set Labels, Button and List
        self.l1 = tk.Label(window, text="Address:").pack(
            in_=self.top, side=TOP, padx=5, pady=5)

        self.e1 = tk.Entry(window)
        self.e1.pack(in_=self.top, side=TOP, padx=5, pady=5)

        self.b1 = tk.Button(window, text="Add Connection",
                            command=self.connections_add)
        self.b1.pack(in_=self.top, side=TOP, padx=5, pady=5)
        self.b2 = tk.Button(window, text="Delete Connections",
                            command=self.connections_delete)
        self.b2.pack(in_=self.top, side=TOP, padx=5, pady=5)
        self.b3 = tk.Button(window, text="Check Connections", command=lambda: [
            self.connections_check(), self.switchButtonState()])
        self.b3.pack(in_=self.top, side=TOP, padx=5, pady=5)
        self.b4 = tk.Button(window, text="Stop", command=lambda: [
            self.connections_stop(self.hosts), self.switchButtonState()], state=DISABLED)
        self.b4.pack(in_=self.top, side=TOP, padx=5, pady=5)
        self.b5 = tk.Button(window, text="Set Email",
                            command=self.login_window)
        self.b5.pack(in_=self.bottom, side=BOTTOM, padx=5, pady=5)
        self.b6 = tk.Button(window, text="Delete E-Mail",
                           command=self.askIf)
        self.b6.pack(in_=self.bottom, side=BOTTOM, padx=5, pady=5)
        self.lbox = tk.Listbox(window)

        self.lbox.bind("<Double-Button-1>", lambda x: self.snmp_window())
        self.lbox.pack(in_=self.bottom, side=LEFT)
        self.hosts = self.init()

        for i in self.hosts:
            self.hosts = []
            self.key = "c" + i
            self.v = "var"+i
            self.dic2[self.v] = tk.IntVar()
            self.dic[self.key] = tk.Checkbutton(window, variable=self.dic2["var"+i], onvalue=1, offvalue=0
                                                )
            self.dic[self.key].pack(in_=self.bottom, side=TOP)
            self.lbox.insert("end", i)

        self.frame.pack()
    

    def snmp_window(self):
        self.bindex = self.lbox.curselection()
        index = sum(self.bindex)
        server = self.lbox.get(index)

        self.snmpWindow = tk.Toplevel(self.window)
        self.app = SnmpWindow(self.snmpWindow, server)

    def login_window(self):
        self.loginWindow = tk.Toplevel(self.window)
        self.app = LoginWindow(self.loginWindow)

    def askIf(self):
        question = messagebox.askquestion(title=None, message="Are you sure you want delete the Information")
        if question == "yes":
            networkcheckStorageDB.deleteJson()
        else:
            pass


    def init(self):

        with open("asset/txtData/hosts.txt", "r") as file:
            for line in file:
                self.hosts.append(line.strip())

        return self.hosts

    # If pressed CheckConnection turn of all Buttons except the Stop Button
# If pressed Stop Button turn on all Buttons agian

    def switchButtonState(self):
        if (self.b3['state'] == tk.NORMAL):
            self.b3['state'] = tk.DISABLED
            self.b2['state'] = tk.DISABLED
            self.b1['state'] = tk.DISABLED
            self.b4['state'] = tk.NORMAL
        elif(self.b3['state'] == tk.DISABLED):
            self.b3['state'] = tk.NORMAL
            self.b2['state'] = tk.NORMAL
            self.b1['state'] = tk.NORMAL
            self.b4['state'] = tk.DISABLED
        else:
            self.b3['state'] = tk.NORMAL

# Check Connection if it is Avaible and if not send Email to Checked Checkbox Connections

    def connections_check(self):
        self.hosts = []
        x = -1
        with open("asset/txtData/hosts.txt", "r") as file:
            for line in file:
                self.hosts.append(line.strip())

            for host in self.hosts:

                try:

                    x = x+1

                    y = ping(host, count=1)
                except NameLookupError:
                    self.lbox.itemconfig(x, {'bg': 'yellow'})
                    self.checkChecked(host)
                    continue

                if y.is_alive:
                    self.lbox.itemconfig(x, {'bg': 'green'})

                else:
                    self.lbox.itemconfig(x, {'bg': 'red'})
                    self.checkChecked(host)

            self.after_id = self.window.after(10000, self.connections_check)
            return self.hosts

        # Check Connection before Adding and Add Connection in List and Array

    def connections_add(self):

        self.hosts = []

        with open("asset/txtData/hosts.txt", "r") as file:
            for line in file:
                self.hosts.append(line.strip())

        with open("asset/txtData/hosts.txt", "a") as file:
            try:
                input = self.e1.get()
                host = ping(input)

                if host.is_alive:

                    if input in self.hosts:
                        messagebox.showinfo(
                            title=None, message="The Adress " + input + " is already included.")
                        self.e1.delete(0, 'end')
                    elif input == "":
                        messagebox.showinfo(
                            title=None, message="The Input is Empty please insert an Adress")
                        self.e1.delete(0, 'end')
                    else:
                        self.key = "c" + input
                        self.v = "var"+input
                        self.dic2[self.v] = tk.IntVar()
                        self.dic[self.key] = tk.Checkbutton(
                            self.window, variable=self.dic2["var"+input], onvalue=1, offvalue=0)
                        self.dic[self.key].pack(in_=self.bottom, side=TOP)
                        self.e1.delete(0, 'end')
                        self.lbox.insert("end", input)
                        file.write(input + "\n")
                else:
                    messagebox.showinfo(
                        title=None, message="The Host is no avaible to add it")
            except NameLookupError:
                msgbox = messagebox.askquestion(
                    title=None, message=input + " Cannot be resolved do you wanna still add it?")
                if msgbox == "yes":
                    self.key = "c" + input
                    self.v = "var"+input
                    self.dic2[self.v] = tk.IntVar()
                    self.dic[self.key] = tk.Checkbutton(
                        self.window, variable=self.dic2["var"+input], onvalue=1, offvalue=0).pack()
                    self.e1.delete(0, 'end')
                    self.lbox.insert("end", input)
                    file.write(input + "\n")
                else:
                    self.e1.delete(0, 'end')

# Delete the Connection from List and Array

    def connections_delete(self):
        self.hosts = self.init()
        tuple_index = self.lbox.curselection()
        index = sum(tuple_index)

        input = self.lbox.get(index)
        self.lbox.delete(index)
        self.dic["c" + input].destroy()

        with open("asset/txtData/hosts.txt", "r") as f:
            lines = f.readlines()
            del lines[index]
            self.hosts.pop(index)

        with open("asset/txtData/hosts.txt", "w+") as f:
            for line in lines:
                f.write(line)

    def checkChecked(self, address):

        if self.dic2["var" + address].get() == 1 and self.counter == 0:
            with open("asset/txtData/messageNoPing.txt", "r") as tempFile:
                tempFile1 = tempFile.read()
            tempFile2 = Template(tempFile1)
            sendMail.sendEMail(tempFile2, address)
            self.counter = self.counter + 1

        elif self.dic2["var"+address].get() == 0 and self.counter == 1:
            self.counter = self.counter - 1

        else:
            pass

    def connections_stop(self, hosts):

        hosts = self.init()
        if self.after_id is not None:
            self.window.after_cancel(self.after_id)
            self.after_id = None

        for host in hosts:
            indx = hosts.index(host)
            self.lbox.itemconfig(indx, {'bg': 'white'})


class LoginWindow(MainWindow):

    def __init__(self, topWindow):

        self.topWindow = topWindow
        self.frame = tk.Frame(self.topWindow)
        self.topWindow.title("Email")
        self.topWindow.iconbitmap('asset/Pictures/Network.ico')
        self.bottom = Frame(topWindow)
        self.bottom.pack(side=BOTTOM)
        self.t3 = Label(
            topWindow, text="To use the E-Mail function you have to set an E-Mail Account").pack(padx=5, pady=5)
        self.tl = Label(
            topWindow, text="E-Mail Address: ").pack(padx=5, pady=5)
        self.te = Entry(topWindow)
        self.te.pack()
        self.tl2 = Label(topWindow, text="Password: ").pack(padx=5, pady=5)
        self.te2 = Entry(topWindow, show='*')
        self.te2.pack()
        self.tb2 = Button(self.topWindow, text="Cancel", command=self.close_windows).pack(
            in_=self.bottom, side=LEFT, padx=5, pady=5)
        self.tb = Button(topWindow, text="Set E-Mail",
                         command=lambda: [self.setEmailData(), self.close_windows()]).pack(in_=self.bottom, side=LEFT, padx=5, pady=5)
        self.frame.pack()

    def setEmailData(self):
        email = self.te.get()
        password = self.te2.get()

        key = endecryption.generateKey()
        hashedPW = endecryption.encryptPW(password, key)

        networkcheckStorageDB.writeJson(email, hashedPW, key)

    def close_windows(self):
        self.topWindow.destroy()


class SnmpWindow(MainWindow):

    def __init__(self, snmpWindow, server):
        self.snmpWindow = snmpWindow
        snmpWindow.title(server)
        snmpWindow.iconbitmap('asset/Pictures/Network.ico')
        self.snmpL1 = Label(snmpWindow, text=str(snmp.getComputerName(server)))
        self.snmpL1.pack()
        self.snmpL2 = Label(snmpWindow, text=str(snmp.getComputerRam(server)))
        self.snmpL2.pack()
        self.snmpL3 = Label(snmpWindow, text=str(snmp.getComputerUpTime(server)))
        self.snmpL3.pack()
        self.snmpL4 = Label(snmpWindow, text=str(snmp.getComputerServices(server)))
        self.snmpL4.pack()
        self.snmpL5 = Label(snmpWindow, text=str(snmp.getMACAdress(server)))
        self.snmpL5.pack()
        self.frame = tk.Frame(self.snmpWindow)


def main():

    if networkcheckStorageDB.readisSet() == False:
        root = tk.Tk()
        root.title("NetworkChecker")
        root.iconbitmap('asset/Pictures/Network.ico')
        loginW = MainWindow(root)
        loginW.login_window()
        root.mainloop()

    else:
        root = tk.Tk()
        root.title("NetworkChecker")
        root.iconbitmap('asset/Pictures/Network.ico')
        app = MainWindow(root)
        root.mainloop()


if __name__ == '__main__':
    main()
