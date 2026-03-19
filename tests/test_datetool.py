from src.utils.datetool import DateTool
from src.utils.logger import Logger


logger = Logger(__name__)

class TestDateTool():
    def test_get_time_range(self):
        datetool = DateTool()
        r = datetool.get_time_range('202603121222', 1)
        if r is not None:
            assert r.start_time == '202603111222'
        