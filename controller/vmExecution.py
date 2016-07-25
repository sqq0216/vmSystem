#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

# VmExecute类
# 对虚拟机进行策略操作的类



"""
@author:    chenkuan
@license:   GNU General Public License 2.0
@contact:   chen1511@foxmail.com
@version:   1.0-2016-07-21
"""



class VmExecute(object):

    def execute(self, name, vm, history, policy):
        """
        # 根据现有的操作历史和策略进行相应的执行
        :param vm:
        :param policy:
        :param history:
        :return:
        """
        self.name = name
        self.vm = vm
        self.history = history
        self.policy = policy

        # 如果恢复或重启过了或策略要求恢复，那当前只能恢复
        if history.vmRestoreTimes > 0 or history.vmRestartTimes > 0 or policy.level == 3:
            self.restoreVm()
        elif policy.level == 2:
            self.restartVm()


    def restartProcess(self, process):
        """
        # 重启进程process
        :param process:
        :return:
        """

    def restartVm(self):
        """
        # 重启虚拟机self.name
        :return:
        """
    def restoreVm(self):
        """
        # 恢复虚拟机self.name
        :return:
        """