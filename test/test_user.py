import unittest
import user as u
import config as cfg
import database as d


class TestUser(unittest.TestCase):
    """
        A class to test user methods.
    """
    def test_checkCredentials(self):
        database = d.Database()
        database.connect(file=f"../{cfg.db['file']}")
        user = u.User(database)
        user.add('Testcase0', 'Testcase123?', 'Testcase123?')
        self.assertTrue(user.checkCredentials('Testcase0', 'Testcase123?'))
        self.assertFalse(user.checkCredentials('Testcase0', 'testcase123?'))

if __name__ == '__main__':
    unittest.main()