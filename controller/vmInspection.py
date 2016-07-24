#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

# VmInspection类
# 根据相应的vol指令来获取相应的数据



"""
@author:    chenkuan
@license:   GNU General Public License 2.0
@contact:   chen1511@foxmail.com
@version:   1.0-2016-07-21
"""

import os

class VmInspection(object):

    def getNeedData(self, name, vm, vmConf):
        """
        #根据vmConf中的配置信息得到数据存入vm中
        :param vm:
        :param vmConf:
        :return:
        """
        self.name = name
        #self.systype = vmConf.systype
        self.profile = vmConf.systype
        #self.command = "vol.py profile" + self.profile + " -f /lab/winxp.raw "
        self.command = "vol.py profile " + self.profile + " -l vmi://" + name + " "

        #如果有监控pslist
        if vmConf.processes:
            vm.processes = self.getData("pslist")

        #如果有监控ports
        if vmConf.ports:
            vm.ports = self.getData("sockets")

        #如果有监控Rootkit
        if vmConf.checkRootkit:
            vm.ssdt = self.getData("ssdt")

    def getData(self, plugin):
        return os.popen(self.command + plugin)