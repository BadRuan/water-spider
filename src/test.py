from asyncio import run
from service.api import ApiService


async def main():
    api = ApiService()
    r = await api.get_recently_data()
    print(type(r))

if __name__ == "__main__":
    run(main())
