from utils.logger import Logger


logger = Logger(__name__)


class WaterSecurity:
    def __init__(self):
        self.version = "2.1"
        self._encode_chars = (
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvwxyz" + "0123456789+/"
        )
        self._decode_chars = [-1] * 256
        for i, char in enumerate(self._encode_chars):
            self._decode_chars[ord(char)] = i

    def gblen(self, s: str) -> int:
        length = 0
        for char in s:
            if ord(char) > 127 or ord(char) == 94:
                length += 2
            else:
                length += 1
        return length

    def encode(self, data: str) -> str:
        data += ""
        if not data:
            return ""

        processed_data = self.utf16to8(encode_uri_component(data).replace("+", "%2B"))
        if self.gblen(processed_data) % 2 != 0:
            processed_data += "*"

        transposed_data = self.parity_transposition(processed_data)
        encoded_str = self._encode(transposed_data)
        return f"{self.version}{encoded_str}"

    def decode(self, data: str) -> str:
        if not isinstance(data, str):
            data += ""
        if len(data) < 5 or not data:
            return "[]"

        if self.version and data[:3] != self.version:
            return data

        processed_data = data[3:]
        end_tag = processed_data[-4:]
        tags_str = processed_data[processed_data.index(end_tag) :]
        tags_str = tags_str[4:-4]

        tags = [tags_str[i : i + 4] for i in range(0, len(tags_str), 4)]
        positions = self._get_tags_position(processed_data, tags)

        content = {}
        index = 0
        for pos in sorted(positions):
            msg = processed_data[index:pos]
            tag = processed_data[pos : pos + 4]
            content[tag] = msg
            index = pos + 4

        result = "".join([content[tag] for tag in tags])
        decoded_str = self._decode(result)
        return self.utf8to16(decoded_str)

    def parity_transposition(self, data: str) -> str:
        new_data = []
        for i in range(0, len(data), 2):
            new_data.append(data[i + 1])
            new_data.append(data[i])
        return "".join(new_data)

    def _encode(self, str_: str) -> str:
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

    def _decode(self, str_: str) -> str:
        out = []
        i = 0
        while i < len(str_):
            error_message = "解密数据异常"
            while True:
                if i >= len(str_):
                    logger.error(error_message)
                    raise ValueError(error_message)
                c1 = self._decode_chars[ord(str_[i])]
                i += 1
                if c1 != -1:
                    break

            while True:
                if i >= len(str_):
                    logger.error(error_message)
                    raise ValueError(error_message)
                c2 = self._decode_chars[ord(str_[i])]
                i += 1
                if c2 != -1:
                    break

            out.append(chr((c1 << 2) | (48 & c2) >> 4))

            while True:
                if i >= len(str_):
                    return "".join(out)
                c3 = self._decode_chars[ord(str_[i])]
                i += 1
                if c3 != -1:
                    break

            out.append(chr((15 & c2) << 4 | (60 & c3) >> 2))

            while True:
                if i >= len(str_):
                    return "".join(out)
                c4 = self._decode_chars[ord(str_[i])]
                i += 1
                if c4 != -1:
                    break

            out.append(chr((3 & c3) << 6 | c4))
        return "".join(out)

    def utf16to8(self, str_: str) -> str:
        out = []
        for char in str_:
            c = ord(char)
            if 1 <= c <= 127:
                out.append(char)
            elif c > 2047:
                out.extend(
                    [
                        chr(224 | (c >> 12) & 15),
                        chr(128 | (c >> 6) & 63),
                        chr(128 | c & 63),
                    ]
                )
            else:
                out.extend([chr(192 | (c >> 6) & 31), chr(128 | c & 63)])
        return "".join(out)

    def utf8to16(self, str_: str) -> str:
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
                message = f"Tag {tag} not found in data."
                logger.error(message)
                raise ValueError(message)
            positions.append(data.index(tag))
        return sorted(positions)


def encode_uri_component(s: str) -> str:
    import urllib.parse

    return urllib.parse.quote(s, safe="~()*!.'")
