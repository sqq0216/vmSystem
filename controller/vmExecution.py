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
import subprocess
import kvm
import unix
import socket
import time
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
        self.backport = 15001

        self.history = history
        self.policy = policy

        # self.kvm_host = kvm.KVM(unix.Local())

        # 先判断策略与历史记录的严重等级，决定清除某些记录或更新策略
        if policy.shouldRestoreVm:
            logger.info("综合所有策略，选择恢复虚拟机" + self.name)
            if history.vmRestoreTimes:
                logger.info("已经恢复虚拟机" + self.name + str(history.vmRestoreTimes) + "次，继续恢复虚拟机")
                history.vmRestoreTimes += 1
            else:
                logger.info("恢复虚拟机" + self.name)
                history.vmRestoreTimes = 1
        elif policy.shouldRestartVm:
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
                logger.info("综合所有策略，选择重启虚拟机" + self.name)
                logger.info("重启虚拟机" + self.name)
                history.vmRestartTimes = 1
        elif policy.shouldShutdownVm:
            logger.info("综合所有策略，选择关闭虚拟机" + self.name)
            logger.info("关闭虚拟机" + self.name)

        else:

            if policy.shouldOpenProcesses:
                logger.info("打开进程" + str(policy.shouldOpenProcesses))

            if policy.shouldShutdownProcesses:
                logger.info(("关闭进程" + str(policy.shouldShutdownProcesses)))

            if policy.shouldShutdownPorts:
                logger.info("关闭端口" + str(policy.shouldShutdownPorts))

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
                    for ps, path, pid in policy.shouldRestartProcesses:
                        if ps not in history.processesRestartTimes:
                            history.processesRestartTimes[ps] = 1
                        elif history.processesRestartTimes[ps] >= 3:
                            shouldRestartVm = True
                            pslist.append(ps)
                        else:
                            history.processesRestartTimes[ps] += 1
                    if shouldRestartVm:
                        policy.setPolicy(u"重启虚拟机")
                        logger.info("进程" + str(pslist) + "已经重启达到3次，选择重启虚拟机")
                        history.vmRestartTimes = 1
                    else:
                        logger.info("重启进程" + str(policy.shouldRestartProcesses))

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
        else:
            if self.policy.shouldRestartProcesses:
                for ps, path, pid in self.policy.shouldRestartProcesses:
                    self.restartProcess(ps, path, pid)

            if self.policy.shouldOpenProcesses:
                for ps, path in self.policy.shouldOpenProcesses:
                    self.openProcess(ps, path)

            if self.policy.shouldShutdownProcesses:
                for ps, pid in self.policy.shouldShutdownProcesses:
                    self.shutdownProcess(ps, pid)

            if self.policy.shouldShutdownPorts:
                for pt in self.policy.shouldShutdownPorts:
                    self.shutdownPort(pt)


    def shutdownPort(self, port):
        """
        # 关闭端口
        :param port:
        :return:
        """

    def shutdownProcess(self, process, pid):
        """
        # 关闭进程
        :param process:
        :return:
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((self.ip, self.backport))
            if self.vm.platform == u"Windows":
                sock.sendall("tskill " + pid + "\0")
                logger.info("虚拟机" + self.name + "关闭进程" + process.encode('utf-8') + "，使用命令：tskill " + pid)
            else:
                sock.sendall("kill " + pid + '\0')
                logger.info("虚拟机" + self.name + "关闭进程" + process.encode('utf-8') + "，使用命令：kill " + pid)
        except socket.error, e:
            logger.warning("虚拟机连接异常，错误：%s" %e)
        finally:
            sock.close()

    def openProcess(self, process, path):
        """
        # 打开进程
        :param process:
        :param path:
        :return:
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((self.ip, self.backport))
            #sock.sendall("start " + path)
            sock.sendall(path + '\0')
            logger.info("虚拟机" + self.name + "打开进程" + process.encode('utf-8') + "，使用命令：" + path.encode('utf-8'))
        except socket.error, e:
            logger.warning("虚拟机连接异常，错误：%s" %e)
        finally:
            sock.close()


    def restartProcess(self, process, path, pid):
        """
        # 重启进程process
        :param process:
        :return:
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((self.ip, self.backport))
            if self.vm.platform == u"Windows":
                if pid:
                    sock.sendall("tskill " + pid + "\0")
                sock.sendall(path + "\0")
                logger.info("虚拟机" + self.name + "重启进程" + process.encode('utf-8') + ",使用命令:" + (("tskill " + pid + ", ") if pid else "") + path.encode('utf-8'))
            else:
                if pid:
                    sock.sendall("kill " + pid + "\0")
                sock.sendall(path + "\0")
                logger.info("虚拟机" + self.name + "重启进程" + process.encode('utf-8') + ",使用命令:" + (("kill " + pid + ", ") if pid else "") + path.encode('utf-8'))

        except socket.error, e:
            logger.warning("虚拟机连接异常，错误：%s" %e)
        finally:
            sock.close()

    def shutdownVm(self):
        """
        # 关闭虚拟机self.name
        :return:
        """
        # self.kvm_host.destroy(self.name)
        subprocess.Popen("sudo virsh destroy " + self.name, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        time.sleep(10)


    def restartVm(self):
        """
        # 重启虚拟机self.name
        :return:
        """
        #return

        #self.kvm_host.reboot(self.name)
        subprocess.Popen("sudo virsh destroy " + self.name, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        subprocess.Popen("sudo virsh start " + self.name, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        # self.kvm_host.destroy(self.name)
        # self.kvm_host.start(self.name)
        time.sleep(60)

    def restoreVm(self):
        """
        # 恢复虚拟机self.name
        :return:
        """
        # self.kvm_host.restore(self.name)
        subprocess.Popen("sudo virsh destroy " + self.name, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        subprocess.Popen("sudo virsh snapshot_revert " + self.name + " --snapshotname snap2-" + self.name, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        # self.kvm_host.destroy(self.name)
        # self.kvm_host.snapshot_revert(self.name, "snap2-"+self.name)
        time.sleep(60)
