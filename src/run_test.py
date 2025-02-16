from unittest import TestSuite, TextTestRunner
from tests.test_date_tool import TestDateTool
from tests.test_configruation import TestConfiguration
from tests.test_parser import TestParser
from tests.test_storage import TestStorage


if __name__ == "__main__":
    suite = TestSuite()
    runner = TextTestRunner()

    case_list = [
        TestDateTool("test_get_time_range"),
        TestDateTool("test_get_recently_time_range"),
        TestDateTool("test_get_target_year_date_range_list"),
        TestConfiguration("test_getStations"),
        TestConfiguration("test_getStationName"),
        TestConfiguration("test_getDateRange"),
        TestParser("test_translate"),
        TestStorage("test_query")
    ]
    suite.addTests(case_list)

    runner.run(suite)
