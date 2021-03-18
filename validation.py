import re


class Validation:
    """
        A class to validate data.
    """
    def validateLogin(self, login):
        """
        Validates login.
        :param login: string
        :return: boolean
        """
        length = len(login)
        if(length >= 8 and length <= 16):
            return True
        else:
            return False

    def validatePassword(self, password):
        """
        Validates login.
        :param password: string
        :return: boolean
        """
        regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,128}$"
        pattern = re.compile(regex)
        if re.fullmatch(pattern, password):
            return True
        else:
            return False

    def validatePasswordMatch(self, password, passwordMatch):
        """
        Checks if two passwords are the same.
        :param password: string
        :param passwordMatch: string
        :return: boolean
        """
        if(password == passwordMatch):
            return True
        else:
            return False