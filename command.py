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
        action = input("Choose action: Create user [0], Login [1] or Exit [2]: ")
        while action != '2':
            login = input("Login: ")
            password = getpass.getpass("Password: ")  # needs enabling terminal emulation when using pyCharm
            user = u(self.db)
            if action == '0':
                passwordMatch = getpass.getpass("Repeat password: ")
                print(user.add(login, password, passwordMatch))
            else:
                if action == '1':
                    if(user.checkCredentials(login, password)):
                        print('Login and password are correct.')
                    else:
                        print('Credentials are incorrect.')

            action = input("Choose action: Create user [0], Login [1] or Exit [2]: ")

