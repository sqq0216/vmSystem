#!/usr/local/bin/python2.7

# VmState类
# 负责保存当前某虚拟机的运行数据


"""
@author:    chenkuan
@license:   GNU General Public License 2.0
@contact:   chen1511@foxmail.com
@version:   1.0-2016-07-21
"""

class VmState(object):

    def __init__(self):

        self.name = ""
        self.systype = ""

        self.processes = []
        self.ports = []
        self.ssdt = []

        self.machineStatus = False  #开关机状态

