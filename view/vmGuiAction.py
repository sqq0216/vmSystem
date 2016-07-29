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

from PyQt4 import QtCore,QtGui
from controller.userInterfaceController import UserInterfaceController
from vmGui import Ui_mainWindow
from vmGuiConfAction import VmGuiConfAction

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class VmGuiAction(Ui_mainWindow):

    def __init__(self, MainWindow):
        """
        #在这里添加控制器作为属性，以实现消息映射
        :param MainWindow:
        """
        self.mainWindow = MainWindow
        self.childWindows = []
        self.uiController = UserInterfaceController()

        #虚拟机树字典，item:index
        self.itemList = {}

        # 获取运行虚拟机列表
        self.vms = self.uiController.getVms()

    def setupUi(self):
        """
        #对界面静态元素可通过调用父类方法添加
        #对需要动态添加的部分在此方法实现
        :param MainWindow:
        :return:
        """
        super(VmGuiAction, self).setupUi(self.mainWindow)

        # 调用函数动态显示treeWidget
        self.addTreeItem()

        #调用函数添加子界面
        self.addChildWindow()

        #添加事件响应
        self.addAction()


    def addChildWindow(self):
        """
        # 从控制器中获取运行虚拟机的列表
        # 维护一个子界面的列表，并依次添加到主界面中
        :return:
        """
        # 生成子界面包装器
        childWndGenerator = VmGuiConfAction()
        #生成子界面列表，对每个子界面进行包装，并将其显示出来
        for name in self.vms:
            childWnd = QtGui.QWidget()
            self.childWindows.append(childWnd)
            #把虚拟机名字也传入了
            childWndGenerator.setupUi(childWnd)
            childWndGenerator.setupName(childWnd, name)
            self.stackedWidget.insertWidget(-1, childWnd)

        self.stackedWidget.setCurrentIndex(0)

    def addTreeItem(self):
        """
        # 调用函数获取虚拟机列表
        # 动态添加到treeWidget上
        :return:
        """
        for i, name in enumerate(self.vms):
            item = QtGui.QTreeWidgetItem(self.treeWidget)
            item.setText(0, name)
            self.itemList[item] = i


    def addAction(self):
        """
        #对界面添加事件响应
        :param MainWindow:
        :return:
        """
        QtCore.QObject.connect(self.treeWidget, QtCore.SIGNAL(_fromUtf8("itemActivated(QTreeWidgetItem*,int)")),self.treeItemSelect)

    def treeItemSelect(self, item, index):
        """
        # 承接treeWidget的项选择事件
        # 使stackedWidget切换到相应的页面
        :param item:
        :param index:
        :return:
        """
        self.stackedWidget.setCurrentIndex(self.itemList[item])