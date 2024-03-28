import base64

# 解密请求参数工具类
class DecodeTool:
    def __init__(self, version: str ="2.1") -> None:
        self.version = version

    def _parity_transposition(self, e) -> str:
        result = [''] * len(e)
        for i in range(0, len(e), 2):
            result[i] = e[i + 1] if i + 1 < len(e) else ''
            result[i + 1] = e[i] if i + 1 < len(e) else ''
        return ''.join(result)

    def _parity_transposition_reverse(self, e) -> str:
        return self._parity_transposition(e)

    def _decode(self, encrypted_data: str) -> str:
        if not encrypted_data or encrypted_data[:3] != self.version:
            raise ValueError("后台版本不一致或无效的加密数据！")

        versioned_data = encrypted_data[3:]
        base64_decoded = base64.b64decode(versioned_data.encode('utf-8'))
        utf8_decoded = base64_decoded.decode('utf-8')
        original_order_restored = self._parity_transposition_reverse(utf8_decoded)

        # 移除可能存在的星号(*)，这里假设末尾只有一个星号，如果不止一个或规则不同，请按实际情况调整
        if original_order_restored.endswith('*'):
            original_order_restored = original_order_restored[:-1]

        return original_order_restored.encode('utf-8').decode('utf-8')

    def decrypt(self, encrypted_text: str) -> str:
        return self._decode(encrypted_text)
