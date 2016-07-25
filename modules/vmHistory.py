#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

# VmPolicy类
# 存储需要对虚拟机执行的指令



"""
@author:    chenkuan
@license:   GNU General Public License 2.0
@contact:   chen1511@foxmail.com
@version:   1.0-2016-07-24
"""

class VmHistory(object):

    def __init__(self):
        self.clearHistory()

    def clearHistory(self):
        self.processesRestartTimes = {}
        self.vmRestartTimes = 0
        self.vmRestoreTimes = 0