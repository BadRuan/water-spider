from unittest import TestSuite, TextTestRunner
from tests.test_config_loader import TestLoadConfig
from tests.test_date_tool import TestDateTool


if __name__ == "__main__":
    case_list = [
        TestLoadConfig("test_load_config"),
        TestDateTool("test_get_time_range"),
        TestDateTool("test_get_recently_time_range"),
        TestDateTool("test_get_target_year_date_range_list"),
    ]
    suite = TestSuite()
    suite.addTests(case_list)
    runner = TextTestRunner()
    runner.run(suite)
