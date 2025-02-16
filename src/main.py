from engine import Engine
from apscheduler.schedulers.blocking import BlockingScheduler


if __name__ == "__main__":
    engine = Engine()
    scheduler = BlockingScheduler()
    # 定时：每天8:21 运行一次
    scheduler.add_job(engine.run, "cron", hour=8, minute=21)
    scheduler.start()

