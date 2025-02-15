from spiders.api_spdier import ApiSpider
from model import DataWaterlevel


if __name__ == "__main__":
    spdier = ApiSpider()
    # spdier.get_data()
    data_waterlevel: DataWaterlevel = spdier.get_data()
    print(data_waterlevel)
