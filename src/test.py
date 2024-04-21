from dao.api import ApiDao
import asyncio


async def main():
    api = ApiDao()
    data = await api.get_recently_data(62900700)
    for i in data:
        print(i)


if __name__ == "__main__":
    asyncio.run(main())
