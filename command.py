import logging
import getpass
from user import User as u

class Command():
    """
        A class to communicate with user via command line.
        ...
        Arguments
        database: Database object
    """
    def __init__(self, database):
        self.db = database

    def run(self):
        """
        Presenting output and watching input.
        :return: void
        """
        action = 0
        while(action != 2):
            action = input("Choose action: Create user [0], Login [1] or Exit [2]: ")
            login = input("Login: ")
            password = getpass.getpass("Password: ") # needs enabling terminal emulation when using pyCharm
            passwordMatch = getpass.getpass("Repeat password: ")
            user = u(self.db)
            print(user.add(login, password, passwordMatch))

