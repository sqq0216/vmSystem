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
import time
import xml.dom.minidom
logger = logging.getLogger()

class VmInspection(object):

    def getNeedData(self, name, vm, vmConf):
        """
        #根据vmConf中的配置信息得到数据存入vm中
        :param vm:
        :param vmConf:
        :return:
        """
        logger.info("从虚拟机" + name + "获取数据中...")

        self.name = name
        # 虚拟机的完整类型
        self.profile = vmConf.systype
        # 虚拟机的简要类型
        self.systype = u""
        if not self.profile:
            logger.warning("虚拟机" + name + "系统类型为空")
            return False
        elif self.profile[:3] == u"Win" or self.profile[:5] == u"Vista":
            self.systype = u"Windows"
        else:
            self.systype = u"linux"
        vm.platform = self.systype

        # 如果虚拟机未在启动状态，则先启动虚拟机
        vm.state = subprocess.Popen("sudo virsh domstate " + name, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).stdout.read()
        if (vm.state[:7] != "running"):
            logger.debug("state:" + vm.state)
            logger.warning("虚拟机" + name + "未启动，自动启动中")
            subprocess.Popen("sudo virsh start " + name)
            time.sleep(60)


        # self.kvm_host = kvm.KVM(unix.Local())
        # if (self.kvm_host.state(name) != kvm.RUNNING):
        #     logger.warning("虚拟机" + name + "未启动，自动启动中")
        #     self.kvm_host.start(name)
        #     time.sleep(60)

        volpath = subprocess.Popen("which vol.py", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).stdout.read()
        if len(volpath) > 15 and volpath[:15] == "/usr/bin/which:":
            logger.warning("找不到volatility安装位置")

        volpath = volpath.split()[0]
        #self.command = "vol.py profile" + self.profile + " -f /lab/winxp.raw "
        self.command = "sudo python " + volpath + " --profile=" + self.profile + " -l vmi://" + name + " "

        # 根据虚拟机的简要类型来选择不同的插件
        try:
            if self.systype == u"Windows":
                if vmConf.processes:
                    vm.processes = self.getData("pslist")
                if vmConf.ports:
                    vm.ports = self.getData("sockscan")
                    vm.serials = self.getData("devicetree") #运行虚拟机需要约25分钟
                if vmConf.checkRootkit:
                    vm.ssdt = self.getData("ssdt")
                    vm.mbr = self.getMbr()
            elif self.systype == u"linux":
                if vmConf.processes:
                    vm.processes = self.getData("linux_pslist")
                if vmConf.ports:
                    vm.ports = self.getData("linux_netstat")
                    vm.serials = self.getData("linux_check_tty")    #只有tty设备，无ttyS设备，即无串口信息
                if vmConf.checkRootkit:
                    vm.ssdt = self.getData("linux_check_syscall")   #xu yao hen jiu
                    vm.mbr = self.getMbr()
        except PopenError, e:
            logger.warning("调用volatility时未获取到数据 " + str(e))
            # logger.warning(self.command)
            #logger.warning(e)
            return False
        except ProfileError, e:
            logger.warning("调用volatility时使用profile出错 " + str(e))
            #logger.warning()
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
        #logger.debug("fileAns:"+str(fileAns))
        if len(fileAns) < 3:
            raise PopenError("No Ans Error:" + self.command + plugin)
        if fileAns[2] == "No suitable address space mapping found" or fileAns[2] == "Tried to open image as:":
            raise ProfileError("Profile Error:" + self.command + plugin)

        ans = []
        for line in fileAns:
            ans.append(line)

        return ans

    def getMbr(self):
        xmlAns = subprocess.Popen("sudo virsh dumpxml " + self.name, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).stdout.read()
        diskpath = xml.dom.minidom.parseString(xmlAns).documentElement.getElementsByTagName("devices")[0].getElementsByTagName("disk")[0].getElementsByTagName("source")[0].getAttribute("file")
        logger.debug("diskpath:" + diskpath.encode('utf-8'))
        # logger.debug("xmlAns:\n" + xmlAns)
        ans = ""
        try:
            with open(diskpath, "rb") as fd:
                ans = fd.read(512)
        except IOError, e:
            logger.warning("无法读取虚拟机磁盘文件" + diskpath.encode('utf-8') + ",错误原因:%s" %e)
        return ans
        '''
        for i, c in enumerate(ans):
            print "%02X" %ord(c),
            if (i+1) % 16 == 0:
                print "\n",
            elif (i+1) % 8 == 0:
                print "    ",
            elif (i+1) % 4 == 0:
                print "  ",
            elif (i+1) % 2 == 0:
                print " ",
        '''

class PopenError(StandardError):
    pass

class ProfileError(StandardError):
    pass
