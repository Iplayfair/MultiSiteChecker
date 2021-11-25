import hashlib
import os


def hashingPW(password):
    salt = os.urandom(32)

    key = hashlib.pbkdf2_hmac(
        'sha256', password.encode('utf-8'), salt, 1000000)

    storage = salt+key

    return str(storage)
