import logging
from engine import App

logger = logging.getLogger(__name__)
app = App()


if __name__ == "__main__":
    app.start()
