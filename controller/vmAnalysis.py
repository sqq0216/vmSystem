#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

# VmAnalysis类
# 对虚拟机进行数据处理和策略分析的类



"""
@author:    chenkuan
@license:   GNU General Public License 2.0
@contact:   chen1511@foxmail.com
@version:   1.0-2016-07-21
"""

from modules.vmPolicy import VmPolicy

class VmAnalysis(object):

    def analyseData(self, vm, vmConf):
        """
        #根据vmConf来调用相应的方法分析数据
        :param vm:
        :param vmConf:
        :return:
        """
        self.vm = vm
        self.vmConf = vmConf

        self.vmPoli = VmPolicy()

        if vmConf.processes:
            self.analyseProcesses()

        if vmConf.ports:
            self.analysePorts()

        if vmConf.checkRootkit:
            self.analyseSsdt()

    def analyseProcesses(self):
        """
        # vmConf.processes是一个dict
        # str:int, 进程名：处理等级
        :return:
        """
        for process, level in self.vmConf.processes.items():
            #在vmState中查找该process，如果没找到该进程
            if self.vm.processes.find(process) < 0:
                # 设置策略响应等级
                self.vmPoli.setLevel(level)
                # 不管什么等级都将需重启进程添加进去
                self.vmPoli.shouldRestartProcesses.append(process)

    def analysePorts(self):
        """
        # vmConf.ports是一个dict
        # str:int, 进程名：处理等级
        :return:
        """
        for port, level in self.vmConf.ports.items():
            #在vmState中查看该端口状态，如果该端口被关闭
            if self.vm.ports.find(port) < 0:
                # 设置策略响应等级
                self.vmPoli.setLevel(level)

    def analyseSsdt(self):
        """

        :return:
        """

    def getPolicy(self):
        return self.vmPoli