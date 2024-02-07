import logging
from logging.handlers import TimedRotatingFileHandler

# ---------------------- 日志操作 ----------------------
class Logger():
    def __init__(self, path):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        # 创建handler对象
        self.handler_info = TimedRotatingFileHandler(filename=path, when="midnight", interval=1,
                                                     backupCount=3)
        self.handler_info.setFormatter(
            logging.Formatter("%(asctime)s  %(message)s"))
        self.handler_info.setLevel(logging.INFO)
        # 添加handler
        self.logger.addHandler(self.handler_info)

    def info(self, msg: str):
        self.logger.info(msg)

    def warn(self, msg: str):
        self.logger.warning(msg)
