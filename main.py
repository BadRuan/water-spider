from asyncio import run
from src.utils import init_db_pool, close_db_pool, Logger
from src.engine import spider

log = Logger(__name__)


async def main() -> None:
    await init_db_pool()
    log.info("数据库连接池初始化完成")

    try:
        await spider.run_in_24_hour()
    finally:
        await close_db_pool()
        log.info("数据库连接池已关闭")


if __name__ == "__main__":
    run(main())
