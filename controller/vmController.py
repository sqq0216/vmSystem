#!/usr/local/bin/python2.7

# VmController类
# 对单个的虚拟机进行控制
# 获取进程、端口等
# 判断rootkit
# 获取处理策略并生成执行策略
# 执行策略



"""
@author:    chenkuan
@license:   GNU General Public License 2.0
@contact:   chen1511@foxmail.com
@version:   1.0-2016-07-21
"""

from modules.vmState import VmState
from modules.vmConf import VmConf

class VmController(object):

    def __init__(self):

        self.name = ""
        self.vm = VmState()
        self.vmConf = VmConf()

    def getProcesses(self):
        pass

    def getPorts(self):
        pass

    def getNeedData(self):
        """
        #根据配置选择性地读取相应策略
        :return:
        """
        pass

    def getPolicy(self):
        """
        #根据数据信息生成策略
        :return:
        """
        pass

    def executePolicy(self):
        """
        #根据生成的策略执行
        :return:
        """
        pass

