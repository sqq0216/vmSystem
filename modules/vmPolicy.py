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

    def __init__(self, extrapol = ""):
        #self.shouldRestartVm = False
        #self.shouldRestoreVm = False
        #self.shouldRestartProcesses = []
        self.clearPolicy()

    def clearPolicy(self):
        """
        # level=0,不执行操作
        # level=1,最高为重启进程
        # level=2,最高为重启虚拟机
        # level=3,最高为恢复虚拟机
        :return:
        """
        self.level = 0

        self.shouldRestartVm = False
        self.shouldRestoreVm = False
        self.shouldRestartProcesses = []

    def setLevel(self, level):
        """
        # 仅当传入的执行等级更高时才更新
        :param level:
        :return:
        """
        if level > self.level:
            self.level = level

    def toString(self):
        if self.level == 0:
            return u""
        elif self.level == 1:
            return u"恢复虚拟机"
        elif self.level == 2:
            return u"重启虚拟机"
        elif self.level == 3:
            return u"重启进程"
        elif self.level == 4:
            return u"关闭进程"
        elif self.level == 5:
            return u"打开进程"
        elif self.level == 6:
            return u"关闭端口"
        elif self.level == 7:
            return u"告警"
        else:
            return u""

    def setPolicy(self, policy):
        pass