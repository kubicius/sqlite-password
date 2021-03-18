from validation import Validation
from hash import Hash
import config as cfg


class User:
    """

        A class to manage user account.

        ...
        Arguments
        database: Database object

        Methods
        -------
        add(login="", password="", passwordMatch=""):
        Adds user.

    """
    def __init__(self, database):
        self.db = database

    def add(self, login, password, passwordMatch):
        """
        Adds user.
        :param login: string
        :param password: string
        :param passwordMatch: string
        :return: string
        """
        v = Validation()
        if v.validateLogin(login=login):
            if v.validatePassword(password):
                if v.validatePasswordMatch(password, passwordMatch):
                    h = Hash()
                    salt = h.generateSalt()
                    hashedPassword = h.encryptPassword(password, salt)
                    if self.db.insertUser(login, hashedPassword, salt):
                        return "Account created successfully."
                    else:
                        return f"Database error occurred. Check {cfg.log['output']} file."
                else:
                    return "Passwords do not match."
            else:
                return "Password is too weak. Password should have at least 8 characters and one character of each type: lowercase, uppercase, digit and special character."
        else:
            return "Login should have between 8 - 16 characters."



