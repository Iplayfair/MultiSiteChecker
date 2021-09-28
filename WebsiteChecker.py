from icmplib import ping,multiping,traceroute,resolve

auswahl = int(input("Was wollen sie tun? \n Connections checken (1) \n Connections bearbeiten (2) \n Connections hinzufügen (3)"))

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

            file.write(input("Welche Website willst du Checken? " + "\n")+"\n")
            x = input("Willst du eine weitere Webseite öffnen? (Y/N)")



if auswahl == 1:
    connections_check()
    
elif auswahl == 2:
    connections_delete

else:
    connections_add()