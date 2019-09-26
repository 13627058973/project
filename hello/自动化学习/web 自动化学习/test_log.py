#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import time
import os


class MyLog:

    def __init__(self, log_name):
        self.log_name = log_name   # 日志收集器的名字

    def my_log(self, msg, level):
        logger = logging.getLogger(self.log_name)
        logger.setLevel("DEBUG")   # 包含info级别在内以及以上的日志
        # 格式： 决定我们日志输出格式
        formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")

        # 2,日志输出器 控制台 指定的文件
        ch = logging.StreamHandler()  # 渠道是指输出到控制台
        ch.setLevel("DEBUG")    # 只输出info以上的
        ch.setFormatter(formatter)

        now = time.strftime('%Y-%m-%d %H:%M:%S')   # 获取当前的时间
        path = "test_api.log"   # 拼接路径
        # 最终日志存放的地方
        fh = logging.FileHandler(path, encoding='utf-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)

        # 3,对接
        logger.addHandler(ch)
        logger.addHandler(fh)

        if level == 'DEBUG':
            logger.debug(msg)
        if level == 'INFO':
            logger.info(msg)
        if level == 'WARNING':
            logger.warning(msg)
        if level == 'ERROR':
            logger.error(msg)
        if level == 'CRITICAL':
            logger.critical(msg)

        logger.removeHandler(ch)
        logger.removeHandler(fh)

    def debug(self, msg):
        self.my_log(msg, 'DEBUG')

    def info(self, msg):
        self.my_log(msg, 'INFO')

    def warning(self, msg):
        self.my_log(msg, 'WARNING')

    def error(self, msg):
        self.my_log(msg, 'ERROR')

    def critical(self, msg):
        self.my_log(msg, 'CRITICAL')


if __name__ == '__main__':
    log = MyLog('root')
    log.debug('这是调试')
    log.info('这是基本信息')
    log.warning('这是警告')
    log.error('这是错误')
    log.critical('这是最严重的的错误，级别最高')


