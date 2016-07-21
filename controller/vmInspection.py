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

    def getNeedData(self, vm, vmConf):
        """
        #根据vmConf中的配置信息得到数据存入vm中
        :param vm:
        :param vmConf:
        :return:
        """
        self.name = vmConf.getName()
        self.systype = vmConf.getSystype()
        self.profile = self.systype
        self.command = "vol.py profile" + self.profile + " -f /lab/winxp.raw "

        vm.processes = self.getData("pslist")
        vm.ports = self.getData("ports")
        vm.ssdt = self.getData("ssdt")

    def getData(self, plugin):
        return os.popen(self.command + plugin)