from json import loads
from typing import List
import threading
from src.model import WaterItem
from src.utils.logger import Logger


logger = Logger(__name__)


class _SingletonMeta(type):
    """线程安全的单例元类"""
    _instances: dict = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                # 双重检查锁定
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]


class WaterSecurity(metaclass=_SingletonMeta):
    """水位数据加解密工具"""

    def __init__(self):
        self.version = "2.1"
        self._encode_chars = (
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvwxyz" + "0123456789+/"
        )
        self._decode_chars = [-1] * 256
        for i, char in enumerate(self._encode_chars):
            self._decode_chars[ord(char)] = i

    def gblen(self, s: str) -> int:
        """计算字符串长度（中文字符算 2）"""
        length = 0
        for char in s:
            if ord(char) > 127 or ord(char) == 94:
                length += 2
            else:
                length += 1
        return length

    def encode(self, data: str) -> str:
        if not data:
            return ""

        processed_data = self._utf16to8(_encode_uri_component(data).replace("+", "%2B"))
        if self.gblen(processed_data) % 2 != 0:
            processed_data += "*"

        transposed_data = self._parity_transposition(processed_data)
        encoded_str = self._base64_encode(transposed_data)
        return f"{self.version}{encoded_str}"

    def decode(self, data: str) -> str:
        if not isinstance(data, str) or len(data) < 5:
            return "[]"

        if data[:3] != self.version:
            return data

        processed_data = data[3:]
        end_tag = processed_data[-4:]
        tags_str = processed_data[processed_data.index(end_tag):]
        tags_str = tags_str[4:-4]

        tags = [tags_str[i: i + 4] for i in range(0, len(tags_str), 4)]
        positions = self._get_tags_position(processed_data, tags)

        content = {}
        index = 0
        for pos in sorted(positions):
            msg = processed_data[index:pos]
            tag = processed_data[pos: pos + 4]
            content[tag] = msg
            index = pos + 4

        result = "".join([content[tag] for tag in tags])
        decoded_str = self._base64_decode(result)
        return self._utf8to16(decoded_str)

    def _parity_transposition(self, data: str) -> str:
        """奇偶位互换"""
        new_data = []
        for i in range(0, len(data), 2):
            if i + 1 < len(data):
                new_data.append(data[i + 1])
                new_data.append(data[i])
            else:
                new_data.append(data[i])
        return "".join(new_data)

    def _base64_encode(self, str_: str) -> str:
        """自定义 base64 编码"""
        out = []
        i = 0
        while i < len(str_):
            c1 = ord(str_[i]) & 255
            i += 1
            if i == len(str_):
                out.append(self._encode_chars[c1 >> 2])
                out.append(self._encode_chars[(3 & c1) << 4])
                out.append("==")
                break

            c2 = ord(str_[i]) & 255
            i += 1
            if i == len(str_):
                out.append(self._encode_chars[c1 >> 2])
                out.append(self._encode_chars[(3 & c1) << 4 | (240 & c2) >> 4])
                out.append(self._encode_chars[(15 & c2) << 2])
                out.append("=")
                break

            c3 = ord(str_[i]) & 255
            i += 1
            out.append(self._encode_chars[c1 >> 2])
            out.append(self._encode_chars[(3 & c1) << 4 | (240 & c2) >> 4])
            out.append(self._encode_chars[(15 & c2) << 2 | (192 & c3) >> 6])
            out.append(self._encode_chars[63 & c3])
        return "".join(out)

    def _base64_decode(self, str_: str) -> str:
        """自定义 base64 解码"""
        out = []
        i = 0
        while i < len(str_):
            while i < len(str_) and self._decode_chars[ord(str_[i])] == -1:
                i += 1
            if i >= len(str_):
                break
            c1 = self._decode_chars[ord(str_[i])]
            i += 1

            while i < len(str_) and self._decode_chars[ord(str_[i])] == -1:
                i += 1
            if i >= len(str_):
                raise ValueError("解密数据异常")
            c2 = self._decode_chars[ord(str_[i])]
            i += 1

            out.append(chr((c1 << 2) | (48 & c2) >> 4))

            while i < len(str_) and self._decode_chars[ord(str_[i])] == -1:
                i += 1
            if i >= len(str_):
                return "".join(out)
            c3 = self._decode_chars[ord(str_[i])]
            i += 1

            out.append(chr((15 & c2) << 4 | (60 & c3) >> 2))

            while i < len(str_) and self._decode_chars[ord(str_[i])] == -1:
                i += 1
            if i >= len(str_):
                return "".join(out)
            c4 = self._decode_chars[ord(str_[i])]
            i += 1

            out.append(chr((3 & c3) << 6 | c4))
        return "".join(out)

    def _utf16to8(self, str_: str) -> str:
        out = []
        for char in str_:
            c = ord(char)
            if 1 <= c <= 127:
                out.append(char)
            elif c > 2047:
                out.extend([
                    chr(224 | (c >> 12) & 15),
                    chr(128 | (c >> 6) & 63),
                    chr(128 | c & 63),
                ])
            else:
                out.extend([chr(192 | (c >> 6) & 31), chr(128 | c & 63)])
        return "".join(out)

    def _utf8to16(self, str_: str) -> str:
        out = []
        i = 0
        while i < len(str_):
            c = ord(str_[i]) >> 4
            i += 1
            if 0 <= c <= 7:
                out.append(str_[i - 1])
            elif c == 12 or c == 13:
                char2 = ord(str_[i]) & 255
                i += 1
                out.append(chr((c << 6) | (char2 & 63)))
            elif c == 14:
                char2 = ord(str_[i]) & 255
                i += 1
                char3 = ord(str_[i]) & 255
                i += 1
                out.append(chr((c << 12) | (char2 << 6) | char3))
        return "".join(out)

    def _get_tags_position(self, data: str, tags: list[str]) -> list[int]:
        positions = []
        for tag in tags:
            if tag not in data:
                raise ValueError(f"Tag {tag} not found in data.")
            positions.append(data.index(tag))
        return sorted(positions)


def _encode_uri_component(s: str) -> str:
    from urllib.parse import quote
    return quote(s, safe="~()*!.'")


class Parser(metaclass=_SingletonMeta):
    """解析 API 响应数据"""

    def __init__(self):
        self._security = WaterSecurity()

    def translate(self, data: str) -> List[WaterItem]:
        _r = loads(data)
        resp_code: str = _r["respCode"]
        if resp_code != "0":
            _msg = f"响应错误，错误信息为 {_r['respMsg']}"
            logger.error(_msg)
            raise ValueError(_msg)

        encode_str: str = _r["data"]
        decode_str: str = self._security.decode(encode_str)
        json_obj = loads(decode_str)
        data_sw: List = json_obj["data_sw"]
        return [WaterItem(height=i["Z"], timestamp=i["TM"]) for i in data_sw]


encode = WaterSecurity().encode
decode = WaterSecurity().decode
translate = Parser().translate
