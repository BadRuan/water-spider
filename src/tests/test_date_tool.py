from unittest import TestCase
from utils.date_tool import DateTool
from typing import List
from model import RequestDateRange


class TestDateTool(TestCase):

    def test_get_time_range(self):
        date_tool = DateTool()
        date_range = date_tool.get_time_range("202412101200", 5)
        self.assertEqual(date_range.btime, "202412051200")
        self.assertEqual(date_range.etime, "202412101200")

    def test_get_recently_time_range(self):
        date_tool = DateTool()
        date_range = date_tool.get_recently_time_range()
        self.assertIsNotNone(date_range.btime)
        self.assertIsNotNone(date_range.etime)

    def test_get_target_year_date_range_list(self):
        date_tool = DateTool()
        date_range_list: List[RequestDateRange] = date_tool.get_target_year_date_range_list(2025)
        for i in date_range_list:
            print(f"begin_time: {i.btime} | end_time: {i.etime}")
