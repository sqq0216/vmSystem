#!/usr/local/bin/python2.7

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


class UserInterfaceController(object):

    def __init__(self):
        self.vms = []
        self.vmsConfs = {}
        self.vmsStates = {}

    def getVms(self):
        """
        #从libvmi中获取运行的虚拟机
        :return:
        """

    def updateVmsConfs(self):
        """
        #当界面更新配置时调用此方法
        :return:
        """
        pass

    def startMonitorVm(self):
        """
        #当界面开始监控某虚拟机时调用此
        #新开线程运行
        :return:
        """
        pass

    def start(self):
        """
        #这里循环显示界面，根据界面的消息响应不同方法
        :return:
        """
        #生成应用和主界面
        app = QtGui.QApplication(sys.argv)
        mainwindow = QtGui.QMainWindow()

        #调用view中的对象对界面进行包装
        #ex = xxx()
        #ex.setupUi(mainwindow)

        #显示界面
        mainwindow.show()
        sys.exit(app.exec_())



