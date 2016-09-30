#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

# UserInterfaceController类
# 接受界面响应消息
# 对其管理的各个虚拟机调用方法生成相应线程进行处理



"""
@author:    chenkuan
@license:   GNU General Public License 2.0
@contact:   chen1511@foxmail.com
@version:   1.0-2016-07-21
"""

import sys
import os
import subprocess
import json
import threading
import logging
logger = logging.getLogger()

import threadCmd as ThreadCmd
#from PyQt4 import QtGui
#from view.vmGuiAction import VmGuiAction
from vmController import VmController


from modules.vmConf import VmConf
from modules.vmState import VmState


class UserInterfaceController(object):

    def __init__(self):
        #self.vms = []
        self.getVms()
        self.vmsConfs = {}
        self.vmsStates = {}
        for vm in self.vms:
            self.vmsConfs[vm] = VmConf(vm)
            #.vmsStates[vm] = VmState(vm)

        # 创建local对象，用来管理各个虚拟机
        self.localVm = threading.local()
        # 保存各线程的列表
        self.threadsVm = {}
        # 保存各线程名称的列表
        #self.threadsName = []

        # 获得读写锁
        breakLock = ThreadCmd.getBreakLock()
        # 初始化命令表
        breakLock.acquire()
        ebList = ThreadCmd.getEBList()
        for vm in self.vms:
            ebList[vm] = False
        breakLock.release()

    def getVms(self):
        """
        #从libvmi中获取virt-manager中实际添加的虚拟机列表
        :return: list:
        """
        import kvm,unix
        # self.vms = kvm.KVM(unix.Local()).vms
        # self.vms = ["win1", "win2", "win3", "WinXP"]
        #self.vms = []
        #self.vms = kvm.Hypervisor(unix.Local()).list_domains()
        self.vms = subprocess.Popen("sudo virsh list --all --name", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).stdout.read().split()
        logger.debug("self.vms:" + str(self.vms))
        if not self.vms:
            self.vms = ["win1", "win2", "win3"]
        return self.vms

    def getVmtypes(self):
        """
        # 从volatility中获取可用的虚拟机类型
        :return:
        """
        # self.vmtypes = ["CentOS65x64", "WinXPSP3x86", "Win7SP1x64"]
        # return self.vmtypes

        logger.debug("从volatility中获取可用的虚拟机类型")
        command = "python /usr/bin/vol.py --info"
        # info = os.popen(command)
        info = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).stdout.read().split("\n")
        profiles = []

        begin = False
        for line in info:
            # logger.debug("this info line:" + line)
            if line == "Profiles":
                begin = True
                #logger.debug("this line equals Profiles")
            elif begin:
                #logger.debug("begin: " + line)
                if line == "":
                    break
                elif line == "--------":
                    continue
                else:
                    # logger.debug("this lineline:" + line)
                    #logger.debug("line.split():" + line.split())
                    profiles.append(line.split()[0])
                    #logger.debug("this profiles:" + profiles)
        # logger.debug(profiles)
        return profiles



    def getVmsConfs(self, vmname):
        """
        #从文件中读取某个虚拟机配置信息
        #然后返回其所有属性值
        :return: tuple:
        """
        self.vmsConfs[vmname].getConfFromFile()
        return self.vmsConfs[vmname].getConf()

    def setVmsConfs(self, vmname, **kwargs):
        """
        #当界面更新配置时调用此方法
        #利用关键字参数传入所有configure属性
        :return:
        """
        # 将配置信息更新
        self.vmsConfs[vmname].setConf(kwargs)
        #将配置保存到文件
        self.vmsConfs[vmname].setConfToFile()

    def startMonitorVm(self, vmname):
        """
        #当界面开始监控某虚拟机时调用此方法
        #新开线程运行
        :return:
        """
        if vmname not in self.threadsVm.keys() or (vmname in self.threadsVm.keys() and not self.threadsVm[vmname].isAlive()):
            # 如果没有此线程或者有此线程但线程已死亡
            self.threadsVm[vmname] = threading.Thread(target=self.generateSingleController, args=(vmname,), name="Thread-"+str(vmname))
            # 暂时将子线程设置为随主线程关闭而关闭，之后可更改为主线程发关闭信号给子线程
            self.threadsVm[vmname].setDaemon(True)
            self.threadsVm[vmname].start()
        else:
            # 如果此线程已有并存活着
            logger.warning("虚拟机" + str(vmname) + "已经处于监控状态")
        logger.debug("已有虚拟机监控列表：名称:线程:" + str([vm for vm in self.threadsVm.keys() if self.threadsVm[vm].isAlive()]))

    def generateSingleController(self, vmname):
        """
        # 此方法用于生成单个控制器，将一系列参数传入,然后调用类方法开始监控
        :param vmname:
        :return:
        """
        # 各个controller存在于各个线程内，互不干扰
        self.localVm.name = vmname
        self.localVm.controller = VmController(vmname, self.vmsConfs[vmname])
        #启动该线程对应的控制器
        self.localVm.controller.startMonitor()

    def stopMonitorVm(self, vmname):
        """
        # 当界面发出停止该虚拟机指令时调用
        :param vmname:
        :return:
        """
        # 如果此线程存活中，发出命令关闭他
        try:
            if self.threadsVm[vmname].isAlive():
                # 更改全局执行与中断命令判断表，迫使子线程结束
                breakLock = ThreadCmd.getBreakLock()
                breakLock.acquire()
                ebList = ThreadCmd.getEBList()
                ebList[vmname] = True
                breakLock.release()
                logger.info("等待对虚拟机" + vmname + "的监控结束")
            else:
                logger.warning("对虚拟机" + vmname + "的监控未在进行")
            logger.debug("线程" + str(self.threadsVm[vmname]) + "状态：" + ("存活" if self.threadsVm[vmname].isAlive() else "死亡"))
        except KeyError:
            logger.warning("对虚拟机" + vmname + "的监控未在进行")


