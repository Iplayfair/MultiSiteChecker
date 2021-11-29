import cryptocode
from database import networkcheckStorageDB
import os


def generateKey():
    return str(os.urandom(32))


def encryptPW(password, key):

    passtext = cryptocode.encrypt(password, key)
    return passtext


def decryptPW():

    passwordMain = networkcheckStorageDB.readPassword()
    keyMain = networkcheckStorageDB.readKey()

    test = cryptocode.decrypt(passwordMain, keyMain)
    print(test)

    return test
