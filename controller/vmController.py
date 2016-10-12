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

import time
import logging
logger = logging.getLogger()

import threadCmd as ThreadCmd
from modules.vmState import VmState
from modules.vmConf import VmConf
from modules.vmPolicy import VmPolicy
from modules.vmHistory import VmHistory

from vmInspection import VmInspection
from vmAnalysis import VmAnalysis
from vmExecution import VmExecute

class VmController(object):

    def __init__(self, name, vmConf):

        self.name = name

        self.vm = VmState(name)
        self.vmConf = vmConf

        self.vmPoli = VmPolicy()
        self.vmHist = VmHistory()

        self.vmInsp = VmInspection()
        self.vmAnal = VmAnalysis()
        self.vmExec = VmExecute()

    def startMonitor(self):
        """
        #死循环监视自身
        :return:
        """
        logger.info("开始监控虚拟机" + self.name)
        breakLock = ThreadCmd.getBreakLock()
        self.vmHist.clearHistory()

        while True:
            breakLock.acquire()
            ebList = ThreadCmd.getEBList()
            if not ebList[self.name]:
                # 没有通知关闭线程，立刻释放锁
                breakLock.release()
                # 根据配置获取数据填入vm
                if not self.vmInsp.getNeedData(self.name, self.vm, self.vmConf):
                    continue
                logger.debug(str(self.vm))
            else:
                # 如果通知关闭线程，更改通知量，释放锁后跳出循环
                ebList[self.name] = False
                breakLock.release()
                break

            breakLock.acquire()
            ebList = ThreadCmd.getEBList()
            if not ebList[self.name]:
                # 没有通知关闭线程，立刻释放锁
                breakLock.release()
                # 分析数据
                self.vmAnal.analyseData(self.vm, self.vmConf)
            else:
                # 如果通知关闭线程，释放锁后跳出循环
                ebList[self.name] = False
                breakLock.release()
                break

            breakLock.acquire()
            ebList = ThreadCmd.getEBList()
            if not ebList[self.name]:
                # 没有通知关闭线程，立刻释放锁
                breakLock.release()
                # 生成处理策略
                self.policy = self.vmAnal.getPolicy()
            else:
                # 如果通知关闭线程，释放锁后跳出循环
                ebList[self.name] = False
                breakLock.release()
                break

            breakLock.acquire()
            ebList = ThreadCmd.getEBList()
            if not ebList[self.name]:
                # 没有通知关闭线程，立刻释放锁
                breakLock.release()
                # 根据历史操作和策略对vm执行相应的操作，并记录在历史操作中
                self.vmExec.execute(self.name, self.vmConf.ip, self.vm, self.vmHist, self.policy)
            else:
                # 如果通知关闭线程，释放锁后跳出循环
                ebList[self.name] = False
                breakLock.release()
                break

        logger.info("虚拟机" + self.name + "监控完毕")
        return

        while True:
            #根据配置获取数据填入vm
            self.vmInsp.getNeedData(self.name, self.vm, self.vmConf)
            #分析数据
            self.vmAnal.analyseData(self.vm, self.vmConf)
            #生成处理策略
            self.policy = self.vmAnal.getPolicy()
            #根据历史操作和策略对vm执行相应的操作，并记录在历史操作中
            self.vmExec.execute(self.name, self.vmConf.ip, self.vm, self.vmHist, self.policy)

