#!/usr/local/bin python3
from logging import Logger, DEBUG, StreamHandler, FileHandler, Formatter


class logger_test(Logger):
    def __init__(self, name):
        super().__init__(name)
        self.setLevel(DEBUG)
        ch = StreamHandler()
        ch.setLevel(DEBUG)
        fh = FileHandler('gamelog.log')
        fh.setLevel(DEBUG)
        formatter = Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        self.addHandler(ch)


