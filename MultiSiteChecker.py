from icmplib import ping, multiping, traceroute, resolve


def connections_check():
    
    try:

        hosts = []
        while True:
            with open("hosts.txt", "r") as file:
                for line in file:
                    hosts.append(line.strip())

            y = multiping(hosts)

            for host in y:
                if host.is_alive:
                    print(host.address + " Is alive")
                else:
                    print("Host is down")
    except KeyboardInterrupt:
        menue()


def connections_add():

    x = "Y"

    with open("hosts.txt", "a") as file:

        while x == "Y":

            file.write(input("Which Website do you wanna check? " + "\n")+"\n")
            x = input("Do you wann check another website? (Y/N)")
    menue()


def connections_delete():

    hosts = []
    x = "Y"

    with open("hosts.txt", "r") as file:

        for line in file:
            hosts.append(line.strip())

    while x == "Y":

        print(hosts)

        user_eingabe = input(str("Which Site you wanna delete? "))

        if user_eingabe in hosts:
            removed_line = hosts.index(user_eingabe)

            with open("hosts.txt", "r") as f:
                lines = f.readlines()
                del lines[removed_line]
                hosts.pop(removed_line)

            with open("hosts.txt", "w+") as f:
                for line in lines:
                    f.write(line)

        else:
            print("The site does not exist")

        x = input(str("Do you wanna delete an another site? (Y/N)"))

    menue()


def menue():

    choose = int(input(
        "What you wanna do? \n Check connections (1) \n Delete connections (2) \n Add connections (3) \n Quit (4)"))

    if choose == 1:
        connections_check()

    elif choose == 2:
        connections_delete()

    elif choose == 3:
        connections_add()

    else:
        quit()


menue()
