#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

# VmController类
# 对单个的虚拟机进行控制
# 获取进程、端口等
# 判断rootkit
# 获取处理策略并生成执行策略
# 执行策略



"""
@author:    chenkuan
@license:   GNU General Public License 2.0
@contact:   chen1511@foxmail.com
@version:   1.0-2016-07-21
"""

from modules.vmState import VmState
from modules.vmConf import VmConf
from modules.vmPolicy import VmPolicy

from vmInspection import VmInspection
from vmAnalysis import VmAnalysis
from vmExecution import VmExecute

class VmController(object):

    def __init__(self, name, vmConf, vmState):

        self.name = name

        self.vm = vmState
        self.vmConf = vmConf
        self.vmPoli = VmPolicy()

        self.vmInsp = VmInspection()
        self.vmAnal = VmAnalysis()
        self.vmExec = VmExecute()

    def startMonitor(self):
        """
        #死循环监视自身
        :return:
        """
        while True:
            #根据配置获取数据填入vm
            self.vmInsp.getNeedData(self.vm, self.vmConf)
            #分析数据
            self.vmAnal.analyseData(self.vm, self.vmConf)
            #生成处理策略
            self.policy = self.vmAnal.getPolicy()
            #对vm执行相应的策略
            self.vmExec.execute(self.vm, self.policy)
