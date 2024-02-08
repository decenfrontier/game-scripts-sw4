from loguru import logger as loguru_logger
from datetime import datetime
import os

from const.const import PATH_SOFTWARE_LOG

# ---------------------- 日志操作 ----------------------
class Logger():
    def __init__(self, path):
        self.logger = loguru_logger
        # chmod 755 logs
        now = datetime.now().strftime("%m-%d_%H-%M-%S")
        log_path_info = os.path.join(path, f'info_{now}.log')
        # file_create(log_path_info)
        log_path_error = os.path.join(path, f'error_{now}.log')
        # file_create(log_path_error)
        self.logger.add(
            sink=log_path_info,
            rotation='10 MB',  # 日志文件最大限制
            retention='7 days',  # 最长保留天
            format="{time}|{message}",  # 日志显示格式
            compression="zip",  # 压缩形式保存
            encoding='utf-8',  # 编码
            level='INFO',  # 日志级别
        )
        self.logger.add(
            sink=log_path_error,
            rotation='10 MB',  # 日志文件最大限制
            retention='7 days',  # 最长保留天
            format="{time}|{message}",  # 日志显示格式
            compression="zip",  # 压缩形式保存
            encoding="utf-8",
            level='ERROR',  # 日志级别
        )

    def info(self, msg: str):
        self.logger.info(msg)

    def warn(self, msg: str):
        self.logger.warning(msg)


log = Logger(PATH_SOFTWARE_LOG)

if __name__ == '__main__':
    cwd = os.getcwd()
    logger = Logger(os.path.join(cwd, 'logs'))
    logger.info('info')
    logger.warn('warn')
