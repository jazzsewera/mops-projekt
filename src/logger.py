import logging

try:
    from colorlog import ColoredFormatter
except:
    print(
        "Install dependencies, e.g. from requirements.txt from the repo root\n\n"
        "$ pip3 install -r requirements.txt\n"
    )
    exit(2)


class Logger(object):
    def __init__(self, obj):
        self.classname = type(obj).__name__ if obj is not None else "Main"

    @classmethod
    def set_logger_params(cls):
        LOGFORMAT = "%(log_color)s%(levelname)-5s | %(log_color)s%(message)s%(reset)s"
        LOGLEVEL = logging.DEBUG
        logging.getLogger().setLevel(LOGLEVEL)
        formatter = ColoredFormatter(LOGFORMAT)
        stream = logging.StreamHandler()
        stream.setLevel(LOGLEVEL)
        stream.setFormatter(formatter)
        logging.getLogger().addHandler(stream)
        logging.debug("Program started")

    def debug(self, msg):
        logging.debug(f"{self.classname} | {msg}")

    def info(self, msg):
        logging.info(f"{self.classname} | {msg}")

    def warn(self, msg):
        logging.warning(f"{self.classname} | {msg}")

    def error(self, msg):
        logging.error(f"{self.classname} | {msg}")

    def critical(self, msg):
        logging.critical(f"{self.classname} | {msg}")
