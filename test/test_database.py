import unittest
import config as cfg
import database as d

class TestDatabase(unittest.TestCase):
    """
        A class to test validation of data.
    """
    def test_addUser(self):
        database = d.Database()
        database.connect(file=f"../{cfg.db['file']}")
        self.assertTrue(database.addUser("Testcase","password","salt"))
        self.assertEqual(database.addUser("Testcase","password","salt"),'login_exist')

    def test_selectUser(self):
        database = d.Database()
        database.connect(file=f"../{cfg.db['file']}")
        self.assertTrue(database.selectUser("Testcase"))
        self.assertFalse(database.selectUser("Test"))

if __name__ == '__main__':
    unittest.main()