from spiders.api_spdier import ApiSpider
from model import DataWaterlevel, RequestDateRange
from utils.date_tool import DateTool
from config.configuration import Configuration


if __name__ == "__main__":
    spider = ApiSpider()
    datetool = DateTool()
    date_range: RequestDateRange = datetool.get_recently_time_range()
    r = spider.get_data(62904500, date_range)
    print(r)
    data_waterlevels: DataWaterlevel = spider.get_recently_data()
    for waterlevel in data_waterlevels[2]:
        print(waterlevel)
