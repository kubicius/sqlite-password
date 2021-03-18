import sqlite3
import cursor

class Database:
    """
     A class to manage sqlite3 database.

     ...

     Attributes
     ----------
     logging : Logging object

     Methods
     -------
     connect(file=""):
         Connects to database.

     """

    def __init__(self, logging):
        self.logging = logging

    def connect(self, file):
        """
        Connects to database and run _checkDatabase function.
        :param file: Database location
        :return: boolean
        """

        self.con = sqlite3.connect(file)
        if(self.con):
            self.cursor = self.con.cursor()
            if(self._checkDatabase()):
                return True
            else:
                self.logging.error('Database structure is corrupted')
                return False
        else:
            self.logging.error('Connection to database failed')
            return False

    def _checkDatabase(self):
        """
        Checks database validity and if needed run functions to create proper structure.
        :return: boolean
        """
        if(self._isThereUsersTable()):
            return True
        else:
            if(self.createUsersTable()):
                return True
            else:
                return False

    def _isThereUsersTable(self):
        """
        Checks if "users" table is present in the database.
        :return: boolean
        """
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        if(self.con.commit()):
            return True
        else:
            return False

    def createUsersTable(self):
        """
        Create "users" table
        :return: boolean
        """
        query = "CREATE TABLE users(login VARCHAR UNIQUE, password VARCHAR, salt VARCHAR)"
        self.cursor.execute(query)
        self.con.commit()