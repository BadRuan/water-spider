import logging
from control.waterlevel import WaterlevelControl

logging.basicConfig(
    level=logging.INFO,
    # filename="console.log",
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%m:%S",
)

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    app = WaterlevelControl()
    a = app.save_waterlevel_info("202404011600")
