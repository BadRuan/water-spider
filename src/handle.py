import httpx
from abc import ABC, abstractmethod
from typing import Optional
from asyncio import sleep
from src.model import Request
from src.utils import Logger, encode, translate, insert_waterlevel


logger = Logger(__name__)

# API 请求失败时的最大重试次数
MAX_RETRIES = 3
RETRY_DELAY = 5  # 秒


class Handler(ABC):
    def __init__(self, successor: Optional['Handler'] = None):
        self._successor = successor

    def set_next(self, handler: 'Handler') -> 'Handler':
        self._successor = handler
        return handler

    @abstractmethod
    async def handle(self, request: Request) -> None:
        if self._successor:
            return await self._successor.handle(request)
        return None

class SendApiHandler(Handler):
    def __init__(self, successor: Handler | None = None):
        super().__init__(successor)
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "DNT": "1",
            "Origin": "http://yc.wswj.net",
            "Referer": "http://yc.wswj.net/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        }
        self.url = "http://61.191.22.196:5566/AHSXX/service/PublicBusinessHandler.ashx"

    def _build_payload(self, request: Request) -> dict:
        """根据站点编码构建请求参数"""
        payload = {
            "name": encode("GetSwLineMap"),
            "stcd": encode(str(request.code)),
            "btime": encode(request.date_range.start_time),
            "etime": encode(request.date_range.end_time),
            "sttp": encode("ZQ"),
            "waterEncode": encode("true"),
        }
        # 凤凰颈新站闸上：特殊接口参数
        if request.code == 62904400:
            payload["name"] = encode("GetSwLineAndZX")
            payload["sttp"] = encode("DD")
            payload["zxstcd"] = encode("62904500")
            payload["zxsttp"] = encode("ZQ")
        # 裕溪闸上：参数不一致
        if request.code == 62900600:
            payload["sttp"] = encode("DD")
        # 新桥闸上：参数不一致
        if request.code == 62905100:
            payload["name"] = encode("GetSwLineAndZX")
            payload["sttp"] = encode("DD")
            payload["zxstcd"] = encode("62905200")
            payload["zxsttp"] = encode("ZZ")
        return payload

    async def handle(self, request: Request) -> None:
        """发送 API 请求，支持自动重试"""
        payload = self._build_payload(request)

        for attempt in range(1, MAX_RETRIES + 1):
            try:
                async with httpx.AsyncClient(verify=False, timeout=30.0) as client:
                    response = await client.post(
                        url=self.url,
                        headers=self.headers,
                        data=payload,
                    )
                    response.raise_for_status()
                    request.encode_date = response.text
                    break
            except (httpx.HTTPStatusError, httpx.RequestError) as e:
                logger.warning(f"API 请求失败 (第 {attempt}/{MAX_RETRIES} 次): {e}")
                if attempt == MAX_RETRIES:
                    logger.error(f"API 请求最终失败，站点: {request.name}，时间: {request.date_range.start_time}")
                    raise ValueError(f"API 请求失败，已重试 {MAX_RETRIES} 次: {e}") from e
                await sleep(RETRY_DELAY)

        if self._successor:
            await self._successor.handle(request)

class DecodeHandler(Handler):
    async def handle(self, request: Request) -> None:
        if request.encode_date is not None:
            request.data += translate(request.encode_date)
        if self._successor:
            await self._successor.handle(request)

class StorageHandle(Handler):
    async def handle(self, request: Request) -> None:
        if request.data:
            await insert_waterlevel(request)
