import logging
from engine import App

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    app = App()
    a = app.start("202404022000")
    # app.get_threeline()
    # app.first_start()
