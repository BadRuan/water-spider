import logging
from lib.engine import Engine

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(module)s | %(message)s",
    datefmt="%Y-%m-%d %H:%m:%s"
)

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    app = Engine()
    app.start('202403301617')
    