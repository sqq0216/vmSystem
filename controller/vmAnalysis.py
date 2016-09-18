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

import logging
logger = logging.getLogger()
import os
import hashlib
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
            self.analyseMbr()

    def analyseProcesses(self):
        """
        # vmConf.processes是一个文件描述符
        :return:
        """
        processes = self.vm.processes
        for i, line in enumerate(processes):
            lines = line.split()
            if len(lines) < 2: continue
            logger.debug("i="+str(i)+",line="+str(line))
            logger.debug("i="+str(i)+",line.split()="+str(line.split()))
            logger.debug("i="+str(i)+",line.split()[1]="+str(line.split()[1]))
            processes[i] = lines[1]
        for name, isneed, policy, path in self.vmConf.processes:
            #在vmState中查找该process
            isFind = False
            if name in processes:
                isFind = True
            # 只要与设置的需要不符，就添加虚拟机策略
            if (isneed and (not isFind)) or ((not isneed) and isFind):
                #logger.info("虚拟机"+self.vm.)
                self.vmPoli.setPolicy(policy, name = name, path = path)

    def analysePorts(self):
        """
        # vmConf.ports是一个文件描述符
        :return:
        """
        ports = self.vm.ports
        for i, line in enumerate(ports):
            lines = line.split()
            if len(lines) < 2: continue
            ports[i] = lines[1]
        for name, isneed, policy in self.vmConf.ports:
            #在vmState中查找该端口
            isFind = False
            if name in ports:
                isFind = True
            # 只要与设置不符，就添加虚拟机策略
            if (isneed and (not isFind)) or ((not isneed) and isFind):
                self.vmPoli.setPolicy(policy, name = name)

    def analyseSsdt(self):
        """
        # vmConf.ssdt是一个文件描述符
        # 如果ssdt发生变化就添加策略
        :return:
        """
        if not self.vm.ssdt_origin:
            # 如果是第一次得到ssdt，则进行备份
            # md5 backup
            self.vm.ssdt_origin = hashlib.md5(str(self.vm.ssdt)).hexdigest().upper()
        else:
            # 已有ssdt的话，进行比对
            # md5 compare
            # add policy
            md5 = hashlib.md5(str(self.vm.ssdt)).hexdigest().upper()
            if md5 != self.vm.ssdt_origin:
                self.vmPoli.setPolicy(self.vmConf.rootkitPolicy)

    def analyseMbr(self):
        pass


    def getPolicy(self):
        return self.vmPoli