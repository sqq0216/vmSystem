#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

# VmGuiDialog类
# 显示对话框用
# 动态显示对话框内的项，并提供方法返回参数



"""
@author:    chenkuan
@license:   GNU General Public License 2.0
@contact:   chen1511@foxmail.com
@version:   1.0-2016-08-28
"""

from PyQt4 import QtGui,QtCore

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

class VmGuiDialog(QtGui.QDialog):

    def __init__(self, parent=None):
        super(VmGuiDialog, self).__init__(parent)

    def setOption(self, action, type, name, isneed, policy, path=None):
        title = u""
        if action == u"add":
            title += u"添加"
        else:
            title += u"修改"
        if type == u"process":
            title += u"进程"
        else:
            title += u"端口"
        title += u"监控"

        self.setWindowTitle(_fromUtf8(title))
        #self.setObjectName(_fromUtf8("Dialog"))
        self.resize(300, 240)
        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayout = QtGui.QGridLayout(self)

        self.label_name = QtGui.QLabel(self)
        if type == u"process":
            self.label_name.setText(_translate("Dialog", "进程名：", None))
        else:
            self.label_name.setText(_translate("Dialog", "端口号：", None))
        self.gridLayout.addWidget(self.label_name, 0, 0, 1, 1)

        self.lineEdit_name = QtGui.QLineEdit(self)
        if name != u"":
            self.lineEdit_name.setText(name)
        self.gridLayout.addWidget(self.lineEdit_name, 0, 2, 1, 1)

        self.radioButton_need = QtGui.QRadioButton(self)
        self.radioButton_need.setText(_translate("Dialog", "需要", None))
        self.radioButton_noneed = QtGui.QRadioButton(self)
        self.radioButton_noneed.setText(_translate("Dialog", "禁止", None))
        if isneed:
            self.radioButton_need.setChecked(True)
        else:
            self.radioButton_noneed.setChecked(True)
        self.gridLayout.addWidget(self.radioButton_need, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.radioButton_noneed, 2, 2, 1, 1)

        self.label_policy = QtGui.QLabel(self)
        self.label_policy.setText(_translate("Dialog", "处理策略：", None))
        self.gridLayout.addWidget(self.label_policy, 3, 0, 1, 1)

        self.comboBox = QtGui.QComboBox(self)
        #self.comboBox.setObjectName(_fromUtf8("comboBox"))
        processPolicys = [u"告警", u"关闭进程", u"打开进程", u"重启进程", u"关闭虚拟机", u"重启虚拟机", u"恢复虚拟机"]
        portPolicys = [u"告警", u"关闭端口", u"关闭虚拟机", u"重启虚拟机", u"恢复虚拟机"]
        if type == u"process":
            for pol in processPolicys:
                self.comboBox.addItem(_fromUtf8(pol))
            if policy != u"":
                try:
                    index = processPolicys.index(policy)
                except ValueError:
                    index = 0
                self.comboBox.setCurrentIndex(index)
        else:
            for pol in portPolicys:
                self.comboBox.addItem(_fromUtf8(pol))
            if policy != u"":
                try:
                    index = portPolicys.index(policy)
                except ValueError:
                    index = 0
                self.comboBox.setCurrentIndex(index)
        self.gridLayout.addWidget(self.comboBox, 3, 2, 1, 1)

        if path != None:
            self.label_path = QtGui.QLabel(self)
            self.label_path.setText(_translate("Dialog", "进程启动路径：", None))
            self.gridLayout.addWidget(self.label_path, 4, 0, 1, 1)

            self.lineEdit_path = QtGui.QLineEdit(self)
            if path != u"":
                self.lineEdit_path.setText(path)
            self.gridLayout.addWidget(self.lineEdit_path, 4, 2, 1, 1)

        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 3)

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.reject)


    def getValue(self):
        valueDict = {}
        valueDict['name'] = self.lineEdit_name.text()
        valueDict['isneed'] = u"需要" if self.radioButton_need.isChecked() else u"禁止"
        valueDict['policy'] = self.comboBox.currentText()
        if hasattr(self, 'lineEdit_path'):
            valueDict['path'] = self.lineEdit_path.text()
        return valueDict