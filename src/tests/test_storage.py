from unittest import TestCase
from model import DataWaterlevel
from utils.logger import Logger
from utils.parser import Parser
from storages.database_storage import DatabaseStorage

logger = Logger(__name__)


class TestStorage(TestCase):

    def test_connect(self):
        with DatabaseStorage() as storage:
            self.assertIsNotNone(storage.conn)
            logger.debug(f"数据库连接测试成功")
    
    def test_insert_waterlevel(self):
        parser = Parser()
        with open("./tests/res_data/correct.txt", "r", encoding="utf-8") as file:
            file_str = file.read()
            data_waterlevel: DataWaterlevel = parser.translate(file_str)
            with DatabaseStorage() as storage:
                storage.insert_waterlevel(data_waterlevel)
        