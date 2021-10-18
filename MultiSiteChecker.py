from icmplib import ping, multiping, traceroute, resolve
import sys
import tkinter as tk
from tkinter.constants import LEFT, RIGHT, X
from typing import List, final
from tkinter import Button, Listbox, messagebox
import icmplib

from icmplib.exceptions import NameLookupError

after_id = None


def switchButtonState():
    if (b3['state'] == tk.NORMAL):
        b3['state'] = tk.DISABLED
    elif(b3['state'] == tk.DISABLED):
        b3['state'] = tk.NORMAL
    else:
        b3['state'] = tk.NORMAL


def connections_check():

    global after_id
    hosts = []

    with open("hosts.txt", "r") as file:
        for line in file:
            hosts.append(line.strip())
    try:
        y = multiping(hosts)
        
        for host in y:

            indx = y.index(host)
            if host.is_alive:
                lbox.itemconfig(indx, {'bg': 'green'})

            else:
                lbox.itemconfig(indx, {'bg': 'red'})
    except NameLookupError:
        pass
    after_id = window.after(500, connections_check)


def connections_add():

    hosts = []

    with open("hosts.txt", "r") as file:
        for line in file:
            hosts.append(line.strip())

    with open("hosts.txt", "a") as file:
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
                else:

                    e1.delete(0, 'end')
                    lbox.insert("end", input)
                    file.write(input + "\n")
            else:
                messagebox.showinfo(
                    title=None, message="The Host is no avaible to add it")
        except NameLookupError:
            messagebox.showinfo(
                title=None, message=input + " Cannot be resolved")


def connections_delete():

    tuple_index = lbox.curselection()
    index = sum(tuple_index)

    lbox.delete(index)

    with open("hosts.txt", "r") as f:
        lines = f.readlines()
        del lines[index]
        hosts.pop(index)

    with open("hosts.txt", "w+") as f:
        for line in lines:
            f.write(line)


def connections_stop():
    global after_id
    if after_id is not None:
        window.after_cancel(after_id)
        after_id = None
        lbox.config(background='white')


"""     
    hosts = connections_check() 

    for host in hosts:
        indx = hosts.index(host)
        lbox.itemconfig(indx, {'bg': 'white'})
 """
# Building GUI


window = tk.Tk()

l1 = tk.Label(text="Address:").pack()

e1 = tk.Entry(window)
e1.pack()

b1 = tk.Button(text="Add Connection", command=connections_add).pack()
b2 = tk.Button(text="Delete Connections", command=connections_delete).pack()
b3 = tk.Button(text="Check Connections", command=lambda: [
               connections_check(), switchButtonState()])
b3.pack()
b4 = tk.Button(text="Stop", command=lambda: [
               connections_stop(), switchButtonState()])
b4.pack()

# Initial the Connection List

hosts = []

with open("hosts.txt", "r") as file:
    for line in file:
        hosts.append(line.strip())

lbox = tk.Listbox(window)
lbox.pack()

for i in hosts:
    lbox.insert("end", i)


window.mainloop()
