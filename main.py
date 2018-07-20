#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

# 程序入口，指向用户界面以开始

"""
@author:    chenkuan
@license:   GNU General Public License 2.0
@contact:   chen1511@foxmail.com
@version:   1.0-2016-07-18
"""

import sys
import logging
from PyQt4 import QtGui
from view.vmGuiAction import VmGuiAction

def initLogger():
    """
    # 配置logging，用于全局日志记录
    :return:
    """
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[func:%(funcName)s() line:%(lineno)d] %(threadName)s-%(levelname)s: %(message)s',
                        datefmt='%Y/%m/%d %X',)
    logger = logging.getLogger()
    logger.debug("配置日志系统")
    logger.info("虚拟机监控恢复系统开始运行")

def start():
    """
    # 这里循环显示界面，根据界面的消息响应不同方法
    :return:None
    """
    # 生成应用和主界面
    app = QtGui.QApplication(sys.argv)
    # 界面风格包括：windows, motif, cde, plastique, windowsxp, macintosh
    app.setStyle(QtGui.QStyleFactory.create("windows"))
    mainWindow = QtGui.QMainWindow()

    # 调用view中的对象对界面进行包装
    ex = VmGuiAction(mainWindow)
    ex.setup()

    # 显示界面
    mainWindow.show()
    sys.exit(app.exec_())
if __name__ == "__main__":

    initLogger()
    start()