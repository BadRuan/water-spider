from unittest import TestSuite, TextTestRunner
from tests.test_date_tool import TestDateTool


if __name__ == "__main__":
    suite = TestSuite()
    runner = TextTestRunner()

    case_list = [TestDateTool('test_get_time_range'), TestDateTool('test_get_recently_time_range'),TestDateTool('test_get_target_year_date_range_list')]
    suite.addTests(case_list)

    runner.run(suite)
