#!/usr/local/bin/python2.7

#程序入口，指向用户界面控制器以开始

"""
@author:    chenkuan
@license:   GNU General Public License 2.0
@contact:   chen1511@foxmail.com
@version:   1.0-2016-07-18
"""

from controller.userInterfaceController import UserInterfaceController

if __name__ == "__main__":

    m = UserInterfaceController()
    m.start()