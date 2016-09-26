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
import re
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
        # vmConf.processes
        :return:
        """
        processes = []
        for i, line in enumerate(self.vm.processes):
            lines = line.split()
            if len(lines) < 2: continue
            #logger.debug("lines:" + str(lines))
            processes.append((lines[1], lines[2]))
            #processes[i] = (lines[1], lines[2]) #process name, process pid
            #logger.debug("processess[" + str(i) + "]:" + str(processes[i]))
        #logger.debug("processes:" + str(processes))
        for name, isneed, policy, path in self.vmConf.processes:
            #在vmState中查找该process
            isFind = False
            pspid = ""

            if re.match(r'.\exe', name, re.I):
                # 如果配置的进程名有exe的话就直接判断相等关系
                for ps, pid in processes:
                    if name == ps:
                        isFind = True
                        pspid = pid
                        break
            else:
                # 如果配置的进程名没有exe的话就两种情况都考虑
                for ps, pid in processes:
                    if name == ps or name+'.exe' == ps:
                        isFind = True
                        pspid = pid
                        break

            # if re.match(r'.\exe', name, re.I):
            #     # 如果配置的进程名有exe的话就直接判断相等关系
            #     if name in processes:
            #         isFind = True
            # else:
            #     # 如果配置的进程名没有exe的话就两种情况都考虑
            #     if name in processes or name+'.exe' in processes:
            #         isFind = True

            # 只要与设置的需要不符，就添加虚拟机策略

            if (isneed and (not isFind)) or ((not isneed) and isFind):
                logger.info("虚拟机"+self.vmConf.name+"进程"+name.encode('utf-8')+("存在"if isFind else "不存在")+"，添加策略"+policy.encode('utf-8'))
                self.vmPoli.setPolicy(policy, name = name, path = path, pid = pspid)

    def analysePorts(self):
        """
        # vmConf.ports是一个文件描述符
        :return:
        """
        ports = []
        for i, line in enumerate(self.vm.ports):
            lines = line.split()
            if len(lines) < 3: continue
            ports.append((lines[2], lines[1]))
            #ports[i] = (lines[2], lines[1]) #port, pid

        for name, isneed, policy in self.vmConf.ports:
            #在vmState中查找该端口
            isFind = False
            ptpid = ""
            for pt, pid in ports:
                if name == pt:
                    isFind = True
                    ptpid = pid
            # if name in ports:
            #     isFind = True

            # 只要与设置不符，就添加虚拟机策略
            if (isneed and (not isFind)) or ((not isneed) and isFind):
                logger.info("虚拟机" + self.vmConf.name + "端口号" + name.encode('utf-8') + ("开启" if isFind else "未开启") + "，添加策略" + policy.encode('utf-8'))
                self.vmPoli.setPolicy(policy, name = name, pid = ptpid)

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
            logger.info("第一次得到系统调用表散列：" + str(self.vm.ssdt_origin))
        else:
            # 已有ssdt的话，进行比对
            # md5 compare
            # add policy
            md5 = hashlib.md5(str(self.vm.ssdt)).hexdigest().upper()
            logger.info("当前系统调用表散列：" + md5)
            if md5 != self.vm.ssdt_origin:
                logger.warning("系统原始调用表散列：" + self.vm.ssdt_origin + "\n系统调用表发生变动，添加策略" + self.vmConf.rootkitPolicy.encode('utf-8'))
                self.vmPoli.setPolicy(self.vmConf.rootkitPolicy)
            else:
                logger.info("系统调用表未改变")

    def analyseMbr(self):
        if not self.vm.mbr_origin:
            self.vm.mbr_origin = hashlib.md5(self.vm.mbr).hexdigest().upper()
            logger.info("第一次得到磁盘MBR散列：" + str(self.vm.mbr_origin))
        else:
            md5 = hashlib.md5(self.vm.mbr).hexdigest().upper()
            logger.info("当前磁盘MBR散列：" + md5)
            if md5 != self.vm.mbr_origin:
                logger.warning("磁盘原始MBR散列：" + self.vm.mbr_origin + "\n磁盘MBR发生变动，添加策略" + self.vmConf.rootkitPolicy.encode('utf-8'))
                self.vmPoli.setPolicy(self.vmConf.rootkitPolicy)
            else:
                logger.info("磁盘MBR未改变")


    def getPolicy(self):
        return self.vmPoli