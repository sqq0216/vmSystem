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

import logging
import kvm
import unix
import socket
logger = logging.getLogger()

class VmExecute(object):

    def execute(self, name, ip, vm, history, policy):
        """
        # 根据现有的操作历史和策略进行相应的执行
        :param vm:
        :param policy:
        :param history:
        :return:
        """
        self.name = name
        self.vm = vm
        self.ip = ip
        self.history = history
        self.policy = policy

        self.kvm_host = kvm.KVM(unix.Local())

        # 先判断策略与历史记录的严重等级，决定清除某些记录或更新策略
        if policy.shouldRestoreVm:
            if history.vmRestoreTimes:
                logger.info("已经恢复虚拟机" + self.name + str(history.vmRestoreTimes) + "次，继续恢复虚拟机")
                history.vmRestoreTimes += 1
            else:
                logger.info("恢复虚拟机" + self.name)
                history.vmRestoreTimes = 1
        elif policy.shouldRestartVm:
            if history.vmRestoreTimes:
                logger.info("已经恢复虚拟机" + self.name + str(history.vmRestoreTimes) + "次，继续恢复虚拟机")
                # logger.info(u"重启虚拟机" + self.name)
                history.vmRestoreTimes += 1
            elif history.vmRestartTimes >= 3:
                logger.info("已经重启虚拟机" + self.name + str(history.vmRestartTimes) + "次，选择恢复虚拟机")
                policy.setPolicy(u"恢复虚拟机")
                history.vmRestoreTimes = 1
            elif history.vmRestartTimes > 0:
                logger.info("已经重启虚拟机" + self.name + str(history.vmRestartTimes) + "次，继续重启虚拟机")
                history.vmRestartTimes += 1
            else:
                logger.info("重启虚拟机" + self.name)
                history.vmRestartTimes = 1
        elif policy.shouldShutdownVm:
            logger.info("关闭虚拟机" + self.name)

        if policy.shouldRestartProcesses:
            if history.vmRestoreTimes:
                logger.info("已经恢复虚拟机" + self.name + str(history.vmRestoreTimes) + "次，继续恢复虚拟机")
                history.vmRestoreTimes += 1
            elif history.vmRestartTimes >= 3:
                logger.info("已经重启虚拟机" + self.name + str(history.vmRestartTimes) + "次，选择恢复虚拟机")
                policy.setPolicy(u"恢复虚拟机")
                history.vmRestoreTimes = 1
            elif history.vmRestartTimes > 0:
                logger.info("已经重启虚拟机" + self.name + str(history.vmRestartTimes) + "次，继续重启虚拟机")
                history.vmRestartTimes += 1
            else:
                shouldRestartVm = False
                pslist = []
                for ps, path in policy.shouldRestartProcesses:
                    if ps not in history.processesRestartTimes:
                        history.processRestartTimes[ps] = 1
                    elif history.processesRestartTimes[ps] >= 3:
                        shouldRestartVm = True
                        pslist.append(ps)
                    else:
                        history.processesRestartTimes[ps] += 1
                if shouldRestartVm:
                    policy.setPolicy(u"重启虚拟机")
                    logger.info("进程" + str(pslist) + "已经重启达到3次，选择重启虚拟机")
                else:
                    logger.info("重启进程" + str(policy.shouldRestartProcesses))

        if policy.shouldOpenProcesses:
            logger.info("打开进程" + str(policy.shouldOpenProcesses))

        if policy.shouldShutdownProcesses:
            logger.info(("关闭进程" + str(policy.shouldShutdownProcesses)))

        if policy.shouldShutdownPorts:
            logger.info("关闭端口" + str(policy.shouldShutdownPorts))

        if policy.level == 0:
            history.clearHistory()

        self.executePolicy()

    def executePolicy(self):
        if self.policy.shouldRestoreVm:
            self.restoreVm()
        elif self.policy.shouldRestartVm:
            self.restartVm()
        elif self.policy.shouldShutdownVm:
            self.shutdownVm()

        if self.policy.shouldRestartProcesses:
            for ps, path in self.policy.shouldRestartProcesses:
                self.restartProcess(ps, path)

        if self.policy.shouldOpenProcesses:
            for ps, path in self.policy.shouldOpenProcesses:
                self.openProcess(ps, path)

        if self.policy.shouldShutdownProcesses:
            for ps in self.policy.shouldRestartProcesses:
                self.shutdownProcess(ps)

        if self.policy.shouldShutdownPorts:
            for pt in self.policy.shouldShutdownPorts:
                self.shutdownPort(pt)


    def shutdownPort(self, port):
        """
        # 关闭端口
        :param port:
        :return:
        """

    def shutdownProcess(self, process):
        """
        # 关闭进程
        :param process:
        :return:
        """

    def openProcess(self, process, path):
        """
        # 打开进程
        :param process:
        :param path:
        :return:
        """


    def restartProcess(self, process, path):
        """
        # 重启进程process
        :param process:
        :return:
        """

    def shutdownVm(self):
        """
        # 关闭虚拟机self.name
        :return:
        """


    def restartVm(self):
        """
        # 重启虚拟机self.name
        :return:
        """
        self.kvm_host.reboot(self.name)

    def restoreVm(self):
        """
        # 恢复虚拟机self.name
        :return:
        """
        self.kvm_host.restore(self.name)