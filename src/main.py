from utils.logger import Logger
from time import sleep
from config.settings import LIMIT_frequency
from engine import Engine

logger = Logger(__name__)

if __name__ == "__main__":
    engine = Engine()
    while True:
        engine.run()
        logger.info(f"间隔{LIMIT_frequency}秒, 执行下趟任务")
        sleep(LIMIT_frequency)
