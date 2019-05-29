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

import logging
logger = logging.getLogger()

class VmPolicy(object):

    def __init__(self, initpol = u""):
        """
        # 初始化时可传入一个policy
        :param initpol:
        """
        #self.shouldRestartVm = False
        #self.shouldRestoreVm = False
        #self.shouldRestartProcesses = []
        self.clearPolicy()
        self.policyList = [u"", u"告警", u"关闭端口", u"关闭进程", u"打开进程", u"重启进程", u"关闭虚拟机", u"重启虚拟机", u"恢复虚拟机"]
        self.setPolicy(initpol)

    def clearPolicy(self):
        """
        # level=0,不执行操作
        # 0 无操作
        # 1 告警
        # 2 关闭端口
        # 3 关闭进程
        # 4 打开进程
        # 5 重启进程
        # 6 关闭虚拟机
        # 7 重启虚拟机
        # 8 恢复虚拟机
        :return:
        """
        self.level = 0

        self.shouldRestore = False
        self.shouldRestart = False
        self.shouldShutdown = False

        self.shouldRestartProcesses = [] # (进程名，进程路径，进程pid）
        self.shouldShutdownProcesses = [] # (进程名，进程pid)
        self.shouldOpenProcesses = [] # (进程名，进程路径)

        self.shouldShutdownPorts = []

        self.shouldAlert = False

    def setLevel(self, level):
        """
        # 仅当传入的执行等级更高时才更新
        :param level:
        :return:
        """
        if level > self.level:
            self.level = level

    def toString(self):
        return self.policyList[self.level]

    def setPolicy(self, policy, **kwargs):
        """
        # 吸收新的策略，更新当前策略
        :param policy:
        :param kwargs:
        :return:
        """
        try:
            level =  self.policyList.index(policy)
        except ValueError:
            logger.warning(policy + " is not a valid policy string")
            # print repr(policy).decode("unicode-escape")
            return
        if level > self.level:
            self.level = level
        if level == 8:
            self.shouldRestore = True
        elif level == 7:
            self.shouldRestart = True
        elif level == 6:
            self.shouldShutdown = True
        elif level == 5:
            self.shouldRestartProcesses.append((kwargs['name'], kwargs['path'], kwargs['pid']))
        elif level == 4:
            self.shouldOpenProcesses.append((kwargs['name'], kwargs['path']))
        elif level == 3:
            self.shouldShutdownProcesses.append((kwargs['name'], kwargs['pid']))
        elif level == 2:
            self.shouldShutdownPorts.append((kwargs['name'], kwargs['pid']))
        elif level == 1:
            self.shouldAlert = True


        #返回一个对象的描述信息
    def __str__(self):
        return self.policyList[self.level].encode("utf-8")
        #return repr(self.policyList[self.level]).decode("unicode-escape")

    def __unicode__(self):
        return self.policyList[self.level]