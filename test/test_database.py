import unittest
import config as cfg
import database as d


class TestDatabase(unittest.TestCase):
    """
        A class to test database operations.
    """
    def test_addUser(self):
        database = d.Database()
        database.connect(file=f"../{cfg.db['file']}")
        self.assertTrue(database.addUser("Testcase","b31c38757c5b7b2bdb3d5c042a2b7d5e52166c0df86bd03638d37436ea002938","b'R\xb9\x8f\xf5\xd5 \xa0\x18=63v\xd1\x91\xfe\xed'"))
        self.assertEqual(database.addUser("Testcase","b31c38757c5b7b2bdb3d5c042a2b7d5e52166c0df86bd03638d37436ea002938","b'R\xb9\x8f\xf5\xd5 \xa0\x18=63v\xd1\x91\xfe\xed'"),'login_exist')

    def test_selectUser(self):
        database = d.Database()
        database.connect(file=f"../{cfg.db['file']}")
        self.assertTrue(database.selectUser("Testcase"))
        self.assertFalse(database.selectUser("Test"))

if __name__ == '__main__':
    unittest.main()