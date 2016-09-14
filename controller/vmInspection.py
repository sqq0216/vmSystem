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
import subprocess
import logging
import kvm
import unix
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
            logger.warning("虚拟机" + name + "系统类型为空")
        elif self.profile[:3] == u"Win" or self.profile[:5] == u"Vista":
            self.systype = u"Windows"
        else:
            self.systype = u"linux"

        # 如果虚拟机未在启动状态，则先启动虚拟机
        self.kvm_host = kvm.KVM(unix.Local())
        if (self.kvm_host.state(name) != kvm.RUNNING):
            logger.warning("虚拟机+" + name + "未启动，自动启动中")
            self.kvm_host.start(name)


        #self.command = "vol.py profile" + self.profile + " -f /lab/winxp.raw "
        self.command = "sudo python /home/chenkuaan/Downloads/volatility-2.4/vol.py --profile=" + self.profile + " -l vmi://" + name + " "

        # 根据虚拟机的简要类型来选择不同的插件
        try:
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
                    vm.ports = self.getData("linux_netstat")
                if vmConf.checkRootkit:
                    vm.ssdt = self.getData("linux_check_syscall")
        except PopenError, e:
            logger.warning("调用volatility时未获取到数据,调用命令:")
            # logger.warning(self.command)
            logger.warning(e)
            return False
        return True


    def getData(self, plugin):
        """
        # 根据命令和插件从终端调用volatility获取数据
        # 将返回的文件描述符拼接成列表返回
        :param plugin:
        :return:
        """
        #fileAns =  os.popen(self.command + plugin)
        fileAns = subprocess.Popen(self.command + plugin, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).stdout.read().split("\n")
        if len(fileAns) < 3:
            raise PopenError("No Ans Error:" + self.command + plugin)

        ans = []
        for line in fileAns[2:]:
            words = line.split()
            if (len(words) > 2):
                ans.append(words[1])

        return ans

        if ans[0].startswith('No suitable address space mapping found'):
            raise PopenError('No suitable address space mapping found')
        return ans

class PopenError(StandardError):
    pass