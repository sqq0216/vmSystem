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
import json
import threading
#from PyQt4 import QtGui
#from view.vmGuiAction import VmGuiAction
from vmController import VmController


class UserInterfaceController(object):

    def __init__(self):
        self.vms = []
        self.vmsConfs = {}
        self.vmsStates = {}

        # 创建local对象，用来管理各个虚拟机
        self.localVm = threading.local()
        # 保存各线程的列表
        self.threadsVm = []

    def getVms(self):
        """
        #从libvmi中获取virt-manager中实际添加的虚拟机列表
        :return: list:
        """
        self.vms = ["win1", "win2", "win3"]
        #self.vms = []
        return self.vms

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
        #将配置信息更新
        self.vmsConfs[vmname].setConf(kwargs)
        #将配置保存到文件
        self.vmsConfs[vmname].setConfToFile()

    def startMonitorVm(self, vmname):
        """
        #当界面开始监控某虚拟机时调用此方法
        #新开线程运行
        :return:
        """
        self.threadsVm.append(threading.Thread(target=self.generateSingleController, args=vmname, name="Thread-"+str(vmname)))
        self.threadsVm[-1].start()

    def generateSingleController(self, vmname):
        """
        # 此方法用于生成单个控制器，将一系列参数传入,然后调用类方法开始监控
        :param vmname:
        :return:
        """
        #各个controller存在于各个线程内，互不干扰
        self.localVm.controller = VmController(vmname, self.vmsConfs[vmname], self.vmsStates[vmname])
        #启动该线程对应的控制器
        self.localVm.controller.startMonitor()



