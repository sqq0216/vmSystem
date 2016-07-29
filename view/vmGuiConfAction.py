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

from vmGuiConf import Ui_Form

class VmGuiConfAction(Ui_Form):

    def setupUi(self, Form):
        super(VmGuiConfAction, self).setupUi(Form)

    def setupName(self, Form, name):
        self.lineEdit_vmname.setText(name)