from unittest import TestCase
from utils.logger import Logger
from storages.database_storage import DatabaseStorage

logger = Logger(__name__)


class TestStorage(TestCase):

    def test_connect(self):
        with DatabaseStorage() as storage:
            self.assertIsNotNone(storage.conn)
            logger.debug(f"数据库连接测试成功")
            