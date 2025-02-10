from .base_spider import BaseSpider


class ApiSpider(BaseSpider):

    def set_request(self, *args, **kwargs):
        pass

    def get_response(self, *args, **kwargs) -> str:
        with open("data.txt", "r", encoding="utf-8") as file:
            return file.read()
