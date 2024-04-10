import base64


# 加密及解密响应数据的工具类
class EncodeTool:
    def __init__(self, version: str = "2.1") -> None:
        self.version = version

    def _parity_transposition(self, e) -> str:
        result = [""] * len(e)
        for i in range(0, len(e), 2):
            result[i] = e[i + 1] if i + 1 < len(e) else ""
            result[i + 1] = e[i] if i + 1 < len(e) else ""
        return "".join(result)

    def _encode(self, e: str) -> str:
        if not e:
            return ""

        utf8_encoded = e.encode("utf-8")
        if len(utf8_encoded) % 2 != 0:
            utf8_encoded += b"*"

        e_parity_transposed = self._parity_transposition(utf8_encoded.decode("utf-8"))
        base64_encoded = base64.b64encode(e_parity_transposed.encode("utf-8"))

        return f"2.1{base64_encoded.decode('utf-8')}"

    def __check_version(self, data: str) -> bool:
        version_info = data[:3]  # 截取前3位复核版本号
        if self.version == version_info:
            return True
        else:
            return False

    def __getTagPosition(self, e: str, r: list) -> list:
        t, n = [], 0
        while n < len(r):
            t.append(e.index(r[n]))
            n = n + 1
        t.sort()
        return t  # 此处排序可能错误，后面验证

    def __decode(self, data: str) -> str:
        if self.__check_version(data):

            e = data[3:]  # data为去除版本号的有效数据

            r = e[-4:]  # r为数据最后4位
            t = e[e.index(r) :]  # r的值
            n, a = [], {}
            t = t[4 : len(t) - 4]

            o = 0
            while 4 * o < len(t):
                i = t[4 * o : 4 * o + 4]
                n.append(i)
                a[i] = ""
                o = o + 1

            c = self.__getTagPosition(e, n)

            o, s = 0, 0
            while o < len(c):
                h = e[s : c[o]]
                i = e[c[o] : c[o] + 4]
                a[i] = h
                s = c[o] + 4
                o = o + 1

            u, o = "", 0
            while o < len(n):
                u = u + a[n[o]]
                o = o + 1
            u = base64.b64decode(u).decode("utf-8")
            return u

        else:
            raise ValueError("版本错误")

    def encrypt(self, text: str) -> str:
        return self._encode(text)

    def decrypt(self, encrypted_text: str) -> str:
        return self.__decode(encrypted_text)
