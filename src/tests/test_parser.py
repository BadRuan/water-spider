from unittest import TestCase
from utils.parser import Parser
from model import DataWaterlevel


class TestParser(TestCase):

    def test_translate(self):
        parser = Parser()
        with open("./tests/res_data/correct.txt", "r", encoding="utf-8") as file:
            file_str = file.read()
            data_waterlevel: DataWaterlevel = parser.translate(file_str)
            count = 1787
            self.assertEqual(count, data_waterlevel.count)
        with open("./tests/res_data/code-1.txt", "r", encoding="utf-8") as file:
            file_str = file.read()
            with self.assertRaises(ValueError):
                parser.translate(file_str)
