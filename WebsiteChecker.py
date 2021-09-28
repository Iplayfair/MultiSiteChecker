from icmplib import ping,multiping,traceroute,resolve

auswahl = int(input("What you wanna do? \n Check connections (1) \n Delete connections (2) \n Add connections (3)"))

def connections_check():
    
    hosts = []

    with open("hosts.txt", "r") as file:
        for line in file:
            hosts.append(line.strip())

    
    y = multiping(hosts)

    for host in y:
        if host.is_alive:
            print(host.address)
        elif host.is_alive:
            print("Host is down")

def connections_add():

    x = "Y"

    with open ("hosts.txt", "a") as file:

        while x == "Y":

            file.write(input("Which Website do you wanna check? " + "\n")+"\n")
            x = input("Do you wann check another website? (Y/N)")


def connections_delete():
    
    hosts = []
    x = "Y"

    with open("hosts.txt", "r") as file:
        for line in file:
            hosts.append(line.strip())
        
    print (hosts)

            
    while x == "Y":

        user_eingabe = input(str("Which Site you wanna delete? "))
    
        if user_eingabe in hosts:
            removed_line = hosts.index(user_eingabe)

            with open("hosts.txt", "r") as f:
                lines = f.readlines()
                del lines[removed_line]

            with open("hosts.txt", "w+") as f:
                for line in lines:
                    f.write(line)

        else: 
            print ("The site does not exist")
        
        x = input(str("Do you wanna delete an another site? (Y/N)"))



if auswahl == 1:
    connections_check()
    
elif auswahl == 2:
    connections_delete()

else:
    connections_add()