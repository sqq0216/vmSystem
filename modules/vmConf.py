#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

# Vmco类
# 用户配置的信息


"""
@author:    chenkuan
@license:   GNU General Public License 2.0
@contact:   chen1511@foxmail.com
@version:   1.0-2016-07-18
"""

import vmState

class VmConf(object):
    """
    This is the class that save the vm information from the GUI
    """
    def __init__(self):
        self.name = ""
        self.systype = ""
        self.process = []   #监控级别应放在process属性里
        self.ports = []  #监控级别应放在port属性里

    def updateConf(self):
        """
        #此方法用于更新当前虚拟机的配置信息信息
        #可于用户界面更新数据后信号式调用此方法
        #从文件中读取json数据
        :return:
        """
        pass

    def saveConf(self):
        """
        #每次在运行中修改配置后都要及时更新到文件中作永久保存
        :return:
        """
        pass

    def readConf(self):
        """
        #每次重新打开程序时都要从文件中读取以前保存
        :return:
        """
        pass