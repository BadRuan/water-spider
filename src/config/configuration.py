from typing import List
from utils.logger import Logger
from model import DatabaseConfig, StationConfig
from config.settings import DATABASE_DEV, STATIONS, DEFAULT_DATE_RANGE, INIT_DATE_RANGE

logger = Logger(__name__)


def getStations() -> List[StationConfig]:
    count: int = len(STATIONS)
    if 0 == count:
        _msg = f"配置文件settings.py中站点信息为空, 请检查确认"
        logger.error(_msg)
        raise ValueError(_msg)
    return STATIONS


def getStationName(stcd: int) -> str:
    stations: List[StationConfig] = getStations()
    for station in stations:
        if stcd == station.stcd:
            return station.name

    _msg = f"配置无站点{stcd} 的配置信息"
    logger.error(_msg)
    raise ValueError(_msg)


def getDatabase() -> DatabaseConfig:
    return DATABASE_DEV


def getDefaultDateRange() -> int:
    if DEFAULT_DATE_RANGE < 1:
        _msg = f"日期范围不能小于1天"
        logger.error(_msg)
        raise ValueError(_msg)
    return DEFAULT_DATE_RANGE


def getInitDateRange() -> int:
    if INIT_DATE_RANGE < 1:
        _msg = f"日期范围不能小于1天"
        logger.error(_msg)
        raise ValueError(_msg)
    return INIT_DATE_RANGE
