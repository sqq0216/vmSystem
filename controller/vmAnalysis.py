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
        # vmConf.processes是一个文件描述符
        :return:
        """
        for name, isneed, policy, path in self.vmConf.processes:
            #在vmState中查找该process
            isFind = False
            for line in self.vm.processes:
                if line.find(name) >= 0:
                    isFind = True
                    break
            # 只要与设置的需要不符，就添加虚拟机策略
            if (isneed and (not isFind)) or ((not isneed) and isFind):
                self.vmPoli.setPolicy(policy, name = name, path = path)

    def analysePorts(self):
        """
        # vmConf.ports是一个文件描述符
        :return:
        """
        for name, isneed, policy in self.vmConf.ports:
            #在vmState中查找该端口
            isFind = False
            for line in self.vm.ports:
                if line.find(name) >= 0:
                    isFind = True
                    break
            # 只要与设置不符，就添加虚拟机策略
            if (isneed and (not isFind)) or ((not isneed) and isFind):
                self.vmPoli.setPolicy(policy, name = name)

    def analyseSsdt(self):
        """
        # vmConf.ssdt是一个文件描述符
        # 如果ssdt发生变化就添加策略
        :return:
        """


    def getPolicy(self):
        return self.vmPoli