import unittest
from core.settings import DATABASE_DEV
from util.tdenginetool import TDengineTool


class TestTDengineTool(unittest.TestCase):

    def test_connectDatabase(self):
        database = ""
        with TDengineTool() as connect:
            result = connect.query("SELECT DATABASE()")
            for i in result:
                database = i[0]
        self.assertEqual(database, DATABASE_DEV.database)
