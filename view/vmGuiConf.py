# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view\vmGuiConf.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(672, 587)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox_4 = QtGui.QGroupBox(Form)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 51))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.checkBox_rootkit = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox_rootkit.setObjectName(_fromUtf8("checkBox_rootkit"))
        self.gridLayout_5.addWidget(self.checkBox_rootkit, 0, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_4)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_5.addWidget(self.label_7, 0, 2, 1, 1)
        self.comboBox_rootkit_policy = QtGui.QComboBox(self.groupBox_4)
        self.comboBox_rootkit_policy.setObjectName(_fromUtf8("comboBox_rootkit_policy"))
        self.comboBox_rootkit_policy.addItem(_fromUtf8(""))
        self.comboBox_rootkit_policy.addItem(_fromUtf8(""))
        self.gridLayout_5.addWidget(self.comboBox_rootkit_policy, 0, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(148, 16, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 0, 4, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 1, 0, 1, 11)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        self.pushButton_save = QtGui.QPushButton(Form)
        self.pushButton_save.setObjectName(_fromUtf8("pushButton_save"))
        self.gridLayout.addWidget(self.pushButton_save, 3, 2, 1, 1)
        self.label_vmname = QtGui.QLabel(Form)
        self.label_vmname.setText(_fromUtf8(""))
        self.label_vmname.setObjectName(_fromUtf8("label_vmname"))
        self.gridLayout.addWidget(self.label_vmname, 0, 3, 1, 1)
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 8, 1, 1)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 4, 1, 1)
        self.pushButton_clear = QtGui.QPushButton(Form)
        self.pushButton_clear.setObjectName(_fromUtf8("pushButton_clear"))
        self.gridLayout.addWidget(self.pushButton_clear, 3, 3, 1, 1)
        self.pushButton_execute = QtGui.QPushButton(Form)
        self.pushButton_execute.setObjectName(_fromUtf8("pushButton_execute"))
        self.gridLayout.addWidget(self.pushButton_execute, 3, 5, 1, 1)
        self.pushButton_break = QtGui.QPushButton(Form)
        self.pushButton_break.setObjectName(_fromUtf8("pushButton_break"))
        self.gridLayout.addWidget(self.pushButton_break, 3, 6, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 5, 1, 1)
        self.comboBox_systype = QtGui.QComboBox(Form)
        self.comboBox_systype.setObjectName(_fromUtf8("comboBox_systype"))
        self.gridLayout.addWidget(self.comboBox_systype, 0, 6, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 3, 8, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.spinBox_ip1 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_ip1.setMaximum(256)
        self.spinBox_ip1.setObjectName(_fromUtf8("spinBox_ip1"))
        self.gridLayout_4.addWidget(self.spinBox_ip1, 0, 1, 1, 1)
        self.spinBox_ip4 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_ip4.setMaximum(256)
        self.spinBox_ip4.setObjectName(_fromUtf8("spinBox_ip4"))
        self.gridLayout_4.addWidget(self.spinBox_ip4, 0, 4, 1, 1)
        self.spinBox_ip3 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_ip3.setMaximum(256)
        self.spinBox_ip3.setObjectName(_fromUtf8("spinBox_ip3"))
        self.gridLayout_4.addWidget(self.spinBox_ip3, 0, 3, 1, 1)
        self.spinBox_ip2 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_ip2.setMaximum(256)
        self.spinBox_ip2.setObjectName(_fromUtf8("spinBox_ip2"))
        self.gridLayout_4.addWidget(self.spinBox_ip2, 0, 2, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton_modifyprocess = QtGui.QPushButton(self.groupBox)
        self.pushButton_modifyprocess.setObjectName(_fromUtf8("pushButton_modifyprocess"))
        self.gridLayout_2.addWidget(self.pushButton_modifyprocess, 2, 3, 1, 1)
        self.pushButton_addprocess = QtGui.QPushButton(self.groupBox)
        self.pushButton_addprocess.setObjectName(_fromUtf8("pushButton_addprocess"))
        self.gridLayout_2.addWidget(self.pushButton_addprocess, 2, 2, 1, 1)
        self.pushButton_delprocess = QtGui.QPushButton(self.groupBox)
        self.pushButton_delprocess.setObjectName(_fromUtf8("pushButton_delprocess"))
        self.gridLayout_2.addWidget(self.pushButton_delprocess, 2, 4, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 2, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.treeWidget_processes = QtGui.QTreeWidget(self.groupBox)
        self.treeWidget_processes.setUniformRowHeights(False)
        self.treeWidget_processes.setItemsExpandable(False)
        self.treeWidget_processes.setExpandsOnDoubleClick(False)
        self.treeWidget_processes.setObjectName(_fromUtf8("treeWidget_processes"))
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_processes)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_processes)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_processes)
        self.gridLayout_2.addWidget(self.treeWidget_processes, 1, 0, 1, 5)
        self.gridLayout_4.addWidget(self.groupBox, 1, 0, 1, 5)
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pushButton_modifyport = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_modifyport.setObjectName(_fromUtf8("pushButton_modifyport"))
        self.gridLayout_3.addWidget(self.pushButton_modifyport, 3, 3, 1, 1)
        self.pushButton_addport = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_addport.setObjectName(_fromUtf8("pushButton_addport"))
        self.gridLayout_3.addWidget(self.pushButton_addport, 3, 2, 1, 1)
        self.pushButton_delport = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_delport.setObjectName(_fromUtf8("pushButton_delport"))
        self.gridLayout_3.addWidget(self.pushButton_delport, 3, 4, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 3, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 3, 0, 1, 1)
        self.treeWidget_ports = QtGui.QTreeWidget(self.groupBox_3)
        self.treeWidget_ports.setUniformRowHeights(False)
        self.treeWidget_ports.setItemsExpandable(False)
        self.treeWidget_ports.setExpandsOnDoubleClick(False)
        self.treeWidget_ports.setObjectName(_fromUtf8("treeWidget_ports"))
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_ports)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_ports)
        self.gridLayout_3.addWidget(self.treeWidget_ports, 1, 0, 1, 5)
        self.gridLayout_4.addWidget(self.groupBox_3, 2, 0, 1, 5)
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 11)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox_4.setTitle(_translate("Form", "Rootkit检查", None))
        self.checkBox_rootkit.setText(_translate("Form", "Rootkit检查", None))
        self.label_7.setText(_translate("Form", "检查到Rootkit后的操作:", None))
        self.comboBox_rootkit_policy.setItemText(0, _translate("Form", "重启虚拟机", None))
        self.comboBox_rootkit_policy.setItemText(1, _translate("Form", "恢复虚拟机", None))
        self.pushButton_save.setText(_translate("Form", "保存", None))
        self.label_6.setText(_translate("Form", "虚拟机名称：", None))
        self.pushButton_clear.setText(_translate("Form", "清空", None))
        self.pushButton_execute.setText(_translate("Form", "执行", None))
        self.pushButton_break.setText(_translate("Form", "中断", None))
        self.label_3.setText(_translate("Form", "虚拟机类型：", None))
        self.groupBox_2.setTitle(_translate("Form", "进程与端口监控", None))
        self.groupBox.setTitle(_translate("Form", "进程监控", None))
        self.pushButton_modifyprocess.setText(_translate("Form", "修改", None))
        self.pushButton_addprocess.setText(_translate("Form", "添加", None))
        self.pushButton_delprocess.setText(_translate("Form", "删除", None))
        self.label.setText(_translate("Form", "添加需要存在和禁止存在的进程，当发现不满足时将执行处理策略", None))
        self.treeWidget_processes.headerItem().setText(0, _translate("Form", "进程名", None))
        self.treeWidget_processes.headerItem().setText(1, _translate("Form", "需要与禁止", None))
        self.treeWidget_processes.headerItem().setText(2, _translate("Form", "处理策略", None))
        self.treeWidget_processes.headerItem().setText(3, _translate("Form", "进程启动路径", None))
        __sortingEnabled = self.treeWidget_processes.isSortingEnabled()
        self.treeWidget_processes.setSortingEnabled(False)
        self.treeWidget_processes.topLevelItem(0).setText(0, _translate("Form", "cstest", None))
        self.treeWidget_processes.topLevelItem(0).setText(1, _translate("Form", "需要", None))
        self.treeWidget_processes.topLevelItem(0).setText(2, _translate("Form", "重启进程", None))
        self.treeWidget_processes.topLevelItem(0).setText(3, _translate("Form", "/csd/cstest", None))
        self.treeWidget_processes.topLevelItem(1).setText(0, _translate("Form", "mspaint", None))
        self.treeWidget_processes.topLevelItem(1).setText(1, _translate("Form", "禁止", None))
        self.treeWidget_processes.topLevelItem(1).setText(2, _translate("Form", "重启虚拟机", None))
        self.treeWidget_processes.topLevelItem(2).setText(0, _translate("Form", "pptest", None))
        self.treeWidget_processes.topLevelItem(2).setText(1, _translate("Form", "需要", None))
        self.treeWidget_processes.topLevelItem(2).setText(2, _translate("Form", "恢复虚拟机", None))
        self.treeWidget_processes.setSortingEnabled(__sortingEnabled)
        self.groupBox_3.setTitle(_translate("Form", "端口监控", None))
        self.pushButton_modifyport.setText(_translate("Form", "修改", None))
        self.pushButton_addport.setText(_translate("Form", "添加", None))
        self.pushButton_delport.setText(_translate("Form", "删除", None))
        self.label_2.setText(_translate("Form", "添加需要存在和禁止存在的端口，当发现不满足时将执行处理策略", None))
        self.treeWidget_ports.headerItem().setText(0, _translate("Form", "端口号", None))
        self.treeWidget_ports.headerItem().setText(1, _translate("Form", "需要与禁止", None))
        self.treeWidget_ports.headerItem().setText(2, _translate("Form", "处理策略", None))
        __sortingEnabled = self.treeWidget_ports.isSortingEnabled()
        self.treeWidget_ports.setSortingEnabled(False)
        self.treeWidget_ports.topLevelItem(0).setText(0, _translate("Form", "8080", None))
        self.treeWidget_ports.topLevelItem(0).setText(1, _translate("Form", "需要", None))
        self.treeWidget_ports.topLevelItem(0).setText(2, _translate("Form", "告警", None))
        self.treeWidget_ports.topLevelItem(1).setText(0, _translate("Form", "8999", None))
        self.treeWidget_ports.topLevelItem(1).setText(1, _translate("Form", "禁止", None))
        self.treeWidget_ports.topLevelItem(1).setText(2, _translate("Form", "关闭端口", None))
        self.treeWidget_ports.setSortingEnabled(__sortingEnabled)
        self.label_5.setText(_translate("Form", "虚拟机ip:", None))

