from icmplib import ping, multiping, traceroute, resolve
import sys
import tkinter as tk
from tkinter.constants import LEFT, RIGHT, X
from typing import List, final
from tkinter import messagebox
import icmplib

from icmplib.exceptions import NameLookupError


def connections_check():

    hosts = []

    with open("hosts.txt", "r") as file:
        for line in file:
            hosts.append(line.strip())

        y = multiping(hosts)

        for host in y:

            indx = y.index(host)
            if host.is_alive:
                lbox.itemconfig(indx, {'bg': 'green'})

            else:
                lbox.itemconfig(indx, {'bg': 'red'})

    window.after(500, connections_check)


def connections_add():

    hosts = []

    with open("hosts.txt", "r") as file:
        for line in file:
            hosts.append(line.strip())

    with open("hosts.txt", "a") as file:

        input = e1.get()
        if input in hosts:
            messagebox.showinfo(
                title=None, message="The Adress " + input + " is already included.")
            e1.delete(0, 'end')
        elif input == "":
            messagebox.showinfo(title=None, message="The Input is Empty please insert an Adress")
        else:

            e1.delete(0, 'end')
            lbox.insert("end", input)
            file.write(input + "\n")


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
    window.after_cancel(connections_check)

# Building GUI

window = tk.Tk()

l1 = tk.Label(text="Address:").pack()

e1 = tk.Entry(window)
e1.pack()

b1 = tk.Button(text="Add Connection", command=connections_add).pack()
b2 = tk.Button(text="Delete Connections", command=connections_delete).pack()
b3 = tk.Button(text="Check Connections", command=connections_check).pack()
b4 = tk.Button(text="Stop", command=connections_stop).pack()

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
