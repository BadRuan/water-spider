import logging
from engine import App

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    app = App()
    app.start()