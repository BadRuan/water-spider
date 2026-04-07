from src.utils.logger import Logger
from src.utils.storage import PostgresStorage

log = Logger(__name__)

def test_get_total_count():
    with PostgresStorage() as storage:
        log.info(storage.get_total_count())