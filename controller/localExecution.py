#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

# LocalExecute类
# 对Local_PC进行策略操作的类



"""
@author:    SunQianqian
@license:   GNU General Public License 2.0
@version:   1.0-2019-05-17
"""

import logging
import subprocess
import time
import paramiko


logger = logging.getLogger()
# add policy execution for local process (can add a localExecution.py to implement) TODO

class LocalExecute(object):

    def execute(self,history, policy):
        """
        # 根据现有的操作历史和策略进行相应的执行
        :param vm:
        :param policy:
        :param history:
        :return:
        """

        self.history = history
        self.policy = policy

        # self.kvm_host = kvm.KVM(unix.Local())

        # 先判断策略与历史记录的严重等级，决定清除某些记录或更新策略
        # if policy.shouldRestore:
        #     logger.info("综合所有策略，选择恢复PC" )
        #     if history.vmRestoreTimes:
        #         logger.info("已经恢复PC" + str(history.vmRestoreTimes) + "次，继续恢复")
        #         history.vmRestoreTimes += 1
        #     else:
        #         logger.info("恢复PC" )
        #         history.vmRestoreTimes = 1
        if policy.shouldRestart:
            # if history.vmRestoreTimes:
            #     logger.info("已经恢复PC" + str(history.vmRestoreTimes) + "次，继续恢复")
            #     history.vmRestoreTimes += 1
            # if history.vmRestartTimes >= 3:
            #     logger.info("已经重启PC" + str(history.vmRestartTimes) + "次，选择恢复PC")
            #     policy.setPolicy(u"恢复虚拟机")
            #     history.vmRestoreTimes = 1
            if history.vmRestartTimes > 0:
                logger.info("已经重启PC" + str(history.vmRestartTimes) + "次，继续重启")
                history.vmRestartTimes += 1
            else:
                logger.info("综合所有策略，选择重启PC")
                logger.info("重启PC")
                history.vmRestartTimes = 1
        elif policy.shouldShutdown:
            logger.info("综合所有策略，选择关闭PC")
            logger.info("关闭PC")

        else:

            if policy.shouldOpenProcesses:
                logger.info("打开进程" + str(policy.shouldOpenProcesses))

            if policy.shouldShutdownProcesses:
                logger.info(("关闭进程" + str(policy.shouldShutdownProcesses)))

            if policy.shouldShutdownPorts:
                logger.info("关闭端口" + str(policy.shouldShutdownPorts))

            if policy.shouldRestartProcesses:
                # if history.vmRestoreTimes:
                #     logger.info("已经恢复PC" + str(history.vmRestoreTimes) + "次，继续恢复")
                #     history.vmRestoreTimes += 1
                # if history.vmRestartTimes >= 3:
                #     logger.info("已经重启PC" + str(history.vmRestartTimes) + "次，选择恢复PC")
                #     policy.setPolicy(u"恢复虚拟机")
                #     history.vmRestoreTimes = 1
                if history.vmRestartTimes > 0:
                    logger.info("已经重启PC" + str(history.vmRestartTimes) + "次，继续重启")
                    history.vmRestartTimes += 1
                else:
                    shouldRestart = False
                    pslist = []
                    for ps, path, pid in policy.shouldRestartProcesses:
                        if ps not in history.processesRestartTimes:
                            history.processesRestartTimes[ps] = 1
                        elif history.processesRestartTimes[ps] >= 3:
                            shouldRestart = True
                            pslist.append(ps)
                        else:
                            history.processesRestartTimes[ps] += 1
                    if shouldRestart:
                        policy.setPolicy(u"重启虚拟机")
                        logger.info("进程" + str(pslist) + "已经重启达到3次，选择重启")
                        history.vmRestartTimes = 1
                    else:
                        logger.info("重启进程" + str(policy.shouldRestartProcesses))

        if policy.level == 0:
            history.clearHistory()

        self.executePolicy()

    def executePolicy(self):
        # if self.policy.shouldRestorePC:
        #     self.restorePC()
        if self.policy.shouldRestart:
            self.restart()
        elif self.policy.shouldShutdown:
            self.shutdown()
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
                for pt,port_pid in self.policy.shouldShutdownPorts:
                    self.shutdownPort(pt,port_pid)



    def shutdownPort(self, pport, portpid):

        """
        # 关闭端口
        :param port:
        :return:
        """
        subprocess.Popen("sudo kill " + portpid, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        logger.info("关闭port" + pport.encode('utf-8') + "，使用命令：kill " + portpid)
        print pport

    def shutdownProcess(self, process, pid):
        """
        # 关闭进程
        :param process:
        :return:
        """

        subprocess.Popen("sudo kill " + pid, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        logger.info("关闭进程" + process.encode('utf-8') + "，使用命令：sudo kill ")


    def openProcess(self, process, path):
        """
        # 打开进程
        :param process:
        :param path:
        :return:
        """

        subprocess.Popen("sudo ./" + path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
        logger.info("打开进程" + process.encode('utf-8') + "，使用命令：sudo ./" + path.encode('utf-8'))


    def restartProcess(self, process, path, pid):
        """
        # 重启进程process
        :param process:
        :return:
        """
        subprocess.Popen("sudo kill " + pid, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
        subprocess.Popen("sudo ./" + path, stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        logger.info("restart process" + process.encode('utf-8'))

    def shutdown(self):
        """
        # 关闭虚拟机self.name
        :return:
        """
        # self.kvm_host.destroy(self.name)
        subprocess.Popen("sudo shutdown -h 10  ' I wil shutdown after 10 mins' ", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        time.sleep(10)

    def restart(self):
        """
        # 重启虚拟机self.name
        :return:
        """
        #return

        #self.kvm_host.reboot(self.name)
        subprocess.Popen("sudo reboot ", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        # self.kvm_host.destroy(self.name)
        # self.kvm_host.start(self.name)
        time.sleep(90)

    # def restorePC(self):
    #     """
    #     # 恢复虚拟机self.name
    #     :return:
    #     """
    #     # self.kvm_host.restore(self.name)
    #     subprocess.Popen("sudo virsh destroy " + self.name, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #     subprocess.Popen("sudo virsh snapshot_revert " + self.name + " --snapshotname snap2-" + self.name, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #     # self.kvm_host.destroy(self.name)
    #     # self.kvm_host.snapshot_revert(self.name, "snap2-"+self.name)
    #     time.sleep(60)
