#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

# UserInterfaceController类
# 负责生成主界面
# 接受界面响应消息
# 对其管理的各个虚拟机调用方法生成相应线程进行处理



"""
@author:    chenkuan
@license:   GNU General Public License 2.0
@contact:   chen1511@foxmail.com
@version:   1.0-2016-07-21
"""

import sys
from PyQt4 import QtGui
from view.vmGuiAction import VmGuiAction


class UserInterfaceController(object):

    def __init__(self):
        self.vms = []
        self.vmsConfs = {}
        self.vmsStates = {}

    def getVms(self):
        """
        #从libvmi中获取virt-manager中实际添加的虚拟机
        :return: list:
        """

    def getVmsConfs(self):
        """
        #从文件中读取配置信息
        :return:
        """

    def updateVmsConfs(self):
        """
        #当界面更新配置时调用此方法
        :return:
        """

    def startMonitorVm(self):
        """
        #当界面开始监控某虚拟机时调用此
        #新开线程运行
        :return:
        """

