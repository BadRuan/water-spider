from storages.database_storage import DatabaseStorage


if __name__ == "__main__":
    storage = DatabaseStorage()

    with DatabaseStorage() as storage:
        count = storage.execute("SELECT count(*) FROM `waterlevel` LIMIT 20")
        print(count)
