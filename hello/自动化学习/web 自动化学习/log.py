#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import time

'''
日志级别：
NOTSET（0）、DEBUG（10）、INFO（20）、WARNING（30）、ERROR（40）、CRITICAL（50）
级别不设置的情况下：日志默认为30
'''
# 获取当前的时间
time = time.strftime("%Y-%m-%d %H:%M %p", time.localtime())
print(time)

logging.basicConfig(filename='test.log', filemode='w', format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S", level=0)
logging.debug('这是调试')
logging.info('这是基本信息')
logging.warning('这是警告')
logging.error('这是错误')
logging.critical('这是最严重的的错误，级别最高')





