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
        self.__platform = "" # 虚拟机系统的类型

        self.__processes = [] # 虚拟机当前的进程列表
        self.__ports = []
        self.__serials = []
        self.__ssdt = []
        self.__ssdt_origin = []
        self.__mbr = []
        self.__mbr_origin = []

        self.machineStatus = False  #开关机状态

    @property
    def platform(self):
        return self.__platform
    @platform.setter
    def platform(self, platform):
        self.__platform = platform

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
    def serials(self):
        return self.__serials
    @serials.setter
    def serials(self, serials):
        self.__serials = serials

    @property
    def ssdt(self):
        return self.__ssdt
    @ssdt.setter
    def ssdt(self, ssdt):
        self.__ssdt = ssdt

    @property
    def mbr(self):
        return self.__mbr
    @mbr.setter
    def mbr(self, mbr):
        self.__mbr = mbr

    @property
    def ssdt_origin(self):
        return self.__ssdt_origin
    @ssdt_origin.setter
    def ssdt_origin(self, ssdt_origin):
        self.__ssdt_origin = ssdt_origin

    @property
    def mbr_origin(self):
        return self.__mbr_origin
    @mbr_origin.setter
    def mbr_origin(self, mbr_origin):
        self.__mbr_origin = mbr_origin

    def __str__(self):
        name = "\nname:" + self.__name
        process = "process:[\n" + "\n".join(self.__processes) + "]"
        port = "port:[\n" + "\n".join(self.__ports) + "]"
        ssdt = "ssdt:[\n" + "\n".join(self.__ssdt) + "]"
        return "\n".join([name, process, port, ssdt])