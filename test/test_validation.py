import unittest
import validation as v

class TestValidation(unittest.TestCase):

    def test_validatePassword_uppercase(self):
        validation = v.Validation()
        self.assertTrue(validation.validatePassword('Testcase123?'))
        self.assertFalse(validation.validatePassword('testcase123?'))

    def test_validatePassword_digit(self):
        validation = v.Validation()
        self.assertTrue(validation.validatePassword('Testcase123?'))
        self.assertFalse(validation.validatePassword('Testcase?'))

    def test_validatePassword_special(self):
        validation = v.Validation()
        self.assertTrue(validation.validatePassword('Testcase123?'))
        self.assertFalse(validation.validatePassword('Testcase123'))

    def test_validatePasswordMatch(self):
        validation = v.Validation()
        self.assertTrue(validation.validatePasswordMatch('Testcase123?','Testcase123?'))
        self.assertFalse(validation.validatePasswordMatch('Testcase123?','testcase123?'))

    def test_validateLogin(self):
        validation = v.Validation()
        self.assertTrue(validation.validateLogin('Testcase123'))
        self.assertFalse(validation.validateLogin('Testca'))

if __name__ == '__main__':
    unittest.main()