import email
import json
from json.decoder import JSONDecodeError
import EMail
from Password import hashing


def writeJson(eMail, password):

    with open('src/database/login.json', 'r') as loginWrite:

        data = json.load(loginWrite)

    data["login"] = eMail
    data["password"] = password
    data["From"] = eMail
    data["isSet"] = True


    with open('src/database/login.json', 'w') as loginWrite:
        json.dump(data, loginWrite)


def readLogin():
    pass


def readPassword():

    with open('src/database/login.json', 'r') as jsonFile:

        data = json.load(jsonFile)
    
    hashedPW = data["password"]

def readisSet():

    with open('src/database/login.json', 'r') as jsonFile:

        data = json.load(jsonFile)
    
    isSet = data["isSet"]
    print(isSet)
    return isSet

