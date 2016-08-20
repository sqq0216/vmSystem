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
import logging
logger = logging.getLogger()

class VmInspection(object):

    def getNeedData(self, name, vm, vmConf):
        """
        #根据vmConf中的配置信息得到数据存入vm中
        :param vm:
        :param vmConf:
        :return:
        """
        self.name = name
        # 虚拟机的完整类型
        self.profile = vmConf.systype
        # 虚拟机的简要类型
        self.systype = u""
        if not self.profile:
            logger.warning(u"虚拟机" + name + u"系统类型为空")
        elif self.profile[:3] == u"Win" or self.profile[:5] == u"Vista":
            self.systype = u"Windows"
        else:
            self.systype = u"linux"

        #self.command = "vol.py profile" + self.profile + " -f /lab/winxp.raw "
        self.command = "vol.py profile " + self.profile + " -l vmi://" + name + " "

        # 根据虚拟机的简要类型来选择不同的插件
        if self.systype == u"Windows":
            if vmConf.processes:
                vm.processes = self.getData("pslist")
            if vmConf.ports:
                vm.ports = self.getData("sockets")
            if vmConf.checkRootkit:
                vm.ssdt = self.getData("ssdt")
        elif self.systype == u"linux":
            if vmConf.processes:
                vm.processes = self.getData("linux_pslist")
            if vmConf.ports:
                vm.ports = self.getData("netstat")
            if vmConf.checkRootkit:
                vm.ssdt = self.getData("check_sys_call")

    def getData(self, plugin):
        """
        # 根据命令和插件从终端调用volatility获取数据
        # 将返回的文件描述符拼接成列表返回
        :param plugin:
        :return:
        """
        fileAns =  os.popen(self.command + plugin)
        ans = []
        for line in fileAns:
            ans.append(line)
        return ans