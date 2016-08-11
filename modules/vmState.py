#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

# VmState类
# 负责保存当前某虚拟机的运行数据


"""
@author:    chenkuan
@license:   GNU General Public License 2.0
@contact:   chen1511@foxmail.com
@version:   1.0-2016-07-21
"""

class VmState(object):

    def __init__(self, name):

        self.__name = name

        self.__processes = [] # 虚拟机当前的进程列表
        self.__ports = []
        self.__ssdt = []

        self.machineStatus = False  #开关机状态

    @property
    def processes(self):
        return self.__processes
    @processes.setter
    def processes(self, processes):
        self.__processes = processes

    @property
    def ports(self):
        return self.__ports
    @ports.setter
    def ports(self, ports):
        self.__ports = ports

    @property
    def ssdt(self):
        return self.__ssdt
    @ssdt.setter
    def ssdt(self, ssdt):
        self.__ssdt = ssdt