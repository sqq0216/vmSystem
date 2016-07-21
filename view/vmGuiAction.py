#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

# VmGuiAction类
# 继承自界面生成的VmGui.py中的类
# 添加事件响应，提供对外接口



"""
@author:    chenkuan
@license:   GNU General Public License 2.0
@contact:   chen1511@foxmail.com
@version:   1.0-2016-07-21
"""

from controller.userInterfaceController import UserInterfaceController
from vmGui import Ui_MainWindow


class VmGuiAction(Ui_MainWindow):

    def __init__(self, MainWindow):
        """
        #在这里添加控制器作为属性，以实现消息映射
        :param MainWindow:
        """
        self.mainWindow = MainWindow
        self.uiController = UserInterfaceController()

    def setupUi(self):
        """
        #对界面静态元素可通过调用父类方法添加
        #对需要动态添加的部分在此方法实现
        :param MainWindow:
        :return:
        """
        super(VmGuiAction, self).setupUi(self.mainWindow)


    def addAction(self):
        """
        #对界面添加事件响应
        :param MainWindow:
        :return:
        """
        pass