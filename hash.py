import hashlib
from os import urandom


class Hash:
    """

        A class to prepare secured data.

        ...
        Methods
        -------
        encryptPassword(password="", salt=""):
        Encrypts password.

        decryptPassword(password="", salt=""):
        Decrypts password.

        generateSalt()
        Generates salt.

    """
    def generateSalt(self):
        """
        Generates salt
        :return: string
        """
        return urandom(16)

    def encryptPassword(self, password, salt):
        """
        Encryptspassword
        :param password: string
        :param salt: string
        :return: string
        """
        if not type(password) == bytes:
            password = password.encode()
        encrypted = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
        return encrypted.hex()
