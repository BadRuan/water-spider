from typing import List
from yaml import safe_load, YAMLError
from pathlib import Path
from utils.logger import Logger

logger = Logger(__name__)


def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton


@Singleton
class Configuration:
    value = None

    def __init__(self, env: str = "dev"):
        try:
            file_name: str = f"{env}_settings.yaml"
            config_path: str = Path(__file__).parent.parent / f"config" / file_name
            with open(config_path, mode="r", encoding="utf-8") as file:
                logger.info(f"配置文件 {file_name} 解析成功")
                self.value = safe_load(file)
        except YAMLError as error:
            logger.error(f"配置文件格式异常：{error}")
        except FileNotFoundError as error:
            logger.error(f"配置文件{config_path}不存在")
        except PermissionError as error:
            logger.error(f"配置文件无读取权限")
        except IOError as error:
            logger.error(f"配置文件读取失败: {error}")
        except Exception as error:
            logger.error(f"配置文件读取失败: {error}")

    def getStations(self) -> List:
        try:
            if None == self.value:
                _msg = "配置为空，请确认配置文件内容"
                logger.error(_msg)
                raise ValueError(_msg)
            return self.value["stations"]
        except ValueError:
            logger.error("无法从配置文件读取站点信息")

    def getDatabase(self):
        try:
            if None == self.value:
                _msg = "配置为空，请确认配置文件内容"
                logger.error(_msg)
                raise ValueError(_msg)
            return self.value["database"]
        except ValueError:
            logger.error("无法从配置文件读取数据库配置信息")
