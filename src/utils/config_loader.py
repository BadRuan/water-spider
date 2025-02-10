from utils.logger_tool import setup_logger
from yaml import safe_load, YAMLError
from pathlib import Path

logger = setup_logger(__name__)


def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton


@Singleton
class Config:
    value = None

    def __init__(self, env: str = "dev"):
        try:
            file_name: str = f"{env}_settings.yaml"
            logger.info(f"配置文件 {file_name}")
            config_path: str = (
                Path(__file__).parent.parent.parent / f"config" / file_name
            )
            logger.debug(f"配置文件路径:  {config_path}")
            with open(config_path, mode="r", encoding="utf-8") as file:
                logger.info(f"配置文件 {file_name} 解析成功")
                self.value = safe_load(file)
        except YAMLError as error:
            logger.error(f"配置文件格式异常：{error}")
        except FileNotFoundError as error:
            logger.error(f"配置文件不存在")
        except PermissionError as error:
            logger.error(f"配置文件无读取权限")
        except IOError as error:
            logger.error(f"配置文件读取失败: {error}")
        except Exception as error:
            logger.error(f"配置文件读取失败: {error}")
