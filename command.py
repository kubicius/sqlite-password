import logging
import getpass
from user import User as u

class Command():
    """

        A class to communicate with user via command line.

        ...
        Arguments
        database: Database object

        Methods
        -------
        run():
        Starts communication with user.

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
            action = input("Choose action: [0] Create user or [1] Login [2] Exit: ")
            login = input("Login: ")
            password = getpass.getpass("Password: ") # needs enabling terminal emulation when using pyCharm
            passwordMatch = getpass.getpass("Repeat password: ")
            user = u(self.db)
            print(user.add(login, password, passwordMatch))

