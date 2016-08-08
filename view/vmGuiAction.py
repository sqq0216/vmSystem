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
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from PyQt4 import QtCore,QtGui
from controller.userInterfaceController import UserInterfaceController
from vmGui import Ui_mainWindow
from vmGuiConf import Ui_Form as VmGuiConf
#from vmGuiConfAction import VmGuiConfAction

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
        self.childWindows = []      #子界面列表
        self.childWindowsGens = []      #子界面包装器列表
        self.uiController = UserInterfaceController()   #主界面控制器

        #虚拟机树字典，item:index，用来确定tree上的item与stackedWidget上的page对应关系
        self.itemList = {}

        # 获取运行虚拟机列表
        self.vms = self.uiController.getVms()

        #获取虚拟机类型列表
        self.vmTypes = self.uiController.getVmtypes()

    def setup(self):
        """
        #对界面静态元素可通过调用父类方法添加
        #对需要动态添加的部分在此方法实现
        # 添加事件响应
        :param MainWindow:
        :return:
        """
        super(VmGuiAction, self).setupUi(self.mainWindow)

        # 调用函数动态显示treeWidget
        self.addTreeItem()

        # 添加主界面事件响应
        self.addAction()

        #调用函数添加子界面
        self.addChildWindow()

    def addTreeItem(self):
        """
        # 根据虚拟机列表动态添加到treeWidget上
        :return:
        """
        for i, name in enumerate(self.vms):
            item = QtGui.QTreeWidgetItem(self.treeWidget)
            item.setText(0, name)
            self.itemList[item] = i

    def addAction(self):
        """
        # 对主界面添加事件响应
        :param MainWindow:
        :return:
        """
        # 当treeWidget点击切换时，调用方法来切换stackedWidget
        QtCore.QObject.connect(self.treeWidget, QtCore.SIGNAL(_fromUtf8("itemClicked(QTreeWidgetItem*,int)")),self.treeItemSelect)

    def treeItemSelect(self, item, index):
        """
        # 承接treeWidget的项选择事件
        # 使stackedWidget切换到相应的页面
        :param item:
        :param index:
        :return:
        """
        self.stackedWidget.setCurrentIndex(self.itemList[item])

    def addChildWindow(self):
        """
        # 根据运行虚拟机的列表
        # 维护一个子界面的列表，并依次添加到主界面中
        :return:
        """
        #生成子界面列表，对每个子界面进行包装，并将其显示出来
        for name in self.vms:
            #生成子界面
            childWnd = QtGui.QWidget()
            self.childWindows.append(childWnd)

            # 生成子界面包装器
            childWndGenerator = VmGuiConf()
            self.childWindowsGens.append(childWndGenerator)

            #简单包装子界面
            childWndGenerator.setupUi(childWnd)
            # 把虚拟机名字传入
            childWndGenerator.label_vmname.setText(name)
            # 把虚拟机类型列表传入
            childWndGenerator.comboBox_systype.addItems(self.vmTypes)
            # 对子界面上按钮加入消息响应
            QtCore.QObject.connect(childWndGenerator.pushButton_save, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.save)
            QtCore.QObject.connect(childWndGenerator.pushButton_clear, QtCore.SIGNAL(_fromUtf8("clicked(bool)")),self.clear)

            # 把子界面插入到stackedWidget中
            self.stackedWidget.insertWidget(-1, childWnd)

        self.stackedWidget.setCurrentIndex(0)

    def save(self):
        index = self.stackedWidget.currentIndex()
        childWndGen = self.childWindowsGens[index]
        # 遍历进程监控设置部分，取出所有设置
        psMonitor = []
        items = QtGui.QTreeWidgetItemIterator(childWndGen.treeWidget_processes)
        item = items.value()
        while item:
            items += 1
            psMonitor.append((str(item.text(0)), str(item.text(1)), str(item.text(2)), str(item.text(3))))
            item = items.value()

        # 遍历端口监控设置部分，取出所有设置
        ptMonitor = []
        items = QtGui.QTreeWidgetItemIterator(childWndGen.treeWidget_ports)
        item = items.value()
        while item:
            items += 1
            ptMonitor.append((str(item.text(0)), str(item.text(1)), str(item.text(2))))
            item = items.value()

        self.uiController.setVmsConfs(self.vms[index],
                                      sysType = str(childWndGen.comboBox_systype.currentText()),
                                      isCheckBootkit = childWndGen.checkBox_rootkit.isChecked(),
                                      rootkitPolicy = str(childWndGen.comboBox_rootkit_policy.currentText()),
                                      ip = (str(childWndGen.spinBox_ip1.text()) + '.' + str(childWndGen.spinBox_ip2.text()) + '.' + str(childWndGen.spinBox_ip3.text()) + '.' + str(childWndGen.spinBox_ip4.text())),
                                      processesMonitor = psMonitor,
                                      portsMonitor = ptMonitor)


    def clear(self):
        index = self.stackedWidget.currentIndex()
        childWndGen = self.childWindowsGens[index]
        childWndGen.comboBox_systype.setCurrentIndex(0)
        childWndGen.checkBox_rootkit.setChecked(False)
        childWndGen.comboBox_rootkit_policy.setCurrentIndex(0)
        childWndGen.spinBox_ip1.clear()
        childWndGen.spinBox_ip2.clear()
        childWndGen.spinBox_ip3.clear()
        childWndGen.spinBox_ip4.clear()
        childWndGen.treeWidget_processes.clear()
        childWndGen.treeWidget_ports.clear()