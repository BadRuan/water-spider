from asyncio import run
from src.utils import init_db_pool
from src.engine import spider


async def main() -> None:
    await init_db_pool()
    await spider.run_in_24_hour()
    

if __name__ == "__main__":
    run(main())