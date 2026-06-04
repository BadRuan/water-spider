import logging
from pathlib import Path
from logging.handlers import TimedRotatingFileHandler
from rich.logging import RichHandler
from rich.traceback import install

# 缓存已创建的 logger，避免重复添加 handler
_initialized_loggers: set[str] = set()

# 日志目录（全局唯一）
LOG_DIR = Path(__file__).parent.parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

# 全局安装 rich 异常美化（只需执行一次）
install(show_locals=True)


def Logger(name: str) -> logging.Logger:
    """获取或创建 logger，确保每个模块名只初始化一次 handler"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if name not in _initialized_loggers:
        _initialized_loggers.add(name)

        # 控制台处理器
        console_handler = RichHandler(
            rich_tracebacks=True,
            tracebacks_show_locals=True,
            level=logging.INFO,
        )
        console_format = logging.Formatter("%(asctime)s | %(levelname)-8s | %(message)s")
        console_handler.setFormatter(console_format)

        # 文件处理器（按天轮转，保留 7 天）
        file_handler = TimedRotatingFileHandler(
            filename=LOG_DIR / "app.log",
            when="midnight",
            backupCount=7,
            encoding="utf-8",
        )
        file_handler.setLevel(logging.DEBUG)
        file_format = logging.Formatter(
            "%(asctime)s | %(name)-20s | %(levelname)-8s | %(message)s"
        )
        file_handler.setFormatter(file_format)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
