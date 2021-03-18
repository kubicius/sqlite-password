import sqlite3
import logging
import config as cfg

class Database:
    """
        A class to manage sqlite3 database.
    """
    def connect(self, file):
        """
        Connects to database and run _checkDatabase function.
        :param file: Database location
        :return: boolean
        """
        try:
            self.con = sqlite3.connect(file)
            self.cursor = self.con.cursor()
            if (self._checkDatabase()):
                return True
            else:
                logging.error('Database structure is corrupted')
                return False
        except sqlite3.Error as er:
            logging.error('SQLite error: %s' % (' '.join(er.args)))
            return False

    def addUser(self, login, password, salt):
        if self.selectUser(login):
            return 'login_exist'
        else:
            return self._insertUser(login, password, salt)

    def selectUser(self, login):
        """
        Checks if "users" table is present in the database.
        :return: boolean
        """
        query = "SELECT * FROM users WHERE login = ?"
        self.cursor.execute(query, (login,))
        result = self.cursor.fetchone()
        self.con.commit()
        if(result):
            return result
        else:
            return False

    def _insertUser(self, login, password, salt):
        """
        Inserts "user" to "users" table
        :return: boolean
        """
        query = f"INSERT INTO users VALUES (?, ?, ?)"
        try:
            self.cursor.execute(query, (login, password, salt))
            self.con.commit()
            logging.info(f'User "{login}" added to database.')
            return True
        except sqlite3.Error as er:
            logging.error('SQLite error: %s' % (' '.join(er.args)))
            return False

    def _checkDatabase(self):
        """
        Checks database validity and if needed run functions to create proper structure.
        :return: boolean
        """
        if(self._isThereUsersTable()):
            return True
        else:
            return self._createUsersTable()

    def _isThereUsersTable(self):
        """
        Checks if "users" table is present in the database.
        :return: boolean
        """
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        self.con.commit()
        if(result):
            return True
        else:
            return False

    def _createUsersTable(self):
        """
        Create "users" table
        :return: boolean
        """
        query = "CREATE TABLE users(login VARCHAR UNIQUE NOT NULL, password VARCHAR NOT NULL, salt VARCHAR NOT NULL)"
        try:
            self.cursor.execute(query)
            self.con.commit()
            logging.info('Created "users" table')
            return True
        except sqlite3.Error as er:
            logging.error('SQLite error: %s' % (' '.join(er.args)))
            return False