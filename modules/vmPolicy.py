#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

# VmPolicy类
# 存储需要对虚拟机执行的指令



"""
@author:    chenkuan
@license:   GNU General Public License 2.0
@contact:   chen1511@foxmail.com
@version:   1.0-2016-07-21
"""

class VmPolicy(object):

    def __init__(self):
        #self.shouldRestartVm = False
        #self.shouldRestoreVm = False
        #self.shouldRestartProcesses = []
        self.clearPolicy()

    def clearPolicy(self):
        self.level = 0

        self.shouldRestartVm = False
        self.shouldRestoreVm = False
        self.shouldRestartProcesses = []

    def setLevel(self, level):
        self.level = level