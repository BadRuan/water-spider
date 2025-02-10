from parsers.base_parser import BaseParser
from utils.decode_tool import DecodeTool
from utils.logger import Logger

logger = Logger(__name__)


class ApiParser(BaseParser):
    def __init__(self):
        super().__init__()
        self.tool = DecodeTool()

    def translate(self, data: str):
        return self.tool.decrypt(data)
