from engine import Engine
from apscheduler.schedulers.blocking import BlockingScheduler


if __name__ == "__main__":
    engine = Engine()
    # scheduler = BlockingScheduler()
    # scheduler.add_job(engine.run, "cron", hour=0, minute=18)
    # scheduler.add_job(engine.run, "cron", hour=8, minute=21)
    # scheduler.add_job(engine.run, "cron", hour=16, minute=43)
    engine.run()
    # scheduler.start()
