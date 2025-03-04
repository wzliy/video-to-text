import logging
from logging.handlers import RotatingFileHandler


class LoggerUtils:
    def __init__(self, name="app", log_file="app.log", level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # 避免重复添加Handler（单例模式）
        if not self.logger.handlers:
            # 控制台Handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(level)

            # 文件Handler（支持轮转）
            file_handler = RotatingFileHandler(log_file, maxBytes=10 * 1024 * 1024, backupCount=5)
            file_handler.setLevel(level)

            # 设置日志格式（参考网页3、8的Formatter思路）
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            console_handler.setFormatter(formatter)
            file_handler.setFormatter(formatter)

            self.logger.addHandler(console_handler)
            self.logger.addHandler(file_handler)