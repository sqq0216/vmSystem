#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

# ThreadCmd类
# 存储全局变量，读写锁和共享命令
# 对外提供两个接口

"""
@author:    chenkuan
@license:   GNU General Public License 2.0
@contact:   chen1511@foxmail.com
@version:   1.0-2016-08-10
"""

import threading

class ThreadCmd(object):

    # 执行与中断命令读写锁
    breakLock = threading.Lock()
    # 执行与中断命令判断表
    ebList = {}

def getBreakLock():
    return ThreadCmd.breakLock

def getEBList():
    return ThreadCmd.ebList
