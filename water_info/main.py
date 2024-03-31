import logging
from lib.engine import Engine

logging.basicConfig(
    level=logging.INFO,
    # filename="console.log",
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%m:%S",
)

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    app = Engine()
    # app.start('202403311700')
    app.get_all_three_line()