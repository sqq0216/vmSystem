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
from PyQt4 import QtGui
from view.vmGuiAction import VmGuiAction


class UserInterfaceController(object):

    def __init__(self):
        self.vms = []
        self.vmsConfs = {}
        self.vmsStates = {}

    def getVms(self):
        """
        #从libvmi中获取virt-manager中实际添加的虚拟机列表
        :return: list:
        """
        self.vms = []
        return self.vms

    def getVmsConfs(self, vmname):
        """
        #从文件中读取某个虚拟机配置信息
        :return: list:
        """
        self.vmsConfs[vmname].updateConf()
        self.vmsConfs = []
        for vmname in self.vms:
            #此处添加异常
            f = open(vmname+".json", "r")
            self.vmsConfs.append(json.load(f))

        return self.vmsConfs

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

    def startMonitorVm(self):
        """
        #当界面开始监控某虚拟机时调用此
        #新开线程运行
        :return:
        """

