#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

#程序入口，指向用户界面以开始

"""
@author:    chenkuan
@license:   GNU General Public License 2.0
@contact:   chen1511@foxmail.com
@version:   1.0-2016-07-18
"""


import sys
from PyQt4 import QtGui
from view.vmGuiAction import VmGuiAction


def start():
    """
    #这里循环显示界面，根据界面的消息响应不同方法
    :return:None
    """
    # 生成应用和主界面
    app = QtGui.QApplication(sys.argv)
    mainWindow = QtGui.QMainWindow()

    # 调用view中的对象对界面进行包装
    ex = VmGuiAction(mainWindow)
    ex.setup()

    # 显示界面
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":

    start()