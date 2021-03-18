import logging
import getpass

class Command:
    """

        A class to communicate with user via command line.

        ...

        Methods
        -------
        run():
        Starts communication with user.

    """
    def run(self):
        """
        Presenting output and watching input.
        :return: void
        """
        action = 0
        while(action != 2):
            action = input("Choose action: [0] Create user or [1] Login [2] Exit: ")

