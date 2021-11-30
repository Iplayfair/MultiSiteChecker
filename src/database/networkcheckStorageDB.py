import email
import json
from json.decoder import JSONDecodeError
import EMail


def writeJson(eMail, password, key):

    with open('src/database/login.json', 'r') as loginWrite:

        data = json.load(loginWrite)

    data["login"] = eMail
    data["password"] = password
    data["From"] = eMail
    data["key"] = key
    data["isSet"] = True

    with open('src/database/login.json', 'w') as loginWrite:
        json.dump(data, loginWrite)




def deleteJson():

    with open('src/database/login.json', 'r') as loginWrite:

        data = json.load(loginWrite)

    data["login"] = ""
    data["password"] = ""
    data["From"] = ""
    data["key"] = ""
    data["isSet"] = False

    with open('src/database/login.json', 'w') as loginWrite:
        json.dump(data, loginWrite)


def readLogin():

    with open('src/database/login.json', 'r') as jsonFile:

        data = json.load(jsonFile)

    login = data["login"]

    return login


def readPassword():

    with open('src/database/login.json', 'r') as jsonFile:

        data = json.load(jsonFile)

    hashedPW = data["password"]

    return hashedPW


def readKey():

    with open('src/database/login.json', 'r') as jsonFile:

        data = json.load(jsonFile)

    key = data["key"]
    return key


def readisSet():

    with open('src/database/login.json', 'r') as jsonFile:

        data = json.load(jsonFile)

    isSet = data["isSet"]
    return isSet
