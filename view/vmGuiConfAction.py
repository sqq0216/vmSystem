#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

# VmGuiConfAction类
# 继承自子界面生成的VmGuiConf.py中的类
# 添加事件响应，提供对外接口



"""
@author:    chenkuan
@license:   GNU General Public License 2.0
@contact:   chen1511@foxmail.com
@version:   1.0-2016-07-29
"""
from PyQt4 import QtGui, QtCore
from vmGuiConf import Ui_Form

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class VmGuiConfAction(Ui_Form):

    def setupUi(self, Form):
        super(VmGuiConfAction, self).setupUi(Form)
        # 添加子界面上的消息响应
        self.addAction()

    def addAction(self):
        # 保存按钮
        QtCore.QObject.connect(self.pushButton_save, QtCore.SIGNAL(_fromUtf8("clicked()")), self.save)
        # 清空按钮
        QtCore.QObject.connect(self.pushButton_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clear)
        # 执行按钮
        QtCore.QObject.connect(self.pushButton_execute, QtCore.SIGNAL(_fromUtf8("clicked()")), self.execute)
        # 中断按钮
        QtCore.QObject.connect(self.pushButton_break, QtCore.SIGNAL(_fromUtf8("clicked()")), self.break_)

    def save(self):
        """
        # 点击保存时调用此方法
        # 将该页上配置保存
        :return:
        """
        processesMonitor =
        self.uiController.setVmsConfs(self.name,
                                      sysType = self.comboBox_systype.currentText(),
                                      isCheckRootkit = self.checkBox_rootkit.isChecked(),
                                      rootkitPolicy = self.comboBox_rootkit_policy.currentText(),
                                      ip = (self.spinBox_ip1.text(), self.spinBox_ip2.text(), self.spinBox_ip3.text(), self.spinBox_ip4.text()),
                                      )

    def clear(self):
        """
        # 点击清空时调用此方法
        # 将该页上配置清空，并清空对应的配置文件
        :return:
        """

    def execute(self):
        """
        # 点击执行时调用此方法
        #
        :return:
        """

    def break_(self):
        """
        #
        :return:
        """


    def setupName(self, name):
        self.name = name
        self.label_vmname.setText(name)

    def setupTypes(self, types):
        self.comboBox_systype.addItems(types)

    def setupController(self, uiController):
        self.uiController = uiController