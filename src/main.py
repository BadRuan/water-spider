from spiders.base_spider import BaseSpider
from spiders.api_spider import ApiSpider
from parsers.base_parser import BaseParser
from parsers.api_parser import ApiParser


if __name__ == "__main__":
    spider: BaseSpider = ApiSpider()
    parser: BaseParser = ApiParser()

    # respose_data = spider.get_response()
    decode_str = parser.translate("2.1cnRldQ==")

    print(decode_str)
