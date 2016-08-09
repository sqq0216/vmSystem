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
#import sys
#reload(sys)
#sys.setdefaultencoding( "utf-8" )

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
        self.vms = self.uiController.vms

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
        # 从文件载入该页的配置
        :param item:
        :param index:
        :return:
        """
        i = self.itemList[item]
        self.stackedWidget.setCurrentIndex(i)
        self.load(i)

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

            #默认载入页面1
            self.load(0)

        self.stackedWidget.setCurrentIndex(0)

    def load(self, i):
        confs = self.uiController.getVmsConfs(self.vms[i])
        print repr(confs).decode("unicode-escape")
        childWndGen = self.childWindowsGens[i]

        # 先清空一下当前页的配置
        self.clear()

        # 根据读取的sysType来定位到comboBox中
        postion = childWndGen.comboBox_systype.findText(confs["sysType"])
        childWndGen.comboBox_systype.setCurrentIndex(postion)

        # 根据读取的isCheckRootkit来定位到checkBox中
        childWndGen.checkBox_rootkit.setChecked(confs['isCheckRootkit'])

        # 根据读取的rootkitPolicy来定位到comboBox中
        postion = childWndGen.comboBox_rootkit_policy.findText(confs["rootkitPolicy"])
        childWndGen.comboBox_rootkit_policy.setCurrentIndex(postion)

        # 根据读取的ip来填入spinbox中
        ip = confs["ip"].split('.')
        childWndGen.spinBox_ip1.setValue(int(ip[0]))
        childWndGen.spinBox_ip2.setValue(int(ip[1]))
        childWndGen.spinBox_ip3.setValue(int(ip[2]))
        childWndGen.spinBox_ip4.setValue(int(ip[3]))

        # 根据读取的processesMonitor来填入treeWidget中
        for ps, isneed, policy, path in confs["processesMonitor"]:
            item = QtGui.QTreeWidgetItem(childWndGen.treeWidget_processes)
            item.setText(0, ps)
            item.setText(1, isneed)
            item.setText(2, policy)
            item.setText(3, path)

        # 根据读取的portsMonitor来填入treeWidget中
        for pt, isneed, policy in confs["portsMonitor"]:
            item = QtGui.QTreeWidgetItem(childWndGen.treeWidget_ports)
            item.setText(0, pt)
            item.setText(1, isneed)
            item.setText(2, policy)

    def save(self):
        index = self.stackedWidget.currentIndex()
        childWndGen = self.childWindowsGens[index]

        # 遍历进程监控设置部分，取出所有设置
        psMonitor = []
        items = QtGui.QTreeWidgetItemIterator(childWndGen.treeWidget_processes)
        item = items.value()
        while item:
            items += 1
            psMonitor.append((unicode(item.text(0)), unicode(item.text(1)), unicode(item.text(2)), unicode(item.text(3))))
            item = items.value()
        # 转码，使得可以正常print出中文, 此句仅供调试
        print "psMonitor:",
        print repr(psMonitor).decode('unicode-escape')

        # 遍历端口监控设置部分，取出所有设置
        ptMonitor = []
        items = QtGui.QTreeWidgetItemIterator(childWndGen.treeWidget_ports)
        item = items.value()
        while item:
            items += 1
            ptMonitor.append((unicode(item.text(0)), unicode(item.text(1)), unicode(item.text(2))))
            item = items.value()
        # 转码，使得可以正常print出中文，此句仅供调试
        print "ptMonitor:",
        print repr(ptMonitor).decode('unicode-escape')


        # 获取配置后发给控制器令其保存至文件
        self.uiController.setVmsConfs(self.vms[index],
                                      sysType = unicode(childWndGen.comboBox_systype.currentText()),
                                      isCheckRootkit = childWndGen.checkBox_rootkit.isChecked(),
                                      rootkitPolicy = unicode(childWndGen.comboBox_rootkit_policy.currentText()),
                                      ip = (unicode(childWndGen.spinBox_ip1.text()) + u'.' + unicode(childWndGen.spinBox_ip2.text()) + u'.' + unicode(childWndGen.spinBox_ip3.text()) + u'.' + unicode(childWndGen.spinBox_ip4.text())),
                                      processesMonitor = psMonitor,
                                      portsMonitor = ptMonitor)

    def clear(self):
        """
        # 清除子界面上的所有输入配置
        :return:
        """
        index = self.stackedWidget.currentIndex()
        childWndGen = self.childWindowsGens[index]
        childWndGen.comboBox_systype.setCurrentIndex(0)
        childWndGen.checkBox_rootkit.setChecked(False)
        childWndGen.comboBox_rootkit_policy.setCurrentIndex(0)
        childWndGen.spinBox_ip1.setValue(0)
        childWndGen.spinBox_ip2.setValue(0)
        childWndGen.spinBox_ip3.setValue(0)
        childWndGen.spinBox_ip4.setValue(0)
        childWndGen.treeWidget_processes.clear()
        childWndGen.treeWidget_ports.clear()