from asyncio import run
from engine import spider


async def main() -> None:
    await spider.run_in_24_hour()
    

if __name__ == "__main__":
    run(main())